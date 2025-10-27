import bpy
from bpy.types import Operator
from ..utils import data_collector


class ATBATCH_OT_rename_uv(Operator):
    """批量重命名UV通道"""
    bl_idname = "atbatch.rename_uv"
    bl_label = "重命名UV通道"
    bl_description = "批量重命名选中的UV通道"
    bl_options = {'REGISTER', 'UNDO'}
    
    uv_name: bpy.props.StringProperty(name="UV名称")
    
    def invoke(self, context, event):
        # 弹出输入对话框
        self.new_name = self.uv_name  # 设置默认值为原名称
        return context.window_manager.invoke_props_dialog(self, width=300)
    
    def draw(self, context):
        layout = self.layout
        layout.label(text=f"重命名UV通道: {self.uv_name}")
        layout.prop(self, "new_name", text="新名称")
    
    new_name: bpy.props.StringProperty(name="新名称", default="")
    
    def execute(self, context):
        old_name = self.uv_name
        new_name = self.new_name
        
        if not old_name or not new_name:
            self.report({'ERROR'}, "请输入新名称")
            return {'CANCELLED'}
        
        if old_name == new_name:
            self.report({'WARNING'}, "新名称与旧名称相同")
            return {'CANCELLED'}
        
        uv_data = data_collector.collect_uv_maps()
        if old_name not in uv_data:
            self.report({'ERROR'}, f"未找到UV通道: {old_name}")
            return {'CANCELLED'}
        
        renamed_count = 0
        # 对所有使用该UV通道的对象进行操作
        for obj in uv_data[old_name]:
            if obj.data and obj.data.uv_layers:
                for uv_layer in obj.data.uv_layers:
                    if uv_layer.name == old_name:
                        uv_layer.name = new_name
                        renamed_count += 1
                        break
        
        self.report({'INFO'}, f"已重命名 {renamed_count} 个UV通道: {old_name} -> {new_name}")
        return {'FINISHED'}


class ATBATCH_OT_delete_uv(Operator):
    """批量删除UV通道"""
    bl_idname = "atbatch.delete_uv"
    bl_label = "删除UV通道"
    bl_description = "批量删除选中的UV通道"
    bl_options = {'REGISTER', 'UNDO'}
    
    uv_name: bpy.props.StringProperty(name="UV名称")
    
    def execute(self, context):
        props = context.window_manager.atbatch_props
        uv_name = self.uv_name
        
        if not uv_name:
            self.report({'ERROR'}, "请选择要删除的UV通道")
            return {'CANCELLED'}
        
        uv_data = data_collector.collect_uv_maps()
        if uv_name not in uv_data:
            self.report({'ERROR'}, f"未找到UV通道: {uv_name}")
            return {'CANCELLED'}
        
        deleted_count = 0
        # 对所有使用该UV通道的对象进行操作
        for obj in uv_data[uv_name]:
            if obj.data and obj.data.uv_layers:
                uv_layer_to_remove = None
                for uv_layer in obj.data.uv_layers:
                    if uv_layer.name == uv_name:
                        uv_layer_to_remove = uv_layer
                        break
                
                if uv_layer_to_remove:
                    obj.data.uv_layers.remove(uv_layer_to_remove)
                    deleted_count += 1
        
        self.report({'INFO'}, f"已删除 {deleted_count} 个UV通道: {uv_name}")
        return {'FINISHED'}


class ATBATCH_OT_set_active_uv(Operator):
    """批量设置活动UV通道"""
    bl_idname = "atbatch.set_active_uv"
    bl_label = "设为活动UV"
    bl_description = "批量设置选中的UV通道为活动UV"
    bl_options = {'REGISTER', 'UNDO'}
    
    uv_name: bpy.props.StringProperty(name="UV名称")
    
    def execute(self, context):
        props = context.window_manager.atbatch_props
        uv_name = self.uv_name
        
        if not uv_name:
            self.report({'ERROR'}, "请选择要设为活动的UV通道")
            return {'CANCELLED'}
        
        uv_data = data_collector.collect_uv_maps()
        if uv_name not in uv_data:
            self.report({'ERROR'}, f"未找到UV通道: {uv_name}")
            return {'CANCELLED'}
        
        set_count = 0
        # 对所有使用该UV通道的对象进行操作
        for obj in uv_data[uv_name]:
            if obj.data and obj.data.uv_layers:
                for uv_layer in obj.data.uv_layers:
                    if uv_layer.name == uv_name:
                        obj.data.uv_layers.active = uv_layer
                        set_count += 1
                        break
        
        self.report({'INFO'}, f"已将 {set_count} 个UV通道设为活动: {uv_name}")
        return {'FINISHED'}


def register():
    """注册UV操作符"""
    try:
        bpy.utils.register_class(ATBATCH_OT_rename_uv)
        bpy.utils.register_class(ATBATCH_OT_delete_uv)
        bpy.utils.register_class(ATBATCH_OT_set_active_uv)
    except ValueError:
        pass


def unregister():
    """注销UV操作符"""
    try:
        bpy.utils.unregister_class(ATBATCH_OT_set_active_uv)
        bpy.utils.unregister_class(ATBATCH_OT_delete_uv)
        bpy.utils.unregister_class(ATBATCH_OT_rename_uv)
    except ValueError:
        pass
