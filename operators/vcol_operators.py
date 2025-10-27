import bpy
from bpy.types import Operator
from ..utils import data_collector


class ATBATCH_OT_rename_vcol(Operator):
    """批量重命名顶点色"""
    bl_idname = "atbatch.rename_vcol"
    bl_label = "重命名顶点色"
    bl_description = "批量重命名选中的顶点色"
    bl_options = {'REGISTER', 'UNDO'}
    
    vcol_name: bpy.props.StringProperty(name="顶点色名称")
    
    def invoke(self, context, event):
        # 弹出输入对话框
        self.new_name = self.vcol_name  # 设置默认值为原名称
        return context.window_manager.invoke_props_dialog(self, width=300)
    
    def draw(self, context):
        layout = self.layout
        layout.label(text=f"重命名顶点色: {self.vcol_name}")
        layout.prop(self, "new_name", text="新名称")
    
    new_name: bpy.props.StringProperty(name="新名称", default="")
    
    def execute(self, context):
        old_name = self.vcol_name
        new_name = self.new_name
        
        if not old_name or not new_name:
            self.report({'ERROR'}, "请输入新名称")
            return {'CANCELLED'}
        
        if old_name == new_name:
            self.report({'WARNING'}, "新名称与旧名称相同")
            return {'CANCELLED'}
        
        vcol_data = data_collector.collect_vertex_colors()
        if old_name not in vcol_data:
            self.report({'ERROR'}, f"未找到顶点色: {old_name}")
            return {'CANCELLED'}
        
        renamed_count = 0
        # 对所有使用该顶点色的对象进行操作
        for obj in vcol_data[old_name]:
            mesh = obj.data
            # Blender 2.8+ 使用 color_attributes
            if hasattr(mesh, 'color_attributes') and mesh.color_attributes:
                for color_attr in mesh.color_attributes:
                    if color_attr.name == old_name:
                        color_attr.name = new_name
                        renamed_count += 1
                        break
            # Blender 2.7x 使用 vertex_colors
            elif hasattr(mesh, 'vertex_colors') and mesh.vertex_colors:
                for vcol in mesh.vertex_colors:
                    if vcol.name == old_name:
                        vcol.name = new_name
                        renamed_count += 1
                        break
        
        self.report({'INFO'}, f"已重命名 {renamed_count} 个顶点色: {old_name} -> {new_name}")
        return {'FINISHED'}


class ATBATCH_OT_delete_vcol(Operator):
    """批量删除顶点色"""
    bl_idname = "atbatch.delete_vcol"
    bl_label = "删除顶点色"
    bl_description = "批量删除选中的顶点色"
    bl_options = {'REGISTER', 'UNDO'}
    
    vcol_name: bpy.props.StringProperty(name="顶点色名称")
    
    def execute(self, context):
        vcol_name = self.vcol_name
        
        if not vcol_name:
            self.report({'ERROR'}, "请选择要删除的顶点色")
            return {'CANCELLED'}
        
        vcol_data = data_collector.collect_vertex_colors()
        if vcol_name not in vcol_data:
            self.report({'ERROR'}, f"未找到顶点色: {vcol_name}")
            return {'CANCELLED'}
        
        deleted_count = 0
        # 对所有使用该顶点色的对象进行操作
        for obj in vcol_data[vcol_name]:
            mesh = obj.data
            # Blender 2.8+ 使用 color_attributes
            if hasattr(mesh, 'color_attributes') and mesh.color_attributes:
                color_attr_to_remove = None
                for color_attr in mesh.color_attributes:
                    if color_attr.name == vcol_name:
                        color_attr_to_remove = color_attr
                        break
                if color_attr_to_remove:
                    mesh.color_attributes.remove(color_attr_to_remove)
                    deleted_count += 1
            # Blender 2.7x 使用 vertex_colors
            elif hasattr(mesh, 'vertex_colors') and mesh.vertex_colors:
                vcol_to_remove = None
                for vcol in mesh.vertex_colors:
                    if vcol.name == vcol_name:
                        vcol_to_remove = vcol
                        break
                if vcol_to_remove:
                    mesh.vertex_colors.remove(vcol_to_remove)
                    deleted_count += 1
        
        self.report({'INFO'}, f"已删除 {deleted_count} 个顶点色: {vcol_name}")
        return {'FINISHED'}


def register():
    """注册顶点色操作符"""
    try:
        bpy.utils.register_class(ATBATCH_OT_rename_vcol)
        bpy.utils.register_class(ATBATCH_OT_delete_vcol)
    except ValueError:
        pass


def unregister():
    """注销顶点色操作符"""
    try:
        bpy.utils.unregister_class(ATBATCH_OT_rename_vcol)
        bpy.utils.unregister_class(ATBATCH_OT_delete_vcol)
    except ValueError:
        pass
