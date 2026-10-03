# MCPBinder

![MCPBinder](assets/icon.png)

Bring project context and next steps into Claude. MCPBinder lets you read project goals, review tasks and activity, plan work, and record decisions in a shared workspace. Task changes and comments are attributed to the agent connection and appear in the workspace's history.

## Connect

This plugin connects to the hosted MCPBinder server at https://www.mcpbinder.com/api/mcp using OAuth. You need an MCPBinder account and access to a workspace. During authorization, choose the workspace, projects, permissions, and expiry. You can reduce or revoke access in MCPBinder's Agent access settings.

For a local Claude Code preview, start Claude with `claude --plugin-dir ./mcpbinder`. Open `/mcp` and authenticate the MCPBinder server. On claude.ai, add the same server URL as a custom connector in Settings → Connectors. Adding the connector alone does not install these skills.

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
