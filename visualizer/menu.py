import bpy
from . import properties

# Operators
class BakeCSVOperator(bpy.types.Operator):
    bl_idname = 'rainman.bake_csv_operator'
    bl_label = 'Bake CSV'
    
    def execute(self, context):
        print('Feature not implemented yet...')
            
        return {'FINISHED'}

class LoadCSVOperator(bpy.types.Operator):
    bl_idname = 'rainman.load_csv_operator'
    bl_label = 'Load CSV'
    
    def execute(self, context):
        print('Feature not implemented yet...')
            
        return {'FINISHED'}

# Classes
class RainmanPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

class DisplayConfigurationPanel(RainmanPanel):
    bl_idname = 'VIEW3D_PT_rainman_display'
    bl_label = "Display Configuration"
    bl_category = 'Rainman'

    def draw(self, context):
        column = self.layout.column()

        column.row().prop(context.scene, properties.display_droplet_size[0][0])

class DisplayDimensionsPanel(RainmanPanel):
    bl_parent_id = "VIEW3D_PT_rainman_display"
    bl_idname = 'VIEW3D_PT_rainman_dimensions'
    bl_label = "Dimensions"

    def draw(self, context):
        column = self.layout.column()
        
        for (name, value) in properties.display_dimensions:
            row = column.row()
            row.prop(context.scene, name)

class DisplaySpacingPanel(RainmanPanel):
    bl_parent_id = "VIEW3D_PT_rainman_display"
    bl_idname = 'VIEW3D_PT_rainman_spacing'
    bl_label = "Spacing"

    def draw(self, context):
        column = self.layout.column()
        
        for (name, value) in properties.display_spacing:
            row = column.row()
            row.prop(context.scene, name)

class RenderingOptionsPanel(RainmanPanel):
    bl_idname = 'VIEW3D_PT_rainman_rendering'
    bl_label = "Rendering Options"
    bl_category = 'Rainman'

    def draw(self, context):
        column = self.layout.column()
        
        for (name, value) in properties.rendering:
            row = column.row()
            row.prop(context.scene, name)

class ActionsPanel(RainmanPanel):
    bl_idname = 'VIEW3D_PT_rainman_actions'
    bl_label = "Actions"
    bl_category = 'Rainman'

    def draw(self, context):
        column = self.layout.column()

        column.operator('rainman.bake_csv_operator', text='Bake CSV')
        column.operator('rainman.load_csv_operator', text='Load CSV')