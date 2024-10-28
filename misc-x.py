# Miscelaneous functions

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import requests
import glob
import os
import pandas as pd


def connect(url, time_limit=15):
    """
    Establishes a connection with a given URL (str) if possible.
    `time_limit` is the maximum time to wait for the connection to be 
    established. If such time is exceeded the connection is understood to fail.
    """
    success = False
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
    timeout = time.time() + time_limit
    while success is False:
        if time.time() > timeout:
            raise ConnectionError
        try:
            content = requests.get(url, headers=headers, timeout=5)
            success = True
        except:
            pass
    return content


def sconnect(url):
    """
    Establish a Selenium connection.
    """
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Firefox(options=options)
    browser.get(url)
    html = browser.page_source
    return (html)



def is_raw_pdf(url, link):
    """Does the given url (str) and link (str) pertain to a PDF?"""
    if url is None or link is None:
        return False
    return (url[3:13].isnumeric() or link.endswith(".pdf"))
