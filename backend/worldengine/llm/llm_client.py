"""
LLM 客户端：与本地/云端模型交互的封装
"""


class LLMClient:
    """LLM 客户端类"""
    
    def __init__(self, model_name=None, api_key=None):
        self.model_name = model_name
        self.api_key = api_key
        # TODO: 初始化 LLM 客户端
    
    def generate(self, prompt, **kwargs):
        """生成文本"""
        # TODO: 实现 LLM 调用逻辑
        return ""
    
    def chat(self, messages, **kwargs):
        """对话"""
        # TODO: 实现对话逻辑
        return ""

