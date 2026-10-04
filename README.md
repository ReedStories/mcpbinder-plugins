# MCPBinder

[![Listed on mcpservers.org](https://mcpservers.org/badge.svg)](https://mcpservers.org/servers/reedstories/mcpbinder-plugins)

![MCPBinder](assets/icon.png)

Bring project context and next steps into your AI assistant. MCPBinder lets you read project goals, review tasks and activity, plan work, and record decisions in a shared workspace. Task changes and comments are attributed to the agent connection and appear in the workspace's history. This repository includes configurations for Claude, Cursor, Kiro, Antigravity, Gemini CLI, and Grok Build; each host's installation, review, and runtime support are separate.

## Connect

This plugin connects to the hosted MCPBinder server at https://www.mcpbinder.com/api/mcp using OAuth. You need an MCPBinder account and access to a workspace. During authorization, choose the workspace, projects, permissions, and expiry. You can reduce or revoke access in MCPBinder's Agent access settings.

### Claude

For a local Claude Code preview, start Claude with `claude --plugin-dir ./mcpbinder`. Open `/mcp` and authenticate the MCPBinder server. On claude.ai, add the same server URL as a custom connector in Settings → Connectors. Adding the connector alone does not install these skills.

### Cursor

Cursor loads the root `plugin.json` and `mcp.json` as an [Agent Plugin](https://prod.cursor.com/docs/reference/plugins#supported-plugin-formats). The Claude configuration stays in `.claude-plugin/plugin.json` and `.mcp.json`; both hosts share the same six skills and icon.

For a local Cursor preview, clone this repository into `~/.cursor/plugins/local/mcpbinder`. Restart Cursor or run **Developer: Reload Window**, then open **Customize** and confirm all six skills and the MCPBinder server appear. Local plugin imports must be allowed by your team. Authenticate the server through OAuth and select only the workspace, projects, and permissions you intend to share. [Cursor's installation and local-testing instructions](https://prod.cursor.com/docs/plugins#test-plugins-locally) describe the supported controls.

Adding the remote server by itself does not install the skills. Marketplace installation is available after Cursor approves the listing. Before submission, test skill activation, reads and persisted task changes in a synthetic project, permission denial, and connection revocation in Cursor.

### Antigravity

Use the self-contained package in [`antigravity/mcpbinder`](antigravity/mcpbinder), which contains Antigravity's `plugin.json` and `mcp_config.json`, the same six skills, icon, and license. Copy that directory into `.agents/plugins/` inside a separate test workspace, or use Antigravity CLI's `agy plugin install` with its absolute path. Authenticate MCPBinder through OAuth in Customizations. See the [package instructions](antigravity/mcpbinder/README.md) and [acceptance checks](antigravity/acceptance.md) before claiming native compatibility.

Maintainers can refresh the package with `python3 scripts/package-antigravity.py`, verify it with `--check`, and export an inspected ZIP with `--archive /absolute/path/to/mcpbinder-antigravity.zip`. The script derives the Antigravity connection and metadata from the shared source and copies the skills without changes. Antigravity's manifest has a different schema from the root Agent Plugins manifest; keep the host package in its own directory. [Google's plugin guide](https://antigravity.google/docs/plugins/) and [Marketplace interest route](https://antigravity.google/docs/marketplace/#next-steps) describe local installation and public listing. Local installation and an interest-form submission do not establish Marketplace approval.

### Gemini CLI

The root `gemini-extension.json` connects the same hosted server using Streamable HTTP and dynamic OAuth discovery. `GEMINI.md` supplies host context, and `skills/` contains the six shared workflows. Install from this repository with `gemini extensions install https://github.com/ReedStories/mcpbinder-plugins`, restart Gemini CLI, and authenticate through `/mcp auth mcpbinder`. [Google's extension reference](https://geminicli.com/docs/extensions/reference/) describes the format and controls.

The manifest excludes the unverified native task forms; ordinary authorized task creation and editing use `item_create` and `item_update`. No API key, client secret, stored token, authorization header, or trust override is included. Gemini CLI runtime testing has been deferred; this listing preparation does not establish OAuth, refresh, skill activation, persisted writes, interactive views, or revocation in Gemini itself.

The [Gemini gallery](https://geminicli.com/docs/extensions/releasing/#list-your-extension-in-the-gallery) discovers public repositories with a root manifest and the `gemini-cli-extension` GitHub topic. Indexing and validation happen externally. Free and Google One users were [transitioned to Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/); Gemini CLI remains a separate route for enterprise licenses and paid API keys.

### Grok Build

Grok Build [reads Claude Code plugin configurations](https://docs.x.ai/build/features/skills-plugins-marketplaces), including this repository's `.claude-plugin/plugin.json`, `.mcp.json`, and shared `skills/`. The only remote MCP endpoint declared here is https://www.mcpbinder.com/api/mcp. Users authenticate through OAuth and choose their MCPBinder workspace, projects, permissions, and expiry; no account credential is bundled. There are no plugin hooks, local MCP processes, install-time scripts, or automatic permission grants.

The [official Grok catalog](https://github.com/xai-org/plugin-marketplace/blob/main/CONTRIBUTING.md) accepts pull requests pointing to an exact public source commit. A catalog submission is a request for review. Native Grok Build testing is deferred, and no native acceptance pass or live catalog listing is claimed.

## MCP Registry publication

The root `server.json` describes the hosted MCPBinder server as `io.github.ReedStories/mcpbinder`. This Registry identifier is separate from the plugin repository name and each host's marketplace review.

Maintainers can run **Actions → Publish MCPBinder to the MCP Registry → Run workflow** from `main`. The workflow uses GitHub Actions identity to authenticate, publishes the reviewed metadata, and verifies the public Registry record. It runs only when manually requested and needs no stored access token. For future releases, review `server.json` and update its version before running the workflow.

## Workflows

- **Get started:** understand the workspace, reachable projects, and approved capabilities.
- **Project update:** draft a status update using goals, tasks, and recent activity.
- **Plan tasks:** turn a brief into a proposed task list and save it after approval.
- **Task focus:** choose the next task using priorities, deadlines, and blockers.
- **Log decision:** record an agreed decision or outcome as a permanent comment.
- **Work assigned task:** pick up a task when asked and report the result with the work.

Try “Summarize the goals and open tasks in my launch project” or “Turn this brief into tasks for my launch project.” Claude Code also exposes commands such as `/mcpbinder:project-update`.

## Permissions and limits

Reading and writing require the corresponding approved MCPBinder permissions. File actions require a separately connected provider account and permission. Task changes may trigger the workspace's configured notifications or webhooks. This plugin does not manage membership, change billing, or reset account credentials. Automatic wakeups for assigned tasks depend on the host and are not established by installing this package. Interactive features vary by Claude product; the core tools also return text results.

MCPBinder is currently for adults 18 or older based in the United States. Reed Stories, LLC operates the service. [Visit MCPBinder](https://www.mcpbinder.com), [get support](https://www.mcpbinder.com/contact), and read the [privacy notice](https://www.mcpbinder.com/privacy) and [terms of service](https://www.mcpbinder.com/terms).
