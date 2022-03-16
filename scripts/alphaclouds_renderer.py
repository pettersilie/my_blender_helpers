import bpy
import random
from random import uniform
from math import pi
from ..utils import toolbox


OUTPUT = "C:\\Users\\Mirko\\Desktop\\alphaclouds\\render\\"

CAMERA_DISTANCE_FROM = -40
CAMERA_DISTANCE_TO = -30

METABALL_AREA_X_FROM = -10
METABALL_AREA_X_TO = 10

METABALL_AREA_Z_FROM = -3
METABALL_AREA_Z_TO = 3

METABALL_AREA_Y_FROM = -0.2
METABALL_AREA_Y_TO = 0.5

METABALL_SCALE_FROM = 0.3
METABALL_SCALE_TO = 1.5
METABALLS_AMOUNT_FROM = 30
METABALLS_AMOUNT_TO = 70

SUN_POWER_FROM = 10
SUN_POWER_TO = 30

RES_X = 0
RES_Y = 0

AMOUNT_OF_RENDERED_CLOUDS = 300


#do not set the variables below

METABALL_SCALE = 0
CAMERA_DISTANCE = 0
METABALLS_AMOUNT = 0

    
def printit():
    global CAMERA_DISTANCE_FROM
    global CAMERA_DISTANCE_TO    
    global OUTPUT
    global CAMERA_DISTANCE_FROM
    global CAMERA_DISTANCE_TO
    global METABALL_AREA_X_FROM
    global METABALL_AREA_X_TO
    global METABALL_AREA_Z_FROM
    global METABALL_AREA_Z_TO
    global METABALL_AREA_Y_FROM
    global METABALL_AREA_Y_TO
    global METABALL_SCALE_FROM
    global METABALL_SCALE_TO
    global METABALLS_AMOUNT_FROM 
    global METABALLS_AMOUNT_TO
    global SUN_POWER_FROM
    global SUN_POWER_TO
    global AMOUNT_OF_RENDERED_CLOUDS

    print ("*************************************************")
    print ("*************************************************")
    print(str(CAMERA_DISTANCE_FROM))
    print(str(CAMERA_DISTANCE_TO))    
    print(str(OUTPUT))
    print(str(CAMERA_DISTANCE_FROM))
    print(str(CAMERA_DISTANCE_TO))
    print(str(METABALL_AREA_X_FROM))
    print(str(METABALL_AREA_X_TO))
    print(str(METABALL_AREA_Z_FROM))
    print(str(METABALL_AREA_Z_TO))
    print(str(METABALL_AREA_Y_FROM))
    print(str(METABALL_AREA_Y_TO))
    print(str(METABALL_SCALE_FROM))
    print(str(METABALL_SCALE_TO))
    print(str(METABALLS_AMOUNT_FROM)) 
    print(str(METABALLS_AMOUNT_TO))
    print(str(SUN_POWER_FROM))
    print(str(SUN_POWER_TO))
    print(str(AMOUNT_OF_RENDERED_CLOUDS))




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
    
   
def setup():
    global SUN_POWER_FROM
    global SUN_POWER_TO
    global METABALL_SCALE
    global CAMERA_DISTANCE
    global METABALLS_AMOUNT
    global METABALL_SCALE_FROM
    global METABALL_SCALE_TO
    global METABALLS_AMOUNT_FROM
    global METABALLS_AMOUNT_TO
    global RES_X
    global RES_Y
    
    METABALL_SCALE = uniform(METABALL_SCALE_FROM,METABALL_SCALE_TO)
    CAMERA_DISTANCE = uniform(CAMERA_DISTANCE_FROM, CAMERA_DISTANCE_TO)
    METABALLS_AMOUNT = random.randint(METABALLS_AMOUNT_FROM,METABALLS_AMOUNT_TO)
    
    
    if "cloudCubes" not in bpy.data.collections :
        create_collection = bpy.data.collections.new(name="setup")
        bpy.context.scene.collection.children.link(create_collection)
        bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0, CAMERA_DISTANCE, 0), rotation=(pi * 90 / 180, 0, 0), scale=(1, 1, 1))
        myCam =  bpy.context.selected_objects[0]
        bpy.context.scene.camera = myCam
       

        bpy.data.collections['setup'].objects.link(myCam)
        bpy.context.scene.collection.objects.unlink(myCam)
        
        
        
        bpy.context.object.data.clip_end = 5000
        bpy.context.scene.render.film_transparent = True
        
        if "alphacloud" not in bpy.data.collections :
            create_collection = bpy.data.collections.new(name="alphacloud")
            bpy.context.scene.collection.children.link(create_collection)
            
        bpy.ops.object.light_add(type='SUN', align='WORLD', location=(0, 0, 3), scale=(1, 1, 1))
    
        sun = bpy.context.selected_objects[0]
        sun.data.energy = random.randint(SUN_POWER_FROM,SUN_POWER_TO)

        bpy.data.collections['setup'].objects.link(sun)
        bpy.context.scene.collection.objects.unlink(sun)    
        bpy.context.scene.eevee.use_ssr = True
        bpy.context.scene.eevee.use_volumetric_shadows = True
        bpy.context.scene.eevee.use_bloom = True
        bpy.context.scene.eevee.use_gtao = True
        bpy.context.scene.render.image_settings.file_format = 'PNG'
        bpy.context.scene.render.resolution_x = RES_X
        bpy.context.scene.render.resolution_y = RES_Y
        









