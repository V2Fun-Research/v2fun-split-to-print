# Uncolored models and reference images

## Establish correspondence

Inspect front/up axes, scale, objects, connected shells, materials, and UVs. Render untextured front, side, and back views to identify actual relief and grooves. Align shared features such as eyes, mouth, collar, cuffs, and shoe tips despite pose, perspective, or lighting differences. Do not stretch the model to fit an image.

List semantic regions and design colors: head/neck, arms, clothing, footwear, face, markings, and lettering. Continue established structure/materials on unseen surfaces where justified. Request evidence for identity-critical hidden patterns instead of inventing them. Environmental blue reflection on a white surface is not a separate blue material.

## Follow geometry

Images provide appearance and approximate location. Actual raised roots, complete sidewalls, grooves, and garment edges define the final boundaries. Combine visibility, normals, seed faces, adjacency, and curvature before labeling faces. A projected rectangle or fixed height is only an initial selection.

Check cuffs, armpits, hands against sleeves, front/back collars, eye color interfaces/highlights, cheek edges, and shoe transitions. Avoid diagonal bands crossing arms, stray triangles on clothing, and duplicate facial pieces beside the original relief.

When a boundary crosses a triangle, split locally using cached shared-edge intersections and consistent subdivision. Reject T-junctions, duplicate edges, and zero-area faces. Face-center classification alone can create stair steps. Global remeshing or moving the exterior is not a substitute for correct selection. Compare solid-color, uncolored, and multiview close-ups before splitting.

## UVs, lettering, and logos

Reuse suitable UVs or construct a model-specific unwrap/region projection. Restrict projection by surface orientation and visibility; do not stamp the front image through the back or onto unrelated objects.

Represent large regions with face materials or explicit masks. Keep fine patterns in UV data until baking into the final vertex colors. Verify text spelling, case, orientation, placement, and completeness. State approximation when accurate type/vector sources are unavailable; generated lookalikes are not exact lettering.

For a requested text-bearing patch, split the complete supporting surface with inward thickness and a matching recess. Existing plates follow their actual roots. A texture-only patch needs a newly designed boundary, which must be disclosed. Do not default to separate letter fragments.

Texture appearance is not printable colored solid geometry. To reproduce a mark with FDM, select closed material volumes, inlaid letters, relief, or a user-accepted decal at the actual print scale. A colored preview alone cannot establish two-color printability.

## Incremental splitting

Maintain separate palette and physical-part lists. Respect same-color separate pieces, multicolor single pieces, independent left/right pieces, and attached details. Only full character splitting invokes the default head connection.

Preserve the outer surface and complete sidewalls; add manufacturing thickness inward and derive the receiver from the same boundary. Adjacent insert pockets can leave fragile pillars or overlapping internal walls; connect the receiving recesses when justified while keeping the inserts distinct.

Modify only affected objects in the latest accepted project. Preserve other geometry, UVs, materials, and transforms. Check cap diagonals against existing shell edges for nonmanifold contacts. Transferred/split normals can improve shading, but cannot repair actual folds or holes.
