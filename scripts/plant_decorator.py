import bpy
import random
import os
from random import uniform
from math import pi
import time
import numpy as np

SRC_DIR = "C:\\Users\\mirko\\Desktop\\plant_generator\\render\\"

FILES = []
BEND_ANGLE = 180
PLANT_SUBDIVIDE_CUTS = 50








def delete_all():
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False, confirm=False)
 
    for collection in bpy.data.collections:
        bpy.data.collections.remove(collection)
        
    for material in bpy.data.materials:

        bpy.data.materials.remove(material)
        
    for texture in bpy.data.textures:

        bpy.data.textures.remove(texture)
        
    for image in bpy.data.images:

        bpy.data.images.remove(image)
        
    for curve in bpy.data.curves:

        bpy.data.curves.remove(curve)
        
    for action in bpy.data.actions:

        bpy.data.actions.remove(action)
        
    for light in bpy.data.lights:

        bpy.data.lights.remove(light)
        
    for mesh in bpy.data.meshes:

        bpy.data.meshes.remove(mesh)


def test_calc():
    
    global PLANT_SUBDIVIDE_CUTS
    global BEND_ANGLE
    
   # bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    bpy.ops.import_image.to_plane(files=[{"name":"plant5.png", "name":"plant5.png"}], directory="C:\\Users\\mirko\\Desktop\\plant_generator\\render\\", align_axis='Z+', relative=False)

    bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.subdivide(number_cuts=PLANT_SUBDIVIDE_CUTS)
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

    bpy.ops.object.modifier_add(type='SIMPLE_DEFORM')
    bpy.context.object.modifiers["SimpleDeform"].deform_method = 'BEND'
    bpy.context.object.modifiers["SimpleDeform"].deform_axis = 'Z'
    
    bpy.context.object.modifiers["SimpleDeform"].angle = (pi * BEND_ANGLE / 180)
    
    bpy.ops.object.modifier_apply(modifier="SimpleDeform")
    tex = bpy.data.textures.new("SomeName", 'IMAGE')
    
   

    


#    bpy.ops.object.modifier_add(type='DISPLACE')
    



    
    

    
    
    
    

def get_alpha_plants():
   
    global SRC_DIR
    global FILES

    
    for i in os.listdir(SRC_DIR):
        print(i)
        
        
        FILES.append(i)

    
    
         




def main():
    
    

    
    
    delete_all()
   
    get_alpha_plants()
    test_calc()
  
   
    
    
