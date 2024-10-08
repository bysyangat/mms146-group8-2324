import datetime

class TaskManager:
    '''
    TaskManager is an object that exhibits the behaviors of a task manager
    '''
    def __init__(self):
        self.tasks = []        # the list of tasks
    
    def add_task(self, task):
        '''
        Add a task to the list
        '''
        # the append method adds an item in a list
        self.tasks.append(task)
    
    def edit_task(self, task, detail, edit):
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
            
    def delete_task(self, task):
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
        Get the tasks that are not yet done but are past the due date
        '''
        now = datetime.datetime.now().date()  # Get today's date without time
        overdue_tasks = []

        for task in self.tasks:
            # Check if the due_date is before today and the task is not completed
            if task.due_date.date() < now and task.completion_status < 100:
                overdue_tasks.append(f"{task.task_name} (Due: {task.due_date}, Priority: {task.priority_level}, Status: {task.completion_status}%)")

        return overdue_tasks
