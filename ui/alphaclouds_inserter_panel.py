import bpy
from .. import *
from ..properties.alphaclouds_renderer_properties import AlphaCloudsRendererProperties




class AlphaCloudsInserterPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_idname = 'VIEW3D_PT_alphaclouds_inserter_panel'
    bl_label = 'Alphaclouds Inserter'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "HELPERS"
    
    def draw(self, context):
        
        
        
        subrow = self.layout
        subrow.prop(context.scene.alphaclouds_inserter_props, 'file_import_path')
        subrow.row()
        subrow.prop(context.scene.alphaclouds_inserter_props, 'delete_toggle')
        subrow.row()
        subrow.prop(context.scene.alphaclouds_inserter_props, 'cloud_area_x_from')
        subrow.prop(context.scene.alphaclouds_inserter_props, 'cloud_area_x_to')
        subrow.row()
        subrow.prop(context.scene.alphaclouds_inserter_props, 'cloud_area_y_from')
        subrow.prop(context.scene.alphaclouds_inserter_props, 'cloud_area_y_to')
        subrow.row()
        subrow.prop(context.scene.alphaclouds_inserter_props, 'cloud_area_z_from')
        subrow.prop(context.scene.alphaclouds_inserter_props, 'cloud_area_z_to')
        subrow.row()
        subrow.prop(context.scene.alphaclouds_inserter_props, 'scale_factor_x')
        subrow.prop(context.scene.alphaclouds_inserter_props, 'scale_factor_z')
        subrow.row()
        subrow.prop(context.scene.alphaclouds_inserter_props, 'amount_of_clouds')
        
        subrow.prop(context.scene.alphaclouds_inserter_props, 'use_duplicates_toggle')
        subrow.prop(context.scene.alphaclouds_inserter_props, 'amount_of_duplicates')
        subrow.row()
        subrow.prop(context.scene.alphaclouds_inserter_props, 'track_to_camera_toggle')
        subrow.row()
        subrow.row()
        subrow.prop(context.scene.alphaclouds_inserter_props, 'emission_color')
        subrow.prop(context.scene.alphaclouds_inserter_props, 'emission_strength')
        
        subrow.operator('custom.alphaclouds_inserter_operator', text = 'Import')
        
 
        
 



    

    