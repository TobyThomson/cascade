import bpy
import bmesh

def draw_bounding_box(self, context):
    print('in bounding box...')

    bpy.ops.object.empty_add(type='CUBE', location=(0,0,0))

    return None