#!/usr/bin/env python3
"""
Blender 5.2.3 LTS Deterministic 3D Solids Foundry
=================================================
Generates publication-grade 3D geometric solid assets for Mathematics & Technical Mathematics:
  1. Orthographic Textbook Shaded Render: public/diagrams/blender_3d_<solid>_textbook.jpg
  2. Orthographic NSC Exam Line/Stipple Render: public/diagrams/blender_3d_<solid>_exam_stipple.jpg
  3. Interactive 3D glTF Binary Mesh: public/models/blender_3d_<solid>.glb

Usage (headless):
  "C:\\Program Files\\Blender Foundation\\Blender 5.2\\blender.exe" -b -P scripts/blender/render_3d_solids_foundry.py
"""
from __future__ import annotations

import math
import os
from pathlib import Path

import bmesh
import bpy
from mathutils import Vector

ROOT = Path(__file__).resolve().parent.parent.parent
DIAGRAMS_DIR = ROOT / "public" / "diagrams"
MODELS_DIR = ROOT / "public" / "models"
DIAGRAMS_DIR.mkdir(parents=True, exist_ok=True)
MODELS_DIR.mkdir(parents=True, exist_ok=True)


def clear_meshes() -> None:
    for obj in list(bpy.data.objects):
        if obj.type == "MESH":
            bpy.data.objects.remove(obj, do_unlink=True)
    for mesh in list(bpy.data.meshes):
        if mesh.users == 0:
            bpy.data.meshes.remove(mesh)


def setup_scene() -> tuple[bpy.types.Object, bpy.types.Material, bpy.types.Material]:
    # Clean scene objects without unloading addons
    for obj in list(bpy.data.objects):
        bpy.data.objects.remove(obj, do_unlink=True)
    scene = bpy.context.scene

    # Use CYCLES CPU for 100% deterministic headless rendering without GPU window context hangs
    scene.render.engine = "CYCLES"
    scene.cycles.device = "CPU"
    scene.cycles.samples = 6
    scene.cycles.use_denoising = False
    scene.render.resolution_x = 600
    scene.render.resolution_y = 480
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "JPEG"
    scene.render.image_settings.quality = 92

    # Enable Freestyle for crisp CAD/Exam ink edges
    scene.render.use_freestyle = True
    view_layer = scene.view_layers[0]
    view_layer.use_freestyle = True
    fs_settings = view_layer.freestyle_settings
    fs_settings.crease_angle = math.radians(135.0)
    if not fs_settings.linesets:
        lineset = fs_settings.linesets.new("VisibleLines")
    else:
        lineset = fs_settings.linesets[0]
    if lineset.linestyle is None:
        lineset.linestyle = bpy.data.linestyles.new("ExamLineStyle")
    lineset.select_silhouette = True
    lineset.select_border = True
    lineset.select_crease = True
    lineset.select_edge_mark = True
    lineset.linestyle.color = (0.06, 0.09, 0.16)
    lineset.linestyle.thickness = 2.6

    # Pure #FFFFFF background with Standard view transform so white stays #FFFFFF
    world = bpy.data.worlds.new("PureWhiteWorld")
    scene.world = world
    world.use_nodes = True
    bg_node = world.node_tree.nodes.get("Background")
    if bg_node:
        bg_node.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
        bg_node.inputs[1].default_value = 1.0
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.look = "None"

    # Orthographic camera
    cam_data = bpy.data.cameras.new("OrthoCam")
    cam_data.type = "ORTHO"
    cam_data.ortho_scale = 4.2
    cam_obj = bpy.data.objects.new("OrthoCam", cam_data)
    scene.collection.objects.link(cam_obj)
    cam_obj.location = (4.8, -5.4, 3.8)
    direction = Vector((0.0, 0.0, 0.0)) - cam_obj.location
    cam_obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    scene.camera = cam_obj

    # 3-Point Studio Lighting
    key_data = bpy.data.lights.new(name="KeyLight", type="SUN")
    key_data.energy = 2.8
    key_obj = bpy.data.objects.new(name="KeyLight", object_data=key_data)
    scene.collection.objects.link(key_obj)
    key_obj.rotation_euler = (math.radians(48), math.radians(15), math.radians(-35))

    fill_data = bpy.data.lights.new(name="FillLight", type="SUN")
    fill_data.energy = 1.2
    fill_obj = bpy.data.objects.new(name="FillLight", object_data=fill_data)
    scene.collection.objects.link(fill_obj)
    fill_obj.rotation_euler = (math.radians(65), math.radians(-30), math.radians(55))

    # Textbook Material (Soft volumetric indigo-blue CAD shading)
    mat_textbook = bpy.data.materials.new("TextbookMaterial")
    mat_textbook.use_nodes = True
    bsdf_tb = mat_textbook.node_tree.nodes.get("Principled BSDF")
    if bsdf_tb:
        bsdf_tb.inputs["Base Color"].default_value = (0.72, 0.82, 0.96, 1.0)
        bsdf_tb.inputs["Roughness"].default_value = 0.65
        if "Specular IOR Level" in bsdf_tb.inputs:
            bsdf_tb.inputs["Specular IOR Level"].default_value = 0.25

    # Exam Stipple Material (High-contrast ivory/grey paper shading with strong ink lines)
    mat_exam = bpy.data.materials.new("ExamStippleMaterial")
    mat_exam.use_nodes = True
    bsdf_ex = mat_exam.node_tree.nodes.get("Principled BSDF")
    if bsdf_ex:
        bsdf_ex.inputs["Base Color"].default_value = (0.91, 0.93, 0.96, 1.0)
        bsdf_ex.inputs["Roughness"].default_value = 0.85
        if "Specular IOR Level" in bsdf_ex.inputs:
            bsdf_ex.inputs["Specular IOR Level"].default_value = 0.1

    return cam_obj, mat_textbook, mat_exam


