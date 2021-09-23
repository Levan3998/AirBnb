from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
email = 'yosefbot369@gmail.com'
password = 'Yosef!!!@'

def login_to_airbnb():
    driver = webdriver.Chrome()
    url = 'https://www.airbnb.com/oauth_connect?from=facebook_login&service=facebook'
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_name('button').click()
    driver.find_element_by_name('button').click()
    time.sleep(1)
    x = driver.find_elements_by_class_name("_55r1")
    x[0].send_keys(email)
    x[1].send_keys(password)
    driver.find_element_by_class_name('_xkt').click()
    time.sleep(10)
    return driver

login_to_airbnb()