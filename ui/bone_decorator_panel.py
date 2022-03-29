import bpy
from .. import *
from ..properties.bone_decorator_properties import BoneDecoratorProperties




class BoneDecoratorPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_idname = 'VIEW3D_PT_bone_decroator_panel'
    bl_label = 'Bone Decorator'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "HELPERS"
    
    def draw(self, context):
        
        
        
        subrow = self.layout
        props = context.scene.bone_decorator_props
        
        subrow.prop(props, 'delete_toggle')
        subrow.row()

        subrow.row()
        subrow.prop(props, 'rot_x')
        subrow.prop(props, 'rot_y')
        subrow.prop(props, 'rot_z')
   

        subrow.row()
        subrow.row()
        subrow.prop(props, 'scale_factor')
        subrow.row()
        subrow.row()
        subrow.prop(props, 'decorate_object')
        
        subrow.row()
        subrow.row()
        subrow.operator('custom.bone_decorator_operator', text = 'Decorate')
         