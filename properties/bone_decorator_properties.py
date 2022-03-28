import bpy


class BoneDecoratorProperties(bpy.types.PropertyGroup):

    

    delete_toggle : bpy.props.BoolProperty(name='Delete current bones?',default=True)
    
    rot_x : bpy.props.FloatProperty(name="Bone X Rot", min=0, max=360)
    rot_y : bpy.props.FloatProperty(name="Bone Y Rot", min=0, max=360)
    rot_z : bpy.props.FloatProperty(name="Bone Z Rot", min=0, max=360)
    
    scale_factor : bpy.props.FloatProperty(name="Scale Factor", min=0)
    
    armature_name : bpy.props.StringProperty(name="Arm Name", default="bone_decorator_arm")

    
    
    decorate_object : bpy.props.PointerProperty(name = "DecorateObject", type = bpy.types.Object)
    
    
    
    
    
    
    
