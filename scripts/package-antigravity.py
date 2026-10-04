#!/usr/bin/env python3
"""Sync the Antigravity package from shared sources and optionally export a ZIP."""

import argparse
import json
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "antigravity" / "mcpbinder"
SKILLS = {
    "get-started", "log-decision", "plan-tasks", "project-update",
    "task-focus", "work-assigned-task",
}


def json_bytes(value):
    return (json.dumps(value, indent=2) + "\n").encode()


def expected_files():
    source = json.loads((ROOT / "plugin.json").read_text())
    remote = json.loads((ROOT / "mcp.json").read_text())["mcpServers"]["mcpbinder"]
    if source["name"] != "mcpbinder" or remote != {
        "type": "streamable-http", "url": "https://www.mcpbinder.com/api/mcp"
    }:
        raise ValueError("Review the shared identity or connection before packaging")
    # The documented manifest allows only name and description. The schema URL
    # currently returns 404, so omit the optional editor-only $schema key.
    manifest = {key: source[key] for key in ("name", "description")}
    if not re.fullmatch(r"[a-zA-Z0-9_-]+", manifest["name"]):
        raise ValueError("Invalid Antigravity plugin name")
    if not isinstance(manifest["description"], str) or not manifest["description"]:
        raise ValueError("A plugin description is required")
    files = {
        "plugin.json": json_bytes(manifest),
        "mcp_config.json": json_bytes({"mcpServers": {
            "mcpbinder": {"serverUrl": remote["url"]}
        }}),
        "LICENSE": (ROOT / "LICENSE").read_bytes(),
        "assets/icon.png": (ROOT / "assets/icon.png").read_bytes(),
    }
    skill_dirs = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
    if skill_dirs != SKILLS:
        raise ValueError("Review the skill inventory before packaging")
    for path in sorted((ROOT / "skills").rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Symlinks are not allowed: {path}")
        if path.is_file():
            if path.suffix != ".md":
                raise ValueError(f"Unexpected skill asset: {path}")
            files[path.relative_to(ROOT).as_posix()] = path.read_bytes()
    for name in SKILLS:
        text = files[f"skills/{name}/SKILL.md"].decode()
        if not text.startswith(f"---\nname: {name}\ndescription: "):
            raise ValueError(f"Invalid skill metadata: {name}")
    readme = (ROOT / "antigravity" / "README.template.md").read_text()
    files["README.md"] = readme.replace("{{VERSION}}", source["version"]).encode()
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify without changing files")
    parser.add_argument("--archive", type=Path, help="Export a ZIP outside the package")
    args = parser.parse_args()
    files = expected_files()
    existing = set()
    if PACKAGE.exists():
        for path in PACKAGE.rglob("*"):
            if path.is_symlink():
                raise ValueError(f"Symlinks are not allowed: {path}")
            if path.is_file():
                existing.add(path.relative_to(PACKAGE).as_posix())
    extra = existing - files.keys()
    if extra:
        raise ValueError(f"Unexpected package files: {sorted(extra)}")
    for name, content in files.items():
        path = PACKAGE / name
        if args.check:
            if not path.is_file() or path.read_bytes() != content:
                raise ValueError(f"Package is out of date: {name}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
    if args.archive:
        archive = args.archive.resolve()
        if archive.is_relative_to(PACKAGE.resolve()):
            raise ValueError("Write the archive outside the package directory")
        archive.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as output:
            for name, content in sorted(files.items()):
                info = zipfile.ZipInfo(f"mcpbinder/{name}")
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                output.writestr(info, content)
        with zipfile.ZipFile(archive) as exported:
            if exported.testzip() is not None:
                raise ValueError("Archive failed its integrity check")
            if set(exported.namelist()) != {f"mcpbinder/{name}" for name in files} or any(
                exported.read(f"mcpbinder/{name}") != content
                for name, content in files.items()
            ):
                raise ValueError("Archive content differs from the reviewed package")
        print(f"Exported and inspected {archive}")
    print(f"Verified {len(SKILLS)} skills, one remote server, and {len(files)} package files")


if __name__ == "__main__":
    main()
