bl_info = {
    "name": "Blender Helper Addon",
    "author": "Mirko",
    "version": (1, 1),
    "blender": (2, 80, 0),
    "location": "View3D > n",
    "description": "Includes Helpers for Blender-Projects",
    "warning": "Some helpers here will delete all your objects inside you blend file before doing the job. Read the doc first!",
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
    importlib.reload(utils)
else:
    import bpy
    from .ui import *
    from .operators import *
    from .properties import *
    from .scripts import *
    from .ui.alphaclouds_renderer_panel import AlphaCloudsRendererPanel
    from .ui.alphaclouds_inserter_panel import AlphaCloudsInserterPanel

    from .operators.alphaclouds_renderer_operator import AlphaCloudsRendererOperator
    from .properties.alphaclouds_renderer_properties import AlphaCloudsRendererProperties
    
    from .operators.alphaclouds_inserter_operator import AlphacloudsInserterOperator
    from .properties.alphaclouds_inserter_properties import AlphaCloudsInserterProperties
    from .scripts import *







__CLASSES__ = [
    AlphaCloudsRendererOperator,
    AlphaCloudsRendererProperties,
    
    AlphacloudsInserterOperator,
    AlphaCloudsInserterProperties,
    
    AlphaCloudsRendererPanel,
    AlphaCloudsInserterPanel
    
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
    bpy.types.Scene.alphaclouds_renderer_props = bpy.props.PointerProperty(type=AlphaCloudsRendererProperties)
    bpy.types.Scene.alphaclouds_inserter_props = bpy.props.PointerProperty(type=AlphaCloudsInserterProperties)
    
    print(__name__ + " loaded")


def unregister():
 
    
    
    for cls in __CLASSES__:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.alphaclouds_renderer_props
    del bpy.types.Scene.alphaclouds_inserter_props
    cleanse_modules()
    



if __name__ == "__main__":
    register()
