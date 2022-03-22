import bpy
from ..scripts import plant_decorator
from ..scripts import plant_renderer
import random
from random import uniform
from ..utils import toolbox


class AlphaPlantsDecoratorOperator(bpy.types.Operator):

    bl_idname = 'custom.alphaplants_decorator_operator'

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
        
        decorator_props = context.scene.alphaplants_decorator_props
        
        renderer_props = context.scene.alphaplants_renderer_props
        
        
        
        
        plant_renderer.OUTPUT = renderer_props.plant_export_path
        plant_renderer.LEAVES_DIR = renderer_props.leaves_path


        plant_renderer.TREE_SEED_MIN = renderer_props.random_seed_from
        plant_renderer.TREE_SEED_MAX = renderer_props.random_seed_to
        
        plant_renderer.LEAVES_MIN = renderer_props.random_leaves_from
        plant_renderer.LEAVES_MAX = renderer_props.random_leaves_to
        
        plant_renderer.LEVELS_MIN = renderer_props.random_levels_from
        plant_renderer.LEVELS_MAX = renderer_props.random_levels_to
        
        plant_renderer.TRUNK_HEIGHT_FROM = renderer_props.random_trunk_heigth_from
        plant_renderer.TRUNK_HEIGHT_TO = renderer_props.random_trunk_height_to
        
        plant_renderer.SCALE_FROM = renderer_props.random_scale_from
        plant_renderer.SCALE_FROM = renderer_props.random_scale_to
        
       
        plant_renderer.TRUNK_EXT_FROM = renderer_props.trunk_extension_from
        plant_renderer.TRUNK_EXT_TO = renderer_props.trunk_extension_to
        
        
        
        
        
        
        plant_decorator.create_collection()
        
        
        
        if (decorator_props.delete_toggle == True):
            plant_decorator.delete_plants()
            
        if (decorator_props.images_toggle == True and (renderer_props.plant_export_path is None or renderer_props.plant_export_path == "")):
            return {'FINISHED'}
        
        
        plant_decorator.USE_IMAGES = decorator_props.images_toggle
        plant_decorator.DECORATE_OBJECT = decorator_props.decorate_object
        plant_decorator.IMAGE_TURNS = decorator_props.images_turns  
        plant_decorator.PLANT_DIRECTORY = renderer_props.plant_export_path
        plant_decorator.SCALE_FROM = renderer_props.random_scale_from
        plant_decorator.SCALE_TO = renderer_props.random_scale_to
        
        if (decorator_props.images_toggle == True):
            plant_decorator.read_alphaplants_from_folder()
        else:
            plant_renderer.get_alpha_plants()
            
            
        if (decorator_props.decorate_object is not None):
            plant_decorator.get_decorate_vertices()
            
        
        counter = 0
        while counter < decorator_props.amount_of_plants:
        
            if (decorator_props.images_toggle == True):
                plant_decorator.import_image_plant()
            else:
                plant_decorator.create_curves_tree()
        
        
            plant_decorator.scale_plant()
            
            if (decorator_props.decorate_object is not None):
                plant_decorator.move_plant_to_decorate_vertex()
            counter = counter + 1;
            plant_decorator.CURRENT_COUNTER = plant_decorator.CURRENT_COUNTER +1
            
            
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    
        
        
        
        
        toolbox.purge_orphans()
        #this is a report, it pops up in the area defined in the word
        #in curly braces {} which is the first argument, second is the actual displayed text
        self.report({'INFO'}, "The custom operator actually worked!")
        #return value tells blender wether the operation finished sueccessfully
        #needs to be in curly braces also {}
        return {'FINISHED'}