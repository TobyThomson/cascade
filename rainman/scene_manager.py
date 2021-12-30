import bpy
import bmesh
from bpy.props import BoolProperty

bounding_box_object_name = 'rainman_bounding_box'

bpy.types.Object.protected = BoolProperty(name='protected', default=False)

class DeleteOverride(bpy.types.Operator):
    bl_idname = "object.delete"
    bl_label = "Object Delete Operator"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        for obj in context.selected_objects:
            if not obj.protected:
                bpy.data.objects.remove(obj)
            
            else:
                print(obj.name +' is protected')
        
        return {'FINISHED'}

def redraw_bounding_box(self, context):
    remove_bounding_box(self, context)
    draw_bounding_box(self, context)

    return None

def draw_bounding_box(self, context):
    width = context.scene.display_width_mm
    depth = context.scene.display_depth_mm
    height = context.scene.display_height_mm

    verticies = [(width, depth, 0.0),
                (width, 0.0, 0.0),
                (0.0, 0.0, 0.0),
                (0.0, depth, 0.0),
                (width, depth, height),
                (width, 0.0, height),
                (0.0, 0.0, height),
                (0.0, depth, height)]

    edges = [(0, 1),
            (1, 2),
            (2, 3),
            (3, 0),
            (4, 5),
            (5, 6),
            (6, 7),
            (7, 4),
            (4, 0),
            (7, 3),
            (6, 2),
            (5, 1)]

    mesh = bpy.data.meshes.new(bounding_box_object_name)
    mesh.from_pydata(verticies, edges, [])

    bounding_box_object = bpy.data.objects.new(bounding_box_object_name, mesh)
    context.scene.collection.objects.link(bounding_box_object)
    
    bounding_box_object.hide_set(not context.scene.rendering_bounding_box)
    bounding_box_object.hide_select = True
    bounding_box_object.protected = True

def remove_bounding_box(self, context):
    bounding_box_object = bpy.data.objects[bounding_box_object_name]
    bpy.data.objects.remove(bounding_box_object)

def toggle_bounding_box_visible(self, context):
    bounding_box_object = bpy.data.objects[bounding_box_object_name]

    current_visibility = bounding_box_object.visible_get()
    bounding_box_object.hide_set(current_visibility)

    return None