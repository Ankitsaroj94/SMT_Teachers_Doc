# Skill: figma-tool-reference

Reference for routing Figma requests to the right MCP tools.

## Use these plugin tools when available

- `get_design_context`, `get_screenshot`, `get_metadata`, `get_variable_defs`, `get_figjam`
- `generate_figma_design`, `generate_diagram`, `use_figma`, `search_design_system`, `create_new_file`
- `get_code_connect_map`, `add_code_connect_map`, `get_code_connect_suggestions`, `send_code_connect_mappings`, `get_context_for_code_connect`
- `create_design_system_rules`, `whoami`

## User MCP coverage

- `get_figma_data`
- `download_figma_images`

## Fallback policy

- Always attempt plugin server first.
- If plugin tools are quota-limited, switch to user MCP for reads.
- For plugin-only actions, provide a precise pending action list and continue with all possible analysis/spec work.
