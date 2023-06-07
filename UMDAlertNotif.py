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

import pync
import urllib.request
import bs4
from datetime import datetime, timezone
from playsound import playsound

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

class Classify():
    def __init__(self, alert):
        self.alert = alert
        
    def alertType(self):
        if 'UMD COMMUNITY ALERT' in self.alert['title']:
            return 'community alert'
        elif 'UMD ALERT Test' in self.alert['title']:
            return 'alert test'
        elif 'UMD Advisory' in self.alert['title']:
            return 'advisory'
        elif 'UMD Safety Notice' in self.alert['title']:
            return 'safety notice'
        elif 'UMD Community Notice' in self.alert['title']:
            return 'community notice'
        else:
            return 'unknown'
class TestClassify(unittest.TestCase):
    def test_alertType_community_alert(self):
        alert = {'title': 'UMD COMMUNITY ALERT', 'date': '2023-05-17', 'description': 'Community alert description'}
        classifyer = Classify(alert)
        self.assertEqual(classifyer.alertType(), 'community alert')
        
    def test_alertType_community_notice(self):
        alert = {'title': 'UMD Community Notice', 'date': '2023-05-17', 'description': 'Community notice description'}
        classifyer = Classify(alert)
        self.assertEqual(classifyer.alertType(), 'community notice')

    def test_alertType_unknown(self):
        alert = {'title': 'Unknown Alert', 'date': '2023-05-17', 'description': 'Unknown alert description'}
        classifyer = Classify(alert)
        self.assertEqual(classifyer.alertType(), 'unknown')
    

class Icon():
    def __init__(self):
        pass
        
    def iconPath(self, classification):
        if classification == 'advisory':
            icon = '/Users/lakshasenthilkumar/INST326/326finalUMDAdvisory.png'
        elif classification == 'community alert':
            icon = '/Users/lakshasenthilkumar/INST326/326finalUMDCommunityAlert.png'
        elif classification == 'alert test':
            icon = '/Users/lakshasenthilkumar/INST326/326FinalAlertTest.png'
        elif classification == "safety notice":
            icon = '/Users/lakshasenthilkumar/INST326/326finalUMDSafetyNotice.png'
        elif classification == 'community notice':
            icon = '/Users/lakshasenthilkumar/INST326/326finalUMDCommunityNotice.png'
        else:
            return None
        
        
    def test_Icon(self):
        # Test that the icon path is returned correctly
        icon = Icon()
        self.assertEqual(icon.iconPath('advisory'), '/Users/lakshasenthilkumar/INST326/326finalUMDAdvisory.png')
        
        return icon
    


class Sound():
    def __init__(self):
        self.advisory_sound = '/Users/jamalibrahim/Documents/GitHub/finalProject/Advisory.mp3'
        self.community_alert_sound = '/Users/jamalibrahim/Documents/GitHub/finalProject/CommunitySound.mp3'
        self.alert_test = '/Users/jamalibrahim/Documents/GitHub/finalProject/CommunitySound.mp3'
        self.safety_notice = '/Users/jamalibrahim/Documents/GitHub/finalProject/alertSound.mp3'
        self.community_notice = '/Users/jamalibrahim/Documents/GitHub/finalProject/CommunityNotice.mp3'
    
    def play_sound(self, sound_path):
        # Play the sound associated with the given sound path
        playsound(sound_path)

    def play_advisory_sound(self):
        self.play_sound(self.advisory_sound)

    def play_community_alert_sound(self):
        self.play_sound(self.community_alert_sound)

    def play_alert_test_sound(self):
        self.play_sound(self.alert_test)

    def play_safety_notice_sound(self):
        self.play_sound(self.safety_notice)

    def play_community_notice_sound(self):
        self.play_sound(self.community_notice)

if __name__ == "__main__":
    icon = Icon()
    sound = Sound()
    for html in get_alert_pages():
        alerts = html_to_alert_list(html)
        for alert in alerts:
            classification = Classify(alert).alertType()
            icon_path = icon.iconPath(classification)
            print(alert['title'])
            pync.notify(title=alert['title'], message=alert['description'], subtitle=alert['date'], appIcon=icon_path)
            
            if classification == 'advisory':
                sound.play_advisory_sound()
            elif classification == 'community alert':
                sound.play_community_alert_sound()
            elif classification == 'alert test':
                sound.play_alert_test_sound()
            elif classification == 'safety notice':
                sound.play_safety_notice_sound()
            elif classification == 'community notice':
                sound.play_community_notice_sound()