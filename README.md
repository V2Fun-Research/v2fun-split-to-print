<div align="center">

<a href="https://v2fun.ai/">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.svg" />
    <img src="assets/logo.svg" width="250" height="100" alt="V2Fun" />
  </picture>
</a>

# V2Fun Split to Print

**Color separation and assembleable parts from existing 3D models**

Follow real geometry, build supported parts and mating interfaces, and export inspectable print assets.

[English](./README.md) | [简体中文](./README.zh-CN.md)

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Version: 1.0.0](https://img.shields.io/badge/version-1.0.0-green.svg)](#roadmap)
[![Runtime: Blender 4.x](https://img.shields.io/badge/runtime-Blender%204.x-E87D0D.svg)](https://www.blender.org/)
[![Tooling: Blender Python](https://img.shields.io/badge/tooling-Blender%20Python-3776AB.svg)](scripts)
[![Sponsor: V2Fun](https://img.shields.io/badge/Sponsor-V2Fun-16161A.svg)](https://v2fun.ai/)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-5865F2?logo=discord&logoColor=white)](https://discord.com/invite/2uBMRp275u)

</div>

---
## Live demos

An offline 3D viewer of a real workflow result. Switch between Assembled and Exploded with smooth motion, or choose a filament color to fade out the other parts. No server or network is needed. GitHub displays source; download the HTML and open it in a browser.

| Example | Contents | View |
| --- | --- | --- |
| 150 mm / 5 colors / 13 parts | Animated assembly/explosion, color isolation, orbit and zoom | [View](example/index.html) |

[Example instructions](example/README.md)

## What it does

Supply an uncolored mesh with references, or a textured/vertex-colored model. The agent uses Blender to clean semantic colors, split requested solid parts, repair fragile edges, and construct supported pins, sockets, and receiving recesses.

- Keep palette and physical-part counts separate; one color need not be one part.
- Full character splitting includes a head/head-and-neck connection by default; limited coloring, export, or repair requests remain limited.
- Preserve text, logos, and important patterns in actual vertex RGB plus compatible materials.
- Set thickness and clearance from actual size, process, and insertion direction.
- Generate an offline assembly demo on request, with animated color isolation and solid-color display.

This is an agent-assisted workflow, not an automatic segmentation command. It does not create models from scratch, automatically slice or control printers, or certify manufacturability.

## How it works

1. Inspect source assets, references, units, and baseline defects.
2. Establish a palette and part manifest; clean boundaries along real roots and sidewalls.
3. Prove the hardest interface before extending supported closures and connectors.
4. Check solids, thickness, assembly order, clearances, and multiple views.
5. Reload the final files and verify vertex colors, part counts, and dimensions before delivery.

[Workflow](SKILL.md) · [Interfaces](references/seams-and-connectors.md) · [Validation](references/validation-and-export.md)

## Quick start

### Install

Copy this folder to `~/.codex/skills/v2fun-split-to-print/`, or `skills/v2fun-split-to-print/` under your custom `CODEX_HOME`. Place `SKILL.md` directly inside it. Use a client with local skill support and Blender 4.x with its bundled Python. No sibling skill, API key, or paid generation is required.

Migrating from `v2fun-part`: back up the old folder outside the active skills directory, install the new name, and remove the old active copy to avoid duplicate discovery. Preserve model projects and outputs. Reload the client's skill list when needed.

### Use it

> Use $v2fun-split-to-print on this existing model. Make it 150 mm tall for FDM with a 0.4 mm nozzle, separate practical single-color parts, and deliver an assembled project, vertex-color OBJ/MTL, and individual STL files.

The dimensions above are an example, not defaults. Attach the model and any needed appearance references. State size, print process/nozzle, material if known, colors, and parts that must stay together. Already-confirmed choices are reused.

### Optional material-only export helper

From the installed directory, resolve `BLENDER` to your executable:

```sh
BLENDER --background --python scripts/export_obj_bundle.py -- --help
```

This helper requires an already-reviewed Blender scene with constant materials. It does not segment, repair, bake vertex colors, or certify printability. See [export scope](references/validation-and-export.md).

If Blender is unavailable, inspect inputs and report the missing runtime. If shader colors are linked, bake/prepare the intended colors rather than bypassing the helper's rejection. A preview is not a physical fit test.

### Generate an offline demo

Ask: “Use $v2fun-split-to-print to create an offline demo of these completed parts.” The bundled generator creates a single HTML with Assembled/Exploded motion, basic solid colors, color isolation, and orbit/zoom. No server or network is required. See [inputs, command and verification](references/offline-demo.md). Manufacturing files stay unchanged.

Prepare the model-specific manifest using the guide above, then run from the installed skill directory:

```sh
BLENDER --background --factory-startup --python-exit-code 1 --python scripts/build_demo.py -- --blend assembled.blend --manifest demo.json --output demo.html
```

Blender 4.x generates the file; the browser needs JavaScript and WebGL. Three.js is bundled with its MIT notice. The default preview uses one uniform color per physical part; texture maps and vertex-color patterns are not displayed.

## What you get

| Deliverable | Contents |
| --- | --- |
| Assembled Blender project | Editable parts and actual assembly structures |
| Vertex-color OBJ + MTL | Actual RGB records, object names, and material fallback |
| Individual STL when requested | Uncolored independent print solids |
| Offline HTML demo when requested | Assembled/Exploded animation, filament filtering, orbit and zoom |
| Assembly guidance and relevant checks | Directions, modifications, dimensions, and unverified items |

Physical fit is not claimed without a trial. OBJ vertex colors are an extension; receiving software may need MTL or manual filament assignment.

## Roadmap

### v1.0.0

- [x] Name migration preserving coloring, splitting, and local repair workflows.
- [x] Default character head connections and thin-part checks.
- [x] Vertex-color delivery contract, bilingual documentation, and offline result example.
- [x] Reusable offline demo generator, configurable part manifest and bundled viewer.

## Star history

V2Fun-Research/v2fun-split-to-print is a private repository. Repository access requires authorization; a public Star History chart is unavailable while it remains private.

[![Star History Chart](https://api.star-history.com/svg?repos=V2Fun-Research/v2fun-split-to-print&type=Date)](https://www.star-history.com/#V2Fun-Research/v2fun-split-to-print&Date)

## Sponsors

<table>
<tr><td align="center" width="160"><a href="https://v2fun.ai/"><img src="assets/sponsors/v2fun-square.png" width="96" height="96" alt="V2Fun" /></a><br /><strong>V2Fun</strong></td><td>V2Fun supports creators developing ideas into usable 3D work. This skill focuses on the stage after a model already exists: identifying intended colors, separating complete physical features, building supported assembly interfaces, and keeping the result connected to an editable project. Its local Blender workflow does not require another generation job or a paid service call just to split a model. Modeling, part preparation, and animation can each use a suitable workflow. Other platform capabilities are not automatically included here. Final printing still depends on the asset, material, machine, and trial results; digital inspection is not a substitute for physical fit testing.</td></tr>
</table>

Maintainer: **V2Fun Team** · [V2Fun Discord](https://discord.com/invite/2uBMRp275u) · [V2Fun](https://v2fun.ai/)

## Acknowledgments

Thanks to [Blender](https://www.blender.org/) and its contributors for the local modeling tools. The V2Fun README template draws presentation inspiration from [img2threejs](https://github.com/img2threejs/img2threejs); no endorsement is implied. The offline viewer includes [Three.js](https://threejs.org/) and its OrbitControls and BufferGeometryUtils components under MIT.

## License

[MIT License](LICENSE)<br>
Copyright © 2026 V2Fun Team.

Applies to this project’s code and documentation. Blender, brand marks, input models, and example character assets have separate rights. The example character is excluded from the MIT grant; public redistribution rights have not been independently confirmed. See [third-party scope](THIRD_PARTY.md).
