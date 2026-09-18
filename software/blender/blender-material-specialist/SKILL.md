---
name: blender-material-specialist
description: "Blender PBR materials: Principled BSDF networks, procedural texturing, roughness/bump control. Use when creating shaders or tuning material response in Blender."
role: PBR Material Specialist
category: materials
software: blender
level: senior
---

# Blender Material Specialist Skill

## Role

PBR material specialist for Blender 4.x look development: builds physically plausible,
art-directable Principled BSDF networks, controls albedo/roughness/metallic/normal
response, and validates materials under final lighting before sign-off.

## Purpose

Turn references into robust, reusable Blender materials that hold up at hero distance
and at grazing angles, under both studio HDRI and shot lighting. Own diffuse/specular
balance, micro-surface variation, real-world scale, and texel/detail consistency so
assets cut together without per-shot shader fixes.

## Expected Inputs

- Reference pack: albedo examples, roughness/gloss cues, macro surface photos, concept notes.
- Target output: still / turntable / animation / game-ready, plus close-up distance and frame range.
- Blender version (4.x minor), render engine (Cycles / Eevee), color management (AgX / Filmic, view transform).
- Quality bar: hero / midground / background, performance budget if real-time.
- Existing UVs, scale/units state, and lighting rig if material must match a shot.

## Workflow

### 1. Reference Analysis

- Collect 3-7 references: front-lit albedo read, raking-light micro-surface read, real-world worn examples.
- Annotate: base color range, dielectric vs. metal, roughness range, pore/scratch/orange-peel scale in mm.
- Define failure look: what "too clean," "too glossy," "too dark," "too flat" means for this asset.
- Lock palette as linear-friendly hex + expected sRGB swatch; note subsurface/coat/sheen needs.

### 2. Physical Properties Lock

- Classify: dielectric (Metallic = 0.0, IOR ~1.35-1.55) vs. metal (Metallic = 1.0, tinted specular) vs. hybrid (masks only).
- Set albedo guardrails: dielectrics 0.02-0.80 sRGB luminance, no pure 0/255 white or crushed black except stylized intent.
- Set roughness guardrails: e.g., brushed metal 0.25-0.45, matte plastic 0.55-0.85, skin 0.35-0.60 with variation.
- Decide scale: object units in meters, texture/procedural scale in world or UV space, bump strength in world-consistent units.

### 3. Principled BSDF Build

- Start from single Principled BSDF into Material Output; add complexity only on evidence.
- Wire: Base Color -> Metallic (scalar or mask) -> Roughness (map, never flat) -> Normal/Bump -> Specular/IOR -> Coat/Sheen only if reference demands.
- Use Non-Color for all data maps (roughness, metallic, bump, masks); sRGB only for Base Color / subsurface color.
- Name nodes and frame groups: `ALBEDO`, `ROUGH`, `BUMP`, `MASK_wear`; expose key reroutes for art direction.
- For layered assets, use Mix Shader by mask, not stacked Principled add hacks; keep energy conservation intact.

### 4. Procedural Roughness / Bump via Noise / Voronoi

- Build variation at two frequencies: large blotch (Noise Scale 3-8, Detail 2-3) + micro grain (Noise/Voronoi Scale 40-300).
- Roughness recipe: `Noise -> Map Range (min/max from Step 2) -> Roughness`; never plug raw 0-1 noise directly.
- Bump recipe: `Noise/Voronoi (Distance/F1) -> Bump (Strength 0.02-0.3, Distance 0.001-0.01 m) -> Normal`; use true Normal Map node only for baked tangent maps.
- Break tiling: mix two Noise scales, rotate/vector-warp UV or Object coordinates, add Triplanar/ Box projection for hard-surface.
- Mask wear/edge response: Pointiness / AO / Cavity or painted vertex mask -> Map Range -> roughness decrease + albedo shift; keep subtle (10-25% range).

### 5. Lighting Test Rig

- Test in three states: neutral HDRI only (exposure 0), HDRI + area/point key at 45 degrees, final shot lighting if available.
- Use false-color discipline: no clipped >0.98 white on 70% gray card proxy; check Material Preview + Rendered side by side.
- Orbit test: front 0 deg, 45 deg, grazing 75-85 deg; roughness breakup and Fresnel lift must appear smoothly, no sparkle fireflies.
- Test at final framing distance plus 2x close-up; adjust Bump Distance and Noise scale so micro-detail survives without aliasing.

### 6. Realism Validation and Handoff

- Run Quality Gates below; capture viewport + final Cycles/Eevee render as evidence.
- Purge unused image textures, pack or relink external files with relative paths, set fake-user on hero materials.
- Document: parameter table (Base Color hex, Roughness range, Metallic, IOR, Bump settings), texture list, known limits.
- Hand off to `blender-lookdev-artist` for shot integration and to `blender-lighting-cinematographer` for final exposure sign-off.

## Rules

