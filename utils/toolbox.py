import bpy
import os
import sys
import random
from pathlib import Path
from math import pi



def purge_orphans():

  for block in bpy.data.meshes:
      if block.users == 0:
          bpy.data.meshes.remove(block)
  
  for block in bpy.data.materials:
      if block.users == 0:
          bpy.data.materials.remove(block)
  
  for block in bpy.data.textures:
      if block.users == 0:
          bpy.data.textures.remove(block)
  
  for block in bpy.data.images:
      if block.users == 0:
          bpy.data.images.remove(block)

  for block in bpy.data.curves:
      if block.users == 0:
          bpy.data.curves.remove(block)
          
  for block in bpy.data.lights:
      if block.users == 0:
          bpy.data.lights.remove(block)
          
  for block in bpy.data.metaballs:
      if block.users == 0:
          bpy.data.metaballs.remove(block)
          
          
  for block in bpy.data.objects:
      if block.users == 0:
          bpy.data.objects.remove(block)

  for block in bpy.data.volumes:
      if block.users == 0:
          bpy.data.volumes.remove(block)
          
  for block in bpy.data.cameras:
      if block.users == 0:
          bpy.data.cameras.remove(block)
          
          
          
          
def create_root_collection(col_name):
    if col_name not in bpy.data.collections :
            create_collection = bpy.data.collections.new(name=col_name)
            bpy.context.scene.collection.children.link(create_collection)
            return create_collection
    return bpy.data.collections[col_name]
            
            
            
            
def link_object_to_collection(col_name, obj):

    obj.users_collection[0].objects.unlink(obj)
    bpy.data.collections[col_name].objects.link(obj)
    
    
def delete_objects_from_collection(col_name):
    if col_name in bpy.data.collections :
        for ob in bpy.data.collections[col_name].objects:
            ob.hide_set(False)
            ob.hide_render = False
            ob.select_set(True)
        
            bpy.ops.object.delete() 
            
            
def get_files_from_directory(path):
    
    FILES = []
    
    if (directory_exists(path) == True):
    
      for i in os.listdir(path):
          print(i)
          FILES.append(i)
      return FILES
    return None
        
def directory_exists(path):
    
    p = Path(path)
    if (p.is_dir()):
        return p.exists()
    else:
        return False
 
def deselect_all(unset_active_object):
    bpy.ops.object.select_all(action='DESELECT')
    
    if (unset_active_object == True):
        bpy.context.scene.objects.active = None 
        
def calculate_rotation(degress):
    return pi * degrees / 180
    
    
def select_object(obj, make_active_object):
    obj.select_set(True)
    if (make_active_object == True):
        bpy.context.scene.objects.active = obj 
        
def set_object_name(obj_name, obj):
    obj.name = obj_name
    obj.data.name = obj_name

          