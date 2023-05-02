# libraries for getting/retreieving data from the Web
import urllib.request, urllib.parse, urllib.error
# library for parsing the data we get from the Web
import bs4
import json
import pandas as pd

# url we want (it's like a file path!)
course_list_url = "https://alert.umd.edu/alerts"
# make a request to the server computer, and store the response data packet in a variable
response = urllib.request.urlopen(course_list_url)

# response object behaves a bit like a file handler (remember?)
course_list_html = response.read()
course_list_html