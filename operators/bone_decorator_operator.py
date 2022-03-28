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
        

        
        
        props = context.scene.bone_decorator_props

        
        
        
        
        
        


    
        
        
        
        
        
        #this is a report, it pops up in the area defined in the word
        #in curly braces {} which is the first argument, second is the actual displayed text
        self.report({'INFO'}, "The custom operator actually worked!")
        #return value tells blender wether the operation finished sueccessfully
        #needs to be in curly braces also {}
        return {'FINISHED'}