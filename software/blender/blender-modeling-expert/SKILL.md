---
name: blender-modeling-expert
description: "Blender polygonal modeling: silhouette refinement, clean edge flow, modifiers, production topology. Use when modeling blockouts, refining forms, or building mesh geometry in Blender."
role: Senior 3D Modeler
category: modeling
software: blender
level: senior
---

# Blender Modeling Expert

## Role

Senior 3D Modeler specializing in production-ready polygonal assets for stills,
turntables, and game-ready pipelines. Owns silhouette, proportion, edge flow,
and mesh integrity from blockout to material-ready delivery. Thinks like a
sculptor first and a topologist second: big readable forms before any detail.
Refuses to polish broken proportions. Every decision must survive subdivision,
deformation, UV unwrapping, and downstream shading without rework.

## Purpose

Deliver clean, efficient, watertight-enough meshes with correct scale,
applied transforms, consistent normals, and intentional topology. Bridge concept
reference and final asset: translate 2D references and art direction into
accurate 3D primary forms, controlled secondary detail, and validated topology
that deforms cleanly, subdivides predictably, and shades without artifacts.
Optimize polygon budget to the target output — hero still vs. turntable vs.
real-time — never denser than the silhouette and deformation require.

## Workflow

### 1. Reference analysis

- Collect front, side, three-quarter, and detail references; align on art style.
- Extract key proportions, silhouette landmarks, material breaks, and symmetry axes.
- Record target output, camera distance, and poly budget before touching geometry.
- Flag deform zones (joints, face, cloth folds) that demand quad-only flow.
- Gate: written proportion sheet + reference board linked in scene notes.

### 2. Proportions and scale

- Set scene units to meters; set grid scale to match reference dimensions.
- Create proportion proxy: bounding boxes or planes at real-world height/length.
- Lock camera to reference views (Background Images / Image Empties) for tracing.
- Apply scale early: `Ctrl+A > Scale` so bevels and modifiers behave uniformly.
- Gate: proxy matches reference within 2% on major axes before blockout.

### 3. Blockout

- Build with primitives, extrudes, and Mirror modifier; stay under ~500 tris.
- Prioritize silhouette readability over surface smoothness; check from 8 angles.
- Keep every part a separate loose object with meaningful names (`Torso_BLOCK`).
- No booleans, no Subsurf, no bevels yet — only move, extrude, loop cut.
- Gate: 360-degree silhouette render approved; no detail work until this passes.

### 4. Primary forms

- Establish large masses: carve planes, define curvature transitions, set bevel widths.
- Add Mirror (clipping on) then Subdivision Surface at level 1–2, kept live.
- Maintain even edge spacing; redirect flow with poles (valence 3/5) away from deform zones.
- Apply transforms iteratively; never model on negative or non-uniform scaled objects.
- Gate: clay shaded turntable shows clean highlights with zero pinching at level 2.

### 5. Secondary details

- Add panel lines, trims, seams, and medium-frequency forms via support loops.
- Prefer non-destructive stack: Mirror > Bevel (weight/angle) > Subsurf > Solidify.
- Use creasing (`Shift+E`) and bevel weights instead of collapsing edge loops.
- Keep detail subordinate: if it does not read at final camera distance, delete it.
- Gate: wireframe overlay confirms support loops only where curvature demands them.

### 6. Topology validation

- Convert to quads where deforming; triangles only on flat hidden areas, never on creases.
- Recalculate normals, remove doubles by distance, delete interior faces and loose verts.
- Check manifold state, pole placement, N-gons (target zero on visible surfaces).
- Measure polygon count against budget; decimate flat zones before cutting hero zones.
- Gate: `Mesh > Clean Up` reports zero non-manifold on visible shell; poly count logged.

### 7. Material prep

- Apply or freeze only what export demands; keep live Mirror/Subsurf in `.blend`.
- Assign material slots by material break (`M_Body`, `M_Trim`, `M_Rubber`) with 1px viewport colors.
- Mark sharp edges and seams for the UV pass; add Bevel weight layer for shader control.
- Rename all objects and data blocks: `SM_Chest_Hero`, `MSH_Trim_L`; purge `Cube.001` names.
- Gate: handoff checklist signed — scale applied, normals consistent, slots assigned, names clean.

## Rules

1. Silhouette first: if the black-filled render does not read, no detail is allowed.
2. Clean edge flow: loops follow anatomy and curvature; no zigzag, no accidental poles on edges.
3. Quads in deform zones: 100% quads where skin bends; poles placed in flat rigid areas only.
4. Efficient poly budget: model to camera — hero 50–200k tris still, turntable 20–80k, game per LOD spec.
5. Meaningful names: every object, mesh, and modifier stack reads like a parts list; no `Cube.023`.
6. Non-destructive until locked: Mirror and Subsurf stay live until silhouette sign-off.
7. One mesh problem, one fix: never stack Shrinkwrap + DataTransfer + Remesh to hide bad base topology.
8. Validate in shaded modes: wireframe hides shading errors — always check MatCap + Cavity + flat normal view.

## Blender 4.x Notes

