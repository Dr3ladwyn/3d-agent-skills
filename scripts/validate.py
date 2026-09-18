#!/usr/bin/env python3
"""Validate 3D Agent Skills repository contracts."""
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FRONTMATTER = ["name", "description", "role", "category", "software", "level"]


def read_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"missing frontmatter: {path}")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError(f"invalid frontmatter: {path}")
    return yaml.safe_load(text[4:end]) or {}


def discover_skills():
    return list(ROOT.glob("skills/**/SKILL.md")) + list(ROOT.glob("software/**/SKILL.md")) + list(ROOT.glob("agents/**/SKILL.md"))


def main():
    errors = []
    names = set()
    for path in discover_skills():
        try:
            data = read_frontmatter(path)
            folder = path.parent.name
            for key in REQUIRED_FRONTMATTER:
                if key not in data:
                    errors.append(f"{path}: missing {key}")
            if data.get("name") != folder:
                errors.append(f"{path}: name must equal folder ({folder})")
            if data.get("name") in names:
                errors.append(f"duplicate skill name: {data.get('name')}")
            names.add(data.get("name"))
        except Exception as exc:
            errors.append(str(exc))

    registry = ROOT / "registry" / "skills.yaml"
    if registry.exists():
        data = yaml.safe_load(registry.read_text()) or {}
        registered = {x.get("name") for x in data.get("skills", [])}
        missing = names - registered
        if missing:
            errors.append("registry missing: " + ", ".join(sorted(missing)))

    if errors:
        print("VALIDATION FAILED")
        print("\n".join(errors))
        return 1
    print(f"VALIDATION PASSED: {len(names)} skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
