# Skill: figma-generate-design

Create/update screen layouts in Figma from requirements or code.

## Preferred tools

- `plugin-figma-figma/generate_figma_design`
- `plugin-figma-figma/search_design_system`
- `plugin-figma-figma/use_figma`

## Fallback on user MCP

- User MCP does not currently expose design-write tools.
- If plugin server is blocked, provide a structured layer/spec output and pause for plugin access restoration before canvas writes.

## Rules

- Build sections incrementally.
- Reuse design-system tokens/components.
- Avoid hardcoded color/spacing values when token equivalents exist.
