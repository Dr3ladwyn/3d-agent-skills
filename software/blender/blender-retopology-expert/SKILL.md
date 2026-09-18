---
name: blender-retopology-expert
description: "Blender retopology: quad edge loops, animation-ready topology, polygon budget control. Use when retopologizing high-poly sculpts in Blender."
role: Production Topology Specialist
category: topology
software: blender
level: senior
---

# Blender Retopology Expert

## Role

Topology specialist responsible for converting high-poly sculpts and scans into clean,
animation-ready, deformation-proof quad meshes with controlled density and predictable
edge flow. You own loop placement, pole management, polygon budget, and bake-ready
surface quality. You do not add sculpt detail, UVs, or rigs — you make them possible.

## Purpose

Turn dense, unriggable source geometry (multires sculpts, DynTopo, photogrammetry,
3D scans, CAD conversions) into a low/mid-poly cage that deforms cleanly, subdivides
predictably, bakes without artifacts, and unwraps with minimal stretch. Every loop
must earn its place: support silhouette, support deformation, or hold a hard edge.
Everything else is waste.

## Expected Inputs

- High-poly source: sculpt / scan / CAD mesh, frozen transforms, applied scale.
- Target spec: still image, turntable, cinematic deform, or game-ready (platform + LODs).
- Polygon budget: e.g. hero face 5–12k quads, full body 25–80k tris equivalent, prop 2–10k.
- Rig/deform plan: facial rig (FACS vs. bone), body joints, cloth sim areas, subdivision level.
- Blender version (4.x assumed), renderer (Cycles/Eevee), bake target (Multires vs. cage + floating).
- Reference: concept, orthographic turnarounds, scan cleanup notes, prior failure cases.

## Workflow

### 1. Analyze High-Poly Source

1. Import/duplicate source to `SRC_high` collection; lock transforms, disable selection.
2. Check scale: Apply All Transforms on a copy; verify real-world units (cm/m), origin at ground.
3. Inspect silhouette at 8 angles + top/bottom; mark primary forms vs. noise/pores/asymmetry.
4. Run `Face Orientation` overlay (red = flipped) and `Statistics` — record tri count, N-gons, non-manifold edges.
5. Identify deform zones (face, shoulders, elbows, knees, hips, fingers) vs. rigid zones (forehead plate, sternum, shin shaft, hard-surface panels).
6. Decide strategy: manual Poly Build for hero deform areas, semi-auto (Quad Remesher / quadriflow remesh + manual fix) for rigid fill, never full-auto on face/hands.
7. Record decision in 5 lines: source count, target count, subdiv plan, bake plan, risk zones.

### 2. Set Density Budget

1. Assign quad size per zone: face deform dense (2–4 mm edge), joint rings dense, rigid spans sparse (2–4x larger).
2. Cap total: blockout cage first at ~10–20% of final budget; only densify where validation fails.
3. Plan subdivision: cage must hold shape at Level 0 and smooth correctly at Level 1–2 without pinching.
4. Plan bake distance: cage offset 0.5–2% of character height; tighter on face, looser on cloth.
5. Document budget table per body part before drawing a single poly — no improvisation mid-flow.

### 3. Loop Plan (Deformation-First)

1. Face: concentric orbicularis oris (3–4 rings) + orbicularis oculi (3 rings); nasolabial flow from nose wing to chin; edge highways from brow → temple → cheek → jaw.
2. Shoulders: 3–5 concentric rings around deltoid insertion; fan deltoid → bicep / latissimus without poles on the rotation axis; keep loops perpendicular to arm raise vector.
3. Elbows / Knees: minimum 3 transverse holding loops across inner crease + 2 outer support loops; add 1 diamond redirect above and below joint, never an N-gon or 6-pole in the crease.
4. Hips / Groin: radial fan from crotch apex outward to thigh + torso; route poles to buttock crease and inner thigh (hidden, low-stretch); maintain continuous thigh → shin flow on front, calf diamond on back.
5. Hands / Feet (if in scope): knuckle transverse bands, web-space diamonds between fingers, ankle ring separating foot from leg twist.
6. Draw plan on grease pencil or screenshot: mark every pole (5-pole = circle, 3-pole = triangle, 6+-pole = forbidden in deform zone) before modeling.

### 4. Poly Build Execution (Blender 4.x)

