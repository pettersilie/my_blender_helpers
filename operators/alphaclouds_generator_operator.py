import bpy
from ..scripts import alphaclouds_generator
import random
from random import uniform


class AlphacloudsGeneratorOperator(bpy.types.Operator):

    bl_idname = 'custom.alphaclouds_generator_operator'

    bl_label = 'Generate'

    bl_options = {'INTERNAL'}


    @classmethod
    def poll(cls, context):
        #check the context here
        return context.object is not None
    
    #this is the cream of the entire operator class, this one's the function that gets
    #executed when the button is pressed
    def execute(self, context):
        #just do the logic here
        

        
        
        props = context.scene.alphaclouds_generator_props
        
        alphaclouds_generator.OUTPUT = props.cloud_export_path

        alphaclouds_generator.CAMERA_DISTANCE_FROM = props.camera_distance_from
        alphaclouds_generator.CAMERA_DISTANCE_TO = props.camera_distance_to

        alphaclouds_generator.METABALL_AREA_X_FROM = props.metaball_area_x_from 
        alphaclouds_generator.METABALL_AREA_X_TO = props.metaball_area_x_to

        alphaclouds_generator.METABALL_AREA_Z_FROM = props.metaball_area_z_from
        alphaclouds_generator.METABALL_AREA_Z_TO = props.metaball_area_z_to

        alphaclouds_generator.METABALL_AREA_Y_FROM = props.metaball_area_y_from
        alphaclouds_generator.METABALL_AREA_Y_TO = props.metaball_area_y_to

        alphaclouds_generator.METABALL_SCALE_FROM = props.metaball_scale_from
        alphaclouds_generator.METABALL_SCALE_TO = props.metaball_scale_to
        alphaclouds_generator.METABALLS_AMOUNT_FROM = props.metaball_amount_from
        alphaclouds_generator.METABALLS_AMOUNT_TO = props.metaball_amount_to

        alphaclouds_generator.SUN_POWER_FROM = props.sun_power_from
        alphaclouds_generator.SUN_POWER_TO = props.sun_power_to

        alphaclouds_generator.AMOUNT_OF_RENDERED_CLOUDS = props.amount_of_clouds
        
        
        alphaclouds_generator.printit()
        
        counter = 1
        
      
    
        while counter <= alphaclouds_generator.AMOUNT_OF_RENDERED_CLOUDS:
            alphaclouds_generator.delete_all()
            alphaclouds_generator.setup()
            alphaclouds_generator.create_metaballs()
            alphaclouds_generator.add_material()
            if (props.render_toggle == True):
                alphaclouds_generator.render(counter)
            print ("Generating Cloud Image: " + str(counter))
           
            counter = counter +1
    
        
        
        
        
        
        #this is a report, it pops up in the area defined in the word
        #in curly braces {} which is the first argument, second is the actual displayed text
        self.report({'INFO'}, "The custom operator actually worked!")
        #return value tells blender wether the operation finished sueccessfully
        #needs to be in curly braces also {}
        return {'FINISHED'}