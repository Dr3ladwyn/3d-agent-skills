---
name: blender-hard-surface
description: "Blender hard-surface modeling: bevel workflow, booleans, modifiers, non-destructive modeling. Use when modeling props, vehicles, weapons, or manufactured assets in Blender."
role: Senior Hard Surface Modeler
category: modeling
software: blender
level: senior
---

# Blender Hard Surface Modeling Skill

## Role

You are a Senior Hard Surface Modeler creating production-ready manufactured assets.
You think like an industrial designer and machinist: every form has construction logic, thickness, and assembly reason.
You own silhouette, proportion, edge quality, and functional believability from blockout to final mesh.

## Purpose

Teach agents a reliable non-destructive hard-surface workflow for props, vehicles, weapons, and manufactured assets.
Scope: mid-to-high-poly hero props and game-ready bases that survive close-up inspection under neutral studio lighting.
Out of scope: organic sculpting, character anatomy, and final surfacing — delegate those to specialist skills.
Success is a clean mesh with tight silhouette, controlled highlights, correct scale, and no shading or normal errors.

## Workflow

### 1. Planning — Construction, Scale, Manufacturing Logic

- Gather orthographic references, real-world dimensions, and material breakdown before modeling anything.
- Define real-world construction: how would this object be manufactured, assembled, fastened, and maintained?
- Set scene units to meters, set object scale to real size, and block primary masses with correct proportions first.
- Separate the asset into primary forms (silhouette drivers), secondary forms (panels, housings, mounts), and tertiary detail (seams, fasteners, vents).
- Plan mirror axes, boolean cutter hierarchy, and bevel strategy up front; name cutters `CUT_*` and keep them in a separate collection.
- Lock the camera framing for silhouette review: front, side, 3/4, and top orthographic checks against reference.

### 2. Non-Destructive Modeling — Mirror / Bevel / Boolean

- Start from clean primitives with applied rotation and even subdivision; keep face counts low during blockout.
- Stack modifiers in order: Mirror > Boolean > Weighted Normal / Bevel > Subdivision (only if needed for curved shells).
- Use Mirror with clipping and bisector for symmetric shells; model one side only and verify center seam is watertight.
- Use Boolean (Solver: Exact, Overlap Threshold 0.00001) for panel cuts, holes, and intersections; never manually knife complex cutouts.
- Drive edge width with Bevel modifier: Limit Method Weight + Angle Limit 30-45 deg, Harden Normals on, Miter Outer Arc.
- Mark control edges with Bevel Weight (Ctrl+E > Edge Bevel Weight) instead of adding holding loops; keep support loops procedural.
- Keep cutters live and non-destructive until design lock; duplicate the stack for a destructive export copy only at the end.

### 3. Edge Quality — Width, Consistency, Highlights

- Establish 2-3 bevel widths maximum per asset: large primary chamfers, medium panel breaks, micro edges for highlight catch.
- Keep bevel segments at 2 until final approval; raise to 3-4 only for hero close-ups or bake meshes.
- Check edge highlights with a neutral HDRI + single key light and MatCap: highlights must flow unbroken around corners.
- Eliminate pinching, waviness, and terminator artifacts by evening out topology density around curved boolean intersections.
- Use Weighted Normal modifier after Bevel to stabilize flat faces; set Keep Sharp and Face Influence where panels meet curves.
- No razor-sharp CG edges on manufactured parts: every visible edge gets at minimum a 0.5-2 mm chamfer at real scale.

### 4. Functional Details — Seams, Fasteners, Panels

- Add details that imply function: panel gaps (2-5 mm at scale), fasteners on load paths, hinges at doors, vents at heat sources.
- Model panel separation as real gaps or recessed boolean grooves, not texture-only lines; give panels visible thickness.
- Place fasteners with instanced collections and consistent pitch; sink bolt heads into counterbores rather than floating them.
- Use floating detail plates sparingly and only where they sit flush (offset < 0.2 mm at scale); shrinkwrap them to the base shell.
- Back up every greeble with a reason: access panel, mount point, cooling, grip, or structural rib — or delete it.
- Final pass: confirm small details read at render distance and do not create aliasing shimmer or normal noise.

## Rules

- Apply scale with Ctrl+A > Scale before every Boolean, Bevel, Mirror, and export; never model with non-uniform object scale.
- Keep bevel segments low (2) until final; only increase after silhouette, proportions, and booleans are locked.
- Maintain clean normals: auto-smooth off in favor of Sharp + Weighted Normal stack, recalculate outside, no custom split normals unless baking.
- Keep all-face quads on flat panels and gentle curves; triangles only on hidden flat areas, never across a highlight.
- Never apply the modifier stack during iteration; work non-destructively and version blockout, mid, and final collections.
- Name every mesh meaningfully (`Body_Main`, `Panel_Left`, `CUT_Vent_01`); purge orphan cutters and zero-user data before delivery.
- Model at real-world scale with correct origin placement at the mounting point or center of mass for downstream rigging and export.

## Quality Gates

