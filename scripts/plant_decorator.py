import bpy
import random
import os
from random import uniform
from math import pi
import time
import numpy as np
from ..utils import toolbox
from . import plant_renderer


CURRENT_COUNTER = 0
CURRENT_PLANT_OBJECT = None
PLANT_FILES = []

SCALE_FROM = 0
SCALE_TO = 0

PLANT_DIRECTORY = None

AMOUNT_OF_PLANTS = 0
AMOUNT_OF_DUPLICATES = 0


USE_IMAGES = False
DECORATE_OBJECT = None

DECORATE_VERTICES = []
IMAGE_TURNS = 2
ORIG_PLANTS = []



def scale_plant():
    global CURRENT_PLANT_OBJECT
    global SCALE_FROM
    global SCALE_TO
    
    toolbox.deselect_all(True)
    toolbox.select_object(CURRENT_PLANT_OBJECT,True)
    
    scale_val = random.uniform(SCALE_FROM,SCALE_TO)
    
    bpy.ops.transform.resize(value=(scale_val,scale_val,scale_val), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)



def move_plant_to_decorate_vertex():
    global DECORATE_VERTICES
    global CURRENT_PLANT_OBJECT
    global DECORATE_OBJECT
    global USE_IMAGES
    if (DECORATE_OBJECT is None):
        return
    if (len(DECORATE_VERTICES) <= 0):
        return
    
    
    
    
    toolbox.deselect_all(True)
    toolbox.select_object(CURRENT_PLANT_OBJECT,True)
    
   
    
    random_vertex = random.randint(0,len(DECORATE_VERTICES)-1)
    
    
    vertex_coordinates = DECORATE_OBJECT.matrix_world @ DECORATE_VERTICES[random_vertex].co
    CURRENT_PLANT_OBJECT.location.x = vertex_coordinates.x
    CURRENT_PLANT_OBJECT.location.y = vertex_coordinates.y
    CURRENT_PLANT_OBJECT.location.z = vertex_coordinates.z
    if (USE_IMAGES == True):
        half = CURRENT_PLANT_OBJECT.dimensions.z / 2
        CURRENT_PLANT_OBJECT.location.z = CURRENT_PLANT_OBJECT.location.z + half
    del DECORATE_VERTICES[random_vertex]
    



def get_decorate_vertices():
    global DECORATE_VERTICES
    global DECORATE_OBJECT
    
    
    
    if (DECORATE_OBJECT is None):
        return
    
    DECORATE_VERTICES = toolbox.get_selected_vertices_from_object_as_vertex(DECORATE_OBJECT)
    print (str(DECORATE_VERTICES))



def create_curves_tree():
    global CURRENT_PLANT_OBJECT
    global ORIG_PLANTS
    plant_renderer.create_tree()
    plant_renderer.create_leaves_material()
    plant_renderer.create_ivy_material()
    plant_renderer.extend_root_trunk()
    
    toolbox.deselect_all(True)
    tree = toolbox.select_object_by_name("tree",True)
    tree.name = "addon_plant" + "_" + str(CURRENT_COUNTER)
    tree.data.name = "addon_plant" + "_" + str(CURRENT_COUNTER)
    toolbox.deselect_all(True)
    leaves = toolbox.select_object_by_name("leaves",True)
    leaves.name = "addon_leaves" + "_" + str(CURRENT_COUNTER)
    leaves.data.name = "addon_leaves" + "_" + str(CURRENT_COUNTER)
    toolbox.deselect_all(True)
    toolbox.select_object_by_name("addon_leaves" + "_" + str(CURRENT_COUNTER),False)
    toolbox.select_object_by_name("addon_plant" + "_" + str(CURRENT_COUNTER),True)
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)
    CURRENT_PLANT_OBJECT = tree
    if (AMOUNT_OF_DUPLICATES > 0):
        ORIG_PLANTS.append(CURRENT_PLANT_OBJECT)
    

    


def read_alphaplants_from_folder():
    global PLANT_FILES
    global PLANT_DIRECTORY
    
    PLANT_FILES = toolbox.get_files_from_directory(PLANT_DIRECTORY)



def create_collection():
    
    toolbox.create_root_collection("plants_addon")
    
def delete_plants():
    global ORIG_PLANTS
    global CURRENT_COUNTER
    global CURRENT_PLANT_OBJECT
    global ORIG_PLANTS
    global DECORATE_VERTICES
    
    toolbox.deselect_all(True)
    toolbox.delete_objects_from_collection("plants_addon")
    CURRENT_COUNTER = 0
    CURRENT_PLANT_OBJECT = None
    ORIG_PLANTS = []
    DECORATE_VERTICES = []
    
    
    
