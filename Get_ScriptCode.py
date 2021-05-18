from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pyautogui as py
import time
from requests_html import HTMLSession



def code(ticker):
    browser = webdriver.Edge()
    browser.get('https://nse-scrips.herokuapp.com/')
    time.sleep(2)
    check=browser.find_element_by_xpath('/html/body/div/section/main/div/div/span/input')
    check.send_keys(ticker)
    time.sleep(1)
    #py.press('enter')
    try:
        logout_button = browser.find_element_by_id(ticker)
        print('found')
    except :#NoSuchElementException:
        print('Incorrect login/password')

    #browser.close()
    return check

def scriptCode():
    URL = "https://nse-scrips.herokuapp.com/"
    session = HTMLSession()
    r = session.get(URL)
    r.html.render()  # this call executes the js in the page
    #r = session.get(URL)
    #r = requests.get(URL)
    soup = BeautifulSoup(r.text,
                          'html.parser')  # If this line causes an error, run 'pip install html5lib' or install html5lib
    print(soup.prettify())

code('infy')