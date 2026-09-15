# Universal Agent Harness Installation

`3d-agent-skills` is designed to be installable across modern AI coding and agent harnesses.

Supported targets:

- Claude Code
- OpenAI Codex
- OpenCode
- Cursor Agent
- Cline
- Roo Code
- Continue
- other SKILL.md compatible agents

## Installation concept

The repository provides portable skills. Each harness receives the same production knowledge base and maps it into its own skill directory.

## Generic installation

```bash
git clone https://github.com/Dr3ladwyn/3d-agent-skills
```

Copy required skills into your agent skills directory.

## Skill format

Every skill follows:

```
SKILL.md
references/
examples/
```

The format is intentionally compatible with emerging agent skill standards.
