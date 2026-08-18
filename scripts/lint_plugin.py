#!/usr/bin/env python3
"""
Layer 2 convention linter for the Product Velocity plugin.

Checks the repo's own established conventions — the ones that have already
been broken or nearly broken by hand at least once:

  1. plugin.json is valid JSON with the required manifest fields
  2. every skills/*/SKILL.md has valid frontmatter (name, description) and
     name matches its parent directory
  3. every ${CLAUDE_PLUGIN_ROOT}/... reference in skills/**/*.md resolves to
     a real file
  4. every references/... or assets/... path mentioned in a SKILL.md exists
     relative to that skill's own directory
  5. every role reference file (skills/roles/references/*.md, excluding the
     template) has a well-formed Status line: Draft or Active, nothing else
  6. the Draft/Active gating rule is stated in exactly one place
     (skills/roles/SKILL.md) — flags any other file that restates it
  7. a role file marked Status: Active has no leftover [TBD]/TODO placeholder

This is static analysis over markdown/YAML only. It does not call the
Claude API and does not check whether a role's checklist actually changes
model behaviour — that's a separate, heavier eval layer.

Exit code 0 = all checks passed. Exit code 1 = at least one failure.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
ROLES_REF_DIR = SKILLS_DIR / "roles" / "references"
ROLE_TEMPLATE_NAME = "_role-template.md"

# Phrases that must live in exactly one canonical file. Add to this dict
# whenever a new rule is centralised the same way the Draft/Active rule was.
CANONICAL_PHRASES: dict[str, str] = {
    "is what makes a role usable by the plugin at all": "skills/roles/SKILL.md",
}

failures: list[str] = []
warnings: list[str] = []


def fail(msg: str) -> None:
    failures.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def all_markdown_files(base: Path) -> list[Path]:
    return sorted(base.rglob("*.md"))


def check_manifest() -> None:
    manifest_path = ROOT / ".claude-plugin" / "plugin.json"
    if not manifest_path.exists():
        fail(f"Manifest not found: {manifest_path.relative_to(ROOT)}")
        return
    try:
        data = json.loads(manifest_path.read_text())
    except json.JSONDecodeError as e:
        fail(f"plugin.json is not valid JSON: {e}")
        return
    for field in ("name", "version", "description"):
        if not data.get(field):
            fail(f"plugin.json is missing required field: {field}")


def parse_frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end]
    fields: dict[str, str] = {}
    current_key = None
    for line in block.splitlines():
        m = re.match(r"^([a-zA-Z_]+):\s*(.*)$", line)
        if m:
            current_key = m.group(1)
            fields[current_key] = m.group(2)
        elif current_key and line.startswith((" ", "\t")):
            fields[current_key] += " " + line.strip()
    return fields


def check_skill_frontmatter() -> None:
    for skill_dir in sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir()):
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            fail(f"{skill_dir.relative_to(ROOT)} has no SKILL.md")
            continue
        fm = parse_frontmatter(skill_md.read_text())
        rel = skill_md.relative_to(ROOT)
        if fm is None:
            fail(f"{rel}: missing or malformed frontmatter block")
            continue
        if not fm.get("name"):
            fail(f"{rel}: frontmatter missing 'name'")
        elif fm["name"] != skill_dir.name:
            fail(
                f"{rel}: frontmatter name '{fm['name']}' does not match "
                f"directory name '{skill_dir.name}'"
            )
        if not fm.get("description", "").strip():
            fail(f"{rel}: frontmatter missing or empty 'description'")


CLAUDE_PLUGIN_ROOT_RE = re.compile(r"\$\{CLAUDE_PLUGIN_ROOT\}(/[\w\-./]+)")


def check_cross_references() -> None:
    for md_file in all_markdown_files(SKILLS_DIR):
        text = md_file.read_text()
        for match in CLAUDE_PLUGIN_ROOT_RE.finditer(text):
            rel_path = match.group(1).lstrip("/")
            target = ROOT / rel_path
            if not target.exists():
                fail(
                    f"{md_file.relative_to(ROOT)}: reference to "
                    f"${{CLAUDE_PLUGIN_ROOT}}/{rel_path} does not resolve "
                    f"to a real file"
                )


RELATIVE_REF_RE = re.compile(r"`((?:references|assets)/[\w\-./]+)`")


def check_relative_references() -> None:
    for skill_dir in sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir()):
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue
        text = skill_md.read_text()
        for match in RELATIVE_REF_RE.finditer(text):
            rel_path = match.group(1)
            target = skill_dir / rel_path
            if not target.exists():
                fail(
                    f"{skill_md.relative_to(ROOT)}: mentions `{rel_path}` "
                    f"but that file does not exist in {skill_dir.name}/"
                )


STATUS_LINE_RE = re.compile(r"\*Status:\s*(Draft|Active)\b")
BAD_STATUS_RE = re.compile(r"Status:\s*Template\s*/\s*Draft\s*/\s*Active")


def role_reference_files() -> list[Path]:
    if not ROLES_REF_DIR.exists():
        return []
    return sorted(
        p for p in ROLES_REF_DIR.glob("*.md") if p.name != ROLE_TEMPLATE_NAME
    )


def check_role_status_lines() -> None:
    for role_file in role_reference_files():
        text = role_file.read_text()
        rel = role_file.relative_to(ROOT)
        if BAD_STATUS_RE.search(text):
            fail(
                f"{rel}: still has the template's placeholder Status line "
                f"('Template / Draft / Active') instead of a real value"
            )
            continue
        if not STATUS_LINE_RE.search(text):
            fail(
                f"{rel}: no well-formed Status line found "
                f"(expected '*Status: Draft*' or '*Status: Active*')"
            )


def check_dry_canonical_phrases() -> None:
    for phrase, allowed_rel_path in CANONICAL_PHRASES.items():
        allowed_path = (ROOT / allowed_rel_path).resolve()
        for md_file in all_markdown_files(SKILLS_DIR):
            if md_file.resolve() == allowed_path:
                continue
            if phrase in md_file.read_text():
                fail(
                    f"{md_file.relative_to(ROOT)}: restates a rule that "
                    f"should live only in {allowed_rel_path} "
                    f"(matched: \"{phrase}\")"
                )


TBD_RE = re.compile(r"\[TBD\]|\bTODO\b")


def check_no_stray_tbd_in_active_roles() -> None:
    for role_file in role_reference_files():
        text = role_file.read_text()
        status_match = STATUS_LINE_RE.search(text)
        if not status_match or status_match.group(1) != "Active":
            continue
        hits = TBD_RE.findall(text)
        if hits:
            fail(
                f"{role_file.relative_to(ROOT)}: Status is Active but the "
                f"file still has {len(hits)} [TBD]/TODO placeholder(s)"
            )


def main() -> int:
    check_manifest()
    check_skill_frontmatter()
    check_cross_references()
    check_relative_references()
    check_role_status_lines()
    check_dry_canonical_phrases()
    check_no_stray_tbd_in_active_roles()

    for w in warnings:
        print(f"WARN: {w}")

    if failures:
        print(f"\n{len(failures)} convention check(s) failed:\n")
        for f in failures:
            print(f"FAIL: {f}")
        return 1

    print("All convention checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
