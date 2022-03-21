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
        props = context.scene.alphaplants_renderer_props
        
       
        subrow.prop(props, 'plant_export_path')
        subrow.prop(props, 'leaves_path')
        subrow.row()
        subrow.row()
        subrow.prop(props, 'res_x')
        subrow.prop(props, 'res_y')
        subrow.row()
        subrow.row()
        subrow.prop(props, 'random_seed_from')
        subrow.prop(props, 'random_seed_to')
        subrow.row()
        subrow.row()
        subrow.prop(props, 'random_leaves_from')
        subrow.prop(props, 'random_leaves_to')
        subrow.row()
        subrow.row()
        subrow.prop(props, 'random_levels_from')
        subrow.prop(props, 'random_levels_to')
        subrow.row()
        subrow.row()
        subrow.prop(props, 'random_trunk_heigth_from')
        subrow.prop(props, 'random_trunk_height_to')
        subrow.row()
        subrow.row()
        subrow.prop(props, 'random_scale_from')
        subrow.prop(props, 'random_scale_to')
        subrow.row()
        subrow.row()
        subrow.prop(props, 'trunk_extension_from')
        subrow.prop(props, 'trunk_extension_to')
        subrow.row()
        subrow.row()
        subrow.prop(props, 'amount_plants')
        subrow.row()
        subrow.row()
        subrow.prop(props, 'render_toggle')
        subrow.row()
        subrow.row()
        subrow.operator('custom.alphaplants_renderer_operator', text = 'Render')
        
        
        



    
    
    
  
 
    