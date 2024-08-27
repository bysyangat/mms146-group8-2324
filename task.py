class Task:
    '''
    Task is an object that exhibits the characteristics and behaviors of a task
    '''
    def __init__(self, task_name, description, due_date, priority_level="low", completion_status=0):
        '''
        Initialize Task by providing the task's name, description, 
        due date, priority level, and completion status
        '''
        self.task_name = task_name                    # the name of the task to be added to the task manager
        self.description = description                # the description of the task
        self.due_date = due_date                      # the deadling of the task
        self.priority_level = priority_level          # the level of priority (low, medium, high)
        self.completion_status = completion_status    # the status of the task (% complete)

    def set_description(self, description):
        '''
        Update the description of the task
        '''
        self.description = description

    def set_priority(self, priority):
        '''
        Update the priority of the task
        '''
        self.priority_level = priority

    def set_completion_status(self, status):
        '''
        Update the completion status of the task
        '''
        self.completion_status = status
