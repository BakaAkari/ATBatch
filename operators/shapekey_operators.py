import bpy
from bpy.types import Operator
from ..utils import data_collector


class ATBATCH_OT_rename_shapekey(Operator):
    """批量重命名形态键"""
    bl_idname = "atbatch.rename_shapekey"
    bl_label = "重命名形态键"
    bl_description = "批量重命名选中的形态键"
    bl_options = {'REGISTER', 'UNDO'}
    
    shapekey_name: bpy.props.StringProperty(name="形态键名称")
    
    def invoke(self, context, event):
        # 弹出输入对话框
        self.new_name = self.shapekey_name  # 设置默认值为原名称
        return context.window_manager.invoke_props_dialog(self, width=300)
    
    def draw(self, context):
        layout = self.layout
        layout.label(text=f"重命名形态键: {self.shapekey_name}")
        layout.prop(self, "new_name", text="新名称")
    
    new_name: bpy.props.StringProperty(name="新名称", default="")
    
    def execute(self, context):
        old_name = self.shapekey_name
        new_name = self.new_name
        
        if not old_name or not new_name:
            self.report({'ERROR'}, "请输入新名称")
            return {'CANCELLED'}
        
        if old_name == new_name:
            self.report({'WARNING'}, "新名称与旧名称相同")
            return {'CANCELLED'}
        
        shapekey_data = data_collector.collect_shape_keys()
        if old_name not in shapekey_data:
            self.report({'ERROR'}, f"未找到形态键: {old_name}")
            return {'CANCELLED'}
        
        renamed_count = 0
        # 对所有使用该形态键的对象进行操作
        for obj in shapekey_data[old_name]:
            if obj.data.shape_keys and obj.data.shape_keys.key_blocks:
                for shapekey in obj.data.shape_keys.key_blocks:
                    if shapekey.name == old_name:
                        shapekey.name = new_name
                        renamed_count += 1
                        break
        
        self.report({'INFO'}, f"已重命名 {renamed_count} 个形态键: {old_name} -> {new_name}")
        return {'FINISHED'}


class ATBATCH_OT_delete_shapekey(Operator):
    """批量删除形态键"""
    bl_idname = "atbatch.delete_shapekey"
    bl_label = "删除形态键"
    bl_description = "批量删除选中的形态键"
    bl_options = {'REGISTER', 'UNDO'}
    
    shapekey_name: bpy.props.StringProperty(name="形态键名称")
    
    def execute(self, context):
        shapekey_name = self.shapekey_name
        
        if not shapekey_name:
            self.report({'ERROR'}, "请选择要删除的形态键")
            return {'CANCELLED'}
        
        shapekey_data = data_collector.collect_shape_keys()
        if shapekey_name not in shapekey_data:
            self.report({'ERROR'}, f"未找到形态键: {shapekey_name}")
            return {'CANCELLED'}
        
        deleted_count = 0
        # 对所有使用该形态键的对象进行操作
        for obj in shapekey_data[shapekey_name]:
            if obj.data.shape_keys and obj.data.shape_keys.key_blocks:
                shapekey_to_remove = None
                for shapekey in obj.data.shape_keys.key_blocks:
                    if shapekey.name == shapekey_name:
                        shapekey_to_remove = shapekey
                        break
                
                if shapekey_to_remove:
                    obj.shape_key_remove(shapekey_to_remove)
                    deleted_count += 1
        
        self.report({'INFO'}, f"已删除 {deleted_count} 个形态键: {shapekey_name}")
        return {'FINISHED'}


def register():
    """注册形态键操作符"""
    try:
        bpy.utils.register_class(ATBATCH_OT_rename_shapekey)
        bpy.utils.register_class(ATBATCH_OT_delete_shapekey)
    except ValueError:
        pass


def unregister():
    """注销形态键操作符"""
    try:
        bpy.utils.unregister_class(ATBATCH_OT_rename_shapekey)
        bpy.utils.unregister_class(ATBATCH_OT_delete_shapekey)
    except ValueError:
        pass
