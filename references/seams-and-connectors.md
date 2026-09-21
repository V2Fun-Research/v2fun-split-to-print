# Seams, original shape, and assembly

## Three decisions before cutting

- **Extent:** complete raised feature, panel, color region, sectioned body, or decorative surface? The user's latest complete-part instruction controls.
- **Boundary:** inspect oblique, side, and bottom views for the real root, groove, sidewall, fillet, and supporting base. A front outline or marked screenshot does not define hidden geometry by itself.
- **Closure:** planar support, complementary curved interface, inward pocket, retained opening, or pin/socket? Material IDs do not decide this.

Preserve original roundovers, visible thickness, pose, and outline. Add thickness inward. A raised plate's back belongs at or inside the surrounding base; translating a duplicate inward can leave a second raised platform. If only the raised feature is requested, exclude its surrounding thin skirt.

## Shared boundaries and local geometry

1. Validate an initial color/2D selection with depth, normals, visibility, seeded connected faces, and curvature. Projection alone can select the body behind a backpack.
2. Trace closed loops and check branches, short edges, reversals, and projected self-intersections. Resample and smooth where appropriate, retaining real design corners. Update both sides from one boundary and blend local changes without moving protected surfaces.
3. Cache intersections on shared edges when cutting triangles. Preserve source identity, winding, and materials. Inspect slivers, T-junctions, duplicate edges, and zero-area faces.
4. Use the same interface with reversed winding for paired surfaces. Independent smoothing can create gaps and steps. Reversed faces alone do not establish fit; clearance and insertion must be designed separately.
5. Do not cap a concave/nonplanar loop with a long center fan. A projected triangulation also needs checks for folding, multi-layer projection, holes, and mapping. Use an appropriate local surface, transition rings, or uniform reconstruction and inspect it together with the original shell.

## Supported parts and thin-edge prevention

This applies to head interfaces, face inserts, plates, soles, and all other solids.

- Cut at supported roots, grooves, or suitable solid cross-sections. Do not leave the lower head rim attached to the body as a thin shoulder skirt under a large cap.
- Inspect both sides for broad paper-thin shells, folded lips, hanging edges, sharp wedges, and detached fragments. A closed pin rooted only in a thin lid is not sufficiently supported.
- Correct region ownership and move the interface into supported geometry before adding thickness. Add necessary support inward, preserving the visible outline and accepted neighbors. Do not blindly thicken the entire object, delete all small components, or conceal a fragile perimeter under a large plane.
- Set thickness and support criteria from actual size, material, process, nozzle/line width, load, and print orientation. Historical dimensions are not defaults.
- Sample new caps, transitions, and edges with cross-sections or suitable rays. Record direction, spacing, exclusions, and minimum values. Interior samples do not validate the perimeter. Inward-normal rays near tapering edges can give very small values; inspect those locations rather than asserting a universal minimum from a percentile.
- Inspect exploded side, back, and underside views as well as assembled seams. If broad fragile sheets or unsupported interfaces remain, continue repair and do not label the design print-ready.

## Flattening an entire support face

When flattening is requested, establish the plane and whole support region, excluding intentional pins, socket walls, and retained exterior fillets. Cut excess below the plane; fill recesses above it. Cutting alone cannot fill a hollow. Resolve folded peripheral lips into a continuous outline and update the corresponding receiver.

Measure the full region by rays/sections and inspect bottom/oblique views. Measuring only the vertices just assigned to the plane does not establish whole-face flatness. Quantify and disclose any necessary exterior change.

## Default head or head-and-neck connection

Use only for full character splitting, not export/coloring-only tasks, local repairs, explicit keep-together instructions, or non-characters. Verify and reuse a suitable existing joint.

Choose the real neck root/collar groove and insertion direction after front, side, and rear inspection. If exposed neck and head are continuous and share a material, prefer a combined head/neck part at the clothing junction. Preserve the complete collar and avoid assigning head rim surfaces to the body. A fixed Z plane is not a substitute for this inspection; a planar seam may be appropriate when supported by the actual geometry.

At the confirmed scale and process, use glue-locating pins by default, not fragile unrequested snap fits. Choose a D-shaped pin or asymmetric pair based on available solid support and rotation control. Define diameter/profile, effective length, lead-in chamfer, socket diameter/depth, radial/diametric and end clearances. Boolean or directly construct the actual pin/root and socket walls; overlapping cylinders alone are not a completed joint.

Verify support beneath the pin, remaining socket wall, face recess clearance, and insertion. Measure actual mesh sections/rays after smoothing or remeshing. Inspect the head underside and body support face; preserve original assembled coordinates. Do not claim physical fit without a trial.

## Insertion and numeric reliability

Static non-overlap is insufficient. Check withdrawal/insertion against receivers **and adjacent accessories**, determine an assembly order, and distinguish discrete sampled motion from continuous collision proof. Directional receiving surfaces can avoid hidden undercuts, but their visible boundaries must still follow the source geometry.

Before Booleans inspect orientation, volume, coplanarity, self-intersections, and overlap. Validate non-empty output, plausible volume, expected components, and survival of the main body. After two comparable failures, use direct construction, shared surfaces, local remeshing, or better diagnosis instead of an endless exact/fast/tolerance loop.

Connected surface shells are not always separate solid parts. Negative-volume shells may be required internal cavities. Do not fill them by discarding all negative components or flipping each shell outward. Diagnose residues semantically before removing them.

Check the actual exported precision. Binary STL may merge coincident vertices that were distinct in an indexed mesh; a PLY/Blender topology pass alone can miss that failure. Prefer bounded local correction and recheck intersections after it. Broad remeshing changes geometry and appearance: preserve source correspondence, record resolution/affected area, reproject where appropriate, and repeat checks. Use bulk coordinate/normal snapshots in Blender rather than triggering full mesh recalculation for each vertex.
