# License and asset scope

The skill instructions, first-party helpers, viewer source, templates, and first-party example HTML code are offered under the root MIT License, Copyright 2026 V2Fun Team.

| Component | Distribution | License / scope |
| --- | --- | --- |
| Blender 4.x and its Python API | External required application; no Blender binaries or Blender source are bundled | Blender is GPL-licensed; see [Blender licensing](https://www.blender.org/about/license/). The root MIT license does not relicense Blender or resolve every downstream script-distribution context. |
| Python standard library | External runtime used by the helpers | Python retains its [PSF license](https://docs.python.org/3/license.html). |
| Optional numerical/mesh libraries | None shipped or required by the bundled helpers | If an agent elects to use another library for a model, review and declare that dependency separately. |
| V2Fun logos | Included user-supplied brand assets | Identify V2Fun; no trademark license or third-party endorsement is implied. |
| Character preview meshes embedded in the example | Derived from a user-supplied model processed in the actual split-to-print workflow | Demonstration material only; excluded from the software MIT grant. Underlying character/model ownership and public redistribution rights have not been independently established. Do not treat this local example as a grant to redistribute or sell the design. |

The example embeds simplified preview meshes and bundled Three.js r180 (including OrbitControls and BufferGeometryUtils), under the MIT License, Copyright 2010–2025 three.js authors. The complete notice is embedded inside the HTML and included in [example/THREE-LICENSE.txt](example/THREE-LICENSE.txt). The locally bundled r180 source and license were reviewed. No web font, CDN, API, or native runtime is required by the viewer. It presents a completed result, not a browser implementation of Blender segmentation.

API/service access, reference assets, resulting model rights, and software licensing are separate. This local workflow requires no V2Fun API key or paid generation. Before publicly publishing the illustrated package, establish redistribution rights for its user-supplied example or replace it with authorized material.

## Reusable offline viewer runtime

`assets/demo/viewer.bundle.js` bundles Three.js 0.180.0, OrbitControls and BufferGeometryUtils under MIT. The full notice is in `assets/demo/THREE-LICENSE.txt` and is embedded by `scripts/build_demo.py` in every generated HTML. Editable first-party source is `assets/demo/viewer.js`; the bundle needs no external browser downloads. User model geometry remains separately licensed.
