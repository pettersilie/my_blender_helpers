import bpy
from .. import *
from ..properties.alphacloud_generator_properties import AlphaCloudsGeneratorProperties




class GenerateUI(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_idname = 'VIEW3D_PT_example_panel'
    bl_label = 'Lego Helper'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "LEGO"
    
    def draw(self, context):
        
        self.layout.label(text='ALPHACLOUDS GENERATOR')
        
        subrow = self.layout
        
        subrow.prop(context.scene.alphaclouds_generator_props, 'camera_distance_from')
        subrow.prop(context.scene.alphaclouds_generator_props, 'camera_distance_to')
        subrow.prop(context.scene.alphaclouds_generator_props, 'metaball_area_x_from')
        subrow.prop(context.scene.alphaclouds_generator_props, 'metaball_area_x_to')
        subrow.prop(context.scene.alphaclouds_generator_props, 'metaball_area_y_from')
        subrow.prop(context.scene.alphaclouds_generator_props, 'metaball_area_y_to')
        subrow.prop(context.scene.alphaclouds_generator_props, 'metaball_area_z_from')
        subrow.prop(context.scene.alphaclouds_generator_props, 'metaball_area_z_to')
        subrow.prop(context.scene.alphaclouds_generator_props, 'metaball_scale_from')
        subrow.prop(context.scene.alphaclouds_generator_props, 'metaball_scale_to')
        subrow.prop(context.scene.alphaclouds_generator_props, 'metaball_amount_from')
        subrow.prop(context.scene.alphaclouds_generator_props, 'metaball_amount_to')
        subrow.prop(context.scene.alphaclouds_generator_props, 'sun_power_from')
        subrow.prop(context.scene.alphaclouds_generator_props, 'sun_power_to')
        subrow.prop(context.scene.alphaclouds_generator_props, 'amount_of_clouds')
        subrow.prop(context.scene.alphaclouds_generator_props, 'render_toggle')
        subrow.prop(context.scene.alphaclouds_generator_props, 'cloud_export_path')
        subrow.operator('custom.alphaclouds_generator_operator', text = 'Generate')
        self.layout.separator()  
        
        self.layout.label(text='ALPHACLOUDS INSERTER')
    