def mark_sharp_creases(obj: bpy.types.Object, angle_deg: float = 28.0) -> None:
    bpy.context.view_layer.objects.active = obj
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    thresh = math.radians(angle_deg)
    for edge in bm.edges:
        if len(edge.link_faces) == 2:
            ang = edge.link_faces[0].normal.angle(edge.link_faces[1].normal, 0.0)
            if ang > thresh:
                edge.smooth = False
    bm.to_mesh(obj.data)
    bm.free()
    # Mark Freestyle edges via mesh data if available cleanly in edit mode
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.mark_freestyle_edge(clear=False)
    bpy.ops.object.mode_set(mode="OBJECT")


def build_platonic(name: str, verts: list[tuple[float, float, float]], faces: list[tuple[int, ...]]) -> bpy.types.Object:
    mesh = bpy.data.meshes.new(name)
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.scene.collection.objects.link(obj)
    mark_sharp_creases(obj, 10.0)
    return obj


def build_dodecahedron(scale: float = 1.05) -> bpy.types.Object:
    # Dual of icosahedron: construct icosahedron and take face centroids with convex hull
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    ico_v = [
        (-1, phi, 0), (1, phi, 0), (-1, -phi, 0), (1, -phi, 0),
        (0, -1, phi), (0, 1, phi), (0, -1, -phi), (0, 1, -phi),
        (phi, 0, -1), (phi, 0, 1), (-phi, 0, -1), (-phi, 0, 1),
    ]
    ico_f = [
        (0, 11, 5), (0, 5, 1), (0, 1, 7), (0, 7, 10), (0, 10, 11),
        (1, 5, 9), (5, 11, 4), (11, 10, 2), (10, 7, 6), (7, 1, 8),
        (3, 9, 4), (3, 4, 2), (3, 2, 6), (3, 6, 8), (3, 8, 9),
        (4, 9, 5), (2, 4, 11), (6, 2, 10), (8, 6, 7), (9, 8, 1),
    ]
    centers = []
    for a, b, c in ico_f:
        cx = (ico_v[a][0] + ico_v[b][0] + ico_v[c][0]) / 3.0 * scale
        cy = (ico_v[a][1] + ico_v[b][1] + ico_v[c][1]) / 3.0 * scale
        cz = (ico_v[a][2] + ico_v[b][2] + ico_v[c][2]) / 3.0 * scale
        centers.append((cx, cy, cz))

    bm = bmesh.new()
    for pt in centers:
        bm.verts.new(pt)
    bmesh.ops.convex_hull(bm, input=bm.verts)
    bmesh.ops.dissolve_limit(bm, angle_limit=math.radians(5.0), verts=bm.verts, edges=bm.edges)
    mesh = bpy.data.meshes.new("dodecahedron")
    bm.to_mesh(mesh)
    bm.free()
    obj = bpy.data.objects.new("dodecahedron", mesh)
    bpy.context.scene.collection.objects.link(obj)
    mark_sharp_creases(obj, 10.0)
    return obj


