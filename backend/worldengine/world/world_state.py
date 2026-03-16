"""
世界状态：存储和管理世界的当前状态
"""


class WorldState:
    """世界状态类"""
    
    def __init__(self, config=None):
        self.config = config or {}
        self.regions = {}
        self.entities = {}
        self.time = 0
    
    def add_region(self, region_id, region_data):
        """添加区域"""
        self.regions[region_id] = region_data
    
    def get_region(self, region_id):
        """获取区域"""
        return self.regions.get(region_id)
    
    def add_entity(self, entity_id, entity_data):
        """添加实体"""
        self.entities[entity_id] = entity_data
    
    def get_entity(self, entity_id):
        """获取实体"""
        return self.entities.get(entity_id)
    
    def update_time(self, delta):
        """更新时间"""
        self.time += delta

