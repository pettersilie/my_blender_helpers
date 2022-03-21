import bpy

from ..utils import toolbox
import os
import numpy as np
import math
import random


SCALE_X_FROM = 1
SCALE_X_TO = 10
SCALE_Y_FROM = 1
SCALE_Y_TO = 1
SCALE_Z_FROM = 1
SCALE_Z_TO = 1

ROT_X_FROM = 0
ROT_X_TO = 90
ROT_Y_FROM = 0
ROT_Y_TO = 90
ROT_Z_FROM = 0
ROT_Z_TO = 90

AMOUNT_OF_ROCKS = 0
AMOUNT_OF_DUPLICATES = 0
DISPLACE_PERCENTAGE_FROM = 10
DISPLACE_PERCENTAGE_TO = 80
SUBDIVISIONS = 2


DISPLACEMENT_STRENGTH_FROM = 0
DISPLACEMENT_STRENGTH_TO = 1.5


DECORATE_OBJECT = None

SMOOTH = True
ROCK_TEXTURE_DIR = "C:\\Users\\mirko\\Desktop\\stuff_sternenhexen\\rock_textures"


####################
ROCK_TEXTURES = []
ORIG_ROCKS = []
CURRENT_ROCK = None
CURRENT_COUNTER = 0
DECORATE_VERTICES = []

def delete_rocks():
    global CURRENT_COUNTER
    global ORIG_ROCKS
    
    toolbox.delete_objects_from_collection("rocks")
    CURRENT_COUNTER = 0
    ORIG_ROCKS = []
    
    
def create_collection():
    
    toolbox.create_root_collection("rocks")


def create_material():
    global ROCK_TEXTURES

    print ("Creating Material")
    toolbox.deselect_all(True)
    toolbox.select_object(CURRENT_ROCK,True)
    texture_index = -1
    
    if (ROCK_TEXTURE_DIR is not None and ROCK_TEXTURE_DIR != ""):
        texture_index = random.randint(0,len(ROCK_TEXTURES)-1)
        texture = ROCK_TEXTURES[texture_index]
    else:
        texture = None

    mat_name = "rockmaterial_" + str(texture_index)
    if (mat_name in bpy.data.materials):
        CURRENT_ROCK.data.materials.append(bpy.data.materials[mat_name])
        return
    
    
    mat = bpy.data.materials.new(mat_name)
    mat.use_nodes = True
    
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    
    bsdf =  nodes['Principled BSDF']
    print ("ROCK_TEXTURE: " + str(texture))
    
    if (ROCK_TEXTURE_DIR is not None and ROCK_TEXTURE_DIR != ""):
        rock_texture_image =  bpy.data.images.load(filepath = ROCK_TEXTURE_DIR + os.sep + texture)
        
        imageTextureNode = nodes.new(type="ShaderNodeTexImage")
        imageTextureNode.image = rock_texture_image
        
        links.new(imageTextureNode.outputs[0], bsdf.inputs[0])
    
    
    CURRENT_ROCK.data.materials.append(mat)
    
    

def make_smooth():
    toolbox.deselect_all(True)
    toolbox.select_object(CURRENT_ROCK,True)
    bpy.ops.object.shade_smooth()



def read_textures():
    global ROCK_TEXTURE_DIR
    global ROCK_TEXTURES
    
    if (ROCK_TEXTURE_DIR is not None and ROCK_TEXTURE_DIR != ""):
    
        ROCK_TEXTURES = toolbox.get_files_from_directory(ROCK_TEXTURE_DIR)
    else:
        print ("Rock Texture Dir is empty or None")

def add_displacement_modifier():

    global DISPLACEMENT_STRENGTH_FROM
    global DISPLACEMENT_STRENGTH_TO

    toolbox.deselect_all(True)
    toolbox.select_object(CURRENT_ROCK,True)
    bpy.ops.object.modifier_add(type='DISPLACE')
    CURRENT_ROCK.modifiers["Displace"].vertex_group = "rock_displacement"
    
    strength = random.uniform(DISPLACEMENT_STRENGTH_FROM,DISPLACEMENT_STRENGTH_TO)
    
    bpy.context.object.modifiers["Displace"].strength = strength


def rotate_rock():
    global ROT_X_FROM
    global ROT_X_TO
    global ROT_Y_FROM
    global ROT_Y_TO
    global ROT_Z_FROM
    global ROT_Z_TO
    
    toolbox.deselect_all(True)
    toolbox.select_object(CURRENT_ROCK,True)
    
    
    rot_x = random.uniform(ROT_X_FROM,ROT_X_TO)
    rot_y = random.uniform(ROT_Y_FROM,ROT_Y_TO)
    rot_z = random.uniform(ROT_Z_FROM,ROT_Z_TO)
    bpy.ops.transform.rotate(value=toolbox.calculate_rotation(rot_x), orient_axis='X')
    bpy.ops.transform.rotate(value=toolbox.calculate_rotation(rot_y), orient_axis='Y')
    bpy.ops.transform.rotate(value=toolbox.calculate_rotation(rot_z), orient_axis='Z')
    
  
    
