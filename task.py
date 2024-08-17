class Task:
    pass

    def __init__(self, task_name, description, due_date, priority_level="low", completion_status=0):
        self.task_name = task_name
        self.description = description
        self.due_date = due_date
        self.priority_level = priority_level
        self.completion_status = completion_status
