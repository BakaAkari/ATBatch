# ATBatch 轻量级翻译系统
import bpy
from typing import Dict, Optional

class ATBatchTranslationManager:
    """ATBatch翻译管理器 - 轻量级实现"""
    
    def __init__(self):
        self._translations = self._load_translations()
    
    def _load_translations(self) -> Dict[str, Dict[str, str]]:
        """加载翻译数据"""
        return {
            # 面板标题
            "ATBacth": {"en_US": "ATBatch", "zh": "ATBatch"},
            "UV通道": {"en_US": "UV Channels", "zh": "UV通道"},
            "顶点色": {"en_US": "Vertex Colors", "zh": "顶点色"},
            "顶点组": {"en_US": "Vertex Groups", "zh": "顶点组"},
            "形态键": {"en_US": "Shape Keys", "zh": "形态键"},
            "修改器": {"en_US": "Modifiers", "zh": "修改器"},
            "材质": {"en_US": "Materials", "zh": "材质"},
            
            # 操作按钮
            "重命名": {"en_US": "Rename", "zh": "重命名"},
            "删除": {"en_US": "Delete", "zh": "删除"},
            "设为活动": {"en_US": "Set Active", "zh": "设为活动"},
            "替换": {"en_US": "Replace", "zh": "替换"},
            "切换": {"en_US": "Toggle", "zh": "切换"},
            
            # 对话框
            "新名称": {"en_US": "New Name", "zh": "新名称"},
            "新材质": {"en_US": "New Material", "zh": "新材质"},
            
            # 状态信息
            "没有找到": {"en_US": "No", "zh": "没有找到"},
            "UV通道": {"en_US": "UV channels", "zh": "UV通道"},
            "顶点色": {"en_US": "vertex colors", "zh": "顶点色"},
            "顶点组": {"en_US": "vertex groups", "zh": "顶点组"},
            "形态键": {"en_US": "shape keys", "zh": "形态键"},
            "修改器": {"en_US": "modifiers", "zh": "修改器"},
            "材质": {"en_US": "materials", "zh": "材质"},
            
            # 操作符标签
            "批量重命名UV通道": {"en_US": "Batch Rename UV Channels", "zh": "批量重命名UV通道"},
            "批量删除UV通道": {"en_US": "Batch Delete UV Channels", "zh": "批量删除UV通道"},
            "批量设置活动UV通道": {"en_US": "Batch Set Active UV Channels", "zh": "批量设置活动UV通道"},
            "批量重命名顶点色": {"en_US": "Batch Rename Vertex Colors", "zh": "批量重命名顶点色"},
            "批量删除顶点色": {"en_US": "Batch Delete Vertex Colors", "zh": "批量删除顶点色"},
            "批量重命名顶点组": {"en_US": "Batch Rename Vertex Groups", "zh": "批量重命名顶点组"},
            "批量删除顶点组": {"en_US": "Batch Delete Vertex Groups", "zh": "批量删除顶点组"},
            "批量重命名形态键": {"en_US": "Batch Rename Shape Keys", "zh": "批量重命名形态键"},
            "批量删除形态键": {"en_US": "Batch Delete Shape Keys", "zh": "批量删除形态键"},
            "批量删除修改器": {"en_US": "Batch Delete Modifiers", "zh": "批量删除修改器"},
            "批量切换修改器启用状态": {"en_US": "Batch Toggle Modifier States", "zh": "批量切换修改器启用状态"},
            "批量重命名材质": {"en_US": "Batch Rename Materials", "zh": "批量重命名材质"},
            "批量删除材质": {"en_US": "Batch Delete Materials", "zh": "批量删除材质"},
            "批量替换材质": {"en_US": "Batch Replace Materials", "zh": "批量替换材质"},
        }
    
    def get_text(self, key: str, context: Optional[bpy.types.Context] = None) -> str:
        """获取翻译后的文本"""
        if context is None:
            context = bpy.context
        
        # 获取当前语言设置
        current_lang = context.preferences.view.language
        is_chinese = current_lang not in ["en_US"]
        
        # 从翻译字典获取文本
        if key in self._translations:
            lang_key = "zh" if is_chinese else "en_US"
            return self._translations[key].get(lang_key, key)
        
        # 如果没有找到翻译，返回原文本
        return key
    
    def add_translation(self, key: str, en_text: str, zh_text: str):
        """动态添加翻译"""
        self._translations[key] = {"en_US": en_text, "zh": zh_text}


# 全局翻译管理器实例
_translation_manager = ATBatchTranslationManager()

def get_text(key: str, context: Optional[bpy.types.Context] = None) -> str:
    """获取翻译文本的便捷函数"""
    return _translation_manager.get_text(key, context)

def add_translation(key: str, en_text: str, zh_text: str):
    """添加翻译的便捷函数"""
    _translation_manager.add_translation(key, en_text, zh_text)
