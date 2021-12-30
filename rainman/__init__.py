# Make rainman the root module name, (if rainman dir not exactly named "rainman")
if __name__ != "rainman":
    sys.modules["rainman"] = sys.modules[__name__]

# Check if this add-on is being reloaded
if "bpy" not in locals():
    from rainman import properties, menu, droplet_generation, scene_manager

else:
    import importlib

    properties = importlib.reload(properties)
    menu = importlib.reload(menu)
    droplet_generation = importlib.reload(droplet_generation)
    scene_manager = importlib.reload(scene_manager)

import bpy
from bpy.app.handlers import persistent

bl_info = {
    'name': 'Rainman',
    'blender': (3, 0, 0),
    'category': 'Animation',
    'version': (0, 0, 1),
    'author': 'Toby Thomson',
    'description': 'A savant to simulate and generate animations for the "cascade" display system',
}

rainman_classes = [
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
    
    for rainman_class in rainman_classes:
        bpy.utils.register_class(rainman_class)
    
    bpy.app.handlers.depsgraph_update_pre.append(setup_scene)

def unregister():
    bpy.app.handlers.depsgraph_update_pre.remove(droplet_generation.render_droplets)
    
    properties.reset_attributes()

    for rainman_class in rainman_classes:
        bpy.utils.unregister_class(rainman_class)
    
    scene_manager.remove_bounding_box(None, bpy.context)