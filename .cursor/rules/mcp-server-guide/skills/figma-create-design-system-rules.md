# Skill: figma-create-design-system-rules

Generate project-specific rules for Figma-to-code consistency.

## Steps

1. If available, call `plugin-figma-figma/create_design_system_rules`.
2. Analyze current project structure:
   - component directories
   - styling approach
   - design tokens
   - import and naming conventions
3. Write actionable rules with explicit paths and patterns.
4. Save rules in project rule files and verify with a sample Figma task.

## Fallback behavior

- If plugin tool is unavailable/quota-limited, manually author rules from codebase conventions.
