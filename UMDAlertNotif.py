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

import urllib.request
import bs4
from datetime import datetime, timezone

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


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
    
    #print("Initializing html parser")
    # init parser
    soup = bs4.BeautifulSoup(html, 'html.parser')
    
    # to hold the alert data
    alerts = []
    
    #print("Parsing all alerts...")
    # find all the divs that contain alert information
    alert_divs = soup.find_all("div", {"class": "feed-item-body"})
    
    
    # iterate through each div to extract the necessary information
    for alert_div in alert_divs:
        # extract the title from the div
        title = alert_div.find("h2").text.strip()
        date = alert_div.find("div", {"class": "feed-item-date"}).text.strip()
        
        description = alert_div.find("div", {"class": "feed-item-description"})
        
        local = {'title': title, 'date': date, 'description': description}
        
        alerts.append(local)
    # return the list of alerts
    return alerts

from datetime import datetime

class CreateNoti:
    def __init__(self, message, date = None) -> None:
        self.message = message
        self.date = date or datetime.now()


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
        
class classify:
    def __init__(self, notification):
        self.notification = notification
        #self.emergency = emergency
        #self.advisory = advisory
        #self.safety = safety
        
    def alert_types(self, notification):
        self.notification.emergency = self.emergency
        self.notification.advisory = self.advisory
        self.notification.safety = self.safety

class icon:
    def __init__(self,notification):
        self.notification = notification
        noti = classify(notification)
        
    def add_icon(self, emergency, advisory, safety):
        if self.noti == emergency:
            return emergency
        elif self.noti == advisory:
            return advisory
        else:
            return safety

class sound:
    def __init__(self,notification):
        self.notification = notification
        noti = icon(notification)
        
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
            AddTitle(alert, alert['title'])
            classify(alert)
            icon(alert)
            sound(alert)
            