# Color, UVs, and optional topology changes

## Separate the asset from its appearance

Inspect whether color comes from textures, vertex attributes, constants, or mixed shaders. Record UV channels, image color spaces, transparency, and multiple materials. Compare a neutral color view with the reference; do not bake lighting, highlights, shadows, or ambient occlusion into filament colors. Preserve the only source texture before replacing material bindings.

An explicit request to remove/repaint textures applies to the new version, with the original retained. Blender-native UV workflows include unwrap, seam/overlap checks, layout, painting/baking, and multiview inspection. Do not substitute a remote texturing service for a native-workflow request.

## Semantic palette and regions

1. Establish target colors and available filaments. Perceptual clustering may propose regions but does not replace semantic labeling.
2. Distinguish meaningful face, clothing, accessory, and marking colors. Do not lose a small iris color or the second color in a back label through global clustering.
3. Correct labels using geometry, curvature, normals, UV islands, and adjacency. Clean highlight speckles, shadow contamination, and unintended asymmetry.
4. Evaluate minimum line width, island area, and color-layer thickness at actual size. Merge noise where justified, but do not silently discard a requested logo or important pattern. Explain a real resolution tradeoff.
5. Map accurate vector lettering when available; otherwise trace and verify contours, holes, spelling, and stripe counts. Do not present an approximate logo as exact.

Establish labels before storage. Point colors cannot represent two different corner colors at the same position. Use corner attributes or split exported vertex records at color discontinuities. Verify hard boundaries without averaging across regions.

## Color and physical printing

Color count, material volumes, physical parts, and slicer color changes are different quantities. A single eye may contain two colors; two pink cheeks may be separate parts. Small patterned patches can remain one physical part with a user-accepted multicolor strategy.

A curved 0.2 mm color layer does not imply one slice layer. Closed multi-material volumes must have valid interfaces without gaps or overlaps. Single-color part separation may reduce simultaneous colors, but actual waste/time require a real slicer result; do not invent savings.

## Topology choices

Refine boundary topology locally before increasing the whole mesh. Follow a user request for quad retopology or a specific service only within its actual scope and authorization.

If remote retopology is explicitly requested, verify current official endpoints, formats, quad support, and face-count controls; do not assume an old API or target count guarantees an exact result. Upload only authorized assets, preserve task IDs and budget records, and keep credentials out of outputs. Reconcile uncertain requests before resubmitting a paid job; use bounded retries.

Transfer or rebake colors after topology changes. Inspect mouths, lettering, tiny iris regions, and back labels; old face indices cannot label a new mesh. Creating/editing the skill, local repair, or export alone does not initiate an external service.
