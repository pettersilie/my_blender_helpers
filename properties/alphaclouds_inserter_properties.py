import bpy


class AlphaCloudsInserterProperties(bpy.types.PropertyGroup):



    delete_toggle : bpy.props.BoolProperty(name='Delete current Clouds?',default=False)
    cloud_area_x_from : bpy.props.FloatProperty(name='Area X From', default=-50)
    cloud_area_x_to : bpy.props.FloatProperty(name='Area X To', default=50)
    
    cloud_area_y_from : bpy.props.FloatProperty(name='Area Y From', default=-50)
    cloud_area_y_to : bpy.props.FloatProperty(name='Area Y To', default=50)
    
    cloud_area_z_from : bpy.props.FloatProperty(name='Area Z From', default=-50)
    cloud_area_z_to : bpy.props.FloatProperty(name='Area Z To', default=50)
    
    scale_factor_x : bpy.props.FloatProperty(name='Scale Factor X', default=2)
    scale_factor_z : bpy.props.FloatProperty(name='Scale Factor Y', default=2)
    
    amount_of_clouds : bpy.props.IntProperty(name='Amount of Clouds', default=10)
    use_duplicates_toggle : bpy.props.BoolProperty(name='use dupblicates?',default=False)
    amount_of_duplicates : bpy.props.IntProperty(name='Amount of Duplicates', default=0)
    
    track_to_camera_toggle : bpy.props.BoolProperty(name='Track to Cam?',default=False)
    file_import_path : bpy.props.StringProperty(name="Image-Dir", subtype='FILE_PATH')
    
    