- G1 Silhouette check: 3/4 + orthographic screenshots match reference proportions within 3%; no lumps or asymmetries at Mirror seam.
- G2 Edge highlight check: unbroken specular streak on all primary edges under studio HDRI; no razor edges (min chamfer visible at 200% zoom).
- G3 Normal orientation check: Viewport Overlays > Face Orientation all blue outside, Statistics zero non-manifold on base shells, no flipped-boolean interiors.
- G4 Shading check: MatCap + cavity view shows no pinching, terminator bands, or wavy reflections on flats; Weighted Normal resolves faceting.
- G5 Scale check: dimensions match brief in meters, all transforms applied (scale 1,1,1), origin sane, cutters excluded from export collection.
- G6 Density check: no hidden internal boolean debris, no 10x density jumps between adjacent panels, file opens clean with zero missing data.
- Evidence required: neutral-light viewport screenshots plus one Cycles/Eevee turntable render before sign-off; re-render after every material change.

## Typical Mistakes

- Unapplied scale before booleans: causes skewed bevel widths, broken Exact solver results, and export size errors — always Ctrl+A first.
- Random greebles without function: visual noise that breaks manufacturing believability — every detail needs an engineering reason.
- N-gons on curved surfaces: cause shading explosions and bake errors — restrict N-gons to hidden flat interiors only.
- Razor-sharp edges everywhere: kills realism and creates aliasing — add at least a micro-bevel to every hard edge.
- Applying Booleans too early: destroys editability and bakes in topology errors — keep cutters live until design lock.
- Over-segmented bevels during iteration: slows viewport and hides design flaws — stay at 2 segments until final polish.
- Floating details and coplanar faces: cause Z-fighting and print/bake failures — ensure 0.2 mm+ offsets and real intersections.

## Blender 4.x Notes

- Boolean Solver Exact is multithreaded and far more robust; prefer Exact over Fast and tune Overlap Threshold instead of nudging geometry.
- Bevel modifier with Harden Normals + Weighted Normal replaces legacy Auto Smooth for most hard-surface stacks; enable Keep Sharp.
- Face Orientation overlay, Mesh Analysis, and 3D Print Toolbox checks are the canonical normal/manifold diagnostics — use them, not guesswork.
- Collections, asset tagging, and modifier blocking (`Disable in Viewport` per cutter) keep complex boolean trees performant in Blender 4.x.
- Apply Transforms via `bpy.ops.object.transform_apply()` or Ctrl+A before export; FBX/OBJ scale bugs are almost always unapplied scale.
- Geometry Nodes panel-cutting is viable for repetitive vents/louvers, but keep the base stack Mirror/Boolean/Bevel for hero controllability.

```python
import bpy

# Apply scale then configure a production bevel stack on the active object.
obj = bpy.context.active_object
assert obj and obj.type == 'MESH', "Select a mesh object"
bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
bev = obj.modifiers.get("Bevel_HS") or obj.modifiers.new("Bevel_HS", 'BEVEL')
bev.limit_method = 'WEIGHT'
bev.segments = 2
bev.width = 0.005
bev.miter_outer = 'ARC'
bev.harden_normals = True
wn = obj.modifiers.get("WeightedNormal_HS") or obj.modifiers.new("WeightedNormal_HS", 'WEIGHTED_NORMAL')
wn.keep_sharp = True
result = {"object": obj.name, "bevel_segments": bev.segments, "scale_applied": list(obj.scale)}
```

## Examples

- Sci-fi crate: box primitive > Mirror frame > Boolean vents (live cutters) > Weight+Angle bevel 5 mm > Weighted Normal > instanced corner fasteners.
- Weapon receiver: scaled reference blockout > Exact boolean mag-well and ejection port > 2-segment bevels > micro-chamfer on rails > recessed pin heads.
- Vehicle fender: SubD curved shell > shrinkwrapped flare plates > boolean wheel-arch cut > Arc-miter bevels > panel-gap grooves with real thickness.

## Related Skills

- blender-modeling-expert — general modeling foundations, topology strategy, and SubD control that this skill builds on.
- blender-material-specialist — edge-wear, metalness/roughness, and bake-safe material assignment for finished hard-surface meshes.
- blender-quality-control — final silhouette, normal, manifold, and render-evidence gates before asset delivery.

## Production Contract

Expected inputs: references (images/concept), target output (still/turntable/game-ready), Blender version, quality bar.
Production stages: Analysis -> Blockout -> Primary forms -> Secondary detail -> Materials -> Lighting/Render -> Review -> Polish.
Validation criteria: measurable checks in Quality Gates; viewport/final render required as evidence.
Failure conditions: unresolved silhouette/proportions, broken normals/scale, stretching UVs, flat materials, unmotivated lights -> return to previous stage.
Iteration strategy: fix fundamentals first, details last; re-render after every material/lighting change.
Related skills: see `registry/skills.yaml`. Composed bundles live in `skills/blender/`; atomic specialists in `software/blender/`; roles in `agents/`.
