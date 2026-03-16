"""
基础测试：测试基本功能
"""

import pytest


def test_engine_initialization():
    """测试引擎初始化"""
    from worldengine.core import Engine
    
    engine = Engine()
    assert engine.running is False
    assert engine.world_state is None
    assert engine.scheduler is None


def test_scheduler_basic():
    """测试调度器基本功能"""
    from worldengine.core import Scheduler
    
    scheduler = Scheduler()
    assert scheduler.current_time == 0
    assert len(scheduler.events) == 0


def test_world_state():
    """测试世界状态"""
    from worldengine.world import WorldState
    
    world = WorldState()
    assert world.time == 0
    assert len(world.regions) == 0
    assert len(world.entities) == 0

