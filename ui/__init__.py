# ATBatch UI模块

from . import panels, uv_list

def register():
    """注册所有UI组件"""
    uv_list.register()
    panels.register()


def unregister():
    """注销所有UI组件"""
    panels.unregister()
    uv_list.unregister()
