---
name: "figma"
displayName: "Figma"
description: "Figma workflows for implementation, code connect, and design-system rules with plugin/user MCP fallback."
---

# Figma Power

## Overview

Use this power when the user provides a Figma URL or asks to:

- implement design in code
- map components via Code Connect
- generate design-system rules
- create/update design in Figma

## Plugin tool capabilities (full set)

- Read/context: `get_screenshot`, `get_design_context`, `get_metadata`, `get_variable_defs`, `get_figjam`
- Design generation/edit: `generate_figma_design`, `generate_diagram`, `use_figma`, `search_design_system`, `create_new_file`
- Code Connect: `get_code_connect_map`, `add_code_connect_map`, `get_code_connect_suggestions`, `send_code_connect_mappings`, `get_context_for_code_connect`
- Setup/admin: `create_design_system_rules`, `whoami`

## MCP fallback policy

1. Try `plugin-figma-figma` first.
2. If blocked (rate limit/plan/quota), use `user-figma-dev-mode-mcp-server` and continue with `get_figma_data`.
3. If operation needs plugin-only tools (Code Connect/design-write), capture intent and continue with best-possible read/spec output until plugin access is restored.

## Steering files

- Implement design: `../skills/figma-implement-design.md`
- Code Connect: `../skills/figma-code-connect.md`
- Design system rules: `../skills/figma-create-design-system-rules.md`
