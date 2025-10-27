import bpy
from bpy.types import Operator
from ..utils import data_collector


class ATBATCH_OT_rename_vgroup(Operator):
    """批量重命名顶点组"""
    bl_idname = "atbatch.rename_vgroup"
    bl_label = "重命名顶点组"
    bl_description = "批量重命名选中的顶点组"
    bl_options = {'REGISTER', 'UNDO'}
    
    vgroup_name: bpy.props.StringProperty(name="顶点组名称")
    
    def invoke(self, context, event):
        # 弹出输入对话框
        self.new_name = self.vgroup_name  # 设置默认值为原名称
        return context.window_manager.invoke_props_dialog(self, width=300)
    
    def draw(self, context):
        layout = self.layout
        layout.label(text=f"重命名顶点组: {self.vgroup_name}")
        layout.prop(self, "new_name", text="新名称")
    
    new_name: bpy.props.StringProperty(name="新名称", default="")
    
    def execute(self, context):
        old_name = self.vgroup_name
        new_name = self.new_name
        
        if not old_name or not new_name:
            self.report({'ERROR'}, "请输入新名称")
            return {'CANCELLED'}
        
        if old_name == new_name:
            self.report({'WARNING'}, "新名称与旧名称相同")
            return {'CANCELLED'}
        
        vgroup_data = data_collector.collect_vertex_groups()
        if old_name not in vgroup_data:
            self.report({'ERROR'}, f"未找到顶点组: {old_name}")
            return {'CANCELLED'}
        
        renamed_count = 0
        # 对所有使用该顶点组的对象进行操作
        for obj in vgroup_data[old_name]:
            for vgroup in obj.vertex_groups:
                if vgroup.name == old_name:
                    vgroup.name = new_name
                    renamed_count += 1
                    break
        
        self.report({'INFO'}, f"已重命名 {renamed_count} 个顶点组: {old_name} -> {new_name}")
        return {'FINISHED'}


class ATBATCH_OT_delete_vgroup(Operator):
    """批量删除顶点组"""
    bl_idname = "atbatch.delete_vgroup"
    bl_label = "删除顶点组"
    bl_description = "批量删除选中的顶点组"
    bl_options = {'REGISTER', 'UNDO'}
    
    vgroup_name: bpy.props.StringProperty(name="顶点组名称")
    
    def execute(self, context):
        vgroup_name = self.vgroup_name
        
        if not vgroup_name:
            self.report({'ERROR'}, "请选择要删除的顶点组")
            return {'CANCELLED'}
        
        vgroup_data = data_collector.collect_vertex_groups()
        if vgroup_name not in vgroup_data:
            self.report({'ERROR'}, f"未找到顶点组: {vgroup_name}")
            return {'CANCELLED'}
        
        deleted_count = 0
        # 对所有使用该顶点组的对象进行操作
        for obj in vgroup_data[vgroup_name]:
            vgroup_to_remove = None
            for vgroup in obj.vertex_groups:
                if vgroup.name == vgroup_name:
                    vgroup_to_remove = vgroup
                    break
            
            if vgroup_to_remove:
                obj.vertex_groups.remove(vgroup_to_remove)
                deleted_count += 1
        
        self.report({'INFO'}, f"已删除 {deleted_count} 个顶点组: {vgroup_name}")
        return {'FINISHED'}


def register():
    """注册顶点组操作符"""
    try:
        bpy.utils.register_class(ATBATCH_OT_rename_vgroup)
        bpy.utils.register_class(ATBATCH_OT_delete_vgroup)
    except ValueError:
        pass


def unregister():
    """注销顶点组操作符"""
    try:
        bpy.utils.unregister_class(ATBATCH_OT_rename_vgroup)
        bpy.utils.unregister_class(ATBATCH_OT_delete_vgroup)
    except ValueError:
        pass
