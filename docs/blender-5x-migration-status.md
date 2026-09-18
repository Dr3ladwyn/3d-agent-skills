# Blender 5.x Migration Status

## Goal

Upgrade all 3D Agent Skills from Blender 4.x assumptions to Blender 5.x production workflows.

## Required skill updates

Every Blender skill must target:

- Blender 5.x Python API
- Cycles and Eevee workflows
- Metric units
- AgX / OCIO color management
- MCP-based inspection and evidence collection

## Execution Layer Requirements

Each skill must contain:

1. Role and production responsibility
2. Inputs and expected outputs
3. Ordered workflow
4. Blender 5.x execution instructions
5. bpy/bmesh examples
6. MCP inspection steps
7. Measurable quality gates
8. Failure recovery strategy

## Blender 5.x Baseline

```python
scene.unit_settings.system = "METRIC"
scene.unit_settings.scale_length = 1.0
scene.render.engine = "CYCLES"
scene.cycles.samples = 256
scene.cycles.use_denoising = True
```

## Evidence Contract

Agents must provide:

- screenshots or renders;
- object inspection data;
- dimensions and transforms;
- modifier state;
- material node validation;
- render settings.

A completed action without evidence is not considered production-ready.

## Migration Order

1. blender-production-master
2. blender-character-artist
3. blender-hard-surface
4. blender-quality-control
5. software/blender atomic skills
6. agents and registries
7. validation schema
