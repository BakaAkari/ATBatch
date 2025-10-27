import bpy
from bpy.types import Operator
from ..utils import data_collector


class ATBATCH_OT_delete_modifier(Operator):
    """批量删除修改器"""
    bl_idname = "atbatch.delete_modifier"
    bl_label = "删除修改器"
    bl_description = "批量删除选中的修改器类型"
    bl_options = {'REGISTER', 'UNDO'}
    
    modifier_type: bpy.props.StringProperty(name="修改器类型")
    
    def execute(self, context):
        modifier_type = self.modifier_type
        
        if not modifier_type:
            self.report({'ERROR'}, "请选择要删除的修改器类型")
            return {'CANCELLED'}
        
        modifier_data = data_collector.collect_modifiers()
        if modifier_type not in modifier_data:
            self.report({'ERROR'}, f"未找到修改器类型: {modifier_type}")
            return {'CANCELLED'}
        
        deleted_count = 0
        # 对所有使用该修改器类型的对象进行操作
        for obj in modifier_data[modifier_type]:
            modifiers_to_remove = []
            for modifier in obj.modifiers:
                if modifier.type == modifier_type:
                    modifiers_to_remove.append(modifier)
            
            for modifier in modifiers_to_remove:
                obj.modifiers.remove(modifier)
                deleted_count += 1
        
        self.report({'INFO'}, f"已删除 {deleted_count} 个修改器: {modifier_type}")
        return {'FINISHED'}


class ATBATCH_OT_toggle_modifier(Operator):
    """批量切换修改器启用状态"""
    bl_idname = "atbatch.toggle_modifier"
    bl_label = "切换修改器状态"
    bl_description = "批量切换选中修改器类型的启用/禁用状态"
    bl_options = {'REGISTER', 'UNDO'}
    
    modifier_type: bpy.props.StringProperty(name="修改器类型")
    
    def execute(self, context):
        modifier_type = self.modifier_type
        
        if not modifier_type:
            self.report({'ERROR'}, "请选择要切换的修改器类型")
            return {'CANCELLED'}
        
        modifier_data = data_collector.collect_modifiers()
        if modifier_type not in modifier_data:
            self.report({'ERROR'}, f"未找到修改器类型: {modifier_type}")
            return {'CANCELLED'}
        
        # 检查第一个修改器的状态来决定切换方向
        first_obj = modifier_data[modifier_type][0]
        first_modifier = None
        for modifier in first_obj.modifiers:
            if modifier.type == modifier_type:
                first_modifier = modifier
                break
        
        if not first_modifier:
            self.report({'ERROR'}, "无法找到修改器")
            return {'CANCELLED'}
        
        # 如果第一个是启用的，则全部禁用；否则全部启用
        new_state = not first_modifier.show_viewport
        action = "启用" if new_state else "禁用"
        
        toggled_count = 0
        # 对所有使用该修改器类型的对象进行操作
        for obj in modifier_data[modifier_type]:
            for modifier in obj.modifiers:
                if modifier.type == modifier_type:
                    modifier.show_viewport = new_state
                    modifier.show_render = new_state
                    toggled_count += 1
        
        self.report({'INFO'}, f"已{action} {toggled_count} 个修改器: {modifier_type}")
        return {'FINISHED'}


def register():
    """注册修改器操作符"""
    try:
        bpy.utils.register_class(ATBATCH_OT_delete_modifier)
        bpy.utils.register_class(ATBATCH_OT_toggle_modifier)
    except ValueError:
        pass


def unregister():
    """注销修改器操作符"""
    try:
        bpy.utils.unregister_class(ATBATCH_OT_delete_modifier)
        bpy.utils.unregister_class(ATBATCH_OT_toggle_modifier)
    except ValueError:
        pass
