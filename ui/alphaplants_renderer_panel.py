import bpy
from .. import *
from ..properties.alphaplants_renderer_properties import AlphaPlantsRendererProperties




class AlphaPlantsRendererPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_idname = 'VIEW3D_PT_alphaplants_renderer_panel'
    bl_label = 'Alphaplants Renderer'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "HELPERS"
    
    def draw(self, context):
        
        
        
        subrow = self.layout
        
        subrow.prop(context.scene.alphaplants_renderer_props, 'camera_distance_from')
        
        
        
        subrow.row()
        subrow.row()
        subrow.operator('custom.alphaplants_renderer_operator', text = 'Render')
        self.layout.separator()  