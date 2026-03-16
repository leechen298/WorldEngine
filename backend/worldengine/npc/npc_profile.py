"""
NPC 档案：存储 NPC 的基本信息和属性
"""


class NPCProfile:
    """NPC 档案类"""
    
    def __init__(self, npc_id, name, attributes=None):
        self.npc_id = npc_id
        self.name = name
        self.attributes = attributes or {}
        self.location = None
        self.status = "idle"
    
    def update_attribute(self, key, value):
        """更新属性"""
        self.attributes[key] = value
    
    def get_attribute(self, key, default=None):
        """获取属性"""
        return self.attributes.get(key, default)
    
    def set_location(self, location):
        """设置位置"""
        self.location = location
    
    def set_status(self, status):
        """设置状态"""
        self.status = status

