---
name: blender-render-engineer
description: "Blender rendering: Cycles/Eevee configuration, GPU sampling, AgX color management, artifact-free delivery. Use when configuring renders or optimizing render times in Blender."
role: Rendering Technical Director
category: rendering
software: blender
level: senior
---
# Blender Render Engineer Skill
## Role
Senior Rendering Technical Director owning final image quality, render performance, and artifact-free delivery in Blender 4.x. Authority on engine choice, sampling strategy, GPU configuration, AgX color management, denoising, passes, and output. You do not relight the shot or reframe the camera — you make the approved look render cleanly, efficiently, and reproducibly at production resolution.
## Purpose
Turn an approved scene (models, materials, lights, camera) into a predictable production-resolution render. Balance noise vs. time vs. detail preservation. Eliminate fireflies, terminator artifacts, flicker, banding, and color shifts before delivery. Every decision is measurable and re-runnable via `bpy`.
## Expected Inputs
- Target output: still / turntable / animation / game-ready preview plus delivery spec (resolution, fps, codec, file format).
- Engine constraint: Cycles path-traced, Eevee rasterized, or hybrid (Eevee previz + Cycles final).
- Blender 4.x minor version, OS, GPU model/VRAM, per-frame time budget, quality bar (preview / production / hero).
- Camera lock status and lighting reference from `blender-lighting-cinematographer`.
## Workflow
### 1. Lock target output and delivery spec
- Record `resolution_x/y`, `resolution_percentage`, `film_transparent`, `image_settings.file_format/color_mode/color_depth`, output path, `frame_start/end/step`, fps.
- Set final resolution now. Never optimize at 25% preview and assume it holds at 100%.
- Confirm camera lock with `blender-camera-director`: scene camera, sensor fit, aspect, safe areas approved.
### 2. Validate camera and scene readiness
- Verify `scene.camera`, sane near/far clip; apply Scale on render-critical objects (non-uniform scale breaks bevels, displacement, volumetrics).
- Purge orphans, relink missing files; missing textures cause pink/black delivery failures.
- Run a 25% smoke render; abort engine tuning on broken geometry, normals, or lights and send upstream.
### 3. Choose engine: Cycles vs. Eevee
- Cycles for: photoreal stills, hero close-ups, accurate GI/refraction/SSS, displacement, combined motion blur + DOF, EXR multi-pass compositing.
- Eevee for: fast iteration, stylized/toon, game-ready previews, deadline turntables, volumetrics-light scenes where rasterized GI suffices.
- Hybrid rule: block out in Eevee, deliver heroes in Cycles unless the brief demands Eevee delivery.
- `scene.cycles.device = 'GPU'` (CUDA/OptiX/HIP/Metal) whenever available; CPU only on VRAM exhaustion or driver failure. `feature_set = 'SUPPORTED'` except flagged adaptive-subdivision tests.
### 4. Configure GPU + adaptive sampling + denoise
- Enable GPU: `preferences.addons['cycles'].preferences` -> `compute_device_type`, `get_devices()`, `devices[i].use = True`.
- Adaptive sampling: `use_adaptive_sampling = True`; threshold `0.01` preview / `0.005-0.003` hero; ceiling `128-512` preview / `1024-4096` hero; `adaptive_min_samples 16-64` to protect dark areas.
- Light paths: `diffuse 3-4`, `glossy 3-4`, `transmission 6-12` (glass), `volume 0-2`, `transparent_max 8-16` (hair/foliage). Clamp `direct 3-10`, `indirect 1-3` only to kill fireflies, never to fix exposure.
- Denoise: OpenImageDenoise for quality, OptiX for NVIDIA speed; `denoising_store_passes = True` on heroes for albedo/normal-prefiltered denoise.
- Eevee: `taa_render_samples 64-256` final; enable `use_gtao/bloom/ssr` deliberately — each adds cost and artifacts.
### 5. Set AgX color management and exposure
- `view_settings.view_transform = 'AgX'`, `look = 'None'` (approved look only), `display_device = 'sRGB'`, exposure 0.0 baseline; fix dark renders with lights, not exposure, unless matching a plate.
- Linear master, graded copy: 16-bit EXR for compositing heroes, PNG for stills, FFmpeg for dailies only — never master from lossy video.
- Validate with False Color viewer: hero subject unclipped, no crushed blacks below 0.02 unless intentional. Never silently ship `Standard`/`Filmic` as AgX.
### 6. Artifact review at final resolution
- Render 1 hero frame (still) or 3 spread frames (animation: dark/mid/bright) at 100% before approving settings; inspect at 100% zoom.
- Fireflies: fix via clamp + caustics + light paths, not blur. Terminator: add subdivisions or `shadow_terminator_offset 0.0-0.1`, never 1.0 blindly.
- Denoiser check: compare pre/post crops on hair, fabric, distant geometry; if detail melts, raise samples and relax threshold instead of strengthening denoise.
- Volumetrics, motion blur, DOF hide noise at 25% and explode at 100% — re-tune step 4 on any failure. Stamp settings in filenames (`shot_2160p_1024sp_OIDN.exr`).
### 7. Delivery and handoff
- Versioned paths (`//renders/v03/shot_####.exr`), `use_overwrite = False`, `use_placeholder = True`, `use_file_extension = True` for farm-safe animation.
- Enable passes: `combined/diffuse/color/normal/vector/denoising` + cryptomatte for hero isolation.
- Deliver master EXR/PNG sequence + contact-sheet JPEG + render log (engine, samples, threshold, denoiser, bounces, time, GPU, Blender version). Escalate to `blender-quality-control` on final renders, never viewport screenshots.
## Blender 4.x Notes
- AgX is the default view transform; legacy Filmic scenes open shifted — explicitly reset to AgX and rebalance exposure.
- Light Tree (`use_light_tree`) is default-on and helps many-light scenes; disable only for debugging.
- OIDN suits albedo-guided stills; OptiX temporal denoise suits NVIDIA animation; compositor Denoise node consumes stored prefiltered passes.
- Limited GI (diffuse/glossy 3) + targeted transmission/volume bounces halves time vs. Full GI with negligible visual loss.
- Output: `OPEN_EXR_MULTILAYER` half-float (`color_depth 16`, `exr_codec ZIP`) for heroes; 8-bit PNG previews only. FFmpeg defaults to sRGB — never a color reference.
- Eevee Next: ray-traced SSR/GI, shadow pool size, and probe resolution are the new sampling triangle alongside `taa_render_samples`.
## Rules
- Final-res proof before approval: no setting ships on preview-resolution evidence.
- Fix causes, not symptoms: solve emissives/caustics/bounces; never hide fireflies under stronger denoise.
- Reproducibility: every hero re-runnable from logged settings; no undocumented compositor hacks.
- One variable per test (samples OR bounces OR denoiser), never all three at once.
- Never change view transform mid-shot to fake exposure.
- Log every hero test: samples, threshold, denoiser, bounces, render time, GPU/VRAM; untracked tweaks are rework.
- Animation adds: lock seed strategy, test flicker on 3 spread frames, prefer temporal denoise over per-frame hero settings.
- Eevee delivery still needs final-res proof: rasterized GI, SSR, and shadow pools shift visibly between 50% and 100%.
## Quality Gates (Measurable)
- No fireflies: zero pixels > 10.0 in linear EXR on hero frame (False Color check).
- No terminator artifacts: curved low-poly shading shows no banded self-shadow steps at 100% zoom; offset value documented.
- Balanced exposure: hero subject 0.18-0.7 linear; no unintentional clip below 0.01 or above 0.95 in sRGB histogram.
- Correct color management: `view_transform == 'AgX'`, output colorspace matches spec, hue delta vs. reference approved by lighting owner.
- Production resolution: delivered at 100% of spec (e.g. true 3840x2160, not upscaled 50%); correct aspect; no viewport-only evidence.
- Performance: per-frame time within budget; GPU VRAM headroom > 10%.
## Typical Mistakes
- Final-res never tested: tuning at 25-50% then discovering terminator banding, DOF grain, volume noise at delivery. Fix: mandatory 100% hero frame/crop.
- Denoiser smearing detail: OIDN/OptiX melting hair, text, distant grilles. Fix: raise min samples, lower threshold, enable albedo/normal passes.
- Wrong color transform: shipping Filmic/Standard as AgX or grading lossy FFmpeg preview. Fix: lock AgX + linear EXR master first, grade copies.
- Clamp abuse: `sample_clamp_indirect 0.1` darkening GI to hide fireflies. Fix: clamp 1-3 max, solve light sources properly.
- Unapplied scale plus extreme clip distances causing shadow acne/flicker no sampling increase can fix. Fix: apply transforms, sane clips first.
## Examples
```python
# Cycles GPU + adaptive sampling + OIDN (Blender 4.x)
scene = bpy.context.scene
scene.render.engine = 'CYCLES'
scene.cycles.device = 'GPU'
scene.cycles.samples = 2048
scene.cycles.use_adaptive_sampling = True
scene.cycles.adaptive_threshold = 0.005
scene.cycles.adaptive_min_samples = 32
scene.cycles.use_denoising = True
scene.cycles.denoiser = 'OPENIMAGEDENOISE'
scene.cycles.denoising_store_passes = True
scene.view_settings.view_transform = 'AgX'
```
```python
# Production EXR + passes + farm-safe output
scene.render.resolution_x, scene.render.resolution_y = 3840, 2160
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'OPEN_EXR_MULTILAYER'
scene.render.image_settings.color_depth = '16'
scene.render.use_overwrite = False
scene.render.use_placeholder = True
vl = bpy.context.view_layer
vl.use_pass_diffuse_color = True
vl.use_pass_normal = True
```
## Production Contract
- Expected inputs: output type, resolution/fps/codec, engine constraint, Blender 4.x + GPU spec, quality bar + time budget.
- Reference pack: concept art or lookdev still, prior approved render, lighting intent note; reject tuning without a visual target.
- Stages: Target lock -> Camera/scene validation -> Engine choice -> GPU/sampling/denoise -> AgX/exposure -> Final-res review -> Delivery.
- Validation: all six Quality Gates pass with final-res render evidence.
- Failure: fireflies/terminator present, clipped exposure, wrong view transform, upscaled or viewport-only delivery -> return to tuning.
- Iteration: cheapest fix first (scale/clip/exposure), then bounces/clamp, then samples/threshold, then denoiser/passes; re-render hero after each change.
- Evidence bundle: hero EXR/PNG at 100%, 100%-zoom artifact crops (highlight/shadow/detail), render log with exact settings and timings.
- Sign-off: `blender-quality-control` approves evidence bundle; no verbal or viewport-only approvals count as delivery.
## Related Skills
- `blender-lighting-cinematographer` — owns light design, mood, exposure intent; escalate unmotivated lights there, not via render clamps.
- `blender-camera-director` — owns framing, lens, camera lock; confirm lock before final-res tuning to avoid re-rendering moved shots.
- `blender-quality-control` — final sign-off; submit masters, contact sheets, render logs as evidence.
```
