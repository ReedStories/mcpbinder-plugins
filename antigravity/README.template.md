# MCPBinder for Antigravity

![MCPBinder](assets/icon.png)

Package version: {{VERSION}}. [Published source](https://github.com/ReedStories/mcpbinder-plugins/tree/main/antigravity/mcpbinder).

Read project context and manage tasks in MCPBinder, with access you control. This package includes the six shared MCPBinder skills and one hosted MCP server. It is generated from the repository's shared sources; maintainers run `python3 scripts/package-antigravity.py` from the repository root to refresh it.

## Install for a local preview

Copy this entire `mcpbinder` directory into `.agents/plugins/` inside a separate test workspace. Restart Antigravity if needed and inspect the installed plugin, its six skills, and the MCPBinder server in Customizations. Antigravity CLI also supports `agy plugin install /absolute/path/to/antigravity/mcpbinder`. [Google's installation instructions](https://antigravity.google/docs/plugins/) describe the available surfaces.

Use this Antigravity directory rather than the repository root, which contains the Claude and Agent Plugins configurations. Manual installation does not publish a Marketplace listing.

## Connect

You need an MCPBinder account and access to a workspace. In Customizations, choose Authenticate for MCPBinder and complete OAuth in your browser. The server supports dynamic client registration, so no API key or client secret belongs in this package. [Google's OAuth instructions](https://antigravity.google/docs/mcp/#oauth) explain how to return to the app if it requests an authorization code.

MCPBinder's consent screen lets you choose the workspace, projects, permissions, and expiry. For testing, use a synthetic project and the narrow permissions needed for project reads, task changes, and comments. You can reduce or revoke access under MCPBinder's Agent access settings.

## Try the workflows

- Get started: describe the reachable workspace, projects, and approved capabilities.
- Project update: summarize goals, tasks, and recent activity.
- Plan tasks: propose tasks from a brief and save them after confirmation.
- Task focus: prioritize open work by deadlines, priority, and blockers.
- Log decision: record an agreed decision as an attributed comment.
- Work assigned task: handle assigned work when explicitly asked and report the result.

Try “What can MCPBinder access?” or “Summarize the goals and open tasks in my launch project.” Inspect persisted task and comment changes in MCPBinder after testing. Installation alone does not establish automatic background wakeups for assigned tasks.

## Permissions and support

Reading and writing require the corresponding approved MCPBinder permissions. File actions require a separately connected provider account and permission. Task changes may trigger the workspace's configured notifications or webhooks. This plugin does not manage membership, billing, or account credentials. Interactive features depend on host support; core tools also return text results.

MCPBinder is currently for adults 18 or older based in the United States. Reed Stories, LLC operates the service. [Website](https://www.mcpbinder.com) · [Support](https://www.mcpbinder.com/contact) · [Privacy](https://www.mcpbinder.com/privacy) · [Terms](https://www.mcpbinder.com/terms).
