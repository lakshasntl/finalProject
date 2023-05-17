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
    calls icon Class to add icons to each notifcation object
    calls sound Class to add sound to each notification object
    """


import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime, timezone

def get_alert_pages():
    """
    Generator that yields each page of alerts
    """
    page_num = 1
    while page_num < 4:
        url = f"https://alert.umd.edu/alerts?page={page_num}"
        response = urllib.request.urlopen(url)
        html = response.read()
        if not html:
            break
        yield html
        page_num += 1

def html_to_alert_list(html):
    """
    Get html page and parse out alert info and dump into list of alert entries
    Params:
    - html (str) - a str representation of an html page that lists alerts from UMD Alert page
    Returns: alerts: list of alert entries, which can then be printed
    """

    # init parser
    soup = BeautifulSoup(html, 'html.parser')

    # to hold the alert data
    alerts = []

    # find all the divs that contain alert information
    alert_divs = soup.find_all("div", {"class": "feed-item-body"})

    # iterate through each div to extract the necessary information
    for alert_div in alert_divs:
        # extract the title from the div
        title = alert_div.find("h2").text.strip()
        date = alert_div.find("div", {"class": "feed-item-date"}).text.strip()
        description = alert_div.find("div", {"class": "feed-item-description"}).text.strip()

        alerts.append(title)
        alerts.append(date)
        alerts.append(description)

    # return the list of alerts
    return alerts


from datetime import datetime

# Class to create notification objects for every new notification
class CreateNoti:
    def __init__(self, message, date = None) -> None:
        self.message = message
        self.date = date or datetime.now()

# Class to store the notification objects
class Notification:
    def __init__(self) -> None:
        self.noti = []


    def create_notification(self,message):
       noti = CreateNoti(message)
       self.noti.append(noti)

# Class to add a title to a notification
class AddTitle:
    def __init__(self,notification,title) -> None:
        self.notification = notification
        self.title = title
    
    def add_title(self):
        self.notification.title = self.title
        
# Class to classify notifications into different types of alerts
class Classify:
    def __init__(self, notification, emergency, advisory, safety):
        self.notification = notification
        self.emergency = emergency
        self.advisory = advisory
        self.safety = safety

        
    def alert_types(self):
        self.notification.emergency = self.emergency
        self.notification.advisory = self.advisory
        self.notification.safety = self.safety
        #Use .contain(...) an if statemenet to find, returns true or false
        return self.emergency, self.advisory, self.safety
    
# Class to add icons to notifications based on their classification
class Icon:
    def __init__(self,notification):
        self.notification = notification
        noti = Classify(notification)
        
    def add_icon(self, emergency, advisory, safety):
        if self.noti == emergency:
            return emergency
        elif self.noti == advisory:
            return advisory
        else:
            return safety
        
# Class to add sounds to notifications based on their classification
class Sound:
    def __init__(self,notification):
        self.notification = notification
        noti = Icon(notification)
        
    def add_sound(self, emergency, advisory, safety):
        if self.noti == emergency:
            return emergency
        elif self.noti == advisory:
            return advisory
        else:
            return safety
    pass

if __name__ == "__main__":
    for html in get_alert_pages():
        alerts = html_to_alert_list(html)
        for alert in alerts:
            createNotiObj = CreateNoti(alert)
            print(createNotiObj.message)
            AddTitle(alert, alert['title'])
            Classify(alert)
            Icon(alert)
            Sound(alert)
