import bpy
import os
from ..utils import toolbox


SELECTED_OBJECT = None
SELECTED_OBJECT_LOCATION = None
SELECTED_OBJECT_FOUND = 0
SELECTED_OBJECT_DIMENSION = None
SELECTED_OBJECT_COLLECTION = None
SELECTED_OBJECT_COLLECTION_NAME = None
FACE_BLEND_FILE = None
SCALE_PERCENTAGE = 10



def delete_current_face():
    collection = bpy.data.collections.get('2DFace')
    if (collection is None):
        return
 
    for obj in collection.objects:
        bpy.data.objects.remove(obj, do_unlink=True)
    
    bpy.data.collections.remove(collection)



def import_face():

  global SELECTED_OBJECT_FOUND
  global SELECTED_OBJECT 
  global SELECTED_OBJECT_COLLECTION
  global SELECTED_OBJECT_COLLECTION_NAME
  global FACE_BLEND_FILE
  if SELECTED_OBJECT_FOUND == 0:
    return


  toolbox.deselect_all(True)
  
  
  

  
  section = "\\Collection\\"
  object = "2DFace"


  filepath  = FACE_BLEND_FILE + section + object
  directory = FACE_BLEND_FILE + section
  filename  = object

    
  bpy.ops.wm.append(
      filepath=filepath, 
      filename=filename,
      directory=directory)
      

    
  toolbox.deselect_all(True)
  faceCollection = bpy.data.collections['2DFace']
  
  
  print ("DOOOOOF " + str(SELECTED_OBJECT_COLLECTION_NAME))
 
  
  active_collection = bpy.context.view_layer.active_layer_collection.collection

  targetCollection = SELECTED_OBJECT_COLLECTION
  print ("DOOOOOF " + str(targetCollection.name))
  

  #bpy.context.scene.collection.children.unlink(faceCollection)
    
  active_collection.children.unlink(faceCollection)  
  targetCollection.children.link(faceCollection)
  
  
  
  
 # targetCollection.children.link(faceCollection)
 # bpy.context.scene.collection.children.unlink(faceCollection)
  

  
  
  
  for obj in bpy.data.collections['2DFace'].all_objects:
    obj.select_set(True)
    
    
    
def get_selected_object():
    

    global SELECTED_OBJECT
    global SELECTED_OBJECT_LOCATION 
    global SELECTED_OBJECT_FOUND 
    global SELECTED_OBJECT_DIMENSION
    global SELECTED_OBJECT_COLLECTION
    global SELECTED_OBJECT_COLLECTION_NAME

    print ("OBJECT SELECTED")
    
    print (SELECTED_OBJECT.name)
    print (str(SELECTED_OBJECT.dimensions))
    bpy.context.scene.cursor.location = SELECTED_OBJECT.location
    SELECTED_OBJECT_FOUND = 1
    SELECTED_OBJECT_LOCATION = SELECTED_OBJECT.matrix_world.translation 
    SELECTED_OBJECT_DIMENSION = SELECTED_OBJECT.dimensions
    print (str(SELECTED_OBJECT.users_collection[0].name))
    SELECTED_OBJECT_COLLECTION = SELECTED_OBJECT.users_collection[0]
    SELECTED_OBJECT_COLLECTION_NAME = SELECTED_OBJECT.users_collection[0].name
    
    
          
      




def move_2Dface():
    global SELECTED_OBJECT_DIMENSION
    global SELECTED_OBJECT_FOUND
    global SELECTED_OBJECT
    global SELECTED_OBJECT_LOCATION
    global SCALE_PERCENTAGE
    if SELECTED_OBJECT_FOUND == 0:
      print("NO selected Object found")
      return
    
      
    toolbox.deselect_all(True)
  #  for obj in bpy.data.collections['2Dface'].all_objects:
    #  obj.select_set(True)
    print("SELECTED_OBJECT_LOCATION " + str(SELECTED_OBJECT_LOCATION))  


    armobj = find_face_armature()
    if armobj == None:
        print("Face Armature not found")
        return
    
    #armobj = bpy.data.objects["Armature"]
    armobj.select_set(True)
   
    
    #bpy.ops.object.select_grouped(type='CHILDREN_RECURSIVE') myObj.select = True    
        
   # for obj in bpy.context.selected_objects:
    #    print (obj.name)    
    
    dim_y = SELECTED_OBJECT_DIMENSION.y
    print ("Dimension selected Object Y:" + str(dim_y))

    armobj.location = SELECTED_OBJECT_LOCATION
      
    
    
   
    armobj.location.y = armobj.location.y - ((dim_y / 2) + (dim_y / 100 * SCALE_PERCENTAGE))
  #  armobj.location.x = SELECTED_OBJECT_LOCATION.x
    
    
    
    
