import bpy
from .. import *
from ..properties.rocks_generator_properties import RocksGeneratorProperties




class FaceImporterPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_idname = 'VIEW3D_PT_face_importer_panel'
    bl_label = 'Face Importer'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "HELPERS"
    
    def draw(self, context):
        
        
        
        subrow = self.layout
        props = context.scene.face_importer_props
        
        subrow.prop(props, 'rock_texture_dir')
        subrow.row()
        subrow.row()
        
        subrow.prop(props, 'import object')
        
        subrow.row()
        subrow.row()
        subrow.operator('custom.face_importer_operator', text = 'Import')
         