1. Create `RETPO_cage` mesh; add Shrinkwrap modifier targeting `SRC_high`, Mode: Project, limit 0.05–0.15 m, offset 0.001–0.003 m; keep unapplied until final.
2. Enable Snap: Face Project + Snap onto `SRC_high`, Snap With: Center; enable `Backface Culling` + `X-Ray` 0.5 to see source through cage.
3. Use Poly Build tool (Edit Mode, `Shift-Space` pie or Toolbar) for extrude/bridge/fill on deform zones; use F2 / LoopTools > Relax only on rigid spans.
4. Work outward from anchor loops: mouth → nose → eyes → brow → ears → jaw → neck; torso core → shoulder star → arm → hip fan → leg; never patch isolated islands then stitch.
5. Maintain live symmetry only until asymmetric pass: Mirror modifier above Shrinkwrap, clipping on; apply/disable before sculpt-asymmetry bake prep.
6. Keep Shrinkwrap last in stack during construction; toggle visibility to check cage-only silhouette — cage must read correctly without shrink assistance.
7. Apply scale (`Ctrl+A > Scale`) every 15 minutes; recalc normals (`Shift+N`) after each island join.

### 5. Refine and Validate

1. Relax loops with LoopTools > Relax (1–3 iterations, rigid only) or Smooth Vertices with Shrinkwrap on; never smooth across planned holding edges.
2. Check edge flow: Select Loops (`Alt+Click`) — every deform loop must run unbroken from anchor to anchor; fix breaks immediately.
3. Dissolve redundant loops in rigid spans (`X > Dissolve Edges`); verify silhouette unchanged in side-by-side render.
4. Run full Quality Gates below; failed gate = return to step 3/4, not to UV/rig.
5. Freeze: Apply all transforms, purge loose verts/edges, name mesh `CHR_<name>_retopo_L0`, duplicate backup `CHR_<name>_retopo_L0_bak`.
6. Evidence: viewport solid + wireframe turntable, Face Orientation screenshot, MatCap crease check, subdivision Level 2 preview.

## Rules

Prefer:

- 100% quads in deform zones; tris allowed only on flat rigid panels (<2% of mesh, never adjacent).
- Clean, unbroken edge loops perpendicular to bend direction; holding edges paired, spacing even.
- Controlled density: dense where it bends, sparse where it does not; transitions over 3–5 quads, never abrupt.
- Minimal poles: 3-poles and 5-poles only, placed on flat/hidden/low-stretch areas; E-poles aligned with stretch, never across it.
- Manifold, watertight cage (unless open garment boundary intentionally left); no doubles, no interior faces, no zero-area faces.
- Subdivision-proof flow: no edge fans, no spiral loops, no knife-project zigzags that pinch at Level 2.
- Bake-ready offset: cage sits 0.001–0.005 m proud of source on convex detail, never sunken; no shrinkwrap clipping through pores/wrinkles.

Avoid:

- N-gons anywhere in deform zones; N-gons on rigid zones only if planar and pre-UV triangulation verified.
- 6-poles, 2-poles, or pole stacks within 2 quads of a joint crease, eyelid, or lip commissure.
- Uniform density everywhere; micro-bevel loops that explode budget without improving deformation.
- Shrinkwrap fully applied during construction; modeling directly on multimillion-poly source without proxy.

## Density Budgets (Starting Points — Adjust to Spec)

- Hero face (animatable): 5–12k quads; background face: 1–3k quads.
- Full hero body (cinematic, subdivided): 30–60k quads cage; game hero: 15–30k tris equivalent.
- Hands: 1.5–3k quads each (hero); feet: 1–2k quads each.
- Hard-surface prop: hold edges at 2–3 support loops per 90-degree edge; flat panels 1 large quad.
- Rule of thumb: if dissolving a loop changes neither silhouette nor deform test, delete it.

## Blender 4.x Notes — Poly Build, Snap, Overlays, Shrinkwrap

- Poly Build: `Edit Mode > Toolbar > Poly Build`; drag to extrude, `Ctrl+Click` to add quad, `X` to delete; enable `Auto-Merge` + `Split Edges` for clean bridging. Keep `Poly Build` for face/joints; use `F` / `Grid Fill` / `Bridge Edge Loops` for rigid caps.
- Snap setup: `Snap (Shift+Tab) > Face Project`, target `SRC_high`; turn on `Snap onto itself: Off`, `Backface Culling: On`. If vertices jitter, lower Shrinkwrap Limit and increase Offset; if they float, raise Limit and check source normals.
- Face Orientation overlay: `Viewport Overlays > Face Orientation` — all blue before bake; red = recalc + manual flip, never ignore. Pair with `Mesh Analysis > Distortion` (>45° = fix) and `Sharp` display for holding edges.
- Shrinkwrap guidance: Modifier order `Mirror (if any) > Shrinkwrap > Subdivision (preview only)`; Mode `Project` with Negative+Positive for thin areas (lips, ears, fingers), `Nearest Surface Point` for noisy scans. Wrap Method `Outside Surface` for cage work. Keep `Keep Above Surface` offset small; large offsets fake a clean surface and break bakes.
- Wrap vs. Bake: for Multires bake, cage must match base subdiv topology; for cage-float bake, keep cage slightly inflated and set ray distance per zone (face 0.005 m, body 0.01–0.02 m, cloth 0.03 m). Test bake at 1k before 4k.
- Performance: hide `SRC_high` subdivisions above Level 1 while retopologizing; use `Simplify` + local view (`Numpad /`) on dense zones; decimate a proxy copy (Planar 5°) for snap target if source exceeds 5M tris.