def create_solid(solid_id: str) -> bpy.types.Object:
    clear_meshes()
    if solid_id == "cube":
        bpy.ops.mesh.primitive_cube_add(size=2.1, location=(0, 0, 0))
        obj = bpy.context.active_object
        mark_sharp_creases(obj)
        return obj
    if solid_id == "rectangular_prism":
        bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0))
        obj = bpy.context.active_object
        obj.scale = (2.7, 1.7, 1.5)
        bpy.ops.object.transform_apply(scale=True)
        mark_sharp_creases(obj)
        return obj
    if solid_id == "triangular_prism":
        bpy.ops.mesh.primitive_cylinder_add(vertices=3, radius=1.45, depth=2.5, location=(0, 0, 0))
        obj = bpy.context.active_object
        obj.rotation_euler = (math.radians(90), 0, math.radians(25))
        bpy.ops.object.transform_apply(rotation=True)
        mark_sharp_creases(obj)
        return obj
    if solid_id == "hexagonal_prism":
        bpy.ops.mesh.primitive_cylinder_add(vertices=6, radius=1.35, depth=2.3, location=(0, 0, 0))
        obj = bpy.context.active_object
        mark_sharp_creases(obj)
        return obj
    if solid_id == "cylinder":
        bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=1.25, depth=2.4, location=(0, 0, 0))
        obj = bpy.context.active_object
        bpy.ops.object.shade_smooth()
        return obj
    if solid_id == "square_pyramid":
        bpy.ops.mesh.primitive_cone_add(vertices=4, radius1=1.65, radius2=0.0, depth=2.4, location=(0, 0, 0))
        obj = bpy.context.active_object
        obj.rotation_euler = (0, 0, math.radians(45))
        bpy.ops.object.transform_apply(rotation=True)
        mark_sharp_creases(obj)
        return obj
    if solid_id in ("triangular_pyramid", "tetrahedron"):
        s = 1.45
        verts = [
            (s, s, s),
            (s, -s, -s),
            (-s, s, -s),
            (-s, -s, s),
        ]
        faces = [(0, 1, 2), (0, 3, 1), (0, 2, 3), (1, 3, 2)]
        return build_platonic(solid_id, verts, faces)
    if solid_id == "hexagonal_pyramid":
        bpy.ops.mesh.primitive_cone_add(vertices=6, radius1=1.55, radius2=0.0, depth=2.4, location=(0, 0, 0))
        obj = bpy.context.active_object
        mark_sharp_creases(obj)
        return obj
    if solid_id == "cone":
        bpy.ops.mesh.primitive_cone_add(vertices=64, radius1=1.35, radius2=0.0, depth=2.45, location=(0, 0, 0))
        obj = bpy.context.active_object
        bpy.ops.object.shade_smooth()
        return obj
    if solid_id == "sphere":
        bpy.ops.mesh.primitive_uv_sphere_add(segments=48, ring_count=24, radius=1.45, location=(0, 0, 0))
        obj = bpy.context.active_object
        bpy.ops.object.shade_smooth()
        return obj
    if solid_id == "octahedron":
        r = 1.65
        verts = [(r, 0, 0), (-r, 0, 0), (0, r, 0), (0, -r, 0), (0, 0, r), (0, 0, -r)]
        faces = [
            (4, 0, 2), (4, 2, 1), (4, 1, 3), (4, 3, 0),
            (5, 2, 0), (5, 1, 2), (5, 3, 1), (5, 0, 3),
        ]
        return build_platonic("octahedron", verts, faces)
    if solid_id == "icosahedron":
        bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1, radius=1.55, location=(0, 0, 0))
        obj = bpy.context.active_object
        mark_sharp_creases(obj, 10.0)
        return obj
    if solid_id == "dodecahedron":
        return build_dodecahedron(scale=1.15)
    raise ValueError(f"Unknown solid_id: {solid_id}")


def main() -> None:
    _, mat_textbook, mat_exam = setup_scene()
    scene = bpy.context.scene

    solids = [
        "cube",
        "rectangular_prism",
        "triangular_prism",
        "hexagonal_prism",
        "cylinder",
        "square_pyramid",
        "triangular_pyramid",
        "tetrahedron",
        "hexagonal_pyramid",
        "cone",
        "sphere",
        "octahedron",
        "dodecahedron",
        "icosahedron",
    ]

    for solid_id in solids:
        obj = create_solid(solid_id)

        # 1. Export .glb 3D model for Surface 2 Interactive Companion
        obj.data.materials.clear()
        obj.data.materials.append(mat_textbook)
        glb_path = MODELS_DIR / f"blender_3d_{solid_id}.glb"
        bpy.ops.export_scene.gltf(
            filepath=str(glb_path),
            export_format="GLB",
            use_selection=False,
        )

        # 2. Render Textbook Shaded View
        tb_path = DIAGRAMS_DIR / f"blender_3d_{solid_id}_textbook.jpg"
        scene.render.filepath = str(tb_path)
        bpy.ops.render.render(write_still=True)

        # 3. Render NSC Exam Stipple / Line View
        obj.data.materials.clear()
        obj.data.materials.append(mat_exam)
        ex_path = DIAGRAMS_DIR / f"blender_3d_{solid_id}_exam_stipple.jpg"
        scene.render.filepath = str(ex_path)
        bpy.ops.render.render(write_still=True)

        print(f"[BLENDER FOUNDRY OK] {solid_id}: {tb_path.name}, {ex_path.name}, {glb_path.name}")


if __name__ == "__main__":
    main()
