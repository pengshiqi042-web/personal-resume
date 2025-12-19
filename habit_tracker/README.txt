HABIT TRACKER - Final Project

1.DESCRIPTION:

A comprehensive habit tracking application that helps users build and maintain 
daily habits. The program allows users to add habits, log daily completions 
with mood tracking, calculate streaks, unlock achievements, and analyze habit 
patterns using multi-dimensional data structures.

2.ADVANCED TOPICS USED:

2.1 FILE I/O (Week 9):
   - Reading and writing JSON files (habits.json, records.json)
   - Appending to text files (achievements.txt)
   - Data persistence across program sessions
   - Error handling for file operations

2.2 MULTI-DIMENSIONAL LISTS (Week 12):
   - Building 2D matrices for habit-date analysis
   - Matrix structure: rows represent dates, columns represent habits
   - Analyzing patterns across multiple dimensions
   - Calculating completion rates, consistency scores, and productivity metrics

3.HOW TO RUN:

3.1 Ensure Python 3.x is installed
3.2 Place all files in the same directory:
   - habit_tracker.py
   - habits.json
   - records.json
   - achievements.txt
3.3 Run: python habit_tracker.py
3.4 Follow the menu prompts

4. DEPENDENCIES:

- No external libraries required (only built-in Python modules)
- Uses: json, os, datetime

5.FEATURES:

- Add and view habits with resistance/confidence levels
- Log daily habit completions with mood tracking
- Calculate and display current streaks
- Unlock achievements (7-day, 30-day streaks)
- Multi-dimensional analysis of habit patterns
- Data persistence across sessions

6.PROJECT MOTIVATION:

I chose this project because building good habits is essential for personal growth,
and I wanted to create a tool that not only tracks habits but also provides insights
into behavior patterns through data analysis.
