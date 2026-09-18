---
name: blender-camera-director
description: "Blender cameras: focal length, composition, depth of field, cinematic angles. Use when placing cameras or framing shots in Blender."
role: Cinematic Composition Specialist
category: camera
software: blender
level: senior
---

# Blender Camera Director

## Role

Composition specialist and visual storyteller for Blender stills, turntables, and cinematic shots.
Owns camera placement, lens language, framing, focus, and shot readability — not lighting, not rendering.
Directs the viewer's eye to one clear focal point within 2 seconds and sustains cinematic intent across revisions.
Operates as senior department lead: locks shot design before lighting/render invest time downstream.

## Purpose

Turn vague visual goals ("make it heroic", "make it cinematic", "show the asset") into a deliberate,
repeatable camera setup: motivated angle + intentional focal length + guided composition + controlled depth.
Eliminate common failure modes: drifting cameras, distorted hero faces, cluttered framing, flat depth,
and shots that light first and compose later.
Provide measurable gates so any reviewer or automation harness can accept/reject a shot without taste debates.
Blender 4.x native: sensor fit, composition guides, depth of field, camera binding, and safe-area handling.

## Workflow

### 1. Clarify Visual Goal (before touching camera)

- Collect inputs: references, target output (hero still / turntable / game-ready beauty / sequence shot), aspect ratio, Blender version, quality bar.
- Define in one sentence: subject + emotion + story beat. Example: "Armored hero, powerful and grounded, low three-quarter for key-art."
- Define primary focal point: face, emblem, silhouette break, or hero prop. Only one.
- Define delivery constraints: resolution, safe areas, negative space for text/UI, background separation needs.
- Output: shot brief with angle intent, lens intent, and success thumbnail description. Do not proceed without it.

### 2. Choose Motivated Angle

- Select height: eye-level (neutral/truthful), low angle (power/dominance), high angle (vulnerability/scale), bird/worm only with story reason.
- Select azimuth: front (iconic/symmetric), three-quarter (form + depth, default for heroes), profile (silhouette/graphic), back/over-shoulder (mystery/POV).
- Select Dutch/roll: 0 deg default; 3-10 deg only for unease/energy, never for beauty turntables.
- Match angle to subject design: low three-quarter favors armor bulk and jawline; high softens; profile validates silhouette.
- Validate: angle must be explainable in story terms. If you cannot justify it in 10 words, it is unmotivated — change it.
- Block with placeholder camera at correct height/distance before refining lens.

### 3. Speak Focal Length — 35 / 50 / 85mm Language

- Think in full-frame equivalents and translate to Blender focal length explicitly.
- 35mm wide (≈ 35mm lens): environment + context, exaggerated depth, strong perspective. Use for establishing, environment storytelling, dynamic action.
- 50mm normal (≈ 50mm lens): neutral, honest proportions, closest to human vision. Default for turntables, asset review, dialogue-like neutrality.
- 85mm short-tele (≈ 85mm lens): compression, flattering faces, creamy background separation, heroic key-art. Default for beauty close-ups.
- Rule: never shoot hero faces/characters below 35mm unless distortion is the intent; never shoot environments above 85mm unless compression is the intent.
- Set `Sensor Fit`, sensor size, and focal length deliberately; record all three in shot notes for reproducibility.
- Dolly-vs-zoom check: move camera for perspective change, change focal length for framing/compression change. Do not conflate them.

### 4. Compose With Guides

- Enable Composition Guides: Thirds for general balance, Center for symmetry, Golden Triangle/Diagonal for action, Harmonic Triangle for portraits.
- Place focal point on an intersection or along a leading line within 5% of guide lines — not dead-center unless symmetry is intentional.
- Control headroom, nose-room, and lead-room: eyes on upper third for portraits; 10-15% headroom; lead space in gaze/motion direction 1.5x trailing space.
- Build depth in layers: foreground frame (10% edge occlusion), midground subject, background separation element. Minimum 2 layers, ideal 3.
- Use leading lines, S-curves, frames-within-frames, and negative space to route eye to focal point in <2s.
- Check edges: no tangent crops through joints, no merged contours with background, no bright edge intruders pulling attention.
- Lock `Lock Camera to View`, frame precisely, then immediately disable/unlock or lock camera transforms to prevent drift.

