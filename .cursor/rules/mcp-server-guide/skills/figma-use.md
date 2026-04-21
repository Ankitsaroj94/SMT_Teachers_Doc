# Skill: figma-use

Use this before any Figma MCP operation.

## Workflow

1. Parse the Figma URL into `fileKey` and `nodeId` (`1-2` -> `1:2`).
2. Prefer `plugin-figma-figma`.
3. If plugin server is blocked by quota/plan, switch to `user-figma-dev-mode-mcp-server`.
4. For reads:
   - Plugin server: `get_design_context` (preferred), fallback `get_metadata`.
   - User server: `get_figma_data`.
5. For assets:
   - Plugin server asset URLs directly, or user server `download_figma_images`.

## Notes

- Do not stop when plugin quota fails if user MCP is available.
- Keep node IDs in colon format for MCP calls.
