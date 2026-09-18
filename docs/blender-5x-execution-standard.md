# Blender 5.x Execution Standard

## Purpose

All Blender skills in this repository target Blender 5.x production workflows.
Skills must provide both artistic methodology and executable technical guidance.

## Runtime Contract

Target environment:

- Blender 5.x
- Python API 5.x
- Cycles and Eevee rendering
- Metric units
- AgX / OCIO compatible color management

## Scene Initialization

Use explicit scene configuration before production work:

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

Adjust samples according to delivery requirements.

## Material Requirements

Production materials should expose:

- Base Color
- Roughness
- Metallic
- Normal
- IOR where relevant

Use Principled BSDF nodes and validate under neutral and final lighting.

## Evidence Requirements

Every skill execution should produce evidence:

- viewport screenshot
- rendered output
- object statistics
- modifier state
- material inspection when applicable

## MCP Validation

When Blender MCP is available, validate:

- object names
- world transforms
- dimensions
- modifiers
- materials
- render settings

## Quality Rule

No skill is complete when it only describes intent. A production skill must define:

1. Decision workflow
2. Blender execution
3. Validation criteria
4. Failure recovery
