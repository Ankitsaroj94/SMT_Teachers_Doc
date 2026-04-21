# Skill: figma-implement-design

Translate a Figma node to production code with visual parity.

## Required steps

1. Parse URL (`fileKey`, `nodeId`).
2. Fetch design data:
   - Preferred: `plugin-figma-figma/get_design_context`
   - Fallback: `user-figma-dev-mode-mcp-server/get_figma_data`
3. Fetch screenshot:
   - Preferred: `plugin-figma-figma/get_screenshot`
   - If unavailable on user MCP, use the returned node structure and visible labels.
4. Download referenced images/icons where needed.
5. Implement using project tokens/components (not raw generated Tailwind).
6. Validate spacing, typography, color, and interaction behavior against design.

## Rules

- Reuse existing project components first.
- Do not invent hidden data fields not present in design.
- Preserve UX text labels from Figma where practical.
