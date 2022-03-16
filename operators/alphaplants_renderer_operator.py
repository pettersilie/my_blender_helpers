import bpy
from ..scripts import plant_renderer
import random
from random import uniform
from ..utils import toolbox


class AlphaPlantsRendererOperator(bpy.types.Operator):

    bl_idname = 'custom.alphaplants_renderer_operator'

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
        

        
        
        props = context.scene.alphaplants_renderer_props
        
 #       alphaclouds_renderer.OUTPUT = props.cloud_export_path

 #       alphaclouds_renderer.CAMERA_DISTANCE_FROM = props.camera_distance_from
  #      alphaclouds_renderer.CAMERA_DISTANCE_TO = props.camera_distance_to

   #     alphaclouds_renderer.METABALL_AREA_X_FROM = props.metaball_area_x_from 
   #     alphaclouds_renderer.METABALL_AREA_X_TO = props.metaball_area_x_to

    #    alphaclouds_renderer.METABALL_AREA_Z_FROM = props.metaball_area_z_from
    #    alphaclouds_renderer.METABALL_AREA_Z_TO = props.metaball_area_z_to

    #    alphaclouds_renderer.METABALL_AREA_Y_FROM = props.metaball_area_y_from
    #    alphaclouds_renderer.METABALL_AREA_Y_TO = props.metaball_area_y_to

   #     alphaclouds_renderer.METABALL_SCALE_FROM = props.metaball_scale_from
   #     alphaclouds_renderer.METABALL_SCALE_TO = props.metaball_scale_to
   #     alphaclouds_renderer.METABALLS_AMOUNT_FROM = props.metaball_amount_from
   #     alphaclouds_renderer.METABALLS_AMOUNT_TO = props.metaball_amount_to

    #    alphaclouds_renderer.SUN_POWER_FROM = props.sun_power_from
    #    alphaclouds_renderer.SUN_POWER_TO = props.sun_power_to

    #    alphaclouds_renderer.AMOUNT_OF_RENDERED_CLOUDS = props.amount_of_clouds
    #    alphaclouds_renderer.RES_X = props.resolution_x
    #    alphaclouds_renderer.RES_Y = props.resolution_y
        
        
     #   alphaclouds_renderer.printit()
        
      #  counter = 1
        
      
    
    #    while counter <= alphaclouds_renderer.AMOUNT_OF_RENDERED_CLOUDS:
    #        alphaclouds_renderer.delete_all()
    #        alphaclouds_renderer.setup()
    #        alphaclouds_renderer.create_metaballs()
    #        alphaclouds_renderer.add_material()
     #       if (props.render_toggle == True):
     #           alphaclouds_renderer.render(counter)
     #       print ("Generating Cloud Image: " + str(counter))
           
      #      counter = counter +1
    
        
        
        
        
        toolbox.purge_orphans()
        #this is a report, it pops up in the area defined in the word
        #in curly braces {} which is the first argument, second is the actual displayed text
        self.report({'INFO'}, "The custom operator actually worked!")
        #return value tells blender wether the operation finished sueccessfully
        #needs to be in curly braces also {}
        return {'FINISHED'}