import bpy
from mathutils import Vector  
from mathutils.bvhtree import BVHTree
import gpu
from gpu_extras.batch import batch_for_shader
import time

then = time.time()

# TODO:
# 1. Get handlers to work
# 2. Refresh the rain effect each frame
# 3. Draw wireframe bounding box of the display area
# 4. Buttons in blender to set display size + colour + etc.
# 5. See if I can speed up some bits [x]
# 6. Deal with line length clipping bug [x]
# 7. Get raycast depth working properly [x]

# Setup variables
Nozzle_Grid_Height_mm = 100

Nozzle_Grid_Width_mm = 120
Nozzle_Grid_Width_Spacing_mm = 5

Nozzle_Grid_Depth_mm = 80
Nozzle_Grid_Depth_Spacing_mm = 5

Minimum_Droplet_Length_mm = 2

Raycast_Depth_Multiplier = 1

Jet_Vector = Vector((0, 0, -(Nozzle_Grid_Height_mm * Raycast_Depth_Multiplier)))

# Droplet rendering stuff
Droplet_Colour = Vector((0.0, 0.0, 1.0, 0.5))

shader = gpu.shader.from_builtin('3D_SMOOTH_COLOR')

droplets = []

# Main
context = bpy.context
scene = context.scene
depsgraph = context.evaluated_depsgraph_get()

depsgraph.update()

def get_intersections(ray_origin, ray_pickup, ray_vector, intersections):
    if not ray_pickup:
        ray_pickup = ray_origin
    
    raycast_depth = abs(ray_vector[2])
    success, intersection, normal, index, object, matrix = scene.ray_cast(depsgraph, ray_pickup, ray_vector, distance = raycast_depth)
    
    if success:
        new_ray_pickup = intersection - Vector((0, 0, Minimum_Droplet_Length_mm))
        
        if new_ray_pickup[2] < Minimum_Droplet_Length_mm:
            intersection = intersection * Vector((1, 1, 0))
            intersections.append(intersection)
            
            return intersections
        
        ray_delta = Vector((0, 0, 1)) * (ray_origin - intersection)        
        new_ray_vector = Jet_Vector + ray_delta
        
        intersections.append(intersection)
        
        get_intersections(ray_origin, new_ray_pickup, new_ray_vector, intersections)
    
    return intersections

def generate_droplets(intersections):
    for start_index in range(0, len(intersections), 2):
        start_location = intersections[start_index]
        
        # This rationale behind the follwing check is pretty subtle...
        # With Raycast_Depth_Multipliers greater than 1, the first time a ray might encounter the mesh is
        # below the 0-plane. This results in droplets being generated with a start location on the 0-plane
        # which need to be ignored.
        if start_location[2] < Minimum_Droplet_Length_mm:
            continue
        
        try:
            stop_location = intersections[start_index + 1]
        
        except IndexError:
            stop_location = Vector((start_location[0], start_location[1], (start_location[2] - Minimum_Droplet_Length_mm)))
        
        droplets.append(start_location)
        droplets.append(stop_location)

for x in range(0, Nozzle_Grid_Width_mm, Nozzle_Grid_Width_Spacing_mm):
    for y in range(0, Nozzle_Grid_Depth_mm, Nozzle_Grid_Depth_Spacing_mm):
        nozzle_location = Vector((x, y, Nozzle_Grid_Height_mm))
        intersections = get_intersections(nozzle_location, [], Jet_Vector, [])
        
        if intersections:
            generate_droplets(intersections)

def draw():
    shader.bind()
    batch.draw(shader)

droplet_colours = []

for droplet in droplets:
    droplet_colours.append(Droplet_Colour)

batch = batch_for_shader(shader, 'LINES', {"pos": droplets, "color": droplet_colours})
draw_handler = bpy.types.SpaceView3D.draw_handler_add(draw, (), 'WINDOW', 'POST_VIEW')

for area in bpy.context.window.screen.areas:
    if area.type == 'VIEW_3D':
        area.tag_redraw()

now = time.time()
print(f'EXECUTION TIME: {now - then} s')