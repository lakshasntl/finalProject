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
    
    print("Initializing html parser")
    # init parser
    soup = bs4.BeautifulSoup(html, 'html.parser')
    
    # to hold the alert data
    alerts = []
    
    print("Parsing all alerts...")
    # find all the divs that contain alert information
    alert_divs = soup.find_all("div", {"class": "feed-item-body"})
    
    # iterate through each div to extract the necessary information
    for alert_div in alert_divs:
        # extract the title from the div
        title = alert_div.find("h2").text.strip()
        date = alert_div.find("div", {"class": "feed-item-date"}).text.strip()
        description = alert_div.find("div", {"class": "feed-item-description"}).text.strip()
        
        # create a dictionary to hold the alert information
        alert_info = {'title': title, 'date': date, 'description': description}
        
        alerts.append(alert_info)
    
    # return the list of alerts
    return alerts


# iterate over each page of alerts and print the titles
for html in get_alert_pages():
    alerts = html_to_alert_list(html)
    for alert in alerts:
        print(alert)
        print("---------------")
