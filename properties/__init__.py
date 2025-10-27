# ATBatch属性模块

from . import property_groups

def register():
    """注册所有属性组"""
    property_groups.register()


def unregister():
    """注销所有属性组"""
    property_groups.unregister()