def import_image_plant():
    global PLANT_FILES
    global USE_IMAGES
    global IMAGE_TURNS
    global CURRENT_COUNTER
    global PLANT_DIRECTORY
    global CURRENT_PLANT_OBJECT
    global AMOUNT_OF_DUPLICATES
    
    toolbox.deselect_all(True)

    if (USE_IMAGES == False):
        return
        
    if (len(PLANT_FILES) == 0):
        return
        
    img_index = random.randint(0,len(PLANT_FILES)-1)
    
    img_name = PLANT_FILES[img_index]
        
    bpy.ops.import_image.to_plane(files=[{"name":"plant" + str(CURRENT_COUNTER), "name":img_name}], directory=PLANT_DIRECTORY, relative=False)
    obj = bpy.context.selected_objects[0]
    print ("OBJECT: " + obj.name)
    CURRENT_PLANT_OBJECT = obj
    toolbox.set_object_name("addon_plant" + "_" + str(CURRENT_COUNTER), CURRENT_PLANT_OBJECT)
    toolbox.link_object_to_collection("plants_addon", CURRENT_PLANT_OBJECT)
    
    toolbox.deselect_all(True)
    toolbox.select_object_by_name("addon_plant" + "_" + str(CURRENT_COUNTER),True)
    
    
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action='SELECT')

    degrees = 360 / IMAGE_TURNS
    counter = 0
    while (counter < IMAGE_TURNS -1):
    
        bpy.ops.mesh.duplicate(mode=1)


        bpy.ops.transform.rotate(value=toolbox.calculate_rotation(degrees), orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        counter = counter + 1
    bpy.ops.object.editmode_toggle()
    if (AMOUNT_OF_DUPLICATES > 0):
        ORIG_PLANTS.append(CURRENT_PLANT_OBJECT)
        



def create_duplicate_image():
    
   
    global CURRENT_PLANT_OBJECT
    global CURRENT_COUNTER
    global ORIG_PLANTS
    toolbox.deselect_all(True)
    random_plant = random.randint(0,len(ORIG_PLANTS)-1)
    plant_to_duplicate = ORIG_PLANTS[random_plant]
    
    toolbox.select_object_by_name(plant_to_duplicate.name,True)
    
    bpy.ops.object.duplicate(linked=True)
    
    dupli_obj = toolbox.get_object_by_prefix(plant_to_duplicate.name + ".")
    
    dup_name = "addon_plant" + "_" + str(CURRENT_COUNTER)
    toolbox.set_object_name(dup_name,dupli_obj)
    CURRENT_PLANT_OBJECT = dupli_obj 

    
def create_duplicate_curve_tree():
    
    global CURRENT_PLANT_OBJECT
    global CURRENT_COUNTER
    global ORIG_PLANTS
    
    toolbox.deselect_all(True)
    random_plant = random.randint(0,len(ORIG_PLANTS)-1)
    plant_to_duplicate = ORIG_PLANTS[random_plant]
    
   
   
    leaves_to_dupblicate = plant_to_duplicate.children[0]
    toolbox.select_object_by_name(leaves_to_dupblicate.name,True)
    toolbox.select_object_by_name(plant_to_duplicate.name,False)
    
    bpy.ops.object.duplicate(linked=True)
    
    dupli_plant = toolbox.get_object_by_prefix(plant_to_duplicate.name + ".")
    dupli_leaves = toolbox.get_object_by_prefix(leaves_to_dupblicate.name + ".")
    
    toolbox.set_object_name("addon_plant" + "_" + str(CURRENT_COUNTER),dupli_plant)
    toolbox.set_object_name("addon_leaves" + "_" + str(CURRENT_COUNTER),dupli_leaves)
    
    CURRENT_PLANT_OBJECT = dupli_plant
    
   
    
    





    
    
    
    


    
    
def get_decorate_vertices():
    global DECORATE_VERTICES
    global DECORATE_OBJECT
    
    
    if (DECORATE_OBJECT is None):
        return
    
    DECORATE_VERTICES = toolbox.get_selected_vertices_from_object_as_vertex(DECORATE_OBJECT)       




def main():
    
    

    
    
    delete_all()
   
    get_alpha_plants()
    test_calc()
  
   
    
    
