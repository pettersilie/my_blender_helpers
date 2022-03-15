import bpy


class AlphaCloudsRendererProperties(bpy.types.PropertyGroup):

    


    camera_distance_from : bpy.props.IntProperty(name='Camera Distance From', soft_min=-100, soft_max=100,default=-44)
    camera_distance_to : bpy.props.IntProperty(name='Camera Distance To', soft_min=-100, soft_max=100,default=-30)


    metaball_area_x_from : bpy.props.FloatProperty(name='MetaBall X From', soft_min=-10, soft_max=10,default=-10)
    metaball_area_x_to : bpy.props.FloatProperty(name='MetaBall X To', soft_min=-10, soft_max=10,default=10)
    
    metaball_area_y_from : bpy.props.FloatProperty(name='MetaBall Y From', soft_min=-10, soft_max=10,default=-0.2)
    metaball_area_y_to : bpy.props.FloatProperty(name='MetaBall Y To', soft_min=-10, soft_max=10,default=0.5)
    
    metaball_area_z_from : bpy.props.FloatProperty(name='MetaBall Z From', soft_min=-10, soft_max=10,default=-3)
    metaball_area_z_to : bpy.props.FloatProperty(name='MetaBall Z To', soft_min=-10, soft_max=10,default=3)
    
    metaball_scale_from : bpy.props.FloatProperty(name='MetaBall Scake From', soft_min=-10, soft_max=10,default=0.3)
    metaball_scale_to : bpy.props.FloatProperty(name='MetaBall Scale To', soft_min=-10, soft_max=10,default=1.5)
    
    metaball_amount_from : bpy.props.IntProperty(name='MetaBall Amount From', soft_min=-100, soft_max=100,default=40)
    metaball_amount_to : bpy.props.IntProperty(name='MetaBall Amount To', soft_min=-100, soft_max=100,default=80)
    
    sun_power_from : bpy.props.IntProperty(name='Sun Power From', soft_min=-1000, soft_max=1000,default=500)
    sun_power_to : bpy.props.IntProperty(name='Sun Power To', soft_min=-1000, soft_max=1000,default=700)
    
    amount_of_clouds : bpy.props.IntProperty(name='Amount of Clouds', soft_min=0, soft_max=100,default=1)
    
    render_toggle : bpy.props.BoolProperty(name='Render?',default=False)
    cloud_export_path : bpy.props.StringProperty(name="Output", subtype='FILE_PATH')
    
    
