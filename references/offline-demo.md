# Offline assembly demo

Use this route when the user asks for an interactive demo, assembly viewer, or offline webpage for completed parts. Generate from the latest accepted engineering scene. This is presentation only; do not rerun segmentation or modify manufacturing assets.

## Prepare inputs

Use one mesh object per physical part, with assembled world transforms and Z up. If needed, prepare a separate display scene to join objects belonging to the same physical part or orient the model. Do not count material regions as separate physical parts.

Copy [the manifest example](../assets/demo/manifest.example.json) and replace its sample values:

- `title`, `notes`: plain English display text by default; follow the user's language preference. Notes should describe actual assembly guidance and limitations.
- `mm_per_unit`: millimeters per Blender world-coordinate unit, explicitly verified against the intended size. For a correctly configured scene this is `scene.unit_settings.scale_length * 1000`. Unitless legacy scenes may need a different value. The generator does not resize the engineering model. Displayed height is the evaluated Z extent.
- `palette`: array of `{ "name": "...", "hex": "#RRGGBB" }`, containing the used filament colors.
- `parts`: array of `{ "object": "ExactBlenderObjectName", "name": "Optional display name", "color": 0, "exploded_mm": [0,0,25] }`. `color` is a zero-based palette index; each object appears once. Only listed objects are exported. Audit this list against the accepted physical-part inventory; cameras, references, hidden backups and old versions must not enter it.
- `exploded_mm`: world-axis translation in millimeters from assembled coordinates. Choose vectors using the current part/interface plan. They illustrate separation, not a collision-tested insertion sequence. Do not inherit the example's directions or distances blindly.
- `preview_ratio`: optional decimation ratio in `(0,1]`, default `1`. Reduces display geometry only, with no guaranteed surface-error bound. Check thin parts and small features after any simplification.

The viewer uses one uniform solid color per physical part, with lighting but no texture maps or vertex-color patterns. For a multicolor physical part, explicitly disclose that this is a simplified color preview and get the intended display representation from the user's request/context. Do not silently claim that texture details, logos, or all filament regions are preserved. Use a custom region-aware display implementation if faithful multicolor visualization is required; do not split the engineering solid just to satisfy the viewer schema.

## Generate

From the installed skill directory, replace `BLENDER` with the local Blender 4.x executable and supply the actual input paths:

```sh
BLENDER --background --factory-startup --python-exit-code 1 --python scripts/build_demo.py -- --blend assembled.blend --manifest demo.json --output demo.html
```

Use `--overwrite` only when replacing the intended existing HTML. The script reads the source, evaluates world transforms/modifiers, triangulates display meshes, embeds geometry and the bundled viewer, and never saves the Blender file. No API key, Node installation, sibling skill, network fetch, or web server is needed to generate or view it. The browser needs JavaScript and WebGL. Keep the resulting single HTML file for delivery.

## Interaction contract and verification

- Exactly two mode buttons: **Assembled** and **Exploded**, with smooth motion between positions.
- A right-side filament dropdown, with **All colors** plus the model's palette.
- Selecting a color fades other parts out and hides them completely. Restoring All colors fades them back in. Filtering preserves the assembly mode and works during an interrupted transition.
- No individual part buttons. The table lists matching parts and their physical counts.
- Orbit/zoom by mouse or touch; responsive layout, automatic camera framing for both modes, solid basic colors.

Open the actual output via `file://`, preferably with network blocked. Verify both modes, intermediate motion, every color and its expected count, restoration, rapid switching, camera framing, and narrow-screen layout. Inspect small parts and solid-color appearance. Copy only the HTML to a fresh directory and reopen it. Report unchecked items honestly. Rendering is not a physical-fit or printability test.

The editable viewer source, HTML template, prebuilt bundle, and Three.js MIT notice live under `assets/demo/`. For viewer maintenance only, rebuild `viewer.bundle.js` from `viewer.js` with an ES module bundler and Three.js `0.180.0` (`three`, OrbitControls, BufferGeometryUtils), then repeat the browser checks. Normal generation uses the bundled runtime directly. Retain the full bundled MIT notice in every generated HTML.
