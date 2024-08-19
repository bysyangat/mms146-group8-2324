from datetime import datetime

class Reminder(ReminderAbstract):
    def __init__(self, task):
        self.task = task
        #Calculate how much time remains until the assignment's due date.
        self.time_until_deadline = task.due_date - datetime.now()
        #Create the initial reminder message.
        self.notifications = self.generate_reminder()

    def generate_reminder(self):
        if self.time_until_deadline.days < 0:
            return f"Oh no! Task '{self.task.task_name}' is OVERDUE!"
        elif self.time_until_deadline.days == 0:
            return f"Hurry! Task '{self.task.task_name} is DUE TODAY!"
        else:
            return f"Due Soon! Task '{self.task.task_name} is due in {self.time_until_deadline.days} days."

    def display_notification(self):
        print(self.notifications)
        
            
        
  
