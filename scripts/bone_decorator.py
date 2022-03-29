import bpy

from ..utils import toolbox

ROT_X = 0
ROT_Y = 0
ROT_Z = 0
ARMATURE_NAME = "bone_decorator_arm"
SCALE_FACTOR = 1
DECORATE_OBJECT = None

ORIG_CURSOR_X = 0
ORIG_CURSOR_Y = 0
ORIG_CURSOR_Z = 0


DECORATE_VERTICES = []
CURRENT_COUNTER = 0



def delete_current_bones():
    global ARMATURE_NAME
    
    global CURRENT_COUNTER
    
    arm = toolbox.get_object_by_name(ARMATURE_NAME)
    
    if (arm is not None):
        toolbox.deselect_all(True)
        toolbox.select_object_by_name(ARMATURE_NAME,True)
        bpy.ops.object.delete()
    CURRENT_COUNTER = 0

def add_armature():
    global ARMATURE_NAME
    global SCALE_FACTOR
    global CURRENT_COUNTER
    global ROT_X 
    global ROT_Y
    global ROT_Z 
    bpy.ops.object.armature_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(SCALE_FACTOR, SCALE_FACTOR, SCALE_FACTOR))

    arm = bpy.context.selected_objects[0]
    toolbox.set_object_name(ARMATURE_NAME, arm)
    arm.location = bpy.context.scene.cursor.location
    bpy.ops.object.editmode_toggle()
    
    first_bone = arm.data.bones["Bone"]
    first_bone.select = True
    first_bone.name = "dec_bone." + str(CURRENT_COUNTER)
    print (str(first_bone))
    
    bpy.ops.transform.translate(value=(0, 0, SCALE_FACTOR), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.ops.object.editmode_toggle()
    
    bpy.ops.transform.rotate(value=toolbox.calculate_rotation(ROT_X), orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        
    bpy.ops.transform.rotate(value=toolbox.calculate_rotation(ROT_Y), orient_axis='Y', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        
    bpy.ops.transform.rotate(value=toolbox.calculate_rotation(ROT_Z), orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
 

    
    
    
def get_decorate_vertices():
    global DECORATE_OBJECT
    global DECORATE_VERTICES
    
    if (DECORATE_OBJECT is None):
        return
    
    DECORATE_VERTICES = toolbox.get_selected_vertices_from_object_as_vertex(DECORATE_OBJECT)  


def set_cursor_to_vertex(vertex):

    global DECORATE_OBJECT
    global DECORATE_VERTICES
    
    coord = DECORATE_OBJECT.matrix_world @ vertex.co
    bpy.context.scene.cursor.location.x = coord.x
    bpy.context.scene.cursor.location.y = coord.y
    bpy.context.scene.cursor.location.z = coord.z
    

def add_bone(vertex):
    global ROT_X 
    global ROT_Y
    global ROT_Z 
    global ARMATURE_NAME
    global CURRENT_COUNTER
    
    toolbox.deselect_all(True)
    
    arm = toolbox.get_object_by_name(ARMATURE_NAME)
    set_cursor_to_vertex(vertex)
    
    if (arm is None):
        add_armature()
    else:
    
        toolbox.deselect_all(True)
        toolbox.select_object_by_name(ARMATURE_NAME,True)
        bpy.ops.object.editmode_toggle()
        bpy.ops.armature.bone_primitive_add()
        
        
        bpy.ops.transform.translate(value=(0, 0, SCALE_FACTOR), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        
        bpy.ops.transform.rotate(value=toolbox.calculate_rotation(ROT_X), orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        
        bpy.ops.transform.rotate(value=toolbox.calculate_rotation(ROT_Y), orient_axis='Y', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        
        bpy.ops.transform.rotate(value=toolbox.calculate_rotation(ROT_Z), orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
      

        
        
        
        
        bpy.ops.object.editmode_toggle()
        next_bone = bpy.data.objects[ARMATURE_NAME].data.bones["Bone"]
                    
        
        next_bone.name = "dec_bone." + str(CURRENT_COUNTER)

        return
        
        



def rotate_bones():
    global ROT_X 
    global ROT_Y
    global ROT_Z 
    
    



def save_cursor_location():

    global ORIG_CURSOR_X
    global ORIG_CURSOR_Y
    global ORIG_CURSOR_Z
 
    
    ORIG_CURSOR_X = bpy.context.scene.cursor.location.x
    ORIG_CURSOR_Y = bpy.context.scene.cursor.location.y
    ORIG_CURSOR_Z = bpy.context.scene.cursor.location.z
    
    
def restore_cursor_location():

    global ORIG_CURSOR_X
    global ORIG_CURSOR_Y
    global ORIG_CURSOR_Z
 
    
    bpy.context.scene.cursor.location.x = ORIG_CURSOR_X
    bpy.context.scene.cursor.location.y = ORIG_CURSOR_Y
    bpy.context.scene.cursor.location.z = ORIG_CURSOR_Z