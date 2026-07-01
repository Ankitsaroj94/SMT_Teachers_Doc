# Skill: figma-implement-design

Translate a Figma node to production code with visual parity.

## Required steps

1. Parse URL (`fileKey`, `nodeId`).
2. Fetch design data:
   - Preferred: `plugin-figma-figma/get_design_context`
   - Fallback: `user-figma-dev-mode-mcp-server/get_figma_data`
   - **If design data extraction fails** (rate limit, auth, timeout, oversized): call `plugin-figma-figma/get_screenshot` for the same node and extract visible labels, values, and layout from the screenshot. See `figma-tool-reference.md` → *Figma MCP failure → screenshot extraction*.
3. Fetch screenshot (always for validation; required when step 2 failed):
   - Preferred: `plugin-figma-figma/get_screenshot`
   - If unavailable on user MCP, use the returned node structure and visible labels.
4. Download referenced images/icons where needed.
5. Implement using project tokens/components (not raw generated Tailwind).
6. Validate spacing, typography, color, and interaction behavior against design.

## Rules

- Reuse existing project components first.
- Do not invent hidden data fields not present in design.
- Preserve UX text labels from Figma where practical.
