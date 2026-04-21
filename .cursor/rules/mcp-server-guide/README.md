# MCP Server Guide

This guide wires Figma skills to both available Figma MCP servers in this workspace:

- `plugin-figma-figma` (official Figma MCP with full toolset)
- `user-figma-dev-mode-mcp-server` (user MCP with `get_figma_data` and image download tools)

## Server selection

- Prefer `plugin-figma-figma` when available.
- If `plugin-figma-figma` is blocked by quota/seat limits, use `user-figma-dev-mode-mcp-server`.

## URL parsing

For links like:

`https://www.figma.com/design/<fileKey>/<name>?node-id=14542-97281`

- `fileKey` = `iv4SFTxeHwgBYQ6TNhydaL`
- `nodeId` = `14542:97281` (convert `-` to `:`)

## Tool mapping

### Official plugin server (`plugin-figma-figma`)
- Read/design context: `get_design_context`, `get_screenshot`, `get_metadata`, `get_variable_defs`, `get_figjam`
- Design generation/edit: `generate_figma_design`, `generate_diagram`, `use_figma`, `create_new_file`, `search_design_system`
- Code Connect: `get_code_connect_suggestions`, `send_code_connect_mappings`, `get_code_connect_map`, `add_code_connect_map`, `get_context_for_code_connect`
- Admin/info: `create_design_system_rules`, `whoami`

### User server (`user-figma-dev-mode-mcp-server`)
- `get_figma_data` (primary fallback read tool)
- `download_figma_images`

## Skills folder

Use the skill docs in `./skills/`:

- `figma-use.md`
- `figma-implement-design.md`
- `figma-generate-design.md`
- `figma-code-connect.md`
- `figma-create-design-system-rules.md`
- `figma-generate-library.md`
- `figma-tool-reference.md`

## Tool coverage note

The plugin tool list above is the default capability set to use when available.
When plugin access is limited by plan/quota, keep working via user MCP read tools and document unsupported operations (especially Code Connect and design writes) instead of stopping.
