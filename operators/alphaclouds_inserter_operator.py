import bpy
from ..scripts import alphaclouds_inserter
import random
from random import uniform


class AlphacloudsInserterOperator(bpy.types.Operator):

    bl_idname = 'custom.alphaclouds_inserter_operator'

    bl_label = 'Insert'

    bl_options = {'INTERNAL'}


    @classmethod
    def poll(cls, context):
        #check the context here
        return True
    
    #this is the cream of the entire operator class, this one's the function that gets
    #executed when the button is pressed
    def execute(self, context):
        #just do the logic here
        

        
        
        props = context.scene.alphaclouds_inserter_props
        
        alphaclouds_inserter.CLOUD_AREA_X_FROM = props.cloud_area_x_from
        alphaclouds_inserter.CLOUD_AREA_X_TO = props.cloud_area_x_to
        
        alphaclouds_inserter.CLOUD_AREA_Y_FROM = props.cloud_area_y_from
        alphaclouds_inserter.CLOUD_AREA_Y_TO = props.cloud_area_y_to
        
        alphaclouds_inserter.CLOUD_AREA_Z_FROM = props.cloud_area_z_from
        alphaclouds_inserter.CLOUD_AREA_Z_TO = props.cloud_area_z_to
        
        alphaclouds_inserter.SCALE_FACTOR_X = props.scale_factor_x
        alphaclouds_inserter.SCALE_FACTOR_Y = props.scale_factor_x
        alphaclouds_inserter.SCALE_FACTOR_Z = props.scale_factor_z
        
        alphaclouds_inserter.CLOUDPATH = props.file_import_path
      
        alphaclouds_inserter.TRACK_TO_CAM = props.track_to_camera_toggle

        alphaclouds_inserter.AMOUNT_OF_CLOUDBOXES = props.amount_of_clouds
        alphaclouds_inserter.USE_DUPLICATES = props.use_duplicates_toggle
        alphaclouds_inserter.AMOUNT_OF_DUBPLICATES = props.amount_of_duplicates

        if (props.delete_toggle == True):
            alphaclouds_inserter.cleanup()
            
        alphaclouds_inserter.create_collection()  
        alphaclouds_inserter.get_alphaclouds()
  
        counter = 1
        if (alphaclouds_inserter.CURRENT_COUNTER <= 1):            
            image_name_counter = 1
        else:
            image_name_counter = alphaclouds_inserter.CURRENT_COUNTER 
            
        while counter <= alphaclouds_inserter.AMOUNT_OF_CLOUDBOXES:
            
            print("Creating CloudBox: " + str(image_name_counter))
            
            cloud_overall_name = "cloudMesh" + str(image_name_counter)
            
            alphaclouds_inserter.createCube(cloud_overall_name)
    
    
            alphaclouds_inserter.move_cloudbox_in_area(cloud_overall_name)
            alphaclouds_inserter.scale_cloud(cloud_overall_name)
    
            
            counter = counter +1        
            image_name_counter = image_name_counter + 1
            alphaclouds_inserter.CURRENT_COUNTER = alphaclouds_inserter.CURRENT_COUNTER + 1
        
        if (alphaclouds_inserter.USE_DUPLICATES == True):
            
            counter = 1
            while (counter <= alphaclouds_inserter.AMOUNT_OF_DUBPLICATES):
            
                curr_cloud_index = random.randInt(0,len(alphaclouds_inserter.ORIGINAL_CLOUDS) -1)
                
                more code goes here
        
        
        #this is a report, it pops up in the area defined in the word
        #in curly braces {} which is the first argument, second is the actual displayed text
        self.report({'INFO'}, "The custom operator actually worked!")
        #return value tells blender wether the operation finished sueccessfully
        #needs to be in curly braces also {}
        return {'FINISHED'}