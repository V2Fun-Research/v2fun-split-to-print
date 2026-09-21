"""Blender 4.x helper: export reviewed constant-material meshes as millimetre OBJ/MTL.
Run with Blender --background --python this_file.py -- --input scene.blend --output part.obj.
Does not classify colors, repair geometry, bake textures, or certify printability.
"""
import argparse
import json
import math
from pathlib import Path
import sys
import zipfile


def arguments():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--objects', nargs='+')
    p.add_argument('--expected-colors', type=int)
    p.add_argument('--meters-per-unit', type=float)
    axes = ['X', 'Y', 'Z', 'NEGATIVE_X', 'NEGATIVE_Y', 'NEGATIVE_Z']
    p.add_argument('--forward-axis', choices=axes, default='Y')
    p.add_argument('--up-axis', choices=axes, default='Z')
    p.add_argument('--zip', action='store_true')
    return p.parse_args(sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else [])


def constant_material(material):
    """Reject color paths this helper cannot faithfully represent in constant Kd."""
    if material is None:
        raise ValueError('A used material slot is empty; assign its intended solid color first.')
    if not material.use_nodes:
        return
    outputs = [n for n in material.node_tree.nodes if n.type == 'OUTPUT_MATERIAL' and n.is_active_output]
    if len(outputs) != 1 or len(outputs[0].inputs['Surface'].links) != 1:
        raise ValueError(f'{material.name}: no unambiguous surface output.')
    surface = outputs[0].inputs['Surface'].links[0].from_node
    if surface.type != 'BSDF_PRINCIPLED' or surface.inputs['Base Color'].is_linked:
        raise ValueError(f'{material.name}: convert/bake the linked or unsupported color shader first.')
    if surface.inputs['Alpha'].is_linked or surface.inputs['Alpha'].default_value < 0.999:
        raise ValueError(f'{material.name}: transparency needs an explicit export policy.')


def read_obj(path):
    low, high = [math.inf] * 3, [-math.inf] * 3
    used, libraries, objects = set(), [], []
    vertices = faces = 0
    with path.open(encoding='utf-8') as source:
        for line in source:
            fields = line.split()
            if not fields:
                continue
            kind = fields[0]
            if kind == 'v':
                xyz = list(map(float, fields[1:4]))
                if len(xyz) != 3 or not all(math.isfinite(x) for x in xyz):
                    raise ValueError('Invalid OBJ vertex.')
                vertices += 1
                for i, value in enumerate(xyz):
                    low[i], high[i] = min(low[i], value), max(high[i], value)
            elif kind == 'f':
                faces += 1
            elif kind == 'usemtl':
                used.add(line.strip()[7:])
            elif kind == 'mtllib':
                libraries.append(line.strip()[7:])
            elif kind == 'o':
                objects.append(line.strip()[2:])
    if not vertices or not faces:
        raise ValueError('OBJ contains no mesh geometry.')
    return vertices, faces, low, high, used, libraries, objects


