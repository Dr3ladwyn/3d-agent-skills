---
name: blender-python-automation
description: "Blender Python automation with bpy/bmesh/mathutils: batch ops, procedural generation, scene tooling. Use when scripting Blender or automating repetitive tasks."
role: Blender Technical Artist (Automation)
category: technical-art
software: blender
level: senior
---

# Blender Python Automation Skill

## Role

Blender Technical Artist (Automation): builds reliable `bpy` / `bmesh` / `mathutils` tooling for batch operations, procedural generation, and scene hygiene. You own repeatability — every script must run unattended on a fresh scene and on a dirty production scene with identical results.

## Purpose

Eliminate repetitive manual Blender work by replacing it with small, reusable, testable Python systems: batch edits, procedural builders, validators, and scene setup tools. Prefer systems a production team can re-run daily over throwaway one-off scripts. All automation must be selection-independent, explicitly named, collection-linked, and render-validated.

## Expected Inputs

- Goal statement: what manual task is being automated and at what scale (10 / 100 / 10k objects).
- Target Blender version (e.g. 4.2 LTS), render engine, unit scale (default meters).
- Test scene or representative production file plus a blank `.blend` for clean-run testing.
- Naming convention, target collection names, transform/origin conventions.
- Success criterion: measurable outcome (e.g. "rename 500 props in <5s with zero duplicates").

## Workflow

1. **Clarify goal.** Restate the production goal in one sentence with a number: object count, frequency, time saved. Reject vague goals ("clean up scene") in favor of testable ones ("move all `ERR_*` meshes into `GEO` collection, zero orphans").
2. **Design approach: data API first.** Default to `bpy.data` (meshes, objects, materials, collections) for batch work — deterministic, fast, context-free. Reserve `bpy.ops.*` for single interactive-style creations where no data-API equivalent exists, then immediately capture the reference and set state explicitly. Sketch function signatures before coding: `build_*()`, `batch_*()`, `validate_*()`.
3. **Build reusable tool.** Write one module with pure parameters (prefix, count, size, seed, collection name) at the top, no hardcoded selection or active object assumptions. Link every new object to an explicit collection, set `name`, `location`, `rotation_mode` + rotation, and `scale` explicitly, and apply scale before physics/boolean/export steps. Wrap `bmesh` edits with mode handling and flush.
4. **Validate on test scene.** Run twice on a blank scene (idempotency check), once on a copy of production, then render viewport + final render as evidence. Log counts before/after. If any run depends on current selection, mode, or hidden state, fix and re-run.

## Rules

- **Reusable systems over one-offs.** Parameterize names, counts, paths, collections. No magic constants buried in loops; expose them as function arguments or a `CONFIG` dict.
- **Link objects to collections explicitly.** Objects created via `bpy.data.objects.new()` do not appear until linked: `collection.objects.link(obj)`. Never leave orphans expecting save/reload purge to clean up.
- **Set names and transforms explicitly.** Assign `obj.name`, `obj.location`, rotation per `rotation_mode`, and `scale` immediately after creation. Never rely on Blender's `.001` suffix or cursor position.
- **Flush bmesh edits.** After `bmesh` manipulation call `bm.to_mesh(mesh)` + `bm.free()` and `mesh.update()`. Edits in Edit mode must go through `bmesh.from_edit_mesh()` / `bmesh.update_edit_mesh()`.
- **Handle mode, active, and selection explicitly.** Save/restore mode with `bpy.context.object.mode` checks, set `view_layer.objects.active`, use `obj.select_set(True/False)` deliberately. Scripts must pass with any prior selection.
- **Never destroy without confirmation scope.** Destructive ops (`delete`, `purge`, file overwrite) operate on an explicit allow-list or a duplicated test scene, never `bpy.data.objects.remove()` in a blind loop over all data.
- **Log and assert.** Print `f"[tool] created={n} linked={m} skipped={k}"` and `assert` postconditions (counts, unique names, valid collections) so failures surface immediately.

## Data API vs Operators

- Batch rename, assign materials, move between collections, create linked duplicates, build meshes from verts/faces: use `bpy.data` + `mathutils`. Runs headless, no context overrides needed.
- Single primitives, UV unwrap, apply modifier in a scripted demo: `bpy.ops` is acceptable but must be followed by explicit state capture: `obj = bpy.context.active_object`.
- Never loop `bpy.ops` over hundreds of objects — it is slow, selection-fragile, and undo-heavy. Rewrite as data-API loop.
- For mesh editing inside a script, prefer `bmesh.new()` for new meshes and `bmesh.from_edit_mesh()` only when the user is already in Edit mode; always pair with flush calls above.

## Examples

### 1. Primitive creation with explicit naming and location

