import bpy


class FaceImporterProperties(bpy.types.PropertyGroup):

    

    delete_toggle : bpy.props.BoolProperty(name='Delete rocks?',default=True)
    rock_texture_dir : bpy.props.StringProperty(name="TextureDir", subtype='FILE_PATH')
    smooth_toggle : bpy.props.BoolProperty(name='Smooth?',default=True)
    
    sphere_subdivision : bpy.props.IntProperty(name='Sphere Subdivison', min=0, max=10,default=2)
    
    displace_strength_from : bpy.props.FloatProperty(name='Disp Strength From', min=0, soft_max=10,default=0)
   
    
    
    
    
