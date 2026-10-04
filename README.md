# MCPBinder

![MCPBinder](assets/icon.png)

Bring project context and next steps into Claude and Cursor. MCPBinder lets you read project goals, review tasks and activity, plan work, and record decisions in a shared workspace. Task changes and comments are attributed to the agent connection and appear in the workspace's history.

## Connect

This plugin connects to the hosted MCPBinder server at https://www.mcpbinder.com/api/mcp using OAuth. You need an MCPBinder account and access to a workspace. During authorization, choose the workspace, projects, permissions, and expiry. You can reduce or revoke access in MCPBinder's Agent access settings.

### Claude

For a local Claude Code preview, start Claude with `claude --plugin-dir ./mcpbinder`. Open `/mcp` and authenticate the MCPBinder server. On claude.ai, add the same server URL as a custom connector in Settings → Connectors. Adding the connector alone does not install these skills.

### Cursor

Cursor loads the root `plugin.json` and `mcp.json` as an [Agent Plugin](https://prod.cursor.com/docs/reference/plugins#supported-plugin-formats). The Claude configuration stays in `.claude-plugin/plugin.json` and `.mcp.json`; both hosts share the same six skills and icon.

For a local Cursor preview, clone this repository into `~/.cursor/plugins/local/mcpbinder`. Restart Cursor or run **Developer: Reload Window**, then open **Customize** and confirm all six skills and the MCPBinder server appear. Local plugin imports must be allowed by your team. Authenticate the server through OAuth and select only the workspace, projects, and permissions you intend to share. [Cursor's installation and local-testing instructions](https://prod.cursor.com/docs/plugins#test-plugins-locally) describe the supported controls.

Adding the remote server by itself does not install the skills. Marketplace installation is available after Cursor approves the listing. Before submission, test skill activation, reads and persisted task changes in a synthetic project, permission denial, and connection revocation in Cursor.

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
