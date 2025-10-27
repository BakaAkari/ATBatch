import bpy
from bpy.types import Operator
from ..utils import data_collector


class ATBATCH_OT_rename_material(Operator):
    """批量重命名材质"""
    bl_idname = "atbatch.rename_material"
    bl_label = "重命名材质"
    bl_description = "批量重命名选中的材质"
    bl_options = {'REGISTER', 'UNDO'}
    
    material_name: bpy.props.StringProperty(name="材质名称")
    
    def invoke(self, context, event):
        # 弹出输入对话框
        self.new_name = self.material_name  # 设置默认值为原名称
        return context.window_manager.invoke_props_dialog(self, width=300)
    
    def draw(self, context):
        layout = self.layout
        layout.label(text=f"重命名材质: {self.material_name}")
        layout.prop(self, "new_name", text="新名称")
    
    new_name: bpy.props.StringProperty(name="新名称", default="")
    
    def execute(self, context):
        old_name = self.material_name
        new_name = self.new_name
        
        if not old_name or not new_name:
            self.report({'ERROR'}, "请输入新名称")
            return {'CANCELLED'}
        
        if old_name == new_name:
            self.report({'WARNING'}, "新名称与旧名称相同")
            return {'CANCELLED'}
        
        material_data = data_collector.collect_materials()
        if old_name not in material_data:
            self.report({'ERROR'}, f"未找到材质: {old_name}")
            return {'CANCELLED'}
        
        # 检查新名称是否已存在
        if new_name in bpy.data.materials:
            self.report({'ERROR'}, f"材质 '{new_name}' 已存在")
            return {'CANCELLED'}
        
        renamed_count = 0
        # 对所有使用该材质的对象进行操作
        for obj in material_data[old_name]:
            for i, material_slot in enumerate(obj.data.materials):
                if material_slot and material_slot.name == old_name:
                    # 重命名材质本身
                    material_slot.name = new_name
                    renamed_count += 1
                    break
        
        self.report({'INFO'}, f"已重命名 {renamed_count} 个材质: {old_name} -> {new_name}")
        return {'FINISHED'}


class ATBATCH_OT_delete_material(Operator):
    """批量删除材质"""
    bl_idname = "atbatch.delete_material"
    bl_label = "删除材质"
    bl_description = "批量删除选中的材质"
    bl_options = {'REGISTER', 'UNDO'}
    
    material_name: bpy.props.StringProperty(name="材质名称")
    
    def execute(self, context):
        material_name = self.material_name
        
        if not material_name:
            self.report({'ERROR'}, "请选择要删除的材质")
            return {'CANCELLED'}
        
        material_data = data_collector.collect_materials()
        if material_name not in material_data:
            self.report({'ERROR'}, f"未找到材质: {material_name}")
            return {'CANCELLED'}
        
        deleted_count = 0
        # 对所有使用该材质的对象进行操作
        for obj in material_data[material_name]:
            # 找到并移除材质槽
            for i in range(len(obj.data.materials) - 1, -1, -1):
                material_slot = obj.data.materials[i]
                if material_slot and material_slot.name == material_name:
                    obj.data.materials.pop(index=i)
                    deleted_count += 1
                    break
        
        # 删除材质本身（如果没有其他地方使用）
        if material_name in bpy.data.materials:
            material = bpy.data.materials[material_name]
            if material.users == 0:
                bpy.data.materials.remove(material)
        
        self.report({'INFO'}, f"已删除 {deleted_count} 个材质: {material_name}")
        return {'FINISHED'}


class ATBATCH_OT_replace_material(Operator):
    """批量替换材质"""
    bl_idname = "atbatch.replace_material"
    bl_label = "替换材质"
    bl_description = "批量替换选中的材质"
    bl_options = {'REGISTER', 'UNDO'}
    
    material_name: bpy.props.StringProperty(name="材质名称")
    
    def invoke(self, context, event):
        # 弹出输入对话框
        return context.window_manager.invoke_props_dialog(self, width=300)
    
    def draw(self, context):
        layout = self.layout
        layout.label(text=f"替换材质: {self.material_name}")
        layout.prop_search(self, "new_material", bpy.data, "materials", text="新材质")
    
    new_material: bpy.props.StringProperty(name="新材质", default="")
    
    def execute(self, context):
        old_name = self.material_name
        new_name = self.new_material
        
        if not old_name or not new_name:
            self.report({'ERROR'}, "请选择新材质")
            return {'CANCELLED'}
        
        if old_name == new_name:
            self.report({'WARNING'}, "新材质与旧材质相同")
            return {'CANCELLED'}
        
        material_data = data_collector.collect_materials()
        if old_name not in material_data:
            self.report({'ERROR'}, f"未找到材质: {old_name}")
            return {'CANCELLED'}
        
        if new_name not in bpy.data.materials:
            self.report({'ERROR'}, f"未找到新材质: {new_name}")
            return {'CANCELLED'}
        
        new_material = bpy.data.materials[new_name]
        replaced_count = 0
        
        # 对所有使用该材质的对象进行操作
        for obj in material_data[old_name]:
            for i, material_slot in enumerate(obj.data.materials):
                if material_slot and material_slot.name == old_name:
                    obj.data.materials[i] = new_material
                    replaced_count += 1
                    break
        
        self.report({'INFO'}, f"已替换 {replaced_count} 个材质: {old_name} -> {new_name}")
        return {'FINISHED'}


def register():
    """注册材质操作符"""
    try:
        bpy.utils.register_class(ATBATCH_OT_rename_material)
        bpy.utils.register_class(ATBATCH_OT_delete_material)
        bpy.utils.register_class(ATBATCH_OT_replace_material)
    except ValueError:
        pass


def unregister():
    """注销材质操作符"""
    try:
        bpy.utils.unregister_class(ATBATCH_OT_replace_material)
        bpy.utils.unregister_class(ATBATCH_OT_delete_material)
        bpy.utils.unregister_class(ATBATCH_OT_rename_material)
    except ValueError:
        pass
