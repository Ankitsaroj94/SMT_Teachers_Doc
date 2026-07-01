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

## Figma MCP failure → screenshot extraction

When **any** Figma MCP read fails for data extraction (`get_design_context`, `get_metadata`, rate limits, auth errors, timeouts, oversized responses):

1. **Take a screenshot** of the same node with `plugin-figma-figma/get_screenshot` (same `fileKey` + `nodeId` from the Figma URL).
2. **Use the screenshot as the source of truth** for visible UI content:
   - Screen title, section headers, filter chip labels
   - Form field labels and placeholders
   - Button / action labels
   - List row text, counts, example values shown in the design
   - Toggle/tab options and selected states
3. Map extracted text into contract fields (`example_response`, `example_request`, `notes`) using project naming (camelCase).
4. **Do not invent** fields, filters, or params not visible in the screenshot.
5. If `get_screenshot` also fails, try user MCP `get_figma_data`; if that fails, ask the user for a screenshot or node URL and pause speculative keys.

Applies to API screen contracts (`api-screens/`), filter JSONs, and any Figma-driven spec work in this repo.
