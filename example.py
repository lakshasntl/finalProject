"""this is an example"""

"""
import notify module 
import OS

createNotif class:
    creates notification object for every new notification
    Notificiation object will contain date and time
    Returns a List
    
addTitle class:
    adds title to the current notifcation object

addMessage class:
    adds message to the current notifcation object
    
classify class:
    classifies each notification as a type of alert from local police department
        - 3 types(emergency, advisory, safety notice)
    
icon class:
    creates an icon for each notifcation (each icon has a different meaning)
        - icon depends on what's returned from classify class
sound class:
    adds sound to each notifcation
        - sound depends on what's returned from classify class

main function: 
    calls createNotif class to create new objects for every new notification
    calls addTitle class to title the new notifcation object
    calls addMessage class to add message to the new notification object
    calls icon Class to add iconds to each notifcation object
    calls sound Class to add sound to each notification object
    """
from datetime import datetime
class CreateNoti:
    def __init__(self, message, date = None) -> None:
        self.message = message
        self.date = date or datetime.now()
        pass


class Notification:
    def __init__(self) -> None:
        self.noti = []


    def create_notification(self,message):
       noti = CreateNoti(message)
       self.noti.append(noti)


class AddTitle:
    def __init__(self,notification,title) -> None:
        self.notification = notification
        self.title = title
    
    def add_title(self):
        self.notification.title = self.title