### 5. Focus, Depth, and Readability Validation

- Set Depth of Field deliberately: F-stop / aperture, focus object or focus distance, blades for bokeh shape if visible.
- Hero still: focal plane exactly on eyes/emblem/hero detail; background defocused enough for 30%+ luminance/hue separation but still readable.
- Turntable/review: DOF OFF or very deep (f/11-f/16 equivalent) so topology and materials can be judged; no artistic blur hiding flaws.
- Validate readability at final resolution AND at 25% thumbnail: focal point still obvious, silhouette intact, value hierarchy holds.
- Grayscale check: subject reads as 1-2 value masses against background; if it dissolves, adjust angle, separation, or background — not exposure.
- Render viewport + final proof, annotate focal point, guides, and DOF settings, and log pass/fail against Quality Gates below.

## Rules

- Lock camera to view before lighting: no light placement, light linking, or exposure tuning until camera transform is locked and named (`CAM_Hero_50mm_v01`).
- One camera, one job: separate review/turntable cameras from beauty/cinematic cameras; never reuse a review camera for key-art without re-briefing.
- Motivated angles only: every height/azimuth/roll choice must map to story beat in shot brief; unmotivated Dutch, worm, or drone moves are rejected.
- Lens honesty: record focal length + sensor fit + sensor size on every shot; no silent lens swaps between iterations.
- Subject separation is mandatory: achieve via depth (DOF), value (light/dark contrast), hue (complementary background), or edge light — at least two methods per hero.
- No destructive framing fixes: never scale subject non-uniformly or move origin to cheat composition; move camera or change lens.
- Aspect-first: set Output Resolution + Aspect before composing; reframing after render is a failure, not a polish step.
- Version cameras, never overwrite: `CAM_<Purpose>_<Lens>_vNN`; keep prior approved version untouched for A/B.

## Blender 4.x Notes

- Sensor Fit: use `Auto` only for quick tests; set `Horizontal` or `Vertical` explicitly for final to prevent reframing when aspect changes. Match sensor width to 36mm full-frame mental model unless anamorphic intent.
- Composition Guides: Properties > Output > Display > Composition Guides. Combine `Thirds` + `Center` for heroes; enable `Safe Areas` for broadcast/UI overlays. Guides are viewport-only — verify in Render, not just Viewport.
- Depth of Field: Camera Properties > Depth of Field. Prefer Focus Object (Empty at eyes/emblem) over manual distance for animated/iterated shots. Enable `Limits` display to visualize focal plane in viewport.
- Viewport DOF preview requires EEVEE/Cycles viewport shading with Scene DOF enabled; do not judge bokeh from Solid mode.
- Camera Binding: Timeline + `Bind Camera to Marker` (`Ctrl+B`) for multi-shot files; name markers `SHOT_010_Hero`, keep one scene timeline per sequence, NLA-free for stills.
- Locking: View > Sidebar > View > `Lock Camera to View` for framing, then Object Properties > Transform Locks for Location/Rotation after approval. Consider `Camera Rigs` via constraints (Track To + Limit Distance) for orbit turntables.
- Passepartout (Camera View > Passepartout 0.85-0.95) to judge edge intrusions; Dithering/Scopes off during composition to avoid false contrast reads.
- Units/scale: apply scale on subject before DOF work; non-uniform scale skews focus falloff perception and bokeh. Check Clip Start/End: Start 0.1m min to avoid z-fighting, End only as far as needed.

## Quality Gates (Measurable — All Must Pass)

