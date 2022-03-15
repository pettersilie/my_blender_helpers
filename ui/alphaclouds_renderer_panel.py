import bpy
from .. import *
from ..properties.alphaclouds_renderer_properties import AlphaCloudsRendererProperties




class AlphaCloudsRendererPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_idname = 'VIEW3D_PT_alphaclouds_renderer_panel'
    bl_label = 'Alphaclouds Renderer'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "HELPERS"
    
    def draw(self, context):
        
        
        
        subrow = self.layout
        
        subrow.prop(context.scene.alphaclouds_renderer_props, 'camera_distance_from')
        subrow.prop(context.scene.alphaclouds_renderer_props, 'camera_distance_to')
        subrow.prop(context.scene.alphaclouds_renderer_props, 'metaball_area_x_from')
        subrow.prop(context.scene.alphaclouds_renderer_props, 'metaball_area_x_to')
        subrow.prop(context.scene.alphaclouds_renderer_props, 'metaball_area_y_from')
        subrow.prop(context.scene.alphaclouds_renderer_props, 'metaball_area_y_to')
        subrow.prop(context.scene.alphaclouds_renderer_props, 'metaball_area_z_from')
        subrow.prop(context.scene.alphaclouds_renderer_props, 'metaball_area_z_to')
        subrow.prop(context.scene.alphaclouds_renderer_props, 'metaball_scale_from')
        subrow.prop(context.scene.alphaclouds_renderer_props, 'metaball_scale_to')
        subrow.prop(context.scene.alphaclouds_renderer_props, 'metaball_amount_from')
        subrow.prop(context.scene.alphaclouds_renderer_props, 'metaball_amount_to')
        subrow.prop(context.scene.alphaclouds_renderer_props, 'sun_power_from')
        subrow.prop(context.scene.alphaclouds_renderer_props, 'sun_power_to')
        subrow.prop(context.scene.alphaclouds_renderer_props, 'amount_of_clouds')
        subrow.prop(context.scene.alphaclouds_renderer_props, 'render_toggle')
        subrow.prop(context.scene.alphaclouds_renderer_props, 'cloud_export_path')
        subrow.operator('custom.alphaclouds_renderer_operator', text = 'Render')
        self.layout.separator()  