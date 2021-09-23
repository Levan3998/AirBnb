from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

album = 'Tokyo,Japan'

L= []
with open ("best offers.txt",'r') as f:
    data = f.readlines()
    print(data)
    for line in data:
        line = line[:-1]
        L.append(line)

for link in L[:-1]:
    driver = webdriver.Chrome()
    url = str(link)
    driver.get(url)
    time.sleep(1)
    driver.find_elements_by_class_name('_mapkd4u')[1].click()
    time.sleep(0.5)
    temp_elem = driver.find_elements_by_class_name('_ytmuji')
    temp_elem = [x for x in temp_elem if x.text == album]
    #temp_elem.click()
    driver.close()
