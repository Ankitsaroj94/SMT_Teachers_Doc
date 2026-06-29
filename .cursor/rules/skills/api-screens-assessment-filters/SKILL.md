---
name: api-screens-assessment-filters
description: >-
  Authors and updates Assessment module filter JSON contracts in api-screens/assessment/filters/.
  Use when creating or editing assessment form/class/subject filter chips, dropdown options,
  SRF backend filter APIs, or filter dependency chains for Assessment and Add Marks flows.
disable-model-invocation: false
---

# Assessment Filter API Contracts

Reference contracts live in `api-screens/assessment/`. Follow `api-screens-contracts.mdc` for general JSON rules.

**Module root (Figma `19230:56644`):** See `api-screens/assessment/README.md`, `assessment-module-map.json`, `_figma-screen-index.json`.

**Filename pattern:** `{node-id}--{screen-slug}.json` (e.g. `filters/7133-150449--assessment-class-filter.json`).

This skill defines the **filter-specific** shape under `api-screens/assessment/filters/`.

## File naming and location

- Path: `api-screens/assessment/filters/`
- Kebab-case filenames: `assessment-{form|class|subject}-filter.json`
- One JSON contract per filter screen

## Required JSON shape

Every assessment filter contract uses this structure:

```json
{
  "screen": "Assessment — {Form|Class|Subject} Filter",
  "description": "Dropdown / bottom-sheet options for the Assessment {Form|Class|Subject} filter chip.",
  "figmaNodeId": "7133:150449",
  "request": {
    "siteId": "number",
    "sessionId": "number",
    "staffId": "number",
    "userSysId": "number",
    "accessLevel": "number"
  },
  "example_request": {
    "siteId": 47,
    "sessionId": 640,
    "staffId": 0,
    "userSysId": 121173,
    "accessLevel": 10
  },
  "response": {
    "data": [
      {
        "id": "string",
        "label": "string"
      }
    ]
  },
  "example_response": {
    "data": []
  },
  "notes": {}
}
```

Rules:

- Include `screen`, `description`, `request`, `response`, `example_response`.
- Add `figmaNodeId` when a Figma URL/node is known (`1234-5678` → `1234:5678`).
- Add `example_request` when backend or SRF sample request values are documented (required for Form filter).
- `response` keys and `example_response` keys must stay fully aligned.
- Use camelCase in contracts; document SRF PascalCase only in `notes`.

## Response normalization

All filter options are returned under `response.data[]`:

| UI field | Purpose |
|----------|---------|
| `id` | Selected value sent downstream (`formId`, `classId`, `subjectId`) |
| `label` | Text shown in the filter chip / list row |

Optional extra fields (only when API or UI needs them):

| Filter | Extra field |
|--------|-------------|
| Form | `formLevel` (number) — sort band from SRF `FormLevel` |
| Class | `section` (string) — section letter from label (e.g. `A` from `XII - A`) |

Do **not** expose raw SRF keys (`FormId`, `FormName`, `ClassId`, etc.) in `response`; map them in `notes.backendMapping`.

## Request fields (UI only)

| Filter | `request` | Notes |
|--------|-----------|-------|
| Form | `siteId`, `sessionId`, `staffId`, `userSysId`, `accessLevel` (number) | From login/session; SRF URL params use PascalCase |
| Class | `formId`, optional `search` | `formId` required when options are form-scoped |
| Subject | `classId` | Required when options are class-scoped |

Add `example_request` on Form filter when SRF sample values are known. Document PascalCase URL names in `notes.backendRequest`.

## Filter dependency chain

Apply selections in order; pass linkage via request params, not duplicated objects:

```
Form (formId) → Class (classId) → Subject (subjectId)
```

`notes.usage` must state which downstream field the selected `id` maps to.

## SRF / backend notes (when spec is provided)

Add to `notes`:

- `authentication`: `OAuth 2.0 bearer token from Login API.`
- `backendRequest`: PascalCase URL params not shown in UI
- `backendMapping`: e.g. `FormId → id, FormName → label, FormLevel → formLevel`
- `errors`: `Errors returned in the response body.`

Form list API (documented):

- **Request (URL, PascalCase):** `SiteId`, `SessionId`, `StaffId`, `UserSysId`, `AccessLevel`
- **Response (root array):** `{ FormId, FormName, FormLevel }` — wrap as `data` and map to camelCase for the app layer
- **Status:** HTTP 200; errors may appear in the body

## Reference implementations

| File | Figma node |
|------|------------|
| `assessment-form-filter.json` | `19230:56644` |
| `7133-150449--assessment-class-filter.json` | `7133:150449` |
| `7133-150532--assessment-subject-filter.json` | `7133:150532` |

Figma file key for Staff App: `iv4SFTxeHwgBYQ6TNhydaL` (Shriconnect Staff App).

## Downstream linkage

- Class/subject filters feed Assessment list and Add Marks setup (`classId`, `subjectId`).
- `add-marks-setup.json` references class and subject filter contracts in `notes.flow`.

When adding a new assessment filter, copy the closest reference file above and adjust `request`, optional response fields, and `notes` only.
