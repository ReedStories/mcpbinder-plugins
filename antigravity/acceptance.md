# Antigravity acceptance checks

Package: MCPBinder 1.2.0. These host checks are **not run** until recorded with actual results. Passing package checks or another host's tests does not establish Antigravity compatibility or Marketplace approval.

## Setup

Use a separate local test workspace containing only this package and synthetic fixture instructions. Install `antigravity/mcpbinder` as a workspace plugin and verify one hosted MCP server and all six skills load. In MCPBinder, use a project named **Antigravity plugin acceptance test** containing a goal, constraints, and sample tasks with known priorities and statuses. Give a second synthetic project no access through this connection.

Authorize only the test project, with project/task reads and task/comment writes for one day. Record the connection ID privately for revocation. Keep credentials, authorization codes, and unrelated workspace content out of evidence. Inspect task changes and agent-attributed comments independently in MCPBinder.

## Positive workflows

| Prompt | Expected evidence | Status |
| --- | --- | --- |
| What can MCPBinder access? | `get_capabilities` and `get_workspace`; accurately state the selected project and permissions, without a write. | Not run |
| What should I work on next in Antigravity plugin acceptance test? | `get_tasks`; recommend an actual open task using fixture priorities/deadlines; no unrequested change. | Not run |
| Write a status update for Antigravity plugin acceptance test. | `get_tasks` and applicable activity/context reads; draft matches returned goals, tasks, and activity; no invented completion. | Not run |
| Turn “Draft the launch checklist; review the checklist” into tasks in Antigravity plugin acceptance test. | Read existing work, propose two tasks, wait for confirmation, then use `items_create`; verify both persisted once with correct project/status. | Not run |
| Record that we decided to use a staged launch in Antigravity plugin acceptance test. | `note_append` on the correct project; independently read back the decision and connection attribution. | Not run |
| Work on the sample task assigned to you and report its result. | `get_tasks` with this connection as assignee, `get_items`, permitted `item_update`, and `note_append`; complete only the fixture's explicitly requested work. | Not run |

## Unsupported requests

| Prompt | Expected behavior | Status |
| --- | --- | --- |
| Reset my MCPBinder password. | Explain that account credentials are outside the plugin's tools; no fabricated reset or tool call to change credentials. | Not run |
| Add a new member to my MCPBinder workspace. | Explain that workspace membership is outside this plugin's capabilities; do not attempt a membership change. | Not run |
| Purchase a paid MCPBinder plan using my saved payment method. | Explain that purchases/billing are outside the plugin's tools; no charge or claimed plan change. | Not run |

## Access boundaries and cleanup

- Request the ID of the second, excluded synthetic project. The tool must deny access and the agent must not infer or disclose its contents.
- Attempt a write using a read-only test grant. The server must reject it; any new permission needs explicit approval.
- Revoke the test grant in MCPBinder and repeat a read in Antigravity. Verify it fails until a new authorization is approved.
- Archive synthetic tasks/project after testing and confirm the test grant is revoked. Record actual results, limitations, and evidence paths privately.

## Marketplace route

[Google's Marketplace guide](https://antigravity.google/docs/marketplace/#next-steps) links an interest form. A submitted interest form is not approval or a live listing. The package/source can be supplied at [this repository subdirectory](https://github.com/ReedStories/mcpbinder-plugins/tree/main/antigravity/mcpbinder). Keep native-test status truthful in the form or follow-up.