def scale_rock():
    global SCALE_X_FROM
    global SCALE_X_TO
    global SCALE_Y_FROM
    global SCALE_Y_TO
    global SCALE_Z_FROM
    global SCALE_Z_TO
    
    toolbox.deselect_all(True)
    toolbox.select_object(CURRENT_ROCK,True)
    
    scale_x = random.uniform(SCALE_X_FROM,SCALE_X_TO)
    scale_y = random.uniform(SCALE_Y_FROM,SCALE_Y_TO)
    scale_z = random.uniform(SCALE_Z_FROM,SCALE_Z_TO)

    

    
    bpy.ops.transform.resize(value=(scale_x,scale_y,scale_z))
    
    

def add_vertex_group():
    global CURRENT_ROCK
    global DISPLACE_PERCENTAGE_FROM
    global DISPLACE_PERCENTAGE_TO
    
    
    displace_percentage = random.randint(DISPLACE_PERCENTAGE_FROM,DISPLACE_PERCENTAGE_TO)
    print ("DisPerc: " + str(displace_percentage))
    toolbox.deselect_all(True)
    toolbox.select_object(CURRENT_ROCK,True)
    
    vertex_group_size = math.floor(len(CURRENT_ROCK.data.vertices) / 100 * displace_percentage)
    
    randnums= np.random.randint(0,len(CURRENT_ROCK.data.vertices)-1,vertex_group_size,dtype=int).tolist()
    
    
    
    #bpy.ops.object.editmode_toggle()
    #bpy.ops.mesh.select_all(action='DESELECT')
    #bpy.ops.mesh.select_random(ratio=DISPLACE_PERCENTAGE/100, seed=1)
    #bpy.ops.object.editmode_toggle()
    
    new_vertex_group = CURRENT_ROCK.vertex_groups.new(name='rock_displacement')

    
    new_vertex_group.add(randnums,100,"ADD")
    
def move_rock_to_decorate_vertex():
    global DECORATE_VERTICES
    global CURRENT_ROCK
    global DECORATE_OBJECT
    if (DECORATE_OBJECT is None):
        return
    if (len(DECORATE_VERTICES) <= 0):
        return
    
    
    toolbox.deselect_all(True)
    toolbox.select_object(CURRENT_ROCK,True)
    
    rock_half_height = CURRENT_ROCK.dimensions.z / 2
    
    random_vertex = random.randint(0,len(DECORATE_VERTICES)-1)
    
    
    vertex_coordinates = DECORATE_OBJECT.matrix_world @ DECORATE_VERTICES[random_vertex].co
    CURRENT_ROCK.location.x = vertex_coordinates.x
    CURRENT_ROCK.location.y = vertex_coordinates.y
    CURRENT_ROCK.location.z = vertex_coordinates.z
    del DECORATE_VERTICES[random_vertex]
    
def create_duplicate_rock():
    
    global ORIG_ROCKS
    global CURRENT_ROCK
    global CURRENT_COUNTER
    toolbox.deselect_all(True)
    random_rock = random.randint(0,len(ORIG_ROCKS)-1)
    rock_to_duplicate = ORIG_ROCKS[random_rock]
    
    toolbox.select_object_by_name(rock_to_duplicate.name,True)
    
    bpy.ops.object.duplicate(linked=True)
    dupli_obj = toolbox.get_object_by_prefix(rock_to_duplicate.name + ".")
    
    dup_name = "rock" + str(CURRENT_COUNTER)
    toolbox.set_object_name(dup_name,dupli_obj)
    CURRENT_ROCK = dupli_obj
    
    
    
        


def get_decorate_vertices():
    global DECORATE_VERTICES
    global DECORATE_OBJECT
    
    
    
    if (DECORATE_OBJECT is None):
        return
    
    DECORATE_VERTICES = toolbox.get_selected_vertices_from_object_as_vertex(DECORATE_OBJECT)
    print (str(DECORATE_VERTICES))


def create_rock():

    global CURRENT_ROCK
    global CURRENT_COUNTER
    global SUBDIVISIONS
    global ORIG_ROCKS
    global AMOUNT_OF_DUPLICATES
    
    toolbox.deselect_all(True)
    
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=SUBDIVISIONS,radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    
    
    #bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

    
    
    CURRENT_ROCK = bpy.context.selected_objects[0]
    toolbox.link_object_to_collection("rocks",bpy.context.selected_objects[0])
    name = "rock" + str(CURRENT_COUNTER)
    toolbox.set_object_name(name,CURRENT_ROCK)
    
    if (AMOUNT_OF_DUPLICATES > 0):
        ORIG_ROCKS.append(CURRENT_ROCK)
    



def main():
    toolbox.deselect_all(True)
    delete_rocks()
    read_textures()
    create_collection()
    create_rock()
    add_vertex_group()
    add_displacement_modifier()
    create_material()
    make_smooth()
    scale_rock()
    rotate_rock()
    get_decorate_vertices()
    move_rock_to_decorate_vertex()
    
    
    

