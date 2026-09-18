# Product Visualization Pipeline

Pipeline for studio product renders in Blender.

Stages (mirror `registry/pipelines.yaml`):

1. Reference — collect real-world refs, define CM scale, target output.
2. Modeling — `blender-modeling-expert` / `blender-hard-surface`, clean bevels, applied scale.
3. Materials — `blender-material-specialist`, Principled BSDF, procedural roughness/bump.
4. Lighting — `blender-lighting-cinematographer`, key/fill/rim + HDRI, locked camera first.
5. Camera — `blender-camera-director`, focal length language, composition guides.
6. Render — `blender-render-engineer`, Cycles GPU, AgX, denoise, final resolution.
7. Review — `blender-quality-control`, PASS/FAIL gate before delivery.

Standards:

- real-world scale in meters
- no flat materials (roughness variation required)
- every light motivated; readability first
- final render evidence required for approval
