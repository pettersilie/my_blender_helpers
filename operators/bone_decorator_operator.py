import bpy
from ..scripts import bone_decorator
import random
from random import uniform
from ..utils import toolbox


class BoneDecoratorOperator(bpy.types.Operator):

    bl_idname = 'custom.bone_decorator_operator'

    bl_label = 'Generate'

    bl_options = {'INTERNAL'}


    @classmethod
    def poll(cls, context):
        #check the context here
        return True
    
    #this is the cream of the entire operator class, this one's the function that gets
    #executed when the button is pressed
    def execute(self, context):
        #just do the logic here
        
        print ("starting bone decoration operator")
        

        
        
        props = context.scene.bone_decorator_props
        
        if (props.decorate_object is None):
            print ("decorate_object is None. return")
            return {'FINISHED'}
            
        bone_decorator.DECORATE_OBJECT = props.decorate_object
        
        bone_decorator.ROT_X = props.rot_x
        bone_decorator.ROT_Y = props.rot_y
        bone_decorator.ROT_Z = props.rot_z
        bone_decorator.SCALE_FACTOR = props.scale_factor
                       
        
        
        delete = props.delete_toggle
        if (delete == True):
            bone_decorator.delete_current_bones()
            
        bone_decorator.get_decorate_vertices()
        
        if (len(bone_decorator.DECORATE_VERTICES) == 0):
            print ("decorate vertices not found ... return")
            return {'FINISHED'}
            
            
        bone_decorator.save_cursor_location()
        
        for vertex in bone_decorator.DECORATE_VERTICES:
            print ("Adding bone to vertex: " + str(vertex))
            
            bone_decorator.add_bone(vertex)
            
            bone_decorator.CURRENT_COUNTER = bone_decorator.CURRENT_COUNTER + 1

  
        
        #this is a report, it pops up in the area defined in the word
        #in curly braces {} which is the first argument, second is the actual displayed text
        self.report({'INFO'}, "The custom operator actually worked!")
        #return value tells blender wether the operation finished sueccessfully
        #needs to be in curly braces also {}
        return {'FINISHED'}