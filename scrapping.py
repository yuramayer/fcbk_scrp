from selenium import webdriver
import scrolling
import set_settings
from bs4 import BeautifulSoup

""" setting driver's object (check geckodriver for your Firefox version here: 
    https://github.com/mozilla/geckodriver/releases
"""
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('no-sandbox')

driver = webdriver.Firefox(
    executable_path=r"***\geckodriver.exe",
    options=firefox_options)  # your geckodriver's path here

url = set_settings.url  # change your url in set_settings.py
driver.get(url)

""" authorization at the Facebook for getting private page
"""
username = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")
submit = driver.find_element_by_id("loginbutton")

username.send_keys(set_settings.acc_login)  # you can set your log
password.send_keys(set_settings.acc_password)  # and pass in set_settings
submit.click()

""" scrolling to the end of page and getting all the source in soup"""
scrolling.scroll_down(driver)

data = driver.page_source

soup = BeautifulSoup(data)

""" for getting user's post you should find unique container's id
    i'll automate this process in the next commit
"""
