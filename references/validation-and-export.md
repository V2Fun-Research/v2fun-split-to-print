# Validation and vertex-color OBJ delivery

Record passed, failed, and not-checked items, separating source defects from new defects. Useful fields include version/source hash, units, affected objects, palette and physical-part counts, components, boundary/nonmanifold edges, degenerate faces, volume, overlap scope, interface measurements, screenshots, and unverified items.

## Acceptance checks

1. **Parts:** verify the intended connected solids, including meaningful small inserts. A tiny closed shell may be a residue, but size alone does not justify deletion.
2. **Topology:** edge and vertex-manifold structure, orientation, positive solid volume, zero/near-zero triangles, and expected holes. No boundary edges does not prove no folds or extra shells.
3. **Geometry:** inspect rebuilt bands, surrounding shells, thin regions, pins, sockets, and inter-part collision. State BVH/intersection test scope and limitations. Excluding shared-vertex face pairs does not prove adjacent faces never fold.
4. **Interfaces:** assembled silhouette, clearances, insertion order/path, effective pin length, socket depth/end gap, and support. Measure actual geometry. A flatness test covers the complete intended face, excluding deliberate protrusions.
5. **Visuals:** exterior, back, underside, internal support, assembled seams, and exploded views. Preserve roundovers, text, patterns, and multicolor details; do not conceal defects with overexposure or smoothing.
6. **Export reload:** reopen the saved engineering scene or import final files into a clean scene. Check objects, color regions, transforms, units, and geometry at the file's real numeric precision. STL reloading/welding is distinct from checking the original indexed mesh.

Without slicing or physical trials, do not report actual waste, print time, number of tool changes, or physical fit. A trial-print design is not certified manufacturing output.

## Actual RGB and lettering

Default OBJ must contain `v x y z r g b` with numeric RGB, not merely `usemtl`, image files, or Blender shader nodes. Include compatible MTL and preserve names, assembled coordinates, and required patterns.

- Sample accepted base colors and UV textures, with the correct linear/sRGB conversion. Do not bake lighting, specular highlights, or ambient occlusion into the palette.
- Refine only the lettering/pattern regions needing more samples, using linear/preserving subdivision. Sparse vertex sampling can erase letter strokes. Check spelling, spacing, counters, background, and orientation in close-up; counting white pixels is insufficient.
- Keep hard boundaries. Corner colors can be exported as separate vertex records keyed by position/color and, when needed, normal. Do not average across material regions.
- State the RGB range/color space, normally 0–1 sRGB. Inspect actual records, enable the same attribute in the engineering preview, and inspect the reimported OBJ in vertex-color mode.
- Supply MTL fallback. If constants approximate detailed patterns or gradients, explain the difference. OBJ vertex color is an extension; not all viewers/slicers read it.

OBJ has no standard unit declaration. Document numeric millimeters and verify the bounding dimensions after transforms; avoid double conversion. Texture-based companion exports need relative image references and packaged images. STL carries no colors; a colored GLB is useful for viewing but is not proof of filament assignments. Multimaterial 3MF regions require non-overlapping closed component volumes and compatible slicer setup.

## Bundled helper: constant face materials only

Use the existing helper only on an already-colored, reviewed `.blend` with constant materials:

```sh
BLENDER --background --python SKILL_DIR/scripts/export_obj_bundle.py -- \
  --input reviewed.blend --output delivery/model.obj \
  --objects Body Head --expected-colors 2
```

`BLENDER` and `SKILL_DIR` stand for the resolved executable and installed package paths. Replace object names/color count with the actual manifest. The helper does not classify, bake, repair, or prove printability. It exports **no vertex RGB**; create and validate that default deliverable separately. Its purpose is the compatible material bundle for an eligible scene, not the complete workflow.

The helper rejects linked/unsupported Base Color and transparency paths instead of silently losing appearance. `--objects` avoids display copies and old versions. Otherwise visible meshes are selected. Units derive from scene `scale_length`, or explicit `--meters-per-unit`; do not guess source units. Default axes are Y forward/Z up. OBJ/MTL, an export-reference report, and short usage instructions are written; `--zip` is optional, not a publication-example requirement.

## Handoff

Provide the final assembled project, vertex-color OBJ/MTL, requested single-part files, assembly directions, modifications, checks, and known limitations. Keep exploded display transforms out of the saved engineering project. Do not present earlier reports/screenshots/packages as the current version. Update only affected work during iteration, then synchronize final outputs once the relevant checks pass.
