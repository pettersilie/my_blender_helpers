import bpy
from .. import *
from ..properties.alphaplants_decorator_properties import AlphaPlantsDecoratorProperties






class AlphaPlantsDecoratorPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_idname = 'VIEW3D_PT_alphaplants_decorator_panel'
    bl_label = 'Alphaplants Decorator'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "HELPERS"
    
    def draw(self, context):
        
        
        
        subrow = self.layout
        
        subrow.prop(context.scene.alphaplants_decorator_props, 'camera_distance_from')
        
        subrow.row()
        subrow.row()
        subrow.operator('custom.alphaplants_decorator_operator', text = 'Render')
        self.layout.separator()  