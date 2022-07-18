import bpy
from mathutils import Vector  
from mathutils.bvhtree import BVHTree
import gpu
from gpu_extras.batch import batch_for_shader
import time
from bpy.app.handlers import persistent

draw_handler = None

def get_intersections(scene, ray_origin, ray_pickup, jet_vector, ray_vector, intersections):
    context = bpy.context
    depsgraph = context.evaluated_depsgraph_get()
    raycast_depth = abs(ray_vector[2])

    success, intersection, normal, index, object, matrix = scene.ray_cast(depsgraph, ray_pickup, ray_vector, distance = raycast_depth)
    
    if success:
        new_ray_pickup = intersection - Vector((0, 0, scene.display_minimum_droplet_length_mm))
        
        if new_ray_pickup[2] < scene.display_minimum_droplet_length_mm:
            intersection = intersection * Vector((1, 1, 0))
            intersections.append(intersection)
            
            return intersections
        
        ray_delta = Vector((0, 0, 1)) * (ray_origin - intersection)        
        new_ray_vector = jet_vector + ray_delta
        
        intersections.append(intersection)
        
        get_intersections(scene, ray_origin, new_ray_pickup, jet_vector, new_ray_vector, intersections)
    
    return intersections

def generate_droplets(scene, intersections):
    droplets = []

    for start_index in range(0, len(intersections), 2):
        start_location = intersections[start_index]
        
        # This rationale behind the follwing check is pretty subtle...
        # With scene.rendering_raycast_depth_multipliers greater than 1, the first time a ray might encounter the mesh is
        # below the 0-plane. This results in droplets being generated with a start location on the 0-plane
        # which need to be ignored.
        if start_location[2] < scene.display_minimum_droplet_length_mm:
            continue
        
        try:
            stop_location = intersections[start_index + 1]
        
        except IndexError:
            stop_location = Vector((start_location[0], start_location[1], (start_location[2] - scene.display_minimum_droplet_length_mm)))
        
        droplets.append(start_location)
        droplets.append(stop_location)
    
    return droplets

@persistent
def render_droplets(scene):
    global draw_handler

    bpy.app.handlers.depsgraph_update_pre.remove(render_droplets)

    try:
        bpy.types.SpaceView3D.draw_handler_remove(draw_handler, 'WINDOW')

    except:
        pass

    jet_vector = Vector((0, 0, -(scene.display_height_mm * scene.rendering_raycast_depth_multiplier)))

    droplets = []

    for x in range(0, scene.display_width_mm, scene.display_width_nozzle_spacing_mm):
        for y in range(0, scene.display_depth_mm, scene.display_depth_nozzle_spacing_mm):
            nozzle_location = Vector((x, y, scene.display_height_mm))
            intersections = get_intersections(scene, nozzle_location, nozzle_location, jet_vector, jet_vector, [])
            
            if intersections:
                droplets = droplets + generate_droplets(scene, intersections)
    
    droplet_colours = []

    for droplet in droplets:
        droplet_colours.append(scene.rendering_droplet_colour)
    
    shader = gpu.shader.from_builtin('3D_SMOOTH_COLOR')
    batch = batch_for_shader(shader, 'LINES', {"pos": droplets, "color": droplet_colours})

    def draw():
        shader.bind()
        batch.draw(shader)

    draw_handler = bpy.types.SpaceView3D.draw_handler_add(draw, (), 'WINDOW', 'POST_VIEW')

    bpy.app.handlers.depsgraph_update_pre.append(render_droplets)

def register_droplet_handler(self, context):
    live = context.scene.rendering_live

    if live:
        bpy.app.handlers.depsgraph_update_pre.append(render_droplets)
    
    else:
        bpy.app.handlers.depsgraph_update_pre.remove(render_droplets)
