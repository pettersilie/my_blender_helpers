import bpy
import random
from random import uniform
import os





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
CLOUDPATH = "C:\\Users\\Mirko\\Desktop\\alphaclouds\\render"

AMOUNT_OF_CLOUDBOXES = 800


def get_alphaclouds(): 
    global FILES
    global PATH
    
    for i in os.listdir(CLOUDPATH):
        print(i)
        
        
        FILES.append(i)
            
   
    


def cleanup():
    if "cloudCubes" in bpy.data.collections :
        for ob in bpy.data.collections['cloudCubes'].objects:
            ob.hide_set(False)
            ob.hide_render = False
            ob.select_set(True)
        
            bpy.ops.object.delete() 
    

def createCube(name):
    
    global FILES
    global PATH
    
    filesize = len(FILES) -1
    randomfile = random.randint(0,filesize)
    print ("RANDOMFILE: " + str(randomfile))
    file = FILES[randomfile]
    print ("CHOOSENFILE:  " + file)
    bpy.ops.import_image.to_plane(files=[{"name":file, "name":file}], directory=CLOUDPATH)
#    bpy.ops.object.editmode_toggle()

    counter = 1
#    while counter < 60:

#      bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":1}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
#      bpy.ops.transform.rotate(value=3.14159 * 3 / 180, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
#      counter = counter +1
   


#    bpy.ops.object.editmode_toggle()
 
    bpy.ops.object.constraint_add(type='TRACK_TO')
    bpy.context.object.constraints["Track To"].target = bpy.data.objects["Camera"]

     
 
  
    myCube_obj =  bpy.context.selected_objects[0]
    myCube_obj.name = name
    myCube_obj.data.name = name
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


 
            
    


