bl_info = {
    "name": "Blender Helper Addon",
    "author": "Mirko",
    "version": (1, 1),
    "blender": (2, 80, 0),
    "location": "View3D > n",
    "description": "Includes Helpers for Blender-Projects",
    "warning": "",
    "doc_url": "",
    "category": "",
}


import sys
import os


if "bpy" in locals():
    print("BPY IN LOCALS")
    import importlib
    importlib.reload(ui)
    importlib.reload(operators)
    importlib.reload(properties)
    importlib.reload(scripts)
else:
    import bpy
    from .ui import *
    from .ui.generate_ui import GenerateUI
    from .operators import *
    from .properties import *
    from .operators.alphaclouds_generator_operator import AlphacloudsGeneratorOperator
    from .properties.alphacloud_generator_properties import AlphaCloudsGeneratorProperties
    from .operators.alphaclouds_inserter_operator import AlphacloudsInserterOperator
    from .properties.alphacloud_inserter_properties import AlphaCloudsInserterProperties
    from .scripts import *







#from lego_add_on.ui import GenerateUI
#import lego_add_on





__CLASSES__ = [
    AlphacloudsGeneratorOperator,
    AlphaCloudsGeneratorProperties,
    AlphacloudsInserterOperator,
    AlphaCloudsInserterProperties,
    GenerateUI
    
]

def cleanse_modules():
    """search for your plugin modules in blender python sys.modules and remove them"""

    import sys

    all_modules = sys.modules 
    all_modules = dict(sorted(all_modules.items(),key= lambda x:x[0])) #sort them
   
    for k,v in all_modules.items():
        if k.startswith(__name__):
            del sys.modules[k]



def register():
    
    #unregister()
    

    
    for cls in __CLASSES__:
        bpy.utils.register_class(cls)
    bpy.types.Scene.alphaclouds_generator_props = bpy.props.PointerProperty(type=AlphaCloudsGeneratorProperties)
    bpy.types.Scene.alphaclouds_inserter_props = bpy.props.PointerProperty(type=AlphaCloudsInserterProperties)
    
    print(__name__ + " loaded")


def unregister():
 
    
    
    for cls in __CLASSES__:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.alphaclouds_generator_props
    del bpy.types.Scene.alphaclouds_inserter_props
    cleanse_modules()
    



if __name__ == "__main__":
    register()
