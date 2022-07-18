import sys

# Make cascade_visualizer the root module name, (if visualizer dir not exactly named "cascade_visualizer")
if __name__ != "cascade_visualizer":
    sys.modules["cascade_visualizer"] = sys.modules[__name__]

# Check if this add-on is being reloaded
if "bpy" not in locals():
    from cascade_visualizer import properties, menu, cascade_visualizer, scene_manager

else:
    import importlib

    properties = importlib.reload(properties)
    menu = importlib.reload(menu)
    cascade_visualizer = importlib.reload(cascade_visualizer)
    scene_manager = importlib.reload(scene_manager)

import bpy
from bpy.app.handlers import persistent

bl_info = {
    'name': 'Cascade Visualizer',
    'blender': (3, 0, 0),
    'category': 'Animation',
    'version': (0, 0, 1),
    'author': 'Toby Thomson',
    'description': 'Simulates and generate animations for the cascade display system',
}

cascade_visualizer_classes = [
    scene_manager.DeleteOverride,
    menu.BakeCSVOperator,
    menu.LoadCSVOperator,
    menu.DisplayConfigurationPanel,
    menu.DisplayDimensionsPanel,
    menu.DisplaySpacingPanel,
    menu.RenderingOptionsPanel,
    menu.ActionsPanel
]

@persistent
def setup_scene(scene):
    bpy.app.handlers.depsgraph_update_pre.remove(setup_scene)

    try:
        scene_manager.remove_bounding_box(None, bpy.context)

    except:
        pass

    scene_manager.draw_bounding_box(None, bpy.context)

    for area in bpy.context.window.screen.areas:
        if area.type == 'VIEW_3D':
            area.tag_redraw()

def register():
    properties.set_attributes()
    
    for cascade_visualizer_class in cascade_visualizer_classes:
        bpy.utils.register_class(cascade_visualizer_class)
    
    bpy.app.handlers.depsgraph_update_pre.append(setup_scene)

def unregister():
    bpy.app.handlers.depsgraph_update_pre.remove(cascade_visualizer.render_droplets)
    
    properties.reset_attributes()

    for cascade_visualizer_class in cascade_visualizer_classes:
        bpy.utils.unregister_class(cascade_visualizer_class)
    
    scene_manager.remove_bounding_box(None, bpy.context)
