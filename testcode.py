import datetime
from task import Task
from taskmanager import TaskManager
from reminder import Reminder

task_manager = TaskManager()

task1 = Task("Critique Paper", "Assess a scientific journal", datetime.datetime(2024, 8, 20, 11, 59), "low", 80)
task2 = Task("Final Project", "Software Development", datetime.datetime(2024, 9, 1, 8), "low", 70)
task3 = Task("Final Exam", "Multiple Choice Test", datetime.datetime(2024, 9, 1, 11, 59), "high", 0)
task4 = Task("Blog 2", "End term reflection", datetime.datetime(2024, 8, 31, 11, 59), "medium", 20)

#Task Methods Test

task1.set_description("Critically assess a scientific article")
task2.set_priority("medium")
task3.set_completion_status(50)

#TaskManager Methods Test

task_manager.add_task(task1)
task_manager.add_task(task2)
task_manager.add_task(task3)
task_manager.add_task(task4)
task_manager.edit_task(task1, "due_date", datetime.datetime(2024, 8, 25, 11, 59))
task_manager.edit_task(task3, "description", "2 part multiple choice tests")
task_manager.delete_task(task1)
task_manager.sort_tasks_by_priority()
task_manager.view_tasks()

#Overdue Tasks Test

print("Overdue tasks:")
overdue_tasks = task_manager.get_overdue_tasks()
if overdue_tasks:
    for overdue_task in overdue_tasks:
        print(overdue_tasks)
else:
    print("No overdue tasks found.")

#Reminder Methods Test for each task

print("Task Reminders:")
for task in task_manager.tasks:
    reminder = Reminder(task)
    reminder.display_notification()
