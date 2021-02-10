import os
from os.path import join, dirname
from dotenv import load_dotenv

from time import sleep
from selenium import webdriver

# Load instagram account login from .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

print(username)
print(password)

# Load Firefox WebDriver and open instagram login page
browser = webdriver.Firefox()
browser.implicitly_wait(10)

browser.get('https://www.instagram.com')

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys(username)
password_input.send_keys(password)
sleep(5)


login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

#sleep(10)

#browser.close()
