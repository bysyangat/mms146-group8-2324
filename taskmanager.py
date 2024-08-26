import datetime
from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        '''
        Add a task to the list
        '''
        # the append method adds an item in a list
        self.tasks.append(task)
    
    def edit_task(self, item, edited_task):
        '''
        Edit a task
        '''
        # checks if the input for 'item' is an integer
        if item.isdigit(item):
            # this updates a specific item in a list
            self.tasks[item] = edited_task
        # shows the user that 'item' input is not an integer
        else: print("Please enter a number for item.")
            
    def delete_task(self, item):
        '''
        Delete a task from the list
        '''
        self.tasks.remove(task)

    def view_tasks(self):
        '''
        View all tasks
        '''
        for idx, task in enumerate(self.tasks):
            print(f"Task {idx}: {task.task_name}, Description: {task.description}, Due Date: {task.due_date}, Priority: {task.priority_level}, Status: {task.completion_status}%")
    
    def sort_tasks_by_priority(self):
        '''
        Sort tasks by priority level (low, medium, high)
        '''
        priority_map = {"low": 1, "medium": 2, "high": 3}
        self.tasks.sort(key=lambda task: priority_map[task.priority_level])
        print("Tasks sorted by priority.")

    def get_overdue_tasks(self):
        '''
        Show tasks that are overdue
        '''
        now = datetime.datetime.now()
        overdue_tasks = []
    
        for task in self.tasks:
            if task.due_date < now and task.completion_status < 100:
                overdue_tasks.append(task)
                
        return overdue_tasks
