import bpy
import random
import os
from random import uniform
from math import pi
import time
import numpy as np
from ..utils import toolbox

OUTPUT = None
LEAVES_DIR = None


TREE_SEED_MIN = 10
TREE_SEED_MAX = 70
LEAVES_MIN = 10
LEAVES_MAX = 150
LEVELS_MIN = 0
LEVELS_MAX = 1000

TRUNK_HEIGHT_FROM = .5
TRUNK_HEIGHT_TO = .5

SCALE_FROM = 1
SCALE_TO = 2

RES_X = 1280
RES_Y = 1280

IMAGES_TO_PRODUCE = 1

LEAVES_FILES = []



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

def setup():
    global RES_X
    global RES_Y
    
    bpy.context.scene.render.film_transparent = True
    bpy.context.scene.render.resolution_x = RES_X
    bpy.context.scene.render.resolution_y = RES_Y
    


    bpy.context.scene.render.resolution_percentage = 300

    if "setup" not in bpy.data.collections :
        create_collection = bpy.data.collections.new(name="setup")
        bpy.context.scene.collection.children.link(create_collection)
        bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0, -8.11643, 2.37697), rotation=(pi * 90 / 180, 0, 0), scale=(1, 1, 1))
        myCam =  bpy.context.selected_objects[0]
        bpy.context.scene.camera = myCam
       

        bpy.data.collections['setup'].objects.link(myCam)
        bpy.context.scene.collection.objects.unlink(myCam)
        
        if "tree" not in bpy.data.collections :
            create_collection = bpy.data.collections.new(name="tree")
            bpy.context.scene.collection.children.link(create_collection)
        
        
        

        bpy.ops.object.light_add(type='SUN', radius=1, align='WORLD', location=(0, -8.11643, 2.37697), scale=(1, 1, 1))
        bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        sun =  bpy.context.selected_objects[0]
        bpy.data.collections['setup'].objects.link(sun)
        bpy.context.scene.collection.objects.unlink(sun)



def create_leaves_material():
    
    global LEAVES_DIR
    global LEAVES_FILES
    
    
    leaves_obj = bpy.data.collections['tree'].objects["leaves"]
    leaves_obj.parent = None
    leaves_obj.select_set(True)
 
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = leaves_obj
    bpy.ops.material.new()
    material = bpy.data.materials['Material']
    material.use_nodes = True
    material.name = "leaves_material"
    
    material.blend_method = 'CLIP'
    material.shadow_method = 'CLIP'


    
    leaves_obj.data.materials.append(material)
    
    material_nodes = material.node_tree.nodes
    material_links = material.node_tree.links
    bsdf =  material_nodes['Principled BSDF']
    
    
    filesize = len(LEAVES_FILES) -1
    
    print ("Filesize: " + str(filesize))
    randomfile = np.random.randint(low=0,high=filesize,size=1)
    print ("RANDOMFILE: " + str(randomfile))
    
    file = LEAVES_FILES[randomfile[0]]
    
    print ("CHOOSEN FILE: " + file)
    
    
    leaves_image =  bpy.data.images.load(filepath = LEAVES_DIR + "\\" + file)
    
    
    imageTextureNode = material_nodes.new(type="ShaderNodeTexImage")
    
    imageTextureNode.image = leaves_image
    
    material_links.new(imageTextureNode.outputs[0], bsdf.inputs[0])
    
    material_links.new(imageTextureNode.outputs[1], bsdf.inputs[21])
    

def create_ivy_material():
    
    ivy_obj = bpy.data.collections['tree'].objects["tree"]
  
    ivy_obj.select_set(True)
 
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = ivy_obj
    bpy.ops.material.new()
    material = bpy.data.materials['Material']
    material.use_nodes = True
    material.name = "ivy_material"
    ivy_obj.data.materials.append(material)
    
    material_nodes = material.node_tree.nodes
    material_links = material.node_tree.links
    
    bsdf =  material_nodes['Principled BSDF']
    
    bsdf.inputs[0].default_value = (0.180297, 0.0574422, 0.00762058, 1)

    
    
    
    
    
    
    
    
    

def get_alpha_plants():
   
    global LEAVES_DIR
    global LEAVES_FILES

    
    for i in os.listdir(LEAVES_DIR):
        print(i)
        
        
        LEAVES_FILES.append(i)

    
    
         

def create_tree():
    
    global TREE_SEED_MIN
    global TREE_SEED_MAX
    global LEAVES_MIN
    global LEAVES_MAX
    global LEVELS_MIN
    global LEVELS_MAX
    global TRUNK_HEIGHT_FROM
    global TRUNK_HEIGHT_TO

    global SCALE_FROM
    global SCALE_TO
    
