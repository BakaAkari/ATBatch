import bpy
from bpy.types import Panel
from ..utils import data_collector


class VIEW3D_PT_atbatch(Panel):
    """ATBatch主面板"""
    bl_label = "ATB 批量操作"
    bl_idname = "VIEW3D_PT_atbatch"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "ATB"
    
    def draw(self, context):
        layout = self.layout
        layout.label(text="批量操作工具")


class VIEW3D_PT_atbatch_uv(Panel):
    """UV通道子面板"""
    bl_label = "UV通道"
    bl_idname = "VIEW3D_PT_atbatch_uv"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "ATB"
    bl_parent_id = "VIEW3D_PT_atbatch"
    
    def draw(self, context):
        layout = self.layout
        props = context.window_manager.atbatch_props
        
        # 收集UV数据并更新列表
        uv_data = data_collector.collect_uv_maps()
        
        # 清空并重新填充UV列表
        props.uv_items.clear()
        for uv_name, objects in uv_data.items():
            item = props.uv_items.add()
            item.name = uv_name
            item.object_count = len(objects)
        
        if not props.uv_items:
            layout.label(text="没有找到UV通道")
            return
        
        # 使用template_list显示UV通道列表
        layout.template_list("ATBATCH_UL_uv_list", "", props, "uv_items", props, "uv_index")
        
        # 操作按钮行
        if props.uv_items and props.uv_index < len(props.uv_items):
            selected_uv = props.uv_items[props.uv_index]
            row = layout.row()
            row.scale_x = 0.8
            
            # 重命名按钮
            rename_op = row.operator("atbatch.rename_uv", text="重命名")
            rename_op.uv_name = selected_uv.name
            
            # 删除按钮
            delete_op = row.operator("atbatch.delete_uv", text="删除")
            delete_op.uv_name = selected_uv.name
            
            # 设为活动按钮
            active_op = row.operator("atbatch.set_active_uv", text="活动")
            active_op.uv_name = selected_uv.name


class VIEW3D_PT_atbatch_vcol(Panel):
    """顶点色子面板"""
    bl_label = "顶点色"
    bl_idname = "VIEW3D_PT_atbatch_vcol"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "ATB"
    bl_parent_id = "VIEW3D_PT_atbatch"
    
    def draw(self, context):
        layout = self.layout
        props = context.window_manager.atbatch_props
        
        # 收集顶点色数据并更新列表
        vcol_data = data_collector.collect_vertex_colors()
        
        # 清空并重新填充顶点色列表
        props.vcol_items.clear()
        for vcol_name, objects in vcol_data.items():
            item = props.vcol_items.add()
            item.name = vcol_name
            item.object_count = len(objects)
        
        if not props.vcol_items:
            layout.label(text="没有找到顶点色")
            return
        
        # 使用template_list显示顶点色列表
        layout.template_list("ATBATCH_UL_vcol_list", "", props, "vcol_items", props, "vcol_index")
        
        # 操作按钮行
        if props.vcol_items and props.vcol_index < len(props.vcol_items):
            selected_vcol = props.vcol_items[props.vcol_index]
            row = layout.row()
            row.scale_x = 0.8
            
            # 重命名按钮
            rename_op = row.operator("atbatch.rename_vcol", text="重命名")
            rename_op.vcol_name = selected_vcol.name
            
            # 删除按钮
            delete_op = row.operator("atbatch.delete_vcol", text="删除")
            delete_op.vcol_name = selected_vcol.name


class VIEW3D_PT_atbatch_vgroup(Panel):
    """顶点组子面板"""
    bl_label = "顶点组"
    bl_idname = "VIEW3D_PT_atbatch_vgroup"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "ATB"
    bl_parent_id = "VIEW3D_PT_atbatch"
    
    def draw(self, context):
        layout = self.layout
        props = context.window_manager.atbatch_props
        
        # 收集顶点组数据并更新列表
        vgroup_data = data_collector.collect_vertex_groups()
        
        # 清空并重新填充顶点组列表
        props.vgroup_items.clear()
        for vgroup_name, objects in vgroup_data.items():
            item = props.vgroup_items.add()
            item.name = vgroup_name
            item.object_count = len(objects)
        
        if not props.vgroup_items:
            layout.label(text="没有找到顶点组")
            return
        
        # 使用template_list显示顶点组列表
        layout.template_list("ATBATCH_UL_vgroup_list", "", props, "vgroup_items", props, "vgroup_index")
        
        # 操作按钮行
        if props.vgroup_items and props.vgroup_index < len(props.vgroup_items):
            selected_vgroup = props.vgroup_items[props.vgroup_index]
            row = layout.row()
            row.scale_x = 0.8
            
            # 重命名按钮
            rename_op = row.operator("atbatch.rename_vgroup", text="重命名")
            rename_op.vgroup_name = selected_vgroup.name
            
            # 删除按钮
            delete_op = row.operator("atbatch.delete_vgroup", text="删除")
            delete_op.vgroup_name = selected_vgroup.name


