# Blender 5.x Skill Upgrade Standard

## Purpose

All Blender skills must target Blender 5.x production workflows. Skills are not only methodologies; they are executable production contracts for AI agents.

## Required Skill Layers

Every Blender skill should contain:

1. Role
2. Purpose
3. Inputs
4. Workflow
5. Blender 5.x Execution
6. bpy/bmesh examples
7. MCP inspection requirements
8. Quality Gates
9. Failure Conditions
10. Iteration Strategy

## Blender 5.x Baseline

Project assumptions:

- Blender 5.x
- Python API 5.x
- Metric units
- Cycles and Eevee render engines
- AgX / OCIO color management

## Scene Initialization

```python
import bpy

scene = bpy.context.scene
scene.unit_settings.system = "METRIC"
scene.unit_settings.scale_length = 1.0
```

## Cycles Baseline

```python
scene.render.engine = "CYCLES"
scene.cycles.samples = 256
scene.cycles.use_denoising = True
```

Adjust samples depending on delivery target.

## Material Requirements

Principled BSDF workflows must explicitly control:

- Base Color
- Roughness
- Metallic
- IOR
- Normal
- Surface variation

## Evidence Requirements

AI agents must provide evidence:

- screenshots
- renders
- object inspection
- dimensions
- modifiers
- materials
- render settings

A saved .blend file without validation evidence is not considered complete.

## MCP Validation

Before approval inspect:

- object names
- collection structure
- world transforms
- mesh statistics
- modifiers
- materials
- camera
- lighting
- render configuration

## Migration Rules

Replace references to Blender 4.x with Blender 5.x.
Remove obsolete API assumptions.
Prefer Blender 5.x Python API examples.
Keep skills deterministic and executable.
