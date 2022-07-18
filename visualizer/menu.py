import bpy
from . import properties

# Operators
class BakeCSVOperator(bpy.types.Operator):
    bl_idname = 'cascade_visualizer.bake_csv_operator'
    bl_label = 'Bake CSV'
    
    def execute(self, context):
        print('Feature not implemented yet...')
            
        return {'FINISHED'}

class LoadCSVOperator(bpy.types.Operator):
    bl_idname = 'cascade_visualizer.load_csv_operator'
    bl_label = 'Load CSV'
    
    def execute(self, context):
        print('Feature not implemented yet...')
            
        return {'FINISHED'}

# Classes
class CascadeVisualizerPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Cascade Visualizer'

class DisplayConfigurationPanel(CascadeVisualizerPanel):
    bl_idname = 'VIEW3D_PT_cascade_visualizer_display'
    bl_label = 'Display Configuration'

    def draw(self, context):
        column = self.layout.column()
        
        for (name, value) in properties.display_configuration:
            row = column.row()
            row.prop(context.scene, name)

class RenderingOptionsPanel(CascadeVisualizerPanel):
    bl_idname = 'VIEW3D_PT_cascade_visualizer_rendering'
    bl_label = 'Rendering Options'

    def draw(self, context):
        column = self.layout.column()
        
        for (name, value) in properties.rendering:
            row = column.row()
            row.prop(context.scene, name)

class ActionsPanel(CascadeVisualizerPanel):
    bl_idname = 'VIEW3D_PT_cascade_visualizer_actions'
    bl_label = 'Actions'

    def draw(self, context):
        column = self.layout.column()

        column.operator('cascade_visualizer.bake_csv_operator', text='Bake CSV')
        column.operator('cascade_visualizer.load_csv_operator', text='Load CSV')