def do_resizinig():
    
    global SELECTED_OBJECT_DIMENSION
    global SELECTED_OBJECT_FOUND
    global SELECTED_OBJECT
    if SELECTED_OBJECT_FOUND == 0:
      return
  
    scale_up = False
    scale_down = False
    scale_value = 0
    scale_relation = 0
    
    print ("RESIZING")
    deselect_all()
    armobj = find_face_armature()
    
    armobj.select_set(True)
    select_dim_x = SELECTED_OBJECT_DIMENSION.x
    select_dim_z = SELECTED_OBJECT_DIMENSION.z
    

    arm_dim_x = armobj.dimensions.x
    arm_dim_z = armobj.dimensions.z
    
    select_area = select_dim_x * select_dim_z
    arm_area = arm_dim_x * arm_dim_z
    

    print(str(select_area))
    print(str(arm_area))
    
    current_relation = arm_area * 100 / select_area
    
    print ("Percent:")
    print (str(current_relation)) 
    #percentage = 19.30
    percentage = 30
    
    if (current_relation > percentage):
        scale_down = True
        print ("We wil scale down....")
    elif (current_relation < percentage):
        scale_up = True
        print ("We will scale up....")
    else:
        print ("Nothing to scale here...leaving")
        return
        
    print ("calculating scale_value....")
    if scale_up:
        scale_value = percentage - current_relation
    elif scale_down:
        scale_value = current_relation - percentage
    else:
        print ("Nothing to scale... return")
        return
    
    if scale_up:
        scale_relation = 1 + (scale_value / 100)
    elif scale_down:
        scale_relation = 1 - (scale_value / 100)
    else:
        print ("Nothing to do with scale_relation ... return")
        return
    
    deselect_all()
    armobj.select_set(True)
    bpy.context.view_layer.objects.active = armobj
    
    bpy.ops.transform.resize(value=(scale_relation, scale_relation, scale_relation), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.context.view_layer.objects.active = None
  
        
    
    
    

    
    
    
         


def do_shrinkwrapping():
    
    global SELECTED_OBJECT_DIMENSION
    global SELECTED_OBJECT_FOUND
    global SELECTED_OBJECT
    if SELECTED_OBJECT_FOUND == 0:
      return
    
    eye_L = get_object_from_face("eye_object.L")
    eye_R = get_object_from_face("eye_object.R")
    eye_L_outline = get_object_from_face("eye_object_outline.L")
    eye_R_outline = get_object_from_face("eye_object_outline.R")
    mouth = get_object_from_face("mouth_object")
    mouth_outline = get_object_from_face("mouth_object_outline")
    brow_L = get_object_from_face("brow_object.L")
    brow_R = get_object_from_face("brow_object.R")
        
    
    
    eye_L_outline.modifiers.new(name="Shrinkwrap",type='SHRINKWRAP')
    eye_L_outline.modifiers["Shrinkwrap"].wrap_method = 'PROJECT'
    eye_L_outline.modifiers["Shrinkwrap"].wrap_mode = 'OUTSIDE_SURFACE'
    eye_L_outline.modifiers["Shrinkwrap"].use_positive_direction = False
    eye_L_outline.modifiers["Shrinkwrap"].use_negative_direction = True
    eye_L_outline.modifiers["Shrinkwrap"].target = SELECTED_OBJECT
    eye_L_outline.modifiers["Shrinkwrap"].offset = 0.04
    deselect_all()
    eye_L_outline.select_set(True)
    bpy.context.view_layer.objects.active = eye_L_outline
    #bpy.ops.object.modifier_move_to_index(modifier="Shrinkwrap", index=0)
    bpy.context.view_layer.objects.active = None
    deselect_all()   
    
    eye_R_outline.modifiers.new(name="Shrinkwrap",type='SHRINKWRAP')
    eye_R_outline.modifiers["Shrinkwrap"].wrap_method = 'PROJECT'
    eye_R_outline.modifiers["Shrinkwrap"].wrap_mode = 'OUTSIDE_SURFACE'
    eye_R_outline.modifiers["Shrinkwrap"].use_positive_direction = False
    eye_R_outline.modifiers["Shrinkwrap"].use_negative_direction = True
    eye_R_outline.modifiers["Shrinkwrap"].target = SELECTED_OBJECT
    eye_R_outline.modifiers["Shrinkwrap"].offset = 0.04
    deselect_all()
    eye_R_outline.select_set(True)
    bpy.context.view_layer.objects.active = eye_R_outline
    #bpy.ops.object.modifier_move_to_index(modifier="Shrinkwrap", index=0)
    bpy.context.view_layer.objects.active = None
    deselect_all() 
    
    
    
    
    
    eye_L.modifiers.new(name="Shrinkwrap",type='SHRINKWRAP')
    eye_L.modifiers["Shrinkwrap"].wrap_method = 'PROJECT'
    eye_L.modifiers["Shrinkwrap"].wrap_mode = 'OUTSIDE_SURFACE'
    eye_L.modifiers["Shrinkwrap"].use_positive_direction = False
    eye_L.modifiers["Shrinkwrap"].use_negative_direction = True
    eye_L.modifiers["Shrinkwrap"].target = SELECTED_OBJECT
    eye_L.modifiers["Shrinkwrap"].offset = 0.06
    deselect_all()
    eye_L.select_set(True)
    bpy.context.view_layer.objects.active = eye_L
    #bpy.ops.object.modifier_move_to_index(modifier="Shrinkwrap", index=0)
    bpy.context.view_layer.objects.active = None
    deselect_all()     
    
    
    brow_L.modifiers.new(name="Shrinkwrap",type='SHRINKWRAP')
    brow_L.modifiers["Shrinkwrap"].wrap_method = 'PROJECT'
    brow_L.modifiers["Shrinkwrap"].wrap_mode = 'OUTSIDE_SURFACE'
    brow_L.modifiers["Shrinkwrap"].use_positive_direction = False
    brow_L.modifiers["Shrinkwrap"].use_negative_direction = True
    brow_L.modifiers["Shrinkwrap"].target = SELECTED_OBJECT
    brow_L.modifiers["Shrinkwrap"].offset = 0.05
    deselect_all()
    brow_L.select_set(True)
    bpy.context.view_layer.objects.active = brow_L
    #bpy.ops.object.modifier_move_to_index(modifier="Shrinkwrap", index=0)
    bpy.context.view_layer.objects.active = None
    deselect_all()  
    
    
    eye_R.modifiers.new(name="Shrinkwrap",type='SHRINKWRAP')
    eye_R.modifiers["Shrinkwrap"].wrap_method = 'PROJECT'
    eye_R.modifiers["Shrinkwrap"].wrap_mode = 'OUTSIDE_SURFACE'
    eye_R.modifiers["Shrinkwrap"].use_positive_direction = False
    eye_R.modifiers["Shrinkwrap"].use_negative_direction = True
    eye_R.modifiers["Shrinkwrap"].target = SELECTED_OBJECT
    eye_R.modifiers["Shrinkwrap"].offset = 0.06
    deselect_all()
    eye_R.select_set(True)
    bpy.context.view_layer.objects.active = eye_R
    #bpy.ops.object.modifier_move_to_index(modifier="Shrinkwrap", index=0)
    bpy.context.view_layer.objects.active = None
    deselect_all()    
    
    brow_R.modifiers.new(name="Shrinkwrap",type='SHRINKWRAP')
    brow_R.modifiers["Shrinkwrap"].wrap_method = 'PROJECT'
    brow_R.modifiers["Shrinkwrap"].wrap_mode = 'OUTSIDE_SURFACE'
    brow_R.modifiers["Shrinkwrap"].use_positive_direction = False
    brow_R.modifiers["Shrinkwrap"].use_negative_direction = True
    brow_R.modifiers["Shrinkwrap"].target = SELECTED_OBJECT
    brow_R.modifiers["Shrinkwrap"].offset = 0.05
    deselect_all()
    brow_R.select_set(True)
    bpy.context.view_layer.objects.active = brow_R
    #bpy.ops.object.modifier_move_to_index(modifier="Shrinkwrap", index=0)
    bpy.context.view_layer.objects.active = None
    deselect_all()
    
    mouth.modifiers.new(name="Shrinkwrap",type='SHRINKWRAP')
    mouth.modifiers["Shrinkwrap"].wrap_method = 'PROJECT'
    mouth.modifiers["Shrinkwrap"].wrap_mode = 'OUTSIDE_SURFACE'
    mouth.modifiers["Shrinkwrap"].use_positive_direction = False
    mouth.modifiers["Shrinkwrap"].use_negative_direction = True
    mouth.modifiers["Shrinkwrap"].target = SELECTED_OBJECT
    mouth.modifiers["Shrinkwrap"].offset = 0.05
    toolbox.deselect_all(True)
    mouth.select_set(True)
    bpy.context.view_layer.objects.active = mouth
    #bpy.ops.object.modifier_move_to_index(modifier="Shrinkwrap", index=0)
    bpy.context.view_layer.objects.active = None
    toolbox.deselect_all(True)

    mouth_outline.modifiers.new(name="Shrinkwrap",type='SHRINKWRAP')
    mouth_outline.modifiers["Shrinkwrap"].wrap_method = 'PROJECT'
    mouth_outline.modifiers["Shrinkwrap"].wrap_mode = 'OUTSIDE_SURFACE'
    mouth_outline.modifiers["Shrinkwrap"].use_positive_direction = False
    mouth_outline.modifiers["Shrinkwrap"].use_negative_direction = True
    mouth_outline.modifiers["Shrinkwrap"].target = SELECTED_OBJECT
    mouth_outline.modifiers["Shrinkwrap"].offset = 0.03
    toolbox.deselect_all(True)
    mouth_outline.select_set(True)
    bpy.context.view_layer.objects.active = mouth_outline
    #bpy.ops.object.modifier_move_to_index(modifier="Shrinkwrap", index=0)
    bpy.context.view_layer.objects.active = None
    toolbox.deselect_all(True)



def parent_to_headbone():
    global SELECTED_OBJECT_DIMENSION
    global SELECTED_OBJECT_FOUND
    global SELECTED_OBJECT
    
    head_armature = SELECTED_OBJECT.parent
    if (head_armature != None):
        print ("HEAD_ARMATURE FOUND!")
    else:
        print ("NO HEAD_ARMATURE_FOUND")
        return
    
    toolbox.deselect_all(True)
    face_armature = get_object_from_face("Armature")
    if (face_armature != None):
        print("Face Armature found....")
    else:
        print ("No face armature found")
        return
    
    face_armature.select_set(True)
    bpy.context.view_layer.objects.active = face_armature
    bpy.ops.object.posemode_toggle()
    master =  face_armature.pose.bones.get("FACE_Masterbone")
   
  
    crc = master.constraints.new('CHILD_OF')
   # bpy.ops.pose.constraint_add(type='CHILD_OF')
    print (head_armature.name)
    crc.target = head_armature
    crc.subtarget = "HEADBONE"
    
    
    #crc.childof_clear_inverse(constraint="Child Of", owner='BONE')

    #crc.childof_set_inverse(constraint="Child Of", owner='BONE')
    bpy.ops.object.posemode_toggle()



    

    
    



def main():
      #clear_all()
      #import_head()
      get_selected_object()     
      import_face() 
      move_2Dface()
      do_resizinig()
      
      parent_to_headbone()
      



      do_shrinkwrapping()
      
      #finish()
      #deselect_all()

def find_face_armature():
    #print("Finding face armature.....")
    for obj in bpy.data.collections['2DFace'].all_objects:
      #print(obj.name)
      if obj.name.startswith('Armature'):
          #print ("Found obj.. returning " + obj.name)
          return obj
    return None  
        
def get_object_from_face(name):
    for obj in bpy.data.collections['2DFace'].all_objects:
      if obj.name.startswith(name):
          return obj
    return None 
            


def deselect_all():
    #bpy.context.view_layer.objects.active = None
    for obj in bpy.context.selected_objects:
      obj.select_set(False) 
      
      
def finish():
    global SELECTED_OBJECT
    col = bpy.data.collections.get("2DFace")
    if col:
      col.name = SELECTED_OBJECT.name + "_2DFace.ready" 
      

