from abc import ABC, abstractmethod

#Abstract class for reminders
class ReminderAbstract(ABC):
  #This method is implemented to generate the reminder message
  @abstractmethod 
  def generate_reminder(self):
     pass

  #This method is implemented to display notification
  @abstractmethod
  def display_notification(self):
    pass
