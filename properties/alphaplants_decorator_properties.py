import bpy


class AlphaPlantsDecoratorProperties(bpy.types.PropertyGroup):

    

    delete_toggle : bpy.props.BoolProperty(name='Delete current plants?',default=False)
    
    decorate_object : bpy.props.PointerProperty(name = "Object to decorate", type = bpy.types.Object)

    
    

    
    images_toggle : bpy.props.BoolProperty(name='Use images?',default=False)
    images_turns : bpy.props.IntProperty(name='Image Rotations', min=1, soft_max=6,default=4)
    
    
    amount_of_plants : bpy.props.IntProperty(name='Amount of plants', min=1, soft_max=100,default=10)
    amount_of_dups : bpy.props.IntProperty(name='Amount of duplicates', min=0, soft_max=100,default=0)
    
    
    
   
    
    
    
