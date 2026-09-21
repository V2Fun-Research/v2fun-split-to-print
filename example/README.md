# Interactive split-to-print example

Download `index.html` and open it directly in a modern browser with JavaScript and WebGL. The single file embeds the model preview, Three.js, styling, and controls. It needs no server, network, build step, API key, or additional file. GitHub's file page displays source instead of running the viewer.

## Controls

- **Assembled / Exploded:** animate the 13 parts between their original assembly positions and an exploded layout. These are the only view buttons.
- **Filament color:** choose one of five colors to fade out every other part. Choose **All colors** to restore all 13 parts. Filtering preserves the assembly/explosion mode.
- **Orbit and zoom:** drag to rotate; scroll or pinch to zoom. Controls remain usable during transitions.

The real input was a user-supplied textured GLB. The user chose 150 mm, FDM with a 0.4 mm nozzle, and practical single-color parts. The Blender workflow produced 13 parts in five colors, with head/body connectors, supported eye inserts, a connected tooth strip, and repaired nostril rims. These parameters describe this example, not defaults for other models.

The embedded meshes are display copies simplified with a 0.035 mm algorithm tolerance from the actual final parts. That setting is not a certified geometric error bound. Original engineering and print files were not changed. This is a 3D presentation of completed output, not a segmentation rerun, slicer, or manufacturing-file download. Digital checks do not establish physical fit or successful printing. No paid generation was needed for this example update.

First-party HTML/JS code is covered by the root MIT license. Three.js r180 and OrbitControls are MIT-licensed; their notice is embedded in the HTML and retained in THREE-LICENSE.txt. Character preview geometry has separate rights and is excluded from the software MIT grant; underlying ownership and public redistribution rights are unverified. See the root THIRD_PARTY.md before publishing or reusing the character.

## Generate a demo for another model

Use the bundled [offline demo generator](../references/offline-demo.md) with a reviewed assembled Blender scene and its own palette/part manifest. The included showcase remains the previously verified workflow result; its geometry simplification setting is specific to this example. The reusable generator uses a separately configurable display decimation ratio.
