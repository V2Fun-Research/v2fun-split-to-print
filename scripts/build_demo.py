#!/usr/bin/env python3
"""Build a self-contained solid-color viewer from a reviewed Blender scene."""
import argparse
import array
import base64
import html
import json
import math
from pathlib import Path
import re
import sys


def packed(values, kind):
    result = array.array(kind, values)
    if sys.byteorder != 'little':
        result.byteswap()
    return base64.b64encode(result.tobytes()).decode('ascii')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--blend', required=True, type=Path)
    parser.add_argument('--manifest', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--overwrite', action='store_true')
    args = parser.parse_args(sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else sys.argv[1:])
    if args.output.suffix.lower() != '.html':
        raise ValueError('Output must be an .html file')
    if args.output.resolve() in (args.blend.resolve(), args.manifest.resolve()):
        raise ValueError('Output must differ from source files')
    if args.output.exists() and not args.overwrite:
        raise ValueError('Output exists; use --overwrite to replace it')
    config = json.loads(args.manifest.read_text())
    scale = config['mm_per_unit']
    if isinstance(scale, bool) or not isinstance(scale, (int, float)) or not math.isfinite(scale) or scale <= 0:
        raise ValueError('mm_per_unit must be finite and positive; verify source units')
    palette = config['palette']
    if not palette or any(not isinstance(c.get('name'), str) or not re.fullmatch(r'#[0-9a-fA-F]{6}', c.get('hex', '')) for c in palette):
        raise ValueError('Palette requires names and #RRGGBB colors')
    entries = config['parts']
    if not entries or len({p['object'] for p in entries}) != len(entries):
        raise ValueError('List each physical mesh object exactly once')
    for part in entries:
        index = part['color']
        if isinstance(index, bool) or not isinstance(index, int) or not 0 <= index < len(palette):
            raise ValueError('Part color must be a palette index')
        offset = part['exploded_mm']
        if len(offset) != 3 or any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) for v in offset):
            raise ValueError('exploded_mm must contain three finite numbers')
    ratio = config.get('preview_ratio', 1.0)
    if isinstance(ratio, bool) or not isinstance(ratio, (int, float)) or not 0 < ratio <= 1:
        raise ValueError('preview_ratio must be in (0, 1]')
    import bpy
    bpy.ops.wm.open_mainfile(filepath=str(args.blend.resolve()))
    data = []
    z_min, z_max = math.inf, -math.inf
    for entry in entries:
        source = bpy.data.objects.get(entry['object'])
        if source is None or source.type != 'MESH':
            raise ValueError('Missing mesh object: ' + entry['object'])
        # Copy into this disposable process only. Never save or edit the engineering scene.
        obj = source.copy()
        obj.data = source.data.copy()
        bpy.context.scene.collection.objects.link(obj)
        if ratio < 1:
            modifier = obj.modifiers.new('Display simplification', 'DECIMATE')
            modifier.ratio = ratio
        bpy.context.view_layer.update()
        evaluated = obj.evaluated_get(bpy.context.evaluated_depsgraph_get())
        mesh = evaluated.to_mesh()
        try:
            mesh.calc_loop_triangles()
            positions = [component * scale for v in mesh.vertices for component in (evaluated.matrix_world @ v.co)]
            if not positions or not mesh.loop_triangles or not all(math.isfinite(v) for v in positions):
                raise ValueError('Empty or non-finite mesh: ' + entry['object'])
            z_min = min(z_min, min(positions[2::3]))
            z_max = max(z_max, max(positions[2::3]))
            data.append({'name': str(entry.get('name', entry['object'])), 'color': entry['color'],
                         'positions': packed(positions, 'f'),
                         'indices': packed((i for t in mesh.loop_triangles for i in t.vertices), 'I'),
                         'exploded_mm': entry['exploded_mm']})
        finally:
            evaluated.to_mesh_clear()
            copied_mesh = obj.data
            bpy.data.objects.remove(obj, do_unlink=True)
            bpy.data.meshes.remove(copied_mesh)
    assets = Path(__file__).resolve().parents[1] / 'assets' / 'demo'
    payload = json.dumps({'palette': palette, 'parts': data}, ensure_ascii=True, allow_nan=False).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    runtime = (assets / 'viewer.bundle.js').read_text().replace('</script', '<\\/script')
    license_text = (assets / 'THREE-LICENSE.txt').read_text()
    tokens = {'TITLE': config.get('title', 'Split to Print — interactive assembly'),
              'HEIGHT': f'{z_max-z_min:.2f}', 'COLORS': len(palette), 'PARTS': len(data),
              'NOTES': config.get('notes', 'Explore the completed parts by filament color.'),
              'SIMPLIFICATION': 'Display geometry is simplified.' if ratio < 1 else 'Display geometry uses the evaluated source meshes.'}
    result = (assets / 'template.html').read_text()
    # Single-pass substitution keeps user text from becoming template instructions.
    result = re.sub(r'\{\{([A-Z]+)\}\}', lambda m: html.escape(str(tokens[m[1]])), result)
    result = result.replace('<!--BUNDLE-->', '<!-- Three.js r180\n' + license_text + '\n--><script type="application/json" id="demo-data">' + payload + '</script><script>' + runtime + '</script>')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(result)
    print(json.dumps({'output': str(args.output), 'parts': len(data), 'height_mm': z_max-z_min, 'bytes': len(result.encode())}))


if __name__ == '__main__':
    main()
