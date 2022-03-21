import bpy
import random
import os
from random import uniform
from math import pi
import time
import numpy as np
from ..utils import toolbox


CURRENT_COUNTER = 0
CURRENT_PLANT_OBJECT = None
PLANT_FILES = []

PLANT_DIRECTORY = None


USE_IMAGES = False
DECORATE_OBJECT = None

DECORATE_VERTICES = []
IMAGE_TURNS = 2






def read_alphaplants_from_folder():
    global PLANT_FILES
    global PLANT_DIRECTORY
    
    PLANT_FILES = toolbox.get_files_from_directory(PLANT_DIRECTORY)



def create_collection():
    
    toolbox.create_root_collection("plants_addon")
    
def delete_plants():
    global CURRENT_COUNTER
    toolbox.delete_objects_from_collection("plants_addon")
    CURRENT_COUNTER = 0
    
    
def import_image_plant():
    global PLANT_FILES
    global USE_IMAGES
    global IMAGE_TURNS
    global CURRENT_COUNTER
    global PLANT_DIRECTORY

    if (USE_IMAGES == False):
        return
        
    if (len(PLANT_FILES) == 0):
        return
        
    img_index = random.randint(0,len(PLANT_FILES))
    
    img_name = PLANT_FILES[img_index]
        
    bpy.ops.import_image.to_plane(files=[{"name":"plant" + str(CURRENT_COUNTER), "name":img_name}], directory=PLANT_DIRECTORY, relative=False)

        
    





    
    
    
    


    
    
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
  
   
    
    
