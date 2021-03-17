from selenium import webdriver
import pyautogui as py
import time

def code(ticker):
    browser = webdriver.Chrome()
    browser.get('https://www.bseindia.com/index.html')
    check=browser.find_element_by_xpath('/html/body/div/div[4]/div/div[3]/div/section/form/div[1]/input')
    check.send_keys(ticker)
    time.sleep(4)
    py.press('enter')
    time.sleep(4)
    check = browser.find_element_by_xpath('/html/body/div[1]/div[6]/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/div[2]')
    check = check.text
    time.sleep(1)
    browser.close()
    return check