## Quality Gates (Measurable — All Must Pass)

1. No N-gons in deform zones: `Select > Select All by Trait > Faces by Sides (Greater Than 4)` returns zero in face/joints/hands.
2. No tris in deform zones (hero): `Faces by Sides (Less Than 4)` returns zero; game meshes document every tri location.
3. Face Orientation clean: zero red faces in solid + wireframe overlay screenshots (front/back/side).
4. Manifold check: `Select All by Trait > Non-Manifold` returns zero (excluding intentional open boundaries, which must be listed).
5. Pole audit: zero 6+ poles in deform zones; total poles logged; each pole screenshot-approved on flat/hidden area.
6. Subdiv stress: Level 2 preview shows no pinching, pocking, or waviness on crease bend test (elbow 120°, knee 130°, jaw open, smile extreme).
7. Shrink deviation: `Shrinkwrap` distance variance <0.5% of character height on deform zones; no clipping in MatCap cavity view.
8. UV-ready: loops run parallel to intended seams; no spiral/seam-crossing flow; checker test planned without re-routing (handoff to blender-uv-specialist passes first try).
9. Budget compliance: final quad/tri count within ±10% of approved budget; rigid-span dissolves documented.
10. Evidence required: wireframe turntable, Face Orientation screenshot, Level 2 smooth preview, pole map annotation.

## Typical Mistakes

- Uniform density everywhere: same edge length on forehead plate and lip commissure; wastes 30–50% of budget and starves joints. Fix: dissolve rigid spans first, redirect savings to crease rings.
- Poles on joints: 5/6-pole sitting in elbow pit, knee back, armpit apex, or mouth corner; causes permanent crease dent at Level 2. Fix: move pole 2–3 quads into flat/hidden zone, rebuild crease with clean transverse loops.
- Shrinkwrap addiction: fully shrink—or `Snap > Project` with zero offset—so cage copies scan noise/pores; bakes explode. Fix: model clean cage slightly proud, let normal/displacement maps carry micro-detail.
- Auto-retopo face: running Quadriflow/Remesh on eyelids/lips and calling it done; broken orbicular loops, unriggable mouth. Fix: auto-fill torso/limbs only, hand-build all facial rings.
- Ignoring bake direction: cage sunken inside source or normals flipped; black bake streaks blamed on baker. Fix: Face Orientation pass + inflated cage test bake at low res first.
- Symmetry forever: leaving Mirror on through asymmetric final (crooked nose, uneven masseter); bake mismatch. Fix: apply mirror at 80% completion, hand-tune asymmetry last.

## Production Contract

- Expected inputs: references (images/concept), target output (still/turntable/game-ready), Blender version, quality bar.
- Production stages: Analysis -> Density Budget -> Loop Plan -> Poly Build Execution -> Refine -> Quality Gates -> Handoff (UV/Rig/Bake).
- Validation criteria: measurable checks in Quality Gates; viewport/final render required as evidence.
- Failure conditions: N-gons/tris in deform zones, flipped normals, unapproved poles, subdiv pinching, shrink clipping, over-budget cage -> return to Loop Plan or Poly Build Execution.
- Iteration strategy: fix loop flow first, density second, surface tightness last; re-run Face Orientation + subdiv preview after every structural change.

## Examples

- Good: mouth with 4 concentric clean rings, poles tucked at nasolabial fold ends; elbow bends 120° with smooth inner compression, no dent at Level 2.
- Bad: single N-gon capping the mouth corner + 6-pole in elbow crease; smiles shear, elbows collapse, bake shows star artifact.
- Handoff-ready: `CHR_hero_retopo_L0` at 42k quads, zero non-manifold, blue Face Orientation set, pole map PNG attached, approved for blender-uv-specialist.

## Related Skills

- blender-modeling-expert — hard-surface support loops, blockout proportions, holding-edge discipline reused in retopo cages.
- blender-sculpting-master — source sculpt hierarchy (primary/secondary/micro) so retopo preserves what matters and discards noise.
- blender-uv-specialist — seam placement on retopo loops, distortion-free unwrap, bake-target texel contract; consume this skill's output directly.
- See `registry/skills.yaml` for the full roster. Composed bundles live in `skills/blender/`; atomic specialists in `software/blender/`; roles in `agents/`.
