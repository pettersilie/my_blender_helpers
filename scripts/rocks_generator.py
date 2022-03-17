import bpy

from ..utils import toolbox


SCALE_X_FROM = 0
SCALE_X_TO = 0
SCALE_Y_FROM = 0
SCALE_Y_TO = 0
SCALE_Z_FROM = 0
SCALE_Z_TO = 0

ROT_X_FROM = 0
ROT_X_TO = 0
ROT_Y_FROM = 0
ROT_Y_TO = 0
ROT_Z_FROM = 0
ROT_Z_TO = 0

AMOUNT_OF_ROCKS = 0
AMOUNT_OF_DUPLICATES = 0

DECORATE_OBJECT = None

SMOOTH = True
ROCK_TEXTURE_DIR = ""





















def main():
    toolbox.create_root_collection("rocks")
    toolbox.delete_objects_from_collection("rocks")
    
    