def create_metaballs():
    global METABALL_SCALE
    global CAMERA_DISTANCE
    global METABALLS_AMOUNT
    global METABALL_AREA_X_FROM
    global METABALL_AREA_X_TO 
    global METABALL_AREA_Y_FROM
    global METABALL_AREA_Y_TO

    global METABALL_AREA_Z_FROM
    global METABALL_AREA_Z_TO 
    
    
    counter = 1
    
    while counter < METABALLS_AMOUNT:
    
        bpy.ops.object.metaball_add(type='BALL', radius=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(METABALL_SCALE, METABALL_SCALE, METABALL_SCALE))
        metaball = bpy.context.selected_objects[0]
    
    
        bpy.ops.transform.resize(value=(uniform(METABALL_SCALE_FROM,METABALL_SCALE_TO), uniform(METABALL_SCALE_FROM,METABALL_SCALE_TO), uniform(METABALL_SCALE_FROM,METABALL_SCALE_TO)), orient_type='GLOBAL')
        bpy.data.collections['alphacloud'].objects.link(metaball)
        bpy.context.scene.collection.objects.unlink(metaball)
        metaball.location.x = uniform(METABALL_AREA_X_FROM,METABALL_AREA_X_TO)
        metaball.location.y = uniform(METABALL_AREA_Y_FROM,METABALL_AREA_Y_TO)
        metaball.location.z = uniform(METABALL_AREA_Z_FROM,METABALL_AREA_Z_TO)

        

        counter = counter + 1
        
        
    for obj in bpy.data.collections['alphacloud'].all_objects:
        obj.select_set(True)
    
    bpy.ops.object.convert(target='MESH')
    
    cloud_obj = bpy.context.selected_objects[0]
    cloud_obj.name = "cloud"
    cloud_obj.data.name = "cloud"
    
    bpy.ops.object.volume_add(align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    empty_volume = bpy.context.selected_objects[0]
    empty_volume.name = "cloudVol"
    empty_volume.data.name = "cloudVol"
    bpy.data.collections['alphacloud'].objects.link(empty_volume)
    bpy.context.scene.collection.objects.unlink(empty_volume)
    
    
    
    mesh_to_vol_modifier = empty_volume.modifiers.new("MESH_TO_VOLUME",'MESH_TO_VOLUME')
    mesh_to_vol_modifier.object = cloud_obj
    
    cloud_obj.hide_render = True
    cloud_obj.hide_viewport = True



    
   
    displace_modifier = empty_volume.modifiers.new("VOLDisplace1",'VOLUME_DISPLACE')
   
    bpy.ops.texture.new()
    texture = bpy.data.textures["Texture"]
    texture.name = "cloudTexture"
    texture.type = "CLOUDS"
    
    displace_modifier.texture = texture
    

    
    
def add_material():
   
    empty_volume = bpy.data.collections['alphacloud'].objects["cloudVol"]
    
    
    bpy.ops.material.new()
    material = bpy.data.materials['Material']
    material.use_nodes = True
    material.name = "cloudmaterial"
    
   
    empty_volume.data.materials.append(material)
    material_nodes = material.node_tree.nodes
    material_links = material.node_tree.links
    
    
    princVolNode =  material_nodes['Principled Volume']
    
    
    output_node =  material_nodes['Material Output']
    output_node.label = "outputNode"


#    node_to_delete =  MAT_NODES['Principled BSDF']
#    MAT_NODES.remove( node_to_delete )
    
    
    

    
    gradientNode = material_nodes.new(type="ShaderNodeTexGradient")
    material_links.new(gradientNode.outputs[1], princVolNode.inputs[2])

    mappingNode = material_nodes.new(type="ShaderNodeMapping")
    mappingNode.inputs[1].default_value[0] = 12

    
    coordinateNode = material_nodes.new(type="ShaderNodeTexCoord")
    
    material_links.new(mappingNode.outputs[0], gradientNode.inputs[0])
    material_links.new(coordinateNode.outputs[3], mappingNode.inputs[0])
    bpy.data.materials["cloudmaterial"].node_tree.nodes["Mapping"].inputs[2].default_value[1] = pi * 90 / 180
    
    

    noiseNode = material_nodes.new(type="ShaderNodeTexNoise")
    colorRamp = material_nodes.new(type="ShaderNodeValToRGB")
    colorRamp.color_ramp.elements[0].position = 0.4


    material_links.new(noiseNode.outputs[0], colorRamp.inputs[0])

    material_links.new(colorRamp.outputs[0], princVolNode.inputs[0])
    material_links.new(colorRamp.outputs[1], princVolNode.inputs[5])

    
#    LINKS.new(colorRampNode.outputs[0], mathNode.inputs[0])
#    LINKS.new(mathNode.outputs[0], volume_scatter_node.inputs[1])







  
def render(moves):
    global OUTPUT
    
 
    bpy.context.scene.frame_set(moves)
    bpy.data.scenes["Scene"].render.filepath = OUTPUT + "alphacloud_%d.png" % moves
    bpy.ops.render.render(write_still=True)   
    
   # bpy.context.scene.render.filepath = OUTPUT+str(moves)+".png"
#    bpy.ops.render.render(write_still=True) 



    
    
    
    
    

    

    
  



def main():
    
    counter = 1
    
    #while counter <= AMOUNT_OF_RENDERED_CLOUDS:
    #    delete_all()
    #    setup()
    #    create_metaballs()
    #    add_material()
    #    render(counter);
    #    print ("Generating Cloud Image: " + str(counter))
    #    counter = counter +1
        
   
    
    
    
    
    
#main()