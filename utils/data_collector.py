import bpy


def collect_uv_maps():
    """收集所有UV通道名称和使用数量"""
    uv_data = {}
    
    for mesh in bpy.data.meshes:
        if mesh.uv_layers:
            for uv_layer in mesh.uv_layers:
                uv_name = uv_layer.name
                if uv_name not in uv_data:
                    uv_data[uv_name] = []
                
                # 找到使用这个mesh的所有对象
                for obj in bpy.data.objects:
                    if obj.data == mesh and obj.type == 'MESH':
                        uv_data[uv_name].append(obj)
    
    return uv_data


def collect_vertex_colors():
    """收集所有顶点色名称和使用数量"""
    vcol_data = {}
    
    for mesh in bpy.data.meshes:
        # Blender 2.8+ 使用 color_attributes
        if hasattr(mesh, 'color_attributes') and mesh.color_attributes:
            for color_attr in mesh.color_attributes:
                vcol_name = color_attr.name
                if vcol_name not in vcol_data:
                    vcol_data[vcol_name] = []
                
                # 找到使用这个mesh的所有对象
                for obj in bpy.data.objects:
                    if obj.data == mesh and obj.type == 'MESH':
                        vcol_data[vcol_name].append(obj)
        # Blender 2.7x 使用 vertex_colors
        elif hasattr(mesh, 'vertex_colors') and mesh.vertex_colors:
            for vcol in mesh.vertex_colors:
                vcol_name = vcol.name
                if vcol_name not in vcol_data:
                    vcol_data[vcol_name] = []
                
                # 找到使用这个mesh的所有对象
                for obj in bpy.data.objects:
                    if obj.data == mesh and obj.type == 'MESH':
                        vcol_data[vcol_name].append(obj)
    
    return vcol_data


def collect_vertex_groups():
    """收集所有顶点组名称和使用数量"""
    vgroup_data = {}
    
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and obj.vertex_groups:
            for vgroup in obj.vertex_groups:
                vgroup_name = vgroup.name
                if vgroup_name not in vgroup_data:
                    vgroup_data[vgroup_name] = []
                vgroup_data[vgroup_name].append(obj)
    
    return vgroup_data


def collect_shape_keys():
    """收集所有形态键名称和使用数量"""
    shapekey_data = {}
    
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and obj.data.shape_keys and obj.data.shape_keys.key_blocks:
            for shapekey in obj.data.shape_keys.key_blocks:
                shapekey_name = shapekey.name
                if shapekey_name not in shapekey_data:
                    shapekey_data[shapekey_name] = []
                shapekey_data[shapekey_name].append(obj)
    
    return shapekey_data


def collect_modifiers():
    """收集所有修改器类型和使用数量"""
    modifier_data = {}
    
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and obj.modifiers:
            for modifier in obj.modifiers:
                modifier_type = modifier.type
                if modifier_type not in modifier_data:
                    modifier_data[modifier_type] = []
                modifier_data[modifier_type].append(obj)
    
    return modifier_data


def collect_materials():
    """收集所有材质名称和使用数量"""
    material_data = {}
    
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and obj.data.materials:
            for material_slot in obj.data.materials:
                if material_slot:  # 检查材质槽不为空
                    material_name = material_slot.name
                    if material_name not in material_data:
                        material_data[material_name] = []
                    material_data[material_name].append(obj)
    
    return material_data
