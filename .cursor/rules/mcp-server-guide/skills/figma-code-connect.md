# Skill: figma-code-connect

Map Figma components to code components via Code Connect.

## Required flow

1. Parse URL and normalize `nodeId` to colon format.
2. Use plugin server tools:
   - `get_code_connect_suggestions`
   - Search codebase for candidate components
   - Confirm mappings with user
   - `send_code_connect_mappings`

## Fallback behavior

- If plugin MCP is quota-limited, report that Code Connect cannot be completed through user MCP (user MCP does not expose Code Connect tools).
- Continue with a manual candidate mapping report when possible.

## Mapping quality checks

- Match component props/variants to Figma properties.
- Prefer components in established UI directories.
- Do not auto-map ambiguous matches without confirmation.
