import bpy


class AlphaCloudsInserterProperties(bpy.types.PropertyGroup):



    delete_toggle : bpy.props.BoolProperty(name='Delete current Clouds?',default=False)
    cloud_area_x_from : bpy.props.FloatProperty(name='Area X From', default=-10)
    cloud_area_x_to : bpy.props.FloatProperty(name='Area X To', default=10)
    
    cloud_area_y_from : bpy.props.FloatProperty(name='Area Y From', default=-10)
    cloud_area_y_to : bpy.props.FloatProperty(name='Area Y To', default=10)
    
    cloud_area_z_from : bpy.props.FloatProperty(name='MetaBall Z From', default=-10)
    cloud_area_z_to : bpy.props.FloatProperty(name='MetaBall Z To', default=10)
    
    scale_factor_x : bpy.props.FloatProperty(name='MetaBall Scake From', default=2)
    scale_factor_z : bpy.props.FloatProperty(name='MetaBall Scale To', default=2)
    
    amount_of_clouds : bpy.props.IntProperty(name='Amount of Clouds', default=10)
    
    render_toggle : bpy.props.BoolProperty(name='Render?',default=False)
    file_import_path : bpy.props.StringProperty(name="Path", subtype='FILE_PATH')
    
    
