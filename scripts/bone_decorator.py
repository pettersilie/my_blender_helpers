import bpy

from ..utils import toolbox

ROT_X = 0
ROT_Y = 0
ROT_Z = 0
ARMATURE_NAME = "bone_decorator_arm"
SCALE_FACTOR = 1
DECORATE_OBJECT = None

DECORATE_VERTECIS = []



def delete_current_bones():
    global ARMATURE_NAME
    if (ARMATURE_NAME in bpy.data.objects);
        toolbox.deselect_all(True)
        toolbox.select_object_by_name(ARMATURE_NAME,True)
        bpy.ops.object.delete()


def add_armature():
    bpy.ops.object.armature_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(SCALE_FACTOR, SCALE_FACTOR, SCALE_FACTOR))
    
    
    
