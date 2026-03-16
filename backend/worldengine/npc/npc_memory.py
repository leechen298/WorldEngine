"""
NPC 记忆：存储 NPC 的记忆信息（以后会用到，先留空壳）
"""


class NPCMemory:
    """NPC 记忆类"""
    
    def __init__(self, npc_id):
        self.npc_id = npc_id
        self.memories = []
    
    def add_memory(self, memory):
        """添加记忆"""
        # TODO: 实现记忆添加逻辑
        self.memories.append(memory)
    
    def get_memories(self, filter_func=None):
        """获取记忆"""
        # TODO: 实现记忆检索逻辑
        if filter_func:
            return [m for m in self.memories if filter_func(m)]
        return self.memories

