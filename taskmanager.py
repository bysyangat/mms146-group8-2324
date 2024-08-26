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
        # allows the user to edit a specific task attribute based on input 
        if detail == "task_name":
            task.task_name = edit
        if detail == "description":
            task.set_description(edit)
        if detail == "due_date":
            task.due_date = edit
        if detail == "priority_level":
            task.set_priority(edit)
        if detail == "completion_status":
            task.set_completion_status(edit)
        
        else: print("Please enter a task attribute.")
            
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
