import bpy
from bpy.props import StringProperty, BoolProperty, CollectionProperty, IntProperty, EnumProperty
from bpy.types import PropertyGroup


class ATBatchUVItem(PropertyGroup):
    """UV通道项"""
    name: StringProperty(name="UV名称", default="")
    object_count: IntProperty(name="对象数量", default=0)


class ATBatchVColItem(PropertyGroup):
    """顶点色项"""
    name: StringProperty(name="顶点色名称", default="")
    object_count: IntProperty(name="对象数量", default=0)


class ATBatchVGroupItem(PropertyGroup):
    """顶点组项"""
    name: StringProperty(name="顶点组名称", default="")
    object_count: IntProperty(name="对象数量", default=0)


class ATBatchShapeKeyItem(PropertyGroup):
    """形态键项"""
    name: StringProperty(name="形态键名称", default="")
    object_count: IntProperty(name="对象数量", default=0)


class ATBatchModifierItem(PropertyGroup):
    """修改器项"""
    name: StringProperty(name="修改器类型", default="")
    object_count: IntProperty(name="对象数量", default=0)


class ATBatchMaterialItem(PropertyGroup):
    """材质项"""
    name: StringProperty(name="材质名称", default="")
    object_count: IntProperty(name="对象数量", default=0)


class ATBatchProperties(bpy.types.PropertyGroup):
    """ATBatch插件属性组"""
    
    # UV通道相关属性
    uv_items: CollectionProperty(type=ATBatchUVItem)
    uv_index: IntProperty(name="UV索引", default=0)
    
    # 顶点色相关属性
    vcol_items: CollectionProperty(type=ATBatchVColItem)
    vcol_index: IntProperty(name="顶点色索引", default=0)
    
    # 顶点组相关属性
    vgroup_items: CollectionProperty(type=ATBatchVGroupItem)
    vgroup_index: IntProperty(name="顶点组索引", default=0)
    
    # 形态键相关属性
    shapekey_items: CollectionProperty(type=ATBatchShapeKeyItem)
    shapekey_index: IntProperty(name="形态键索引", default=0)
    
    # 修改器相关属性
    modifier_items: CollectionProperty(type=ATBatchModifierItem)
    modifier_index: IntProperty(name="修改器索引", default=0)
    
    # 材质相关属性
    material_items: CollectionProperty(type=ATBatchMaterialItem)
    material_index: IntProperty(name="材质索引", default=0)
    
    # 刷新标志
    refresh_data: BoolProperty(
        name="刷新数据",
        description="刷新数据统计",
        default=False
    )


def register():
    """注册属性组"""
    try:
        bpy.utils.register_class(ATBatchUVItem)
        bpy.utils.register_class(ATBatchVColItem)
        bpy.utils.register_class(ATBatchVGroupItem)
        bpy.utils.register_class(ATBatchShapeKeyItem)
        bpy.utils.register_class(ATBatchModifierItem)
        bpy.utils.register_class(ATBatchMaterialItem)
        bpy.utils.register_class(ATBatchProperties)
    except ValueError:
        # 类已经注册过了，忽略错误
        pass


def unregister():
    """注销属性组"""
    try:
        bpy.utils.unregister_class(ATBatchProperties)
        bpy.utils.unregister_class(ATBatchMaterialItem)
        bpy.utils.unregister_class(ATBatchModifierItem)
        bpy.utils.unregister_class(ATBatchShapeKeyItem)
        bpy.utils.unregister_class(ATBatchVGroupItem)
        bpy.utils.unregister_class(ATBatchVColItem)
        bpy.utils.unregister_class(ATBatchUVItem)
    except ValueError:
        # 类没有注册，忽略错误
        pass
