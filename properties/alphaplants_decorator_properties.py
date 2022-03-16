import bpy


class AlphaPlantsDecoratorProperties(bpy.types.PropertyGroup):

    


    camera_distance_from : bpy.props.IntProperty(name='Camera Distance From', soft_min=-100, soft_max=100,default=-44)
    camera_distance_to : bpy.props.IntProperty(name='Camera Distance To', soft_min=-100, soft_max=100,default=-30)


    metaball_area_x_from : bpy.props.FloatProperty(name='MetaBall X From', soft_min=-10, soft_max=10,default=-10)
    metaball_area_x_to : bpy.props.FloatProperty(name='MetaBall X To', soft_min=-10, soft_max=10,default=10)
    
  
    
    render_toggle : bpy.props.BoolProperty(name='Render?',default=False)
    cloud_export_path : bpy.props.StringProperty(name="Output", subtype='FILE_PATH')
    
    
