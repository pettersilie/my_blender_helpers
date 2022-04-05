import bpy


class FaceImporterProperties(bpy.types.PropertyGroup):

    

    delete_toggle : bpy.props.BoolProperty(name='Delete current?',default=True)
    face_file : bpy.props.StringProperty(name="Face Blendile", subtype='FILE_PATH')
    
    
    scale_percentage : bpy.props.IntProperty(name='Scale Percentage', min=0, max=100,default=10)
    
    face_object : bpy.props.PointerProperty(name = "FaceObject", type = bpy.types.Object)
   
    finish_toggle : bpy.props.BoolProperty(name='Finish?',default=False)
    
    
    
    
