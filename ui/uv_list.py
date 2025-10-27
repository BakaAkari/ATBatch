import bpy
from bpy.types import UIList


class ATBATCH_UL_uv_list(UIList):
    """UV通道列表"""
    bl_idname = "ATBATCH_UL_uv_list"
    
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        # 设置图标
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text=f"{item.name} ({item.object_count})", icon='UV')
        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon='UV')


class ATBATCH_UL_vcol_list(UIList):
    """顶点色列表"""
    bl_idname = "ATBATCH_UL_vcol_list"
    
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text=f"{item.name} ({item.object_count})", icon='GROUP_VCOL')
        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon='GROUP_VCOL')


class ATBATCH_UL_vgroup_list(UIList):
    """顶点组列表"""
    bl_idname = "ATBATCH_UL_vgroup_list"
    
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text=f"{item.name} ({item.object_count})", icon='GROUP_VERTEX')
        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon='GROUP_VERTEX')


class ATBATCH_UL_shapekey_list(UIList):
    """形态键列表"""
    bl_idname = "ATBATCH_UL_shapekey_list"
    
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text=f"{item.name} ({item.object_count})", icon='SHAPEKEY_DATA')
        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon='SHAPEKEY_DATA')


class ATBATCH_UL_modifier_list(UIList):
    """修改器列表"""
    bl_idname = "ATBATCH_UL_modifier_list"
    
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text=f"{item.name} ({item.object_count})", icon='MODIFIER')
        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon='MODIFIER')


class ATBATCH_UL_material_list(UIList):
    """材质列表"""
    bl_idname = "ATBATCH_UL_material_list"
    
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text=f"{item.name} ({item.object_count})", icon='MATERIAL')
        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon='MATERIAL')


def register():
    """注册UIList"""
    try:
        bpy.utils.register_class(ATBATCH_UL_uv_list)
        bpy.utils.register_class(ATBATCH_UL_vcol_list)
        bpy.utils.register_class(ATBATCH_UL_vgroup_list)
        bpy.utils.register_class(ATBATCH_UL_shapekey_list)
        bpy.utils.register_class(ATBATCH_UL_modifier_list)
        bpy.utils.register_class(ATBATCH_UL_material_list)
    except ValueError:
        pass


def unregister():
    """注销UIList"""
    try:
        bpy.utils.unregister_class(ATBATCH_UL_material_list)
        bpy.utils.unregister_class(ATBATCH_UL_modifier_list)
        bpy.utils.unregister_class(ATBATCH_UL_shapekey_list)
        bpy.utils.unregister_class(ATBATCH_UL_vgroup_list)
        bpy.utils.unregister_class(ATBATCH_UL_vcol_list)
        bpy.utils.unregister_class(ATBATCH_UL_uv_list)
    except ValueError:
        pass
