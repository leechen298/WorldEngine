"""
随机工具：提供随机数生成和随机选择功能
"""

import random


class RandomTools:
    """随机工具类"""
    
    @staticmethod
    def set_seed(seed):
        """设置随机种子"""
        random.seed(seed)
    
    @staticmethod
    def random_int(min_val, max_val):
        """生成随机整数"""
        return random.randint(min_val, max_val)
    
    @staticmethod
    def random_float(min_val, max_val):
        """生成随机浮点数"""
        return random.uniform(min_val, max_val)
    
    @staticmethod
    def random_choice(choices):
        """随机选择"""
        return random.choice(choices)
    
    @staticmethod
    def random_sample(choices, k):
        """随机采样"""
        return random.sample(choices, k)

