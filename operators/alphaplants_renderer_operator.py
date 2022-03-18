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
        return True
    
    #this is the cream of the entire operator class, this one's the function that gets
    #executed when the button is pressed
    def execute(self, context):
        #just do the logic here
        

        
        
        props = context.scene.alphaplants_renderer_props
        
        
        plant_renderer.OUTPUT = props.plant_export_path
        plant_renderer.LEAVES_DIR = props.leaves_path
        
        RENDER = props.render_toggle
        
        
        plant_renderer.RES_X = props.res_x
        plant_renderer.RES_Y = props.res_y


        plant_renderer.TREE_SEED_MIN = props.random_seed_from
        plant_renderer.TREE_SEED_MAX = props.random_seed_to
        
        plant_renderer.LEAVES_MIN = props.random_leaves_from
        plant_renderer.LEAVES_MAX = props.random_leaves_to
        
        plant_renderer.LEVELS_MIN = props.random_levels_from
        plant_renderer.LEVELS_MAX = props.random_levels_to
        
        plant_renderer.TRUNK_HEIGHT_FROM = props.random_trunk_heigth_from
        plant_renderer.TRUNK_HEIGHT_TO = props.random_trunk_height_to
        
        plant_renderer.SCALE_FROM = props.random_scale_from
        plant_renderer.SCALE_FROM = props.random_scale_to
        
        plant_renderer.IMAGES_TO_PRODUCE = props.amount_plants
        
        
        counter = 0
        plant_renderer.get_alpha_plants()
        while counter < props.amount_plants:
    
    
          plant_renderer.delete_all()
          plant_renderer.setup()
          
          plant_renderer.create_tree()
          plant_renderer.create_leaves_material()
          plant_renderer.create_ivy_material()
          if (RENDER == True):
            plant_renderer.render(counter)
          counter = counter + 1
        
            

    
    
    
    
    
   
        
        
        
        
        

        #this is a report, it pops up in the area defined in the word
        #in curly braces {} which is the first argument, second is the actual displayed text
        self.report({'INFO'}, "The custom operator actually worked!")
        #return value tells blender wether the operation finished sueccessfully
        #needs to be in curly braces also {}
        return {'FINISHED'}