def main():
    import bpy
    a = arguments()
    source, output = a.input.expanduser().resolve(), a.output.expanduser().resolve()
    if source.suffix.lower() != '.blend' or not source.is_file():
        raise ValueError('--input must name an existing reviewed .blend file.')
    if output.suffix.lower() != '.obj':
        raise ValueError('--output must end in .obj.')
    if a.forward_axis.removeprefix('NEGATIVE_') == a.up_axis.removeprefix('NEGATIVE_'):
        raise ValueError('Forward and up axes must differ.')
    bpy.ops.wm.open_mainfile(filepath=str(source))
    if a.objects:
        if len(set(a.objects)) != len(a.objects):
            raise ValueError('Duplicate object names in --objects.')
        meshes = []
        for name in a.objects:
            ob = bpy.context.scene.objects.get(name)
            if ob is None or ob.type != 'MESH':
                raise ValueError(f'Missing mesh object: {name}')
            meshes.append(ob)
    else:
        meshes = [o for o in bpy.context.scene.objects if o.type == 'MESH' and o.visible_get()]
    if not meshes:
        raise ValueError('No reviewed meshes selected for export.')
    checked = set()
    for ob in meshes:
        if not ob.data.polygons:
            raise ValueError(f'{ob.name}: empty mesh.')
        if any(m.show_viewport for m in ob.modifiers):
            raise ValueError(f'{ob.name}: apply/verify visible modifiers before exporting this bundle.')
        for index in {p.material_index for p in ob.data.polygons}:
            mat = ob.material_slots[index].material if index < len(ob.material_slots) else None
            constant_material(mat)
            checked.add(mat.name)
    meters = a.meters_per_unit if a.meters_per_unit is not None else bpy.context.scene.unit_settings.scale_length
    if not math.isfinite(meters) or meters <= 0:
        raise ValueError('Metres per Blender unit must be finite and positive.')
    scale = meters * 1000.0
    output.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.object.select_all(action='DESELECT')
    for ob in meshes:
        ob.hide_set(False)
        ob.hide_select = False
        ob.select_set(True)
    bpy.context.view_layer.objects.active = meshes[0]
    bpy.ops.wm.obj_export(filepath=str(output), export_selected_objects=True,
                          global_scale=scale, forward_axis=a.forward_axis, up_axis=a.up_axis,
                          export_materials=True, export_uv=True, export_normals=True,
                          export_colors=False, export_object_groups=False, export_material_groups=False)
    vertices, faces, low, high, used, libraries, object_records = read_obj(output)
    if not libraries:
        raise ValueError('Missing mtllib reference.')
    material_files, defined, kd = [], set(), {}
    for library in libraries:
        path = (output.parent / library).resolve()
        if path.parent != output.parent or not path.is_file():
            raise ValueError(f'MTL is not a sibling file: {library}')
        material_files.append(path)
        current = None
        for line in path.read_text(encoding='utf-8').splitlines():
            if line.startswith('newmtl '):
                current = line[7:]; defined.add(current)
            elif line.startswith('Kd ') and current:
                kd[current] = tuple(float(x) for x in line.split()[1:4])
            elif line.startswith('map_'):
                raise ValueError('Unexpected image dependency; use the textured-OBJ workflow instead.')
    if not used or not used <= defined or not used <= kd.keys():
        raise ValueError('Missing material definition or diffuse color for a used OBJ material.')
    distinct_colors = {kd[name] for name in used}
    if a.expected_colors is not None and len(distinct_colors) != a.expected_colors:
        raise ValueError(f'Expected {a.expected_colors} distinct Kd colors, got {len(distinct_colors)}.')
    if len(object_records) != len(meshes):
        raise ValueError(f'OBJ object count {len(object_records)} differs from selected count {len(meshes)}.')
    report = {'source_file': source.name, 'blender_version': bpy.app.version_string,
              'source_meters_per_unit': meters, 'obj_numeric_unit': 'millimeter',
              'forward_axis': a.forward_axis, 'up_axis': a.up_axis,
              'selected_objects': [o.name for o in meshes], 'obj_objects': object_records,
              'object_count': len(meshes), 'used_material_count': len(used),
              'distinct_diffuse_color_count': len(distinct_colors),
              'diffuse_colors': {name: kd[name] for name in sorted(used)},
              'vertices': vertices, 'faces': faces, 'bounds_mm': {'min': low, 'max': high},
              'dimensions_mm': [b - c for b, c in zip(high, low)],
              'geometry_print_validation': 'not performed by this exporter'}
    report_path = output.with_suffix('.export.json')
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    instructions = output.with_suffix('.usage.txt')
    instructions.write_text('Keep OBJ and MTL in the same directory. Numeric units: millimeters.\n'
                            'Colors are face materials; some slicers require manual filament assignment.\n'
                            'Export-reference checks are not geometry validation or a physical print trial.\n', encoding='utf-8')
    if a.zip:
        with zipfile.ZipFile(output.with_suffix('.zip'), 'w', zipfile.ZIP_DEFLATED) as archive:
            for path in [output, *material_files, report_path, instructions]:
                archive.write(path, path.name)
    print(json.dumps({'status': 'export_references_verified', 'output': str(output),
                      'objects': len(meshes), 'colors': len(distinct_colors)}, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
