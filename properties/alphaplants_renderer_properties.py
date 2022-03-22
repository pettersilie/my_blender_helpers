import bpy


class AlphaPlantsRendererProperties(bpy.types.PropertyGroup):

    

    
    res_x : bpy.props.IntProperty(name='Resolution X' ,default=1280)
    res_y : bpy.props.IntProperty(name='Resolution Y',default=1280)
    
    
    random_seed_from : bpy.props.IntProperty(name='Rand Seed From' ,default=0)
    random_seed_to : bpy.props.IntProperty(name='Rand Seed To',default=3)
    
    random_leaves_from : bpy.props.IntProperty(name='Rand Leaves From' ,min=0,default=10)
    random_leaves_to : bpy.props.IntProperty(name='Rand Leaves To', min=0, default=70)
    
    random_levels_from : bpy.props.IntProperty(name='Rand Levels From' ,min=0,max=4,default=1)
    random_levels_to : bpy.props.IntProperty(name='Rand Levels To', min=0, max=4,default=2)


    random_trunk_heigth_from : bpy.props.FloatProperty(name='Trunk Height From', min=-0, max=1,default=.5)
    random_trunk_height_to  : bpy.props.FloatProperty(name='Trunk Height To', soft_min=0, max=1,default=.5)
    
    random_scale_from : bpy.props.FloatProperty(name='Scale From', min=0, default=1)
    random_scale_to  : bpy.props.FloatProperty(name='Scale To',  min=0, default=1)
    
    trunk_extension_from : bpy.props.FloatProperty(name='Trunk Ext From', min=0, default=0)
    trunk_extension_to : bpy.props.FloatProperty(name='Trunk Ext To', min=0, default=0)
    
    
    amount_plants : bpy.props.IntProperty(name='Amount of Plants', min=1, soft_max=100,default=1)
    
    
    
    render_toggle : bpy.props.BoolProperty(name='Render?',default=False)
    plant_export_path : bpy.props.StringProperty(name="Render Dir", subtype='FILE_PATH')
    leaves_path : bpy.props.StringProperty(name="Leaves Dir", subtype='FILE_PATH')
    
    
