#!/usr/bin/env python3
"""
习惯追踪器测试文件
展示 Testing 功能的使用
"""

import unittest
import os
import tempfile
from habit_tracker import HabitTracker

class TestHabitTracker(unittest.TestCase):
    def setUp(self):
        """测试前准备"""
        # 创建临时文件用于测试
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.temp_file.close()
        self.tracker = HabitTracker(self.temp_file.name)
    
    def tearDown(self):
        """测试后清理"""
        # 删除临时文件
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    def test_add_habit(self):
        """测试添加习惯"""
        habit_id = self.tracker.add_habit("跑步", "健康", 3)
        self.assertEqual(len(self.tracker.habits), 1)
        self.assertEqual(self.tracker.habits[0][1], "跑步")
        self.assertEqual(self.tracker.habits[0][2], "健康")
        self.assertEqual(self.tracker.habits[0][3], 3)
    
    def test_record_completion(self):
        """测试记录习惯完成"""
        # 先添加一个习惯
        habit_id = self.tracker.add_habit("阅读", "学习", 5)
        
        # 记录完成
        self.tracker.record_habit_completion(habit_id, "读了30分钟", 8)
        
        # 检查记录
        self.assertEqual(len(self.tracker.daily_records), 1)
        self.assertTrue(self.tracker.daily_records[0][2])  # completed
        self.assertEqual(self.tracker.daily_records[0][3], "读了30分钟")
        self.assertEqual(self.tracker.daily_records[0][4], 8)
    
    def test_habit_stats(self):
        """测试习惯统计"""
        # 添加多个习惯
        self.tracker.add_habit("运动", "健康", 3)
        self.tracker.add_habit("学习", "教育", 5)
        
        # 记录一些完成情况
        self.tracker.record_habit_completion(1, "跑步30分钟", 9)
        self.tracker.record_habit_completion(2, "看书1小时", 7)
        
        # 检查统计
        self.assertEqual(len(self.tracker.habits), 2)
        self.assertEqual(len(self.tracker.daily_records), 2)
    
    def test_data_persistence(self):
        """测试数据持久化"""
        # 添加数据
        self.tracker.add_habit("冥想", "心理健康", 1)
        self.tracker.record_habit_completion(1, "冥想10分钟", 6)
        
        # 创建新的tracker实例来测试数据加载
        new_tracker = HabitTracker(self.temp_file.name)
        
        # 验证数据被正确加载
        self.assertEqual(len(new_tracker.habits), 1)
        self.assertEqual(len(new_tracker.daily_records), 1)
        self.assertEqual(new_tracker.habits[0][1], "冥想")

def run_tests():
    """运行测试"""
    print("🧪 开始运行习惯追踪器测试...")
    
    # 创建测试套件
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHabitTracker)
    
    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # 显示结果
    print(f"\n📊 测试结果:")
    print(f"   运行测试: {result.testsRun}")
    print(f"   失败: {len(result.failures)}")
    print(f"   错误: {len(result.errors)}")
    
    if result.failures:
        print("\n❌ 失败的测试:")
        for test, traceback in result.failures:
            print(f"   {test}: {traceback}")
    
    if result.errors:
        print("\n❌ 错误的测试:")
        for test, traceback in result.errors:
            print(f"   {test}: {traceback}")
    
    if result.wasSuccessful():
        print("\n✅ 所有测试通过！")
    else:
        print(f"\n❌ 有 {len(result.failures + result.errors)} 个测试失败")
    
    return result.wasSuccessful()

if __name__ == "__main__":
    run_tests()

