#!/usr/bin/env python3
"""Validate Filters_teacher catalog and sync index metadata."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIGMA_FILE = "iv4SFTxeHwgBYQ6TNhydaL"
FIGMA_CATALOG = "1837:16870"
REQUIRED = {
    "screen",
    "description",
    "figmaNodeId",
    "request",
    "response",
    "example_request",
    "example_response",
    "notes",
}


def figma_url(nid: str) -> str:
    return f"https://www.figma.com/design/{FIGMA_FILE}/Shriconnect-Staff-App?node-id={nid.replace(':', '-')}"


def shape_keys(obj):
    """Compare JSON key structure; ignore scalar type differences."""
    if isinstance(obj, dict):
        return {k: shape_keys(v) for k, v in sorted(obj.items())}
    if isinstance(obj, list):
        if not obj:
            return []
        merged = {}
        for item in obj:
            if isinstance(item, dict):
                for k, v in item.items():
                    merged[k] = shape_keys(v)
        return [merged] if merged else []
    return "scalar"


def filter_slug(filename: str) -> str:
    m = re.match(r"^.+--(.+)\.json$", filename)
    return m.group(1) if m else filename.replace(".json", "")


def main() -> int:
    errors = []
    filter_files = sorted(
        p for p in ROOT.rglob("*.json") if not p.name.startswith("_")
    )

    filters_meta = []
    for p in filter_files:
        rel = str(p.relative_to(ROOT))
        try:
            data = json.loads(p.read_text())
        except json.JSONDecodeError as exc:
            errors.append(f"{rel}: invalid JSON: {exc}")
            continue

        missing = REQUIRED - set(data)
        if missing:
            errors.append(f"{rel}: missing keys {sorted(missing)}")

        resp = data.get("response")
        ex_resp = data.get("example_response")
        if shape_keys(resp) != shape_keys(ex_resp):
            errors.append(f"{rel}: response/example_response key mismatch")

        notes = data.get("notes", {})
        filters_meta.append(
            {
                "contractFile": rel,
                "filterId": p.stem,
                "filterSlug": filter_slug(p.name),
                "figmaNodeId": data.get("figmaNodeId"),
                "screen": data.get("screen"),
                "figmaUrl": figma_url(data.get("figmaNodeId", FIGMA_CATALOG)),
                "module": rel.split("/")[0],
                "dependsOn": notes.get("dependsOn", []),
                "mapsToField": notes.get("usage", ""),
                "usedByModules": notes.get("usedByModules", []),
            }
        )

    # duplicate slug per module (allowed when notes.uiVariants documents variants)
    by_mod_slug = {}
    for entry in filters_meta:
        key = (entry["module"], entry["filterSlug"])
        by_mod_slug.setdefault(key, []).append(entry["contractFile"])
    for key, files in by_mod_slug.items():
        if len(files) > 1:
            # class-filter duplicates across modules are intentional module copies
            if key[1] in {"class-filter", "subject-filter", "form-filter"}:
                continue
            errors.append(f"duplicate filterSlug {key}: {files}")

    index_path = ROOT / "_figma-filter-index.json"
    index_path.write_text(
        json.dumps(
            {
                "figmaFileKey": FIGMA_FILE,
                "figmaCatalogRoot": FIGMA_CATALOG,
                "figmaCatalogUrl": figma_url(FIGMA_CATALOG),
                "filters": filters_meta,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n"
    )

    dep_path = ROOT / "_filter-dependency-map.json"
    dep = json.loads(dep_path.read_text())
    dep["filters"] = filters_meta
    dep_path.write_text(json.dumps(dep, indent=2, ensure_ascii=False) + "\n")

    print(f"Validated {len(filter_files)} filter contracts")
    if errors:
        print("ERRORS:")
        for err in errors:
            print(f"  {err}")
        return 1
    print("All checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
