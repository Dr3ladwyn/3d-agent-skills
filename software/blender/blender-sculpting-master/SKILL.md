---
name: blender-sculpting-master
description: "Blender sculpting: primary anatomy and silhouette, secondary forms, tertiary details, Multires workflow. Use when sculpting characters, creatures, or organic assets in Blender."
role: Digital Sculptor
category: sculpting
software: blender
level: senior
---

# Blender Sculpting Master

## Role

Digital sculptor for characters, creatures, and organic hero assets.
You own form hierarchy, anatomical believability, and surface quality from blockout to tertiary detail.
You sculpt low-to-high, protect silhouette at every subdivision, and hand off watertight, well-proportioned forms for retopology and texturing.

## Purpose

Deliver production-ready organic sculpts with correct proportions, convincing anatomy, clean volume transitions, and controlled micro-surface.
This skill enforces a leveled workflow: lock primary readability first, then secondary structure, then tertiary detail.
It prevents the classic failure of dense, noisy sculpts built on weak foundations.

## Workflow

### 0. Analysis and Reference Setup

- Collect front/side/back anatomy reference, head/face planes, hand/foot close-ups, and material/skin reference.
- Define scale: set scene units to meters, import scale reference (1.7-1.8 m human), apply scale on base mesh.
- Define deliverable: still, turntable, game-ready high-poly, or film displacement source.
- Establish primary landmarks: height in heads, shoulder/hip ratio, limb segment lengths, head/face proportion grid.

### 1. Blockout — Concept Mass

- Start from low-poly base mesh, skin modifier blockout, or primitive masses joined to correct total height/girth.
- Work at lowest subdivision with Grab, Snake Hook, Clay Strips, and Move at large radius, low strength.
- Establish gesture, balance, weight distribution, and major masses: skull/ribcage/pelvis, limb cylinders, jaw/chin mass.
- Check silhouette every 5-10 strokes: constant 360-degree orbit, pure-black flat MatCap, no detail allowed.
- Gate: recognizable character/gesture in silhouette only, symmetric unless asymmetry is intentional.

### 2. Primary Forms — Proportions / Anatomy / Silhouette

- Refine large landmarks: cranial mass vs. face mass, neck taper, trapezius/deltoid/lat volumes, ribcage ellipse, pelvis wedge.
- Sculpt major bone landmarks: brow ridge, cheekbone arch, jaw angle, clavicles, elbows/knees, Achilles/collar transitions.
- Lock proportions: head units, eye-line mid-head, shoulder width ~2 head widths, arm span ~height.
- Use Multires levels 0-2 only; keep poly density even; use Voxel Remesh or Dyntopo only for concept mass, then retopo.
- Validate with MatCap + neutral lighting: gray Clay or red Wax MatCap, single overhead soft light, no HDRI color.
- Gate: sculpt reads correctly blurred to 3 px, mirrored, and in flat silhouette from 8 turntable angles.

### 3. Secondary Forms — Muscles / Clothing Volumes / Facial Structure

- Layer muscle groups over bone: pectorals, abdominals, obliques, quads/hamstrings/calves, forearm flexor/extensor masses.
- Sculpt fat, tendon, and overlap transitions: muscle insertions pinch, bellies bulge, tendons flatten toward joints.
- Facial structure: eyelid thickness and commissures, nasal alae and nostril wings, philtrum/lip volumes, ear helix/antihelix.
- Clothing/armor volumes: sculpt as separate thickened masses with clear compression folds, tension vs. drape zones.
- Brushes: Clay Strips + Crease for plane breaks, Inflate/Deflate for bellies, Pinch for lids/lips, Smooth at 0.2-0.35 for blends.
- Work Multires levels 2-4; never subdivide to fix a level-1 proportion error — drop down and fix low first.
- Gate: muscle flow correct in relaxed and implied-pose read, face recognizable at neutral expression, cloth volumes sit on body without intersection.

### 4. Tertiary Detail — Pores / Imperfections

