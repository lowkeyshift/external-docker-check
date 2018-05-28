import requests
import os
import urllib

from hashlib import md5
from time import time
from time import sleep
from datadog import initialize, api

# Variables
NAME = os.getenv('NAME')
NAME_1 = os.getenv('NAME_1')
NAME_2 = os.getenv('NAME_2')
NAME_3 = os.getenv('NAME_3')
NAME_4 = os.getenv('NAME_4')
NAME_5 = os.getenv('NAME_5')
NAME_BROKEN_6 = os.getenv('NAME_BROKEN_6')

URL = os.getenv('URL')
URL_PAGE_1 = os.getenv('URL_PAGE_1')
URL_PAGE_2 = os.getenv('URL_PAGE_2')
URL_PAGE_3 = os.getenv('URL_PAGE_3')
URL_PAGE_4 = os.getenv('URL_PAGE_4')
URL_5 = os.getenv('URL_5')
URL_BROKEN_6 = os.getenv('URL_BROKEN_6')

url_list = [URL, URL_PAGE_1, URL_PAGE_2, URL_PAGE_3, URL_PAGE_4, URL_5, URL_BROKEN_6]
default_timeout = 5
now = time()
timeout = float(default_timeout)

API_KEY = os.getenv('API_KEY')
APP_KEY = os.getenv('APP_KEY')

testAI = "dc375d356a9d7ee347a65fa0d2afe02a"
testAP = "9006927ceb4d75c4f741558ddfe46e1ccb4c6b25"

options = {
    'api_key': API_KEY,
    'app_key': APP_KEY
}

initialize(**options)

def error_event(url, http_error):
    tag_entry = "url:{}".format(url)
    tag_entry_2= "{}:{}".format(NAME,http_error)
    timestamp = int(time())
    title = "URL HTTPError"
    alert_type = "error"
    text = "{} has a {} at {}.".format(url,http_error,timestamp)
    tags = [tag_entry, tag_entry_2]
    api.Event.create(title=title, text=text, tags=tags, alert_type=alert_type)


def timeout_event(url, timeout):
    tag_entry = "url:{}".format(url)
    tag_entry_2= "timeout:{}".format(timeout)
    timestamp = int(time())
    title = "URL Timeout"
    alert_type = "error"
    text = "{} timed out after {} seconds.".format(url,timestamp)
    tags = [tag_entry, tag_entry_2]
    api.Event.create(title=title, text=text, tags=tags, alert_type=alert_type)

def status_code_event(url, r):
    tag_entry = "url:{}".format(url)
    tag_entry_2= "timeout:{}".format(timeout)
    timestamp = int(time())
    title = "Invalid response code for {}".format(url)
    alert_type = "warning"
    text = "{} timed out after {} seconds.".format(url, r.status_code)
    tags = [tag_entry, tag_entry_2]
    api.Event.create(title=title, text=text, tags=tags, alert_type=alert_type)


while True:
    for url in url_list:
        # Check the url
        try:
            r = requests.get(url, timeout=timeout)
        except requests.exceptions.Timeout as e:
            # If there's a timeout
            timeout_event(url, timeout)

        if r.status_code != 200:
            status_code_event(url, r)
        try:
            r = requests.get(url).elapsed.total_seconds()
            tag_custom =  "url:{}".format(url)
            # Submit a point with a timestamp (must be ~current)
            api.Metric.send(metric='http.response_time', points=r, tags=[tag_custom])
        except urllib.error.HTTPError as he:
            # If there is an HTTP error
            http_error = he
            error_event(url, http_error)
