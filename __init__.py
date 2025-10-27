import bpy
from bpy.props import PointerProperty

# 导入所有模块
from . import (
    operators,
    ui,
    properties,
    utils
)

# 导入属性组类
from .properties.property_groups import (
    ATBatchProperties, ATBatchUVItem, ATBatchVColItem, 
    ATBatchVGroupItem, ATBatchShapeKeyItem, ATBatchModifierItem, ATBatchMaterialItem
)

# 插件信息
bl_info = {
    "name": "ATBatch",
    "description": "批量操作对象数据工具 - UV通道、顶点色、顶点组、形态键、修改器、材质",
    "author": "Baka_Akari",
    "version": (0, 0, 3),
    "blender": (2, 8, 0),
    "location": "View3D > Sidebar > ATBatch",
    "warning": "",
    "wiki_url": "",
    "support": "COMMUNITY",
    "category": "3D View"
}


def register():
    """注册所有模块"""
    # 1. 先注册属性组
    properties.register()
    
    # 2. 注册WindowManager的属性
    bpy.types.WindowManager.atbatch_props = PointerProperty(type=ATBatchProperties)
    
    # 3. 注册操作符
    operators.register()
    
    # 4. 注册UI
    ui.register()


def unregister():
    """注销所有模块"""
    # 注销UI
    ui.unregister()
    
    # 注销操作符
    operators.unregister()
    
    # 移除WindowManager属性
    try:
        del bpy.types.WindowManager.atbatch_props
    except:
        pass
    
    # 注销属性组
    properties.unregister()


if __name__ == "__main__":
    try:
        unregister()
    except:
        pass
    register()