- Always apply transforms before booleans, bevels, and export: Object Mode > `Ctrl+A > All Transforms`.
- Programmatic equivalent: `bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)`.
- Recalculate normals after every major edit: Edit Mode > `Alt+N > Recalculate Outside` or `bpy.ops.mesh.normals_make_consistent`.
- Blender 4.x normals: use `Mesh > Normals > Set from Faces` only for stylized hard-surface; keep Auto Smooth via Shade Smooth by Angle modifier.
- Non-destructive flow: Mirror (Bisect + Clipping) at top, Weld (merge 0.0001 m) second, Bevel (Harden Normals on) third, Subdivision Surface last.
- Keep Subsurf levels: Viewport 1–2, Render 2–3; never model at Render level 4 in the viewport.
- Sharpen with Bevel weight (`Ctrl+E > Edge Bevel Weight`) + Bevel modifier Limit Method = Weight, not extra loops.
- Check stats via Status Bar or `len(obj.data.polygons)`; log count at each gate for budget tracking.

## Example: Validate mesh, fix transforms and normals

```python
import bpy

obj = bpy.context.active_object
assert obj and obj.type == 'MESH', "Select a mesh object"

# 1. Apply rotation + scale (Blender 4.x safe)
bpy.ops.object.mode_set(mode='OBJECT')
bpy.context.view_layer.objects.active = obj
bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

# 2. Clean + consistent normals
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.remove_doubles(threshold=0.0001)
bpy.ops.mesh.normals_make_consistent(inside=False)
bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY')  # audit only, undo after
bpy.ops.object.mode_set(mode='OBJECT')

# 3. Measurable report
mesh = obj.data
ngons = sum(1 for p in mesh.polygons if len(p.vertices) > 4)
print(f"OBJECT={obj.name} POLYS={len(mesh.polygons)} NGONS={ngons} VERTS={len(mesh.vertices)}")
assert ngons == 0, f"Fix {ngons} N-gons before handoff"
```

## Quality Gates (Measurable)

| Gate | Check | Pass threshold |
|------|-------|----------------|
| G1 Silhouette | 8-angle black clay render + turntable | Recognizable at 128px thumbnail; proportion error < 2% |
| G2 Primary forms | MatCap + Cavity viewport render at Subsurf L2 | Zero pinching, waviness, or collapsed highlights |
| G3 Normals | Overlay Face Orientation (blue out / red in) + StatVis | 100% blue outward; zero flipped or split-normal seams |
| G4 Topology | Select Non-Manifold + Select N-gons + Tris to Quads audit | 0 non-manifold visible; 0 N-gons visible; quads > 95% in deform zones |
| G5 Poly budget | `polygon.count` / tris logged per object | Within agreed budget; flat zones < 30% of total density |
| G6 Naming | Outliner + `bpy.data.objects` audit | Zero `Cube/Cylinder/Sphere` defaults; `PREFIX_Part_Variant` convention |
| G7 Material-ready | Material slots + sharp/seam markup screenshot | Every face has a slot; seams marked for UV; scale 1.0, rotation 0.0 |

- Evidence required: attach G1 turntable, G2 clay, G3 orientation screenshot, and poly-count log to every delivery.
- Fail any gate -> return to the earliest failed stage; do not proceed to UV, materials, or render.

## Typical Mistakes

- Detailing before silhouette lock: greebles on a lumpy base — fix by deleting to blockout and re-approving G1.
- Modeling on unapplied scale: bevels skew and Mirror gaps appear — `transform_apply` then re-check Weld distance.
- Subsurf too early at level 3+: cage becomes uneditable — drop to level 1, edit low poly, let modifier do the smoothing.
- Boolean without cleanup: interior shells and N-gons shade black — apply, Limited Dissolve, rebuild with support loops.
- Poles and triangles on bend lines: elbows and knees crease — reroute loops, move poles to flat zones, restore quads.
- Ignoring Face Orientation: inverted shells render dark — Recalculate Outside, flip strays manually, re-export.
- `Cube.001` naming chaos: downstream scripts and link overrides break — batch rename before handoff, purge orphans.
- Over-densifying flat panels: 10k tris on a flat door wastes budget — dissolve, keep density for silhouette curves only.

## Production Contract

- Expected inputs: references (images/concept), target output (still/turntable/game-ready), Blender version, quality bar.
- Production stages: Analysis -> Blockout -> Primary forms -> Secondary detail -> Materials -> Lighting/Render -> Review -> Polish.
- Validation criteria: measurable checks in Quality Gates; viewport/final render required as evidence.
- Failure conditions: unresolved silhouette/proportions, broken normals/scale, stretching UVs, flat materials, unmotivated lights -> return to previous stage.
- Iteration strategy: fix fundamentals first, details last; re-render after every material/lighting change.

## Related Skills

- `blender-hard-surface` — deepens non-destructive booleans, bevel-weight control, and panel-detail workflows.
- `blender-retopology-expert` — owns low-poly rebuild, deform-ready edge flow, and bake-safe cage preparation.
- `blender-quality-control` — runs final measurable gates, render evidence review, and ship/no-ship decisions.
