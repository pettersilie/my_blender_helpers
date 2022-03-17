import bpy
from ..scripts import rocks_generator
import random
from random import uniform
from ..utils import toolbox


class RocksGeneratorOperator(bpy.types.Operator):

    bl_idname = 'custom.rocks_generator_operator'

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
        

        
        
        props = context.scene.rocks_generator_props

        rocks_generator.SCALE_X_FROM = props.scale_factor_x_from
        rocks_generator.SCALE_X_TO = props.scale_factor_x_to
        rocks_generator.SCALE_Y_FROM = props.scale_factor_y_from
        rocks_generator.SCALE_Y_TO = props.scale_factor_y_to
        rocks_generator.SCALE_Z_FROM = props.scale_factor_z_from
        rocks_generator.SCALE_Z_TO = props.scale_factor_z_to
        
        rocks_generator.ROT_X_FROM = props.rot_x_from
        rocks_generator.ROT_X_TO = props.rot_x_to
        rocks_generator.ROT_Y_FROM = props.rot_y_from
        rocks_generator.ROT_Y_TO = props.rot_y_to
        rocks_generator.ROT_Z_FROM = props.rot_z_from
        rocks_generator.ROT_Z_TO = props.rot_z_to
        
        rocks_generator.AMOUNT_OF_ROCKS = props.amount_of_rocks
        rocks_generator.AMOUNT_OF_DUPLICATES = props.amount_of_duplicates
        rocks_generator.DISPLACE_PERCENTAGE_FROM = props.displace_percentage_from
        rocks_generator.DISPLACE_PERCENTAGE_TO = props.displace_percentage_to
        rocks_generator.SUBDIVISIONS = props.sphere_subdivision
        
        rocks_generator.DISPLACEMENT_STRENGTH_FROM = props.displace_strength_from
        rocks_generator.DISPLACEMENT_STRENGTH_TO = props.displace_strength_to
            
        rocks_generator.DECORATE_OBJECT = props.decorate_object
        
        rocks_generator.SMOOTH = props.smooth_toggle
        rocks_generator.ROCK_TEXTURE_DIR = props.rock_texture_dir
        
        DELETE = props.delete_toggle
        
        counter = 0
        
        if (DELETE == True):
            rocks_generator.delete_rocks()
        rocks_generator.read_textures()
        rocks_generator.create_collection()
        if (rocks_generator.DECORATE_OBJECT is not None):
            rocks_generator.get_decorate_vertices()
        
        
        while counter <= rocks_generator.AMOUNT_OF_ROCKS:
        
            toolbox.deselect_all(True)
            rocks_generator.create_rock()
            rocks_generator.add_vertex_group()
            rocks_generator.add_displacement_modifier()
            rocks_generator.create_material()
            
            if (rocks_generator.SMOOTH == True):
                rocks_generator.make_smooth()
                
            rocks_generator.scale_rock()
            rocks_generator.rotate_rock()
            if (rocks_generator.DECORATE_OBJECT is not None):
                rocks_generator.move_rock_to_decorate_vertex()
        
        
        
            counter = counter +1
            rocks_generator.CURRENT_COUNTER = rocks_generator.CURRENT_COUNTER + 1
  
        if (rocks_generator.AMOUNT_OF_DUPLICATES > 0):
            counter = 0
            while (counter < rocks_generator.AMOUNT_OF_DUPLICATES):
                
                
                rocks_generator.create_duplicate_rock()
                if (rocks_generator.DECORATE_OBJECT is not None):
                    rocks_generator.move_rock_to_decorate_vertex()
                counter = counter+1
                
        
        
        
        
        


    
        
        
        
        
        toolbox.purge_orphans()
        #this is a report, it pops up in the area defined in the word
        #in curly braces {} which is the first argument, second is the actual displayed text
        self.report({'INFO'}, "The custom operator actually worked!")
        #return value tells blender wether the operation finished sueccessfully
        #needs to be in curly braces also {}
        return {'FINISHED'}