- Add skin micro-surface last: pores, fine wrinkles, knuckle creases, lip cracks, scars, calluses, cloth weave only where camera needs it.
- Use low-strength Layer brush, anchored strokes, stencil/alphas at 10-25% strength; break uniformity with variation masks.
- Keep detail frequency consistent with output: film close-up gets full pore pass, game asset gets mid-frequency only, bake rest to normal map.
- Separate detail layer where possible: Multires sculpt layer or separate detail object so director can dial strength.
- Gate: detail invisible at 10% viewport zoom, visible at 100% close-up, no faceting, no alpha stamping repetition.

### 5. Polish, Export, and Handoff

- Final asymmetric pass: subtle left/right variation in face, hands, folds; avoid mirrored CG look.
- Decimate copy for review, keep Multires master untouched; apply transforms, check watertight, fix inverted normals.
- Export high-poly FBX/OBJ plus Multires base for retopology; name LODs and bake targets explicitly.
- Record turntable: 24-48 frames, neutral gray background, MatCap + shaded versions.

## Brushes by Stage

- Blockout: Grab, Snake Hook, Clay Strips (large radius, <0.4 strength), Move, Symmetrize.
- Primary: Clay Strips, Crease, Flatten/Scrape, Fill, Smooth (regular, not enhanced, to preserve volume).
- Secondary: Clay Strips, Pinch, Crease, Inflate/Deflate, Mask + Pose brush for limb adjustments, Elastic Deform for large corrections.
- Tertiary: Layer, Draw Sharp (low strength), Nudge, Thumb brush for pores, Smooth at very low strength for integration.
- Utility: Mask, Box Mask, Hide, Face Sets for isolation; Multires Rebuild Subdivs if topology changes mid-stream.
- Pressure rule: large radius + low strength for form; small radius + low strength for detail; never high strength + small radius on primary.

## Rules

- Never add micro-detail before primary forms are approved — lock silhouette/proportions first, no exceptions.
- Dyntopo for concept mass only, then retopo — never deliver Dyntopo soup as final; rebuild clean base before Multires detailing.
- Always work Multires low-to-high — fix errors at the lowest level where they appear before subdividing.
- Protect volume when smoothing — check dimensions after every major Smooth pass; re-establish landmarks if drift occurs.
- Sculpt with symmetry until secondary pass, then break intentionally — fully symmetric finals look CG and lifeless.
- Keep topology workable — even quad density, no poles in deform zones, no razor-thin triangles before subdivision.
- Reference on screen at all times — pureRef or image empties in viewport; never sculpt anatomy from memory alone.
- Save incremental Multires levels — keep Level 0/1 base, pre-detail Level 3, and final; never flatten history before approval.

## Quality Gates

- Gate P1 Silhouette: flat-black turntable, 8 angles — character readable, no lumps, no broken gesture; fix if any angle collapses.
- Gate P2 Proportion: head-unit tape check — height, limb segments, eye-line, shoulder/hip widths within 3% of brief or anatomy chart.
- Gate P3 Anatomy: MatCap Clay review — bone landmarks palpable, muscle origins/insertions correct, hands/feet believable at 50 cm equivalent.
- Gate S1 Structure: level 2 wire + shaded — even density, no star poles on face/joints, no subdivision faceting or pinholes.
- Gate S2 Expression/Drape: neutral face + 3/4 view — lids/lips/nose resolve without texture; cloth folds follow gravity/tension logic.
- Gate T1 Detail: 100% crop render — pores/wrinkles even, no alpha tiling, no normal inversion, no noise in flat areas (forehead/cheek).
- Evidence required: MatCap turntable MP4 + neutral-light stills (front/side/back/close-up) before sign-off.

## Validation