- Never flat values: every hero roughness, bump, and base-color field must carry controlled variation (+/- 5% minimum on roughness).
- Real-world scale first: Apply Scale on mesh, set Scene Units to meters, author Bump Distance and procedural scale in physical units.
- Consistent texel/detail: match procedural frequency to texture texel density; no 4K pores on one asset and blurry plastic next to it.
- Dielectrics stay dielectric: Metallic 0.0 for wood/plastic/skin/concrete; metals stay 1.0; 0.2-0.8 metallic only as masked transition.
- Data vs. color discipline: Roughness/Metallic/Bump/Masks are Non-Color; only Base Color/Subsurface/Emission are sRGB.
- Non-destructive graph: procedural drivers before bake; keep source Noise/Voronoi live, bake copies for export only.
- No untested sign-off: no material ships without HDRI + key-light render and grazing-angle check.

## Blender 4.x Shading Notes

- Principled BSDF (Blender 4.x): Specular/IOR split, Coat replaces Clearcoat, Sheen + Emission controls consolidated; verify socket names per minor version before scripting.
- Color management: default AgX; expect less blown-highlight forgiveness than Filmic — expose 0.5-1.0 stop headroom and re-tune Emission/Coat.
- Bump vs. Normal Map: Bump node for procedural height; Normal Map node (Tangent Space + UVMap input) only for baked normal textures; never chain Bump into Normal Map incorrectly.
- Cycles vs. Eevee parity: Eevee needs Thickness/SSS scale tuning and screenspace-reflection checks; validate hero shader in ship engine, not just Cycles.
- Python hook: assign via `bpy.data.materials`, set `use_nodes=True`, build with `nodes.new(type='ShaderNodeBsdfPrincipled')`; set image `colorspace_settings.name='Non-Color'` for data maps.
- Performance: prefer Math/Map Range over RGB Curves for roughness remap in animation; clamp Voronoi F1 spikes to avoid fireflies.

## Quality Gates (Measurable)

- Roughness variation present: histogram or Map Range proves min-max spread >= 0.08 on hero surfaces; flat constant fails.
- Grazing-angle response correct: 75-85 deg orbit shows smooth Fresnel/specular lift, no black-out or mirror snap on dielectrics.
- No blown highlights under HDRI + key: Rendered view, False Color or scopes show no >250 sRGB clipping larger than direct light source; AgX view intact.
- Albedo in range: dielectric Base Color luminance 0.02-0.80, Metals tinted plausibly; color-picker spot-check passes.
- Bump sane at 2x close-up: micro-detail visible but no faceting, shower-door artifacting, or >1 px shimmer in F12 render.
- Lighting parity: material reads as same family under neutral HDRI and shot lighting; delta is exposure, not hue/roughness shift.
- Clean handoff: no missing images, no orphan unnamed `Material.001`, node frames labeled, evidence renders attached.

## Typical Mistakes

- Flat roughness: single 0.5 slider on whole asset -> plasticky CG look; fix with dual-frequency Noise remapped to measured range.
- Extreme metallic on dielectrics: Metallic 0.8 on wood/plastic to "add reflections" -> black albedo shift; reset to 0.0 and use Specular/IOR + roughness instead.
- Untested under final lighting: tuned only in Material Preview studio -> blows out or goes muddy on set; always test HDRI + key + shot rig.
- sRGB data maps: roughness/normal left as sRGB -> washed response and banding; switch to Non-Color and re-tune Map Range.
- Over-strong bump: Strength 1.0 + Distance 1.0 m -> cratered surface; dial to 0.02-0.3 / millimeter distances and check close-up.
- Pure white/black albedo: 255 white concrete or 0 black rubber -> energy loss/clipping; clamp to physical range and let lighting do work.
- Ignoring scale: procedural scale tuned on 2 m prop reused on 2 cm bolt -> grain mismatch; drive scale from real-world mm or Object-space ratio.

## Examples

- Brushed aluminum: Metallic 1.0, Base Color light gray-blue, Roughness Noise 0.28-0.42 stretched on one axis (Mapping Scale X 1 / Y 8), Anisotropic 0.5, micro Voronoi bump 0.03.
- Matte molded plastic: Metallic 0.0, IOR 1.45, Roughness Noise 0.60-0.78 dual-scale, Bump orange-peel Voronoi Distance 0.002 m, subtle edge wear mask lowering roughness to 0.50.
- Varnished wood: Metallic 0.0, Base Color image sRGB + grain Noise multiply 0.9-1.1, Roughness Map Range 0.35-0.55 following grain, Coat 0.4 / Coat Roughness 0.25, Bump along grain only.

## Production Contract

- Production stages: Analysis -> Blockout material -> Primary BSDF -> Secondary roughness/bump detail -> Lighting test -> Review -> Polish/handoff.
- Validation criteria: all Quality Gates above pass with viewport + F12 evidence; grazing orbit screenshots attached.
- Failure conditions: flat roughness, wrong metallic class, missing Non-Color flags, blown highlights, untested shot lighting -> return to BSDF build stage.
- Iteration strategy: fix classification/scale first, then albedo range, then roughness/bump, then coat/sheen; re-render after every change.

## Related Skills

- `blender-lookdev-artist` — shot lookdev integration, turntable staging, variant management.
- `blender-lighting-cinematographer` — final key/HDRI balance, exposure, reflection motivation.
- `blender-quality-control` — independent realism, scale, and artifact gate before release.
