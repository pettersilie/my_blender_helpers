import bpy
from .. import *
from ..properties.rocks_generator_properties import RocksGeneratorProperties




class RocksGeneratorPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_idname = 'VIEW3D_PT_rocks_generator_panel'
    bl_label = 'Rocks Generator'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "HELPERS"
    
    def draw(self, context):
        
        
        
        subrow = self.layout
        props = context.scene.rocks_generator_props
        
        subrow.prop(props, 'rock_texture_dir')
        subrow.row()
        subrow.row()
        subrow.prop(props, 'delete_toggle')
        subrow.row()
        subrow.prop(props, 'sphere_subdivision')
        subrow.row()
        subrow.prop(props, 'displace_percentage_from')
        subrow.prop(props, 'displace_percentage_to')
        subrow.row()
        subrow.prop(props, 'displace_strength_from')
        subrow.prop(props, 'displace_strength_to')
        subrow.row()
        subrow.row()
        subrow.prop(props, 'scale_factor_x_from')
        subrow.prop(props, 'scale_factor_x_to')
        subrow.prop(props, 'scale_factor_y_from')
        subrow.prop(props, 'scale_factor_y_to')
        subrow.prop(props, 'scale_factor_z_from')
        subrow.prop(props, 'scale_factor_z_to')
        subrow.row()
        subrow.row()
        
        subrow.prop(props, 'rot_x_from')
        subrow.prop(props, 'rot_x_to')
        subrow.prop(props, 'rot_y_from')
        subrow.prop(props, 'rot_y_to')
        subrow.prop(props, 'rot_z_from')
        subrow.prop(props, 'rot_z_to')
      
        subrow.row()
        subrow.row()
        subrow.prop(props, 'smooth_toggle')
        subrow.row()
        subrow.row()
        
        subrow.prop(props, 'amount_of_rocks')
        subrow.prop(props, 'amount_of_duplicates')
        subrow.row()
        subrow.row()
        subrow.prop(props, 'decorate_object')
        
        subrow.row()
        subrow.row()
        subrow.operator('custom.rocks_generator_operator', text = 'Generate')
         