- Validate primary forms with MatCap + neutral lighting: Studio Clay MatCap, single area light overhead, 0.18 gray world, no HDRI.
- Validate silhouette: cavity off, flat color override, black background — orbit full 360, capture 8 frames for review packet.
- Validate surface: switch to red Wax / metallic MatCap to expose lumps, pinches, and Smooth damage invisible in Clay.
- Validate scale: measure with Ruler/MeasureIt — height, head length, hand length (~3/4 head), foot length (~1 head).
- Validate deformation readiness: bend elbows/knees/jaw with Pose brush — volumes must compress/stretch without collapse.
- Validate bake readiness: check Multires base cage encloses high, no intersecting shells, 2-5 cm ray distance equivalent at human scale.

## Typical Mistakes

- Detailing too early: pore alphas over wrong skull — fix by freezing detail, dropping to Level 1, re-locking proportions.
- Over-smoothing: melted muscles and lost bone — fix by re-scraping planes with Flatten/Scrape + Crease at low levels.
- Lumpy Dyntopo: uneven density and unfixable pits — fix by Voxel Remesh to even size, QuadriFlow/retopo, then re-project Multires.
- Mirrored perfection: uncanny symmetric face — fix with 2-5% asymmetric Grab/Nudge on brow, nose, mouth corners.
- Stamped alphas: visible pore tiling — fix by rotating/scaling alpha per stroke, mixing two pore sets, masking flat zones.
- Ignored hands/feet: blob fingers, mitten feet — fix by dedicated hand/foot pass with separate reference sheet and higher local density via Face Sets.
- Wrong scale detail: pores sized for film on game asset causing bake noise — fix by reducing tertiary to mid-frequency, bake rest.
- Broken handoff: applied Multires, lost base — fix by preserving .blend master with live Multires plus exported decimated review copy.

## Blender 4.x Notes

- Sculpt Mode overhaul: unified brush assets, Expand active tool, improved PBVH performance — use Asset Shelf brushes, keep brush strength curves linear.
- Multires improved subdivision + displacement: prefer Multires over Dyntopo past blockout; use Rebuild Subdivs after base edits.
- Voxel Remesh + Face Sets workflow: block with Dyntopo/Voxel, isolate with Face Sets, remesh at 0.02-0.05 m for human scale before Multires.
- MatCap library and cavity: use `Studio > Clay`, `Red Wax` for lump check; enable Cavity +zy check but disable for silhouette pass.
- Auto-Smooth and normals: set Shade Auto Smooth 30-45 deg on base, recalc outside before Multires to avoid shading seams.
- Performance: enable Fast Navigate, collapse stacks, sculpt with Outline viewport off on >2M faces; decimate review copies to <500k.
- Color Attributes for masks: store cavity/mask variation as attributes for LookDev handoff to blender-material-specialist.

## Production Contract

- Expected inputs: concept sheets, anatomy reference pack, output target (still/turntable/game/film), Blender version, poly/texture budget.
- Production stages: Analysis -> Blockout -> Primary forms -> Secondary detail -> Tertiary detail -> Polish/Export -> Review.
- Validation criteria: all Quality Gates P1-T1 pass with MatCap turntable + neutral-light stills as evidence.
- Failure conditions: failed silhouette/proportion, Dyntopo final without retopo, baked-in asymmetry errors, noisy tertiary, missing base mesh -> return to indicated stage.
- Iteration strategy: fundamentals first, details last; re-validate silhouette after every level-up in Multires.

## Examples

- Character bust: block 6-head canon at Level 0 -> lock skull/face ratio Level 1-2 -> eyelid/lip/ear structure Level 3 -> pore pass Level 5 only on face, masked.
- Creature: Dyntopo gesture mass -> Voxel Remesh even -> retopo clean base -> Multires muscle/fold secondary -> scale/wrinkle tertiary with two alphas.
- Game hero high-poly: mid-frequency detail only, tight Face Sets on hands/face, decimated 400k review turntable + live Multires master for baker.

## Related Skills

- blender-character-artist — full character pipeline that consumes this sculpt as high-poly source.
- blender-retopology-expert — clean deformable topology and bake cage built from this sculpt.
- blender-modeling-expert — hard-surface base meshes, scale setup, and clean base topology before Multires.
