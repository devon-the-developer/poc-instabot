import os
from os.path import join, dirname
from dotenv import load_dotenv

from time import sleep
from selenium import webdriver

accountusername = ''

def getAccountLoginDetails(detail):
    # Load instagram account login from .env file
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    if (detail == 'PASSWORD'):
        password = os.getenv('PASSWORD')
        return(password)
    elif(detail == 'USERNAME'):
        username = os.getenv('USERNAME')
        return(username)
    else:
        return ("")

def logoutAccount(browser):
    #Profile Button Menu
    profile_menu_button = browser.find_element_by_css_selector(
        "span[class='_2dbep qNELH']"
    )
    profile_menu_button.click()
    sleep(1)

    logout_button = browser.find_element_by_xpath("//div[@class='-qQT3']")
    logout_button.click()

    sleep(10)
    browser.close()

def gotoHome(browser):
    homelink = '/'
    browser.get('https://www.instagram.com' + homelink)

def gotoProfile(browser):
    profilelink = '/'+ accountusername + '/'
    browser.get('https://www.instagram.com' + profilelink)

def likePostOnPage(browser, post_number):
    try:
        like_button = browser.find_element_by_css_selector("button span > svg")
        lb_state = like_button.get_attribute('aria-label')
        if(lb_state == "Unlike"):
            print("Post already liked")
        elif(lb_state == "Like"):
            print("Liking Post")
            like_button.click()
    except:
        print('Error Trying To Like Post: ' + str(post_number))
        return        
            
    
    

def main(username, password):
    #set accountusername for use elsewhere 
    global accountusername 
    accountusername = username

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
    sleep(10)

    #Worth creating a variable that has all available options
    notifications_settings_dialog = browser.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
    notifications_settings_dialog.click()
    sleep(2)

    #gotoProfile(browser)
    #sleep(3)

    #gotoHome(browser)
    #sleep(10)

    likePostOnPage(browser, 1)
    sleep(10)

    #logoutAccount(browser)
