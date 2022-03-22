import bpy


class RocksGeneratorProperties(bpy.types.PropertyGroup):

    

    delete_toggle : bpy.props.BoolProperty(name='Delete rocks?',default=True)
    rock_texture_dir : bpy.props.StringProperty(name="TextureDir", subtype='FILE_PATH')
    smooth_toggle : bpy.props.BoolProperty(name='Smooth?',default=True)
    
    sphere_subdivision : bpy.props.IntProperty(name='Sphere Subdivison', min=0, max=10,default=2)
    
    displace_strength_from : bpy.props.FloatProperty(name='Disp Strength From', min=0, soft_max=10,default=0)
    displace_strength_to : bpy.props.FloatProperty(name='Disp Strength To', min=0, soft_max=10,default=1.5)
    
    
    displace_percentage_from : bpy.props.IntProperty(name='Displace % From', min=0, max=100,default=20)
    displace_percentage_to : bpy.props.IntProperty(name='Displace % To', min=0, max=100,default=20)

    amount_of_rocks : bpy.props.IntProperty(name='Amount of Rocks', min=0, soft_max=100,default=10)
    amount_of_duplicates : bpy.props.IntProperty(name='Amount of Duplicates', min=0, soft_max=100,default=0)


    scale_factor_x_from : bpy.props.FloatProperty(name='Scale X From', min=0, soft_max=10,default=1)
    scale_factor_x_to : bpy.props.FloatProperty(name='Scale X To', min=0, soft_max=10,default=2)
    
    scale_factor_y_from : bpy.props.FloatProperty(name='Scale Y From', min=0, soft_max=10,default=1)
    scale_factor_y_to : bpy.props.FloatProperty(name='Scale Y To', min=0, soft_max=10,default=2)
    
    scale_factor_z_from : bpy.props.FloatProperty(name='Scale Z From', min=0, soft_max=10,default=1)
    scale_factor_z_to : bpy.props.FloatProperty(name='Scale T To', min=0, soft_max=10,default=2)
    
    rot_x_from : bpy.props.FloatProperty(name='Rot X From', min=0, max=360,default=0)
    rot_x_to : bpy.props.FloatProperty(name='Rot X To', min=0, max=360,default=0)
    
    rot_y_from : bpy.props.FloatProperty(name='Rot Y From', min=0, max=360,default=0)
    rot_y_to : bpy.props.FloatProperty(name='Rot Y To', min=0, max=360,default=0)
    
    rot_z_from : bpy.props.FloatProperty(name='Rot Z From', min=0, max=360,default=0)
    rot_z_to : bpy.props.FloatProperty(name='Rot Z To', min=0, max=360,default=0)
    
    decorate_object : bpy.props.PointerProperty(name = "Decorate", type = bpy.types.Object)
    
    
    
    
    
    
    
