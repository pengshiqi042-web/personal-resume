#!/usr/bin/env python3
"""
个人习惯追踪器 📊
一个有趣的习惯追踪工具，使用数据分析和可视化来帮助用户建立和维持好习惯。
使用 Numpy, File I/O, 和 Testing
"""

import json
import os
import numpy as np
from datetime import datetime, timedelta
from typing import List, Dict, Any, Tuple
import matplotlib.pyplot as plt
import random

class HabitTracker:
    def __init__(self, data_file: str = "habit_data.json"):
        self.data_file = data_file
        # Multi-dimensional data: [habit_id, name, category, target_frequency, streak_count, total_days]
        self.habits = []
        # Daily records: [date, habit_id, completed, notes, mood_score]
        self.daily_records = []
        self.load_data()
    
    def load_data(self):
        """从文件加载习惯数据 - File I/O"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.habits = data.get('habits', [])
                    self.daily_records = data.get('daily_records', [])
                print(f"📊 加载了 {len(self.habits)} 个习惯和 {len(self.daily_records)} 条记录")
            except Exception as e:
                print(f"❌ 加载数据时出错: {e}")
                self.habits = []
                self.daily_records = []
        else:
            print("📊 开始你的习惯追踪之旅！")
    
    def save_data(self):
        """保存数据到文件 - File I/O"""
        try:
            data = {
                'habits': self.habits,
                'daily_records': self.daily_records,
                'last_updated': datetime.now().isoformat()
            }
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"💾 习惯数据已保存")
        except Exception as e:
            print(f"❌ 保存数据时出错: {e}")
    
    def add_habit(self, name: str, category: str, target_frequency: int = 1):
        """添加新习惯"""
        habit_id = len(self.habits) + 1
        habit = [
            habit_id,
            name,
            category,
            target_frequency,  # 每周目标次数
            0,  # streak_count
            0   # total_days
        ]
        self.habits.append(habit)
        self.save_data()
        print(f"✅ 添加习惯: {name} ({category}) - 每周目标 {target_frequency} 次")
        return habit_id
    
    def record_habit_completion(self, habit_id: int, notes: str = "", mood_score: int = 5):
        """记录习惯完成情况"""
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        # 检查今天是否已经记录过
        today_recorded = any(
            record[0] == current_date and record[1] == habit_id 
            for record in self.daily_records
        )
        
        if today_recorded:
            print(f"⚠️ 今天已经记录过这个习惯了！")
            return
        
        # 添加记录
        record = [
            current_date,
            habit_id,
            True,  # completed
            notes,
            mood_score
        ]
        self.daily_records.append(record)
        
        # 更新习惯统计
        self._update_habit_stats(habit_id)
        
        print(f"✅ 记录完成: {self._get_habit_name(habit_id)}")
        self.save_data()
    
    def _get_habit_name(self, habit_id: int) -> str:
        """获取习惯名称"""
        for habit in self.habits:
            if habit[0] == habit_id:
                return habit[1]
        return "未知习惯"
    
    def _update_habit_stats(self, habit_id: int):
        """更新习惯统计 - 使用 Numpy 进行数据分析"""
        # 获取该习惯的所有记录
        habit_records = [record for record in self.daily_records if record[1] == habit_id]
        
        if not habit_records:
            return
        
        # 使用 Numpy 分析连续完成天数
        dates = [datetime.strptime(record[0], "%Y-%m-%d") for record in habit_records]
        dates.sort()
        
        # 计算连续天数
        streak = 1
        max_streak = 1
        
        for i in range(1, len(dates)):
            if (dates[i] - dates[i-1]).days == 1:
                streak += 1
                max_streak = max(max_streak, streak)
            else:
                streak = 1
        
        # 更新习惯数据
        for habit in self.habits:
            if habit[0] == habit_id:
                habit[4] = max_streak  # streak_count
                habit[5] = len(habit_records)  # total_days
                break
    
    def get_habit_analytics(self):
        """获取习惯分析 - 使用 Numpy 进行数据分析"""
        if not self.habits:
            print("还没有添加任何习惯！")
            return
        
        print("\n📊 习惯分析报告")
        print("=" * 50)
        
        # 使用 Numpy 分析数据
        habit_ids = [habit[0] for habit in self.habits]
        completion_rates = []
        streak_counts = []
        
        for habit_id in habit_ids:
            # 计算完成率
            total_records = len([r for r in self.daily_records if r[1] == habit_id])
            weeks = max(1, len(set(r[0] for r in self.daily_records)) // 7)
            target_completions = weeks * self._get_habit_target(habit_id)
            completion_rate = (total_records / target_completions * 100) if target_completions > 0 else 0
            completion_rates.append(completion_rate)
            
            # 获取连续天数
            streak = self._get_habit_streak(habit_id)
            streak_counts.append(streak)
        
        # 使用 Numpy 计算统计信息
        completion_array = np.array(completion_rates)
        streak_array = np.array(streak_counts)
        
        print(f"📈 整体统计:")
        print(f"   平均完成率: {np.mean(completion_array):.1f}%")
        print(f"   最高完成率: {np.max(completion_array):.1f}%")
        print(f"   平均连续天数: {np.mean(streak_array):.1f} 天")
        print(f"   最长连续天数: {np.max(streak_array)} 天")
        
        # 显示各习惯详情
        print(f"\n📋 各习惯详情:")
        for i, habit in enumerate(self.habits):
            name, category, target, streak, total = habit[1], habit[2], habit[3], habit[4], habit[5]
            completion_rate = completion_rates[i]
            
            # 根据完成率显示状态
            if completion_rate >= 80:
                status = "🟢 优秀"
            elif completion_rate >= 60:
                status = "🟡 良好"
            else:
                status = "🔴 需改进"
            
            print(f"   {status} {name} ({category})")
            print(f"      完成率: {completion_rate:.1f}% | 连续: {streak}天 | 总计: {total}次")
    
    def _get_habit_target(self, habit_id: int) -> int:
        """获取习惯目标频率"""
        for habit in self.habits:
            if habit[0] == habit_id:
                return habit[3]
        return 1
    
    def _get_habit_streak(self, habit_id: int) -> int:
        """获取习惯连续天数"""
        for habit in self.habits:
            if habit[0] == habit_id:
                return habit[4]
        return 0
    
    def generate_habit_visualization(self):
        """生成习惯可视化图表 - 使用 Numpy 和 Matplotlib"""
        if not self.habits or not self.daily_records:
            print("数据不足，无法生成图表！")
            return
        
        try:
            # 准备数据
            habit_names = [habit[1] for habit in self.habits]
            completion_counts = []
            
            for habit in self.habits:
                habit_id = habit[0]
                count = len([r for r in self.daily_records if r[1] == habit_id])
                completion_counts.append(count)
            
            # 使用 Numpy 处理数据
            counts_array = np.array(completion_counts)
            
            # 创建图表
            plt.figure(figsize=(12, 8))
            
            # 子图1: 习惯完成次数柱状图
            plt.subplot(2, 2, 1)
            bars = plt.bar(range(len(habit_names)), counts_array, color='skyblue', alpha=0.7)
            plt.title('各习惯完成次数', fontsize=14, fontweight='bold')
            plt.xlabel('习惯')
            plt.ylabel('完成次数')
            plt.xticks(range(len(habit_names)), habit_names, rotation=45)
            
            # 在柱子上添加数值
            for bar, count in zip(bars, counts_array):
                plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                        str(int(count)), ha='center', va='bottom')
            
            # 子图2: 完成率饼图
            plt.subplot(2, 2, 2)
            total_completions = np.sum(counts_array)
            if total_completions > 0:
                percentages = (counts_array / total_completions) * 100
                colors = plt.cm.Set3(np.linspace(0, 1, len(habit_names)))
                plt.pie(percentages, labels=habit_names, autopct='%1.1f%%', colors=colors)
                plt.title('习惯完成分布', fontsize=14, fontweight='bold')
            
            # 子图3: 连续天数
            plt.subplot(2, 2, 3)
            streak_counts = [habit[4] for habit in self.habits]
            streak_array = np.array(streak_counts)
            bars = plt.bar(range(len(habit_names)), streak_array, color='lightgreen', alpha=0.7)
            plt.title('各习惯连续天数', fontsize=14, fontweight='bold')
            plt.xlabel('习惯')
            plt.ylabel('连续天数')
            plt.xticks(range(len(habit_names)), habit_names, rotation=45)
            
            for bar, streak in zip(bars, streak_array):
                plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                        str(int(streak)), ha='center', va='bottom')
            
            # 子图4: 时间趋势（最近30天）
            plt.subplot(2, 2, 4)
            self._plot_daily_trends()
            
            plt.tight_layout()
            plt.savefig('habit_analysis.png', dpi=300, bbox_inches='tight')
            print("📊 习惯分析图表已保存为 'habit_analysis.png'")
            
        except ImportError:
            print("❌ 需要安装 matplotlib: pip install matplotlib")
        except Exception as e:
            print(f"❌ 生成图表时出错: {e}")
    
    def _plot_daily_trends(self):
        """绘制每日趋势图"""
        # 获取最近30天的数据
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
        
        # 创建日期范围
        date_range = []
        current_date = start_date
        while current_date <= end_date:
            date_range.append(current_date.strftime("%Y-%m-%d"))
            current_date += timedelta(days=1)
        
        # 统计每日完成次数
        daily_counts = []
        for date in date_range:
            count = len([r for r in self.daily_records if r[0] == date])
            daily_counts.append(count)
        
        # 绘制趋势线
        plt.plot(range(len(date_range)), daily_counts, marker='o', linewidth=2, markersize=4)
        plt.title('最近30天完成趋势', fontsize=14, fontweight='bold')
        plt.xlabel('日期')
        plt.ylabel('每日完成次数')
        plt.xticks(range(0, len(date_range), 5), 
                  [date_range[i] for i in range(0, len(date_range), 5)], 
                  rotation=45)
        plt.grid(True, alpha=0.3)
    
    def export_habit_report(self, filename: str = None):
        """导出习惯报告 - File I/O"""
        if filename is None:
            filename = f"habit_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("📊 个人习惯追踪报告\n")
                f.write("=" * 50 + "\n")
                f.write(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                f.write(f"习惯总数: {len(self.habits)}\n")
                f.write(f"记录总数: {len(self.daily_records)}\n\n")
                
                f.write("习惯列表:\n")
                f.write("-" * 30 + "\n")
                
                for habit in self.habits:
                    f.write(f"ID: {habit[0]} | {habit[1]} ({habit[2]})\n")
                    f.write(f"   目标频率: 每周 {habit[3]} 次\n")
                    f.write(f"   连续天数: {habit[4]} 天\n")
                    f.write(f"   总完成次数: {habit[5]} 次\n\n")
                
                f.write("最近记录:\n")
                f.write("-" * 30 + "\n")
                
                recent_records = self.daily_records[-20:]  # 最近20条记录
                for record in recent_records:
                    habit_name = self._get_habit_name(record[1])
                    f.write(f"{record[0]} | {habit_name} | 心情: {record[4]}/10 | {record[3]}\n")
            
            print(f"📄 习惯报告已导出到 {filename}")
        except Exception as e:
            print(f"❌ 导出报告时出错: {e}")

def main():
    """主函数 - Flow Control 菜单系统"""
    tracker = HabitTracker()
    
    while True:
        print("\n" + "="*50)
        print("📊 个人习惯追踪器")
        print("="*50)
        print("1. 添加新习惯")
        print("2. 记录习惯完成")
        print("3. 查看习惯分析")
        print("4. 生成可视化图表")
        print("5. 导出习惯报告")
        print("6. 退出")
        print("-"*50)
        
        choice = input("请选择操作 (1-6): ").strip()
        
        # Flow Control: 处理用户选择
        if choice == '1':
            name = input("习惯名称: ").strip()
            category = input("习惯类别 (如: 健康, 学习, 工作): ").strip()
            try:
                frequency = int(input("每周目标次数 (默认1): ").strip() or "1")
                tracker.add_habit(name, category, frequency)
            except ValueError:
                print("❌ 请输入有效数字")
        
        elif choice == '2':
            if not tracker.habits:
                print("❌ 还没有添加任何习惯！")
                continue
            
            print("\n当前习惯列表:")
            for habit in tracker.habits:
                print(f"ID: {habit[0]} - {habit[1]} ({habit[2]})")
            
            try:
                habit_id = int(input("请输入习惯ID: "))
                notes = input("完成备注 (可选): ").strip()
                mood = int(input("心情评分 (1-10, 默认5): ").strip() or "5")
                tracker.record_habit_completion(habit_id, notes, mood)
            except ValueError:
                print("❌ 请输入有效的数字")
        
        elif choice == '3':
            tracker.get_habit_analytics()
        
        elif choice == '4':
            tracker.generate_habit_visualization()
        
        elif choice == '5':
            filename = input("导出文件名 (按回车自动生成): ").strip()
            if not filename:
                filename = None
            tracker.export_habit_report(filename)
        
        elif choice == '6':
            print("👋 再见！你的习惯数据已保存。")
            break
        
        else:
            print("❌ 无效选择，请输入 1-6")

if __name__ == "__main__":
    main()