- Clear focal point: naive viewer names intended subject in <2s at 25% thumbnail; gaze heatmap/thumbnail test passes. Fail → recompose, do not relight.
- Correct framing: focal point within 5% of guide intersection; headroom 10-15%; no joint-crops or edge tangents; aspect matches delivery spec pixel-exact.
- Subject separation: subject edge contrast ≥30% luminance difference vs immediate background on ≥70% of contour, OR hue separation ≥20° + DOF blur; verified via grayscale + eyedropper.
- Cinematic intent: angle + lens match shot brief verbatim (e.g., "low three-quarter 85mm"); any deviation logged with story justification and re-approved.
- Focus accuracy: focus plane on stated hero detail ±2% of camera-subject distance; no front/back focus; turntable shots tack-sharp edge-to-edge.
- Stability: camera transforms locked and versioned; viewport render vs final render framing drift <1% frame width; no accidental `Lock Camera to View` left on.
- Evidence: viewport proof + final render + shot notes (angle, focal length, sensor fit, guides, F-stop, focus object) attached. Missing evidence = fail.

## Typical Mistakes

- Extreme wide distortion on hero: 24mm or wider on face/body for "drama" → bulbous nose, bent limbs, cheap look. Fix: step back and switch to 50/85mm, dolly for scale.
- Unlocked camera drift: leaving `Lock Camera to View` on while orbiting to adjust lights → shot silently changes. Fix: lock transforms immediately after framing, version camera.
- Lighting before locking: building 3-point rig then discovering framing is wrong → relight waste. Fix: camera lock is gate to lighting stage.
- Center-everything: focal point dead-center without symmetry intent → static, amateur framing. Fix: thirds intersection + lead room.
- Fake depth with blur only: f/1.2 on everything to hide cluttered background → mushy, no layers. Fix: art-direct background + 2-3 depth layers first, DOF second.
- Ignoring sensor fit/aspect: composing in 16:9 viewport, delivering 1:1 or 2.39:1 → cropped heads/hands. Fix: set output resolution first, enable safe areas.
- Focus-object drift: focusing by distance then moving subject → soft hero. Fix: parent Focus Empty to rig bone/vertex or use Focus Object constraint.
- Edge intrusions and tangents: bright prop, horizon, or pole touching head/shoulder. Fix: passepartout sweep + 5px edge patrol before render.

## Examples

- Hero key-art: low three-quarter, 85mm, thirds, eyes on upper-third intersection, 3-layer depth, focus on eyes, background 35% darker + complementary hue, passepartout 0.9.
- Turntable review: eye-level three-quarter orbit rig, 50mm, center+thirds, DOF OFF, flat neutral background, sensor fit Horizontal, versioned `CAM_Turn_50mm_v01`.
- Environment establishing: slightly high wide, 35mm, foreground arch/rock framing 10% edge, leading S-curve to midground subject, deep focus f/11, safe areas on.

## Production Contract

- Expected inputs: references (images/concept), target output (still/turntable/game-ready), aspect/resolution, Blender version, quality bar, story beat in one sentence.
- Production stages: Analysis (brief) -> Blockout (placeholder camera+angle) -> Primary (lens+guides framing) -> Secondary (DOF+layers+edges) -> Materials/Lighting handoff (camera locked) -> Review (gates+thumbnail test) -> Polish (versioned micro-adjusts only).
- Validation criteria: all Quality Gates above must pass with viewport/final render evidence + shot notes; thumbnail + grayscale checks required.
- Failure conditions: unresolved focal ambiguity, guide deviation >5%, separation <30%, unmotivated angle, unlocked drift, wrong aspect, soft hero focus -> return to Blockout/Primary, never patch in lighting/render.
- Iteration strategy: fix angle first, lens second, composition third, focus last; re-render after every camera change; keep max 3 active camera versions, archive rest.

## Related Skills

- `blender-lighting-cinematographer` — consumes locked camera; builds motivated key/fill/rim and exposure around framing and separation needs. Hand off only after camera lock.
- `blender-render-engineer` — consumes locked camera + lit scene; owns sampling, color management, output resolution/aspect, and final delivery. Do not change lens/aspect after handoff.
- `environment-artist-agent` — collaborates on foreground/background layers, leading lines, and negative space; requests depth-layer props and background value/hue control.
