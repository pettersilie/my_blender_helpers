import bpy
from ..scripts import face_importer
import random
from ..utils import toolbox


class FaceImporterOperator(bpy.types.Operator):

    bl_idname = 'custom.face_importer_operator'

    bl_label = 'Import'

    bl_options = {'INTERNAL'}


    @classmethod
    def poll(cls, context):
        #check the context here
        return True
    
    #this is the cream of the entire operator class, this one's the function that gets
    #executed when the button is pressed
    def execute(self, context):
        #just do the logic here
        

        
        
        props = context.scene.face_importer_props

        if (props.face_object is None):
            return {'FINISHED'}
            
        if (props.delete_toggle == True):
            face_importer.delete_current_face()   
            #toolbox.purge_orphans()
            #toolbox.purge_orphans()
            #toolbox.purge_orphans()
            
            
        
        face_importer.SELECTED_OBJECT = props.face_object
        face_importer.FACE_BLEND_FILE = props.face_file
        face_importer.SCALE_FACTOR = props.scale_factor
        face_importer.DISTANCE_PERCENTAGE = props.armature_distance_percent
        
        if (toolbox.file_exists(props.face_file) == False):
            return {'FINISHED'}
        
        face_importer.get_selected_object()
        face_importer.import_face()
        
        face_importer.move_2Dface()
        face_importer.do_resizinig()
      
        face_importer.parent_to_headbone()
      



        face_importer.do_shrinkwrapping()
        
        if (props.finish_toggle == True):
            face_importer.finish()
        
        
        #this is a report, it pops up in the area defined in the word
        #in curly braces {} which is the first argument, second is the actual displayed text
        self.report({'INFO'}, "The custom operator actually worked!")
        #return value tells blender wether the operation finished sueccessfully
        #needs to be in curly braces also {}
        return {'FINISHED'}