class VIEW3D_PT_atbatch_shapekey(Panel):
    """形态键子面板"""
    bl_label = "形态键"
    bl_idname = "VIEW3D_PT_atbatch_shapekey"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "ATB"
    bl_parent_id = "VIEW3D_PT_atbatch"
    
    def draw(self, context):
        layout = self.layout
        props = context.window_manager.atbatch_props
        
        # 收集形态键数据并更新列表
        shapekey_data = data_collector.collect_shape_keys()
        
        # 清空并重新填充形态键列表
        props.shapekey_items.clear()
        for shapekey_name, objects in shapekey_data.items():
            item = props.shapekey_items.add()
            item.name = shapekey_name
            item.object_count = len(objects)
        
        if not props.shapekey_items:
            layout.label(text="没有找到形态键")
            return
        
        # 使用template_list显示形态键列表
        layout.template_list("ATBATCH_UL_shapekey_list", "", props, "shapekey_items", props, "shapekey_index")
        
        # 操作按钮行
        if props.shapekey_items and props.shapekey_index < len(props.shapekey_items):
            selected_shapekey = props.shapekey_items[props.shapekey_index]
            row = layout.row()
            row.scale_x = 0.8
            
            # 重命名按钮
            rename_op = row.operator("atbatch.rename_shapekey", text="重命名")
            rename_op.shapekey_name = selected_shapekey.name
            
            # 删除按钮
            delete_op = row.operator("atbatch.delete_shapekey", text="删除")
            delete_op.shapekey_name = selected_shapekey.name


class VIEW3D_PT_atbatch_modifier(Panel):
    """修改器子面板"""
    bl_label = "修改器"
    bl_idname = "VIEW3D_PT_atbatch_modifier"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "ATB"
    bl_parent_id = "VIEW3D_PT_atbatch"
    
    def draw(self, context):
        layout = self.layout
        props = context.window_manager.atbatch_props
        
        # 收集修改器数据并更新列表
        modifier_data = data_collector.collect_modifiers()
        
        # 清空并重新填充修改器列表
        props.modifier_items.clear()
        for modifier_type, objects in modifier_data.items():
            item = props.modifier_items.add()
            item.name = modifier_type
            item.object_count = len(objects)
        
        if not props.modifier_items:
            layout.label(text="没有找到修改器")
            return
        
        # 使用template_list显示修改器列表
        layout.template_list("ATBATCH_UL_modifier_list", "", props, "modifier_items", props, "modifier_index")
        
        # 操作按钮行
        if props.modifier_items and props.modifier_index < len(props.modifier_items):
            selected_modifier = props.modifier_items[props.modifier_index]
            row = layout.row()
            row.scale_x = 0.8
            
            # 删除按钮
            delete_op = row.operator("atbatch.delete_modifier", text="删除")
            delete_op.modifier_type = selected_modifier.name
            
            # 切换状态按钮
            toggle_op = row.operator("atbatch.toggle_modifier", text="切换")
            toggle_op.modifier_type = selected_modifier.name


class VIEW3D_PT_atbatch_material(Panel):
    """材质子面板"""
    bl_label = "材质"
    bl_idname = "VIEW3D_PT_atbatch_material"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "ATB"
    bl_parent_id = "VIEW3D_PT_atbatch"
    
    def draw(self, context):
        layout = self.layout
        props = context.window_manager.atbatch_props
        
        # 收集材质数据并更新列表
        material_data = data_collector.collect_materials()
        
        # 清空并重新填充材质列表
        props.material_items.clear()
        for material_name, objects in material_data.items():
            item = props.material_items.add()
            item.name = material_name
            item.object_count = len(objects)
        
        if not props.material_items:
            layout.label(text="没有找到材质")
            return
        
        # 使用template_list显示材质列表
        layout.template_list("ATBATCH_UL_material_list", "", props, "material_items", props, "material_index")
        
        # 操作按钮行
        if props.material_items and props.material_index < len(props.material_items):
            selected_material = props.material_items[props.material_index]
            row = layout.row()
            row.scale_x = 0.8
            
            # 重命名按钮
            rename_op = row.operator("atbatch.rename_material", text="重命名")
            rename_op.material_name = selected_material.name
            
            # 删除按钮
            delete_op = row.operator("atbatch.delete_material", text="删除")
            delete_op.material_name = selected_material.name
            
            # 替换按钮
            replace_op = row.operator("atbatch.replace_material", text="替换")
            replace_op.material_name = selected_material.name


def register():
    """注册所有面板"""
    try:
        bpy.utils.register_class(VIEW3D_PT_atbatch)
        bpy.utils.register_class(VIEW3D_PT_atbatch_uv)
        bpy.utils.register_class(VIEW3D_PT_atbatch_vcol)
        bpy.utils.register_class(VIEW3D_PT_atbatch_vgroup)
        bpy.utils.register_class(VIEW3D_PT_atbatch_shapekey)
        bpy.utils.register_class(VIEW3D_PT_atbatch_modifier)
        bpy.utils.register_class(VIEW3D_PT_atbatch_material)
    except ValueError:
        pass


def unregister():
    """注销所有面板"""
    try:
        bpy.utils.unregister_class(VIEW3D_PT_atbatch_material)
        bpy.utils.unregister_class(VIEW3D_PT_atbatch_modifier)
        bpy.utils.unregister_class(VIEW3D_PT_atbatch_shapekey)
        bpy.utils.unregister_class(VIEW3D_PT_atbatch_vgroup)
        bpy.utils.unregister_class(VIEW3D_PT_atbatch_vcol)
        bpy.utils.unregister_class(VIEW3D_PT_atbatch_uv)
        bpy.utils.unregister_class(VIEW3D_PT_atbatch)
    except ValueError:
        pass