#    rect
    
    tree_seed = random.randint(TREE_SEED_MIN,TREE_SEED_MAX)    
    leaves = random.randint(LEAVES_MIN,LEAVES_MAX)
    levels = random.randint(LEVELS_MIN,LEVELS_MAX)
    
    trunk_height = random.uniform(TRUNK_HEIGHT_FROM,TRUNK_HEIGHT_FROM)
    scale = random.uniform(SCALE_FROM,SCALE_TO)
    
    bpy.ops.curve.tree_add(do_update=True, 
                           bevel=True, 
                           prune=False, 
                           showLeaves=True, 
                           useArm=False, 
                           seed=tree_seed, 
                           handleType='0', 
                           levels=levels, 
                           length=(0.8, 0.6, 0.5, 0.1), 
                           lengthV=(0, 0.1, 0, 0), 
                           taperCrown=0.5, 
                           branches=(0, 55, 10, 1), 
                           curveRes=(8, 5, 3, 1), 
                           curve=(0, -15, 0, 0), 
                           curveV=(20, 50, 75, 0), 
                           curveBack=(0, 0, 0, 0), 
                           baseSplits=10, 
                           segSplits=(0.1, 0.5, 0.2, 0), 
                           splitByLen=True, 
                           rMode='rotate', 
                           splitAngle=(18, 18, 22, 0), 
                           splitAngleV=(5, 5, 5, 0), 
                           scale=scale, 
                           scaleV=2, 
                           attractUp=(3.5, -1.89984, 0, 0), 
                           attractOut=(0, 0.8, 0, 0), 
                           shape='7', 
                           shapeS='10', 
                           customShape=(0.5, 1, 0.3, 0.5), 
                           branchDist=1.5, 
                           nrings=0, 
                           baseSize=trunk_height, 
                           baseSize_s=0.16, 
                           splitHeight=0.2, 
                           splitBias=0.55, 
                           ratio=0.015, 
                           minRadius=0.0015, 
                           closeTip=False, 
                           rootFlare=1, 
                           autoTaper=True, 
                           taper=(1, 1, 1, 1), 
                           radiusTweak=(1, 1, 1, 1), 
                           ratioPower=1.2, 
                           downAngle=(0, 26.21, 52.56, 30), 
                           downAngleV=(0, 10, 10, 10), 
                           useOldDownAngle=True, 
                           useParentAngle=True, 
                           rotate=(99.5, 137.5, 137.5, 137.5), 
                           rotateV=(15, 0, 0, 0), 
                           scale0=1, 
                           scaleV0=0.1, 
                           pruneWidth=0.34, 
                           pruneBase=0.12, 
                           pruneWidthPeak=0.5, 
                           prunePowerHigh=0.5, 
                           prunePowerLow=0.001, 
                           pruneRatio=0.75, 
                           leaves=leaves, 
                           leafDownAngle=30, 
                           leafDownAngleV=-10, 
                           leafRotate=137.5, 
                           leafRotateV=15, 
                           leafScale=0.4, 
                           leafScaleX=0.2, 
                           leafScaleT=0.1, 
                           leafScaleV=0.15, 
                           leafShape='rect', 
                           bend=0, 
                           leafangle=-12, 
                           horzLeaves=True, 
                           leafDist='6', 
                           bevelRes=1, 
                           resU=4, 
                           armAnim=False, 
                           previewArm=False, 
                           leafAnim=False, 
                           frameRate=1, 
                           loopFrames=1, 
                           wind=1, 
                           gust=1, 
                           gustF=0.075, 
                           af1=1, 
                           af2=1, 
                           af3=4, 
                           makeMesh=False, 
                           armLevels=2, 
                           boneStep=(1, 1, 1, 1))
    
    


 
   
    bpy.data.objects["tree"].select_set(True)
    
    tree = bpy.context.selected_objects[0]
    bpy.data.collections['tree'].objects.link(tree)
    bpy.context.scene.collection.objects.unlink(tree)
    
    bpy.data.objects["tree"].select_set(False)
    bpy.data.objects["leaves"].select_set(True)
    
    leaves = bpy.context.selected_objects[0]
    bpy.data.collections['tree'].objects.link(leaves)
    bpy.context.scene.collection.objects.unlink(leaves)
    bpy.data.objects["leaves"].select_set(False)


def main():
    
    global IMAGES_TO_PRODUCE
    
    
    counter = 1
    while counter < IMAGES_TO_PRODUCE:
    
    
        delete_all()
        setup()
        get_alpha_plants()
        create_tree()
        create_leaves_material()
        create_ivy_material()
  #      render(counter)
        counter = counter + 1
    
    
    
def render(moves):    
    global OUTPUT
    
    toolbox.select_object_by_name("tree",False)
    toolbox.select_object_by_name("leaves",False)
    bpy.ops.view3d.camera_to_view_selected()

 
    bpy.context.scene.frame_set(moves)
    bpy.data.scenes["Scene"].render.filepath = OUTPUT + "plant%d.png" % moves
    bpy.ops.render.render(write_still=True) 
    
    
