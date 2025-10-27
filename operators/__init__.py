# ATBatch操作符模块

from . import (
    uv_operators,
    vcol_operators,
    vgroup_operators,
    shapekey_operators,
    modifier_operators,
    material_operators
)

def register():
    """注册所有操作符"""
    uv_operators.register()
    vcol_operators.register()
    vgroup_operators.register()
    shapekey_operators.register()
    modifier_operators.register()
    material_operators.register()


def unregister():
    """注销所有操作符"""
    material_operators.unregister()
    modifier_operators.unregister()
    shapekey_operators.unregister()
    vgroup_operators.unregister()
    vcol_operators.unregister()
    uv_operators.unregister()