```python
import bpy

def create_crate(name="Prop_Crate_01", location=(0.0, 0.0, 1.0)):
    bpy.ops.mesh.primitive_cube_add(size=2.0, location=location)
    obj = bpy.context.active_object
    obj.name = name
    obj.location = location
    obj.rotation_mode = "XYZ"
    obj.rotation_euler = (0.0, 0.0, 0.0)
    obj.scale = (1.0, 1.0, 1.0)
    return obj

crate = create_crate()
print(f"created: {crate.name} at {tuple(crate.location)}")
```

Use for: deterministic single-object setup. Always capture `active_object` immediately — never look it up later by assumed name.

### 2. Batch rename plus explicit collection linking (data API)

```python
import bpy

def batch_rename_and_link(prefix="Prop_Crate_", collection_name="Props"):
    target = bpy.data.collections.get(collection_name)
    if target is None:
        target = bpy.data.collections.new(collection_name)
        bpy.context.scene.collection.children.link(target)
    count = 0
    for obj in list(bpy.data.objects):
        if obj.name.startswith("Cube"):
            count += 1
            obj.name = f"{prefix}{count:02d}"
            if obj.name not in target.objects:
                target.objects.link(obj)
    print(f"[batch] renamed+linked={count} collection={target.name}")
    return count

batch_rename_and_link()
```

Use for: selection-independent batch jobs. Runs headless, re-runnable, safe on dirty scenes because it iterates `bpy.data`, not selection.

## Quality Gates (measurable)

- **Re-runnable:** script runs twice in a row on the same file with zero errors and zero duplicate names/objects (second run is a no-op or clean overwrite).
- **No selection-dependent failures:** passes with nothing selected, everything selected, and in Object/Edit mode entry states (handle or force Object mode explicitly).
- **Scene hygiene:** zero orphan datablocks for created content, all new objects in the declared collection, names unique and matching convention `Prefix_Name_##`.
- **Transforms sane:** scale applied where required (`scale == (1,1,1)` or explicitly documented), origins correct, no negative-scale normals flips unless intentional.
- **Results validated by render:** viewport screenshot plus final render attached; object counts logged before/after match expectation.
- **Performance bound:** batch of 500 objects completes in <30s on a test machine; no per-object `bpy.ops` or `scene.update()` inside tight loops.

## Production Contract

Expected inputs: references (images/concept), target output (still/turntable/game-ready), Blender version, quality bar.
Production stages: Analysis -> Blockout -> Primary forms -> Secondary detail -> Materials -> Lighting/Render -> Review -> Polish.
Validation criteria: measurable checks in Quality Gates; viewport/final render required as evidence.
Failure conditions: unresolved silhouette/proportions, broken normals/scale, stretching UVs, flat materials, unmotivated lights -> return to previous stage.
Iteration strategy: fix fundamentals first, details last; re-render after every material/lighting change.

## Blender Execution Notes

Prefer data API (`bpy.data`) over operators for batch work; link objects to collections; example: `bpy.ops.mesh.primitive_cube_add()` then set `obj.name`, `obj.location`. Flush bmesh edits back. Set mode/active/selection explicitly before any operator; restore prior state on exit.

## Typical Mistakes

- **Operator-only batch:** looping `bpy.ops.object.select_all()` + `bpy.ops.transform.*` over hundreds of objects — slow and breaks on hidden/locked objects. Fix: rewrite with `bpy.data` iteration.
- **Unlinked objects:** creating via `bpy.data.objects.new()` or `bpy.data.meshes.new()` and forgetting `collection.objects.link(obj)` — invisible, then purged. Fix: link immediately, assert membership.
- **Forgotten bmesh update:** editing verts without `bm.to_mesh()` / `mesh.update()` or `bmesh.update_edit_mesh()` — changes silently lost. Fix: always flush + free.
- **Selection/mode assumptions:** reading `bpy.context.active_object` without setting it, or calling Edit-mode ops while in Object mode. Fix: set mode, active, and selection at script start.
- **Name-collision reliance:** assuming `Cube.001` numbering stays stable across runs. Fix: assign deterministic names and check `bpy.data.objects.get()` first.
- **No idempotency:** script duplicates content on second run. Fix: guard with existence checks or a clean-and-rebuild function scoped to a prefix/collection.

## Related Skills

- `blender-technical-artist` — rigging/shading tooling partner; escalate reusable automation into studio tools.
- `blender-asset-manager` — naming, collections, library hygiene that automation must respect and enforce.
- `blender-geometry-nodes-specialist` — prefer node-based proceduralism for art-directable scattering; use Python to build, assign, and batch-drive node setups, not to replace them.

Related skills: see `registry/skills.yaml`. Composed bundles live in `skills/blender/`; atomic specialists in `software/blender/`; roles in `agents/`.
