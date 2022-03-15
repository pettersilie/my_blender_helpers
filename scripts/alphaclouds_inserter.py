import bpy
import random
from random import uniform
import os
from ..utils import toolbox





CLOUD_AREA_X_FROM = -20000
CLOUD_AREA_X_TO = 20000
CLOUD_AREA_Y_FROM = -20000
CLOUD_AREA_Y_TO = 20000

CLOUD_AREA_Z_FROM = 500
CLOUD_AREA_Z_TO = 800

SCALE_FACTOR_X = 1500
SCALE_FACTOR_Y = 1500
SCALE_FACTOR_Z = 600

FILES = []
ORIGINAL_CLOUDS = []
CLOUDPATH = "C:\\Users\\Mirko\\Desktop\\alphaclouds\\render"

AMOUNT_OF_CLOUDBOXES = 800
USE_DUPLICATES = False
AMOUNT_OF_DUBPLICATES = 0
TRACK_TO_CAM = False

CURRENT_COUNTER = 1


def get_alphaclouds(): 
    global FILES
    global CLOUDPATH
    
    FILES = toolbox.get_files_from_directory(CLOUDPATH)
            
   
    


def cleanup():
    global CURRENT_COUNTER
    global ORIGINAL_CLOUDS
    
    ORIGINAL_CLOUDS = []
    if "cloudCubes" in bpy.data.collections :
        for ob in bpy.data.collections['cloudCubes'].objects:
            ob.hide_set(False)
            ob.hide_render = False
            ob.select_set(True)
        
            bpy.ops.object.delete() 
            CURRENT_COUNTER = 1
            
    

def createCube(name):
    
    global FILES
    global PATH
    global TRACK_TO_CAM
    global ORIGINAL_CLOUDS
    global USE_DUPLICATES
    
    filesize = len(FILES) -1
    randomfile = random.randint(0,filesize)
    print ("RANDOMFILE: " + str(randomfile))
    file = FILES[randomfile]
    print ("CHOOSENFILE:  " + file)
    bpy.ops.import_image.to_plane(files=[{"name":file, "name":file}], directory=CLOUDPATH)
   
 
    if (TRACK_TO_CAM == True):
        bpy.ops.object.constraint_add(type='TRACK_TO')
        bpy.context.object.constraints["Track To"].target = bpy.data.objects["Camera"]

     
 
  
    myCube_obj =  bpy.context.selected_objects[0]
    myCube_obj.name = name
    myCube_obj.data.name = name
    
    if (USE_DUPLICATES = True):
        ORIGINAL_CLOUDS.append(myCube_obj)
        
   # myCube_obj.select_set(False)
    bpy.data.collections['cloudCubes'].objects.link(myCube_obj)
    bpy.context.scene.collection.objects.unlink(myCube_obj)
    
  
  
  
def create_collection() :
#    print ("CREATING COLLECTION")
    if "cloudCubes" not in bpy.data.collections :
        create_collection = bpy.data.collections.new(name="cloudCubes")
        bpy.context.scene.collection.children.link(create_collection)
        
      
            
            

    

def move_cloudbox_in_area(name):
    
    global CLOUD_AREA_X_FROM 
    global CLOUD_AREA_X_TO 
    global CLOUD_AREA_Y_FROM
    global CLOUD_AREA_Y_TO 
    global CLOUD_AREA_Z_FROM 
    global CLOUD_AREA_Z_TO 
    move_obj = bpy.data.collections['cloudCubes'].objects[name]
    

    move_obj.location.x = random.randint(CLOUD_AREA_X_FROM, CLOUD_AREA_X_TO)
    move_obj.location.y = random.randint(CLOUD_AREA_Y_FROM, CLOUD_AREA_Y_TO)
    move_obj.location.z = random.randint(CLOUD_AREA_Z_FROM, CLOUD_AREA_Z_TO)
    


    
    
    
def scale_cloud(name):
    
    global SCALE_FACTOR_X
    global SCALE_FACTOR_Y
    global SCALE_FACTOR_Z
    scale_obj = bpy.data.collections['cloudCubes'].objects[name]
#    print("SIZE X: " + str(scale_obj.dimensions.x))
    size_x = scale_obj.dimensions.x
    size_y = scale_obj.dimensions.y
    size_z = scale_obj.dimensions.z
    scale_obj.select_set(True)
    
    bpy.ops.transform.resize(value=(SCALE_FACTOR_X,SCALE_FACTOR_Y,SCALE_FACTOR_Z))
    

    
    

    
    

    
    
 

def main():
    doof = True
    if (doof == True):
        return
    global CLOUD_AREA_X_FROM 
    global CLOUD_AREA_X_TO 
    global CLOUD_AREA_Y_FROM
    global CLOUD_AREA_Y_TO 
    global CLOUD_AREA_Z_FROM 
    global CLOUD_AREA_Z_TO 
    global CURRENT_BOX_MESH_AMOUNT

    global AMOUNT_OF_CLOUDBOXES
    
    
    
    cleanup()
    create_collection()  
    get_alphaclouds()
  
    counter = 1
    while counter < AMOUNT_OF_CLOUDBOXES:
        
        print("Creating CloudBox: " + str(counter))
        
        cloud_overall_name = "cloudMesh" + str(counter)
        
        createCube(cloud_overall_name)


        move_cloudbox_in_area(cloud_overall_name)
        scale_cloud(cloud_overall_name)

        
        counter = counter +1
        
        
        
        


#add_sun_to_cloud("cloudMesh")


 
            
    


