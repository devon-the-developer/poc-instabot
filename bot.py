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

# Load Safari WebDriver and open it
browser = webdriver.Safari()
browser.get('https://www.instagram.com')
sleep(5)
browser.close()