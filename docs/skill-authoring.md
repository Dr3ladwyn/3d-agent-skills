# Skill Authoring Guide

## Purpose

A skill is a production workflow definition for AI agents.

Skills must teach agents how to reason and execute, not only which buttons to press.

## Required Structure

```text
skill-name/
└── SKILL.md
```

## Layer Rule (single source of truth)

- `software/<dcc>/<skill>/` — atomic specialist skills (one craft: modeling, UVs, lighting).
- `skills/<dcc>/<bundle>/` — composed bundles (multi-stage pipelines: production-master, character-artist).
- `agents/<role>-agent/` — roles that orchestrate skills, never duplicate skill bodies.
- Never create the same skill name in two layers. Lighting lives once in `software/blender/blender-lighting-cinematographer/`.

## Frontmatter Contract (required by Claude Code / Codex / OpenCode loaders)

```yaml
---
name: <folder-name-exactly>
description: <one sentence, 3rd person, "Use when..." with trigger keywords first>
role: string
category: string
software: blender
level: junior|mid|senior|expert
---
```

- `name` must equal the folder name (enforced by `scripts/validate.py`).
- `description` must contain `Use when` — skills without it are filtered out by harness loaders.

## Skill Sections

- Role
- Purpose
- Workflow
- Rules
- Quality Checks
- Examples

## Quality Requirements

Every skill should define:

- expected inputs
- production stages
- validation criteria
- failure conditions
- iteration strategy

## Design Principle

Think like a senior production artist. The goal is a reliable autonomous workflow.
