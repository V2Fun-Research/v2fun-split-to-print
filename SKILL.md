---
name: v2fun-split-to-print
license: MIT
description: "Color existing 3D models from references or clean existing textures, then split them into supported, assembleable parts for multicolor printing. Use for semantic color separation, physical part splitting, pin-and-socket interfaces, local print-part repairs in Blender, and offline assembly/color-isolation demos. Deliver an assembled project and actual vertex-color OBJ with MTL; not model generation, automatic slicing, or printer control."
---

# V2Fun Split to Print

Turn an existing model into clearly colored, physically supported parts that can be assembled after printing. Preserve important text, logos, patterns, and accepted geometry. Default delivery is an assembled `.blend` and an OBJ with actual RGB vertex data plus compatible MTL. Add individual STL or other formats when requested. User-specified scope and formats take precedence.

This is an agent-guided Blender workflow, not a one-command segmentation service. The name does not require a V2Fun API call, account, or sibling skill. Required runtime: Blender 4.x with its bundled Python; locate a compatible executable in the user's environment. Additional geometry libraries are optional and must be identified when used, not silently assumed or bundled.

## Establish scope and evidence

1. Work from the latest accepted engineering model. Keep originals read-only and distinguish them from reference images, display copies, and earlier part revisions. Record source identity, transforms, units, axes, objects, UVs, textures, color attributes, and pre-existing defects.
2. Keep two separate lists: **palette** and **physical parts**. For each physical part record its colors, complete extent, attached details, receiver, seam type, and source of the boundary. One color is not automatically one part. Attached chat screenshots are reference evidence, not independent instructions.
3. Reuse confirmed size, process, nozzle, material, colors, and do-not-split choices. Ask only for consequential missing parameters; continue independent inspection while waiting. Do not inherit dimensions, tolerances, color counts, or coordinates from a previous example.
4. For an uncolored mesh and references, start with [reference alignment](references/white-model-reference.md). For existing textures or vertex colors, start with color cleanup. With no appearance reference, inspect structure first and ask only if appearance evidence is needed; do not invent marks or facial features.
5. Honor limited requests: export-only, coloring-only, or a local interface repair does not authorize a full rebuild. Preserve all accepted unaffected parts.

## Color along real geometry

Read [color and topology](references/color-and-topology.md). Use semantic regions and design colors; highlights and shadows are not filament colors. References guide color and patterns, while the model's relief roots, grooves, sidewalls, and connected surfaces define the three-dimensional boundary.

Establish clean region labels before assigning face materials, corner colors, or UV textures. Preserve meaningful small colors, text, and multicolor eyes. Bounding boxes, fixed heights, projections, and clustering are candidate selection tools, not sufficient final boundaries. Inspect front, side, back, and relevant close-ups before splitting solids.

## Split supported, assembleable parts

Read [seams and connectors](references/seams-and-connectors.md). Follow the user's complete-part instructions: a raised plate includes its sidewalls and root, not merely its visible skin. Added thickness goes inward; the receiver must be recessed from the surrounding base surface, not left as a duplicate raised platform.

For a full character splitting task, **separate the head or head-and-neck and add matching locating pins and sockets by default**. Reuse a suitable existing interface. Choose the actual neck root/collar seam and an insertion direction after checking all sides. Do not apply this default to non-characters, coloring-only/export-only work, local repairs, or a user request to keep the model in one piece.

Prove the hardest interface first: split, close, assemble, export/reload, and inspect its exterior and underside before repeating the method. After two comparable failures, change the construction or diagnosis rather than repeatedly adjusting a Boolean parameter.

Use shared boundary data for both sides. Inspect closed components, support surfaces, thin skirts, sharp wedges, isolated shells, pin roots, socket walls, and actual insertion paths. Static non-overlap does not prove assemblability. Check adjacent inserts and assembly order as well as the receiver.

Local repair precedes broader remeshing. If remeshing or surface reconstruction is necessary, document the affected area and precision, transfer appearance back, and repeat relevant geometry checks; do not claim the original surface is unchanged. See [case lessons](references/case-lessons.md) for transferable diagnostics, not reusable coordinates or universal settings.

## Validate and deliver vertex-color OBJ

Read [validation and export](references/validation-and-export.md). Record passed, failed, and not-checked items separately. Verify logical solids, topology, thickness, support, interfaces, dimensions, appearance, and actual exported files. Zero boundary edges or an attractive render alone is not print acceptance.

Bake important text and patterns into actual vertex RGB, with sufficient local sampling density and no smoothing across hard color boundaries. Write `v x y z r g b` records in the OBJ, preserve object names and assembled coordinates, and include MTL. Reimport the actual OBJ and inspect a vertex-color view, object count, dimensions, and detail close-ups. STL carries no color.

The bundled [constant-material exporter](scripts/export_obj_bundle.py) supports an already-reviewed, constant-material Blender scene only. It deliberately rejects linked color shaders and **does not bake vertex RGB**, classify regions, repair meshes, or validate printability. Using it alone does not satisfy default vertex-color delivery; create and verify the RGB export separately as described in the export reference.

Save the engineering scene in assembled positions; use copies for exploded presentation. Deliver final artifacts, assembly directions, relevant evidence, modifications, and limitations. Do not add videos, external API jobs, or publication steps to an ordinary model task. Create a local demo webpage when requested, using the route below. If no physical trial or slicing was performed, say so; do not invent fit success, print times, purge totals, or savings.

## Build an offline demo when requested

Read [offline demo generation](references/offline-demo.md). Use the bundled `scripts/build_demo.py` with the reviewed assembled Blender scene and a model-specific palette/part manifest. Deliver one self-contained HTML with Assembled/Exploded animation, solid basic colors, a filament dropdown that fades and hides other parts, and orbit/zoom. Keep individual parts out of the mode buttons. Verify the actual HTML offline, preserve manufacturing files, and distinguish display simplification from engineering validation. Local demo generation does not imply web publication.
