"""
配置模式：定义世界配置的数据结构
"""


class ConfigSchema:
    """配置模式类"""
    
    @staticmethod
    def validate(config):
        """验证配置是否符合模式"""
        # TODO: 实现配置验证逻辑
        return True
    
    @staticmethod
    def get_default_config():
        """获取默认配置"""
        return {
            "world_name": "Default World",
            "seed": None,
            "size": {
                "width": 100,
                "height": 100
            }
        }

