# libraries for getting/retreieving data from the Web
import urllib.request, urllib.parse, urllib.error
# library for parsing the data we get from the Web
import bs4
import json
import pandas as pd

# url we want (it's like a file path!)
alert_list_url = "https://alert.umd.edu/alerts"

# make a request to the server computer, and store the response data packet in a variable
response = urllib.request.urlopen(alert_list_url)
alert_list_html = response.read()
alert_list_html

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
        
    # return the list of alerts
    return alerts

alert_list = html_to_alert_list(alert_list_html)