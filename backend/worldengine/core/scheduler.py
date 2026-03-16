"""
调度器：负责事件调度和时间管理
"""


class Scheduler:
    """事件调度器"""
    
    def __init__(self):
        self.events = []
        self.current_time = 0
    
    def schedule(self, event, delay):
        """调度一个事件"""
        self.events.append({
            "event": event,
            "time": self.current_time + delay
        })
        self.events.sort(key=lambda x: x["time"])
    
    def process_events(self):
        """处理当前时间的所有事件"""
        while self.events and self.events[0]["time"] <= self.current_time:
            event = self.events.pop(0)
            event["event"]()
    
    def advance_time(self, delta):
        """推进时间"""
        self.current_time += delta
        self.process_events()

