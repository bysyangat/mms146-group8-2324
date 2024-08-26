from datetime import datetime

class Reminder:
    def __init__(self, task):
        self.task = task
        self.notifications = self.generate_reminder()

    def generate_reminder(self):
        """
        Generate a reminder message based on the task's due date.
        """
        now = datetime.now().date()  # Get today's date without time
        due_date = self.task.due_date.date()  # Get the task's due date without time

        if due_date < now:
            return f"Oh no! Task '{self.task.task_name}' is OVERDUE!"
        elif due_date == now:
            return f"Hurry! Task '{self.task.task_name}' is DUE TODAY!"
        else:
            days_remaining = (due_date - now).days  # Calculate the days remaining
            return f"Due Soon! Task '{self.task.task_name}' is due in {days_remaining} days."

    def display_notification(self):
        """
        Display the reminder notification to the user.
        """
        print(self.notifications)
