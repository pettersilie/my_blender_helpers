import bpy


class BoneDecoratorProperties(bpy.types.PropertyGroup):

    

    delete_toggle : bpy.props.BoolProperty(name='Delete current bones?',default=True)
    
    rot_x : bpy.props.FloatProperty(name="Bone X Rot", default=0)
    rot_y : bpy.props.FloatProperty(name="Bone Y Rot", default=0)
    rot_z : bpy.props.FloatProperty(name="Bone Z Rot", default=0)
    
    scale_factor : bpy.props.FloatProperty(name="Scale Factor",default=1)
    
    armature_name : bpy.props.StringProperty(name="Arm Name", default="bone_decorator_arm")

    
    
    decorate_object : bpy.props.PointerProperty(name = "DecorateObject", type = bpy.types.Object)
    
    
    
    
    
    
    
