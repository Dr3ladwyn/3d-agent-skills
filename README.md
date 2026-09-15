# 3D Agent Skills

<p align="center">
  <b>Production framework for AI agents that work like professional CG artists, technical directors and art supervisors.</b>
</p>

## What is 3D Agent Skills?

`3d-agent-skills` is an open-source production framework for autonomous AI agents working in 3D content creation.

It is not a prompt collection and not only a tool bridge. It provides the professional knowledge layer required for AI agents to reason through real CG workflows.

The goal:

> Give AI agents the workflow, standards and decision-making process of a professional 3D studio.

---

## Architecture

```text
User Creative Task
        |
        v
CG Supervisor Agent
        |
        +----------------+
        | Specialist Team |
        +----------------+
        |
        + Character Artist
        + Environment Artist
        + Modeler
        + Sculptor
        + LookDev Artist
        + Lighting Artist
        + Render TD
        + Quality Reviewer
        |
        v
Blender / ZBrush / Houdini / Unreal
```

---

## Features

### Agent System

Production roles:

- CG Supervisor
- Character Artist
- Environment Artist
- Technical Director
- Look Development Artist
- Render Supervisor
- Quality Reviewer

### Production Skills

Current Blender foundation:

- Modeling
- Sculpting
- Retopology
- UV workflows
- Materials
- LookDev
- Lighting
- Camera
- Rendering
- Python automation
- Geometry Nodes
- Asset management

### Pipeline System

Built-in production pipelines:

- AAA Character Production
- Product Visualization
- Environment Production
- Cinematic Workflows

### Quality Evaluation

Agents validate:

- silhouette
- topology
- UV quality
- materials
- lighting
- rendering
- production readiness

---

## Installation

Clone repository:

```bash
git clone https://github.com/Dr3ladwyn/3d-agent-skills
cd 3d-agent-skills
```

Install skills through the included tooling:

```bash
3das list
3das install blender-character-artist
```

---

## Supported AI Harnesses

Designed for:

- Claude Code
- Codex
- OpenCode
- Cursor
- Cline
- Roo Code

---

## Repository Structure

```text
3d-agent-skills/

core/              Production framework
agents/            AI specialist roles
skills/            Reusable production skills
software/          DCC integrations
pipelines/         Production workflows
standards/         Quality rules
benchmarks/        Agent evaluations
integrations/      MCP and tooling
registry/          Skill and agent discovery
cli/               Management tools
docs/              Documentation
examples/          Demonstration workflows
```

---

## Roadmap

### v1.0.0

- [x] CG production framework
- [x] Agent architecture
- [x] Skill specification
- [x] Registry system
- [x] Blender production suite
- [x] Evaluation standards
- [x] Harness documentation
- [x] MCP architecture

### v1.x

- CLI package manager
- More Blender automation
- ZBrush workflows
- Houdini workflows
- Unreal workflows
- Substance workflows

### v2.0

- Autonomous CG production teams
- Multi-agent collaboration
- Benchmark suite
- Community skill marketplace

---

## Philosophy

AI should not only know how to operate software.

AI should understand:

- artistic intent
- production constraints
- quality standards
- professional workflows
- iteration cycles

---

## License

Open source project for building the future of AI-assisted computer graphics.
