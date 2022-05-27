import bpy
from . import scene_manager, droplet_generation

# "Display Configuration" Properties
display_dimensions = [
    ('display_width_mm', bpy.props.IntProperty(name='Width [X] (mm)', default=120, min=0, update=scene_manager.redraw_bounding_box)),
    ('display_depth_mm', bpy.props.IntProperty(name='Depth [Y] (mm)', default=80, min=0, update=scene_manager.redraw_bounding_box)),
    ('display_height_mm', bpy.props.IntProperty(name='Height [Z] (mm)', default=100, min=0, update=scene_manager.redraw_bounding_box))
]

display_spacing = [
    ('display_width_nozzle_spacing_mm', bpy.props.IntProperty(name='Width Nozzle Spacing (mm)', default=8, min=0)),
    ('display_depth_nozzle_spacing_mm', bpy.props.IntProperty(name='Depth Nozzle Spacing (mm)', default=8, min=0))
]

display_droplet_size = [('display_minimum_droplet_length_mm', bpy.props.FloatProperty(name='Minimum Droplet Length (mm)', default=2, min=0))]

# "Rendering" Properties
rendering = [
    ('rendering_raycast_depth_multiplier', bpy.props.FloatProperty(name='Raycast Depth Multiplier', default=2, min=0)),
    ('rendering_droplet_colour', bpy.props.FloatVectorProperty(name='Droplet Colour', size=4, subtype="COLOR", default=(0.0, 0.0, 1.0, 0.7))),
    ('rendering_bounding_box', bpy.props.BoolProperty(name='Show Display Bounding Box?', default=True, update=scene_manager.toggle_bounding_box_visible)),
    ('rendering_live', bpy.props.BoolProperty(name='Live Update?', default=False, update=droplet_generation.register_droplet_handler))
]

all_properties = display_dimensions + display_spacing + display_droplet_size + rendering

def set_attributes():
    for (name, value) in all_properties:
        setattr(bpy.types.Scene, name, value)

def reset_attributes():
    for (name, value) in all_properties:
        delattr(bpy.types.Scene, name)