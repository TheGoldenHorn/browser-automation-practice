import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

browser = webdriver.Firefox()
browser.get('http://www.nltk.org/book/')
time.sleep(5)
file = open('nltk.txt','w+')
important = browser.find_element_by_xpath('.//dl')
for link in important.find_elements_by_xpath('.//dd'):
	file.write (link.find_element_by_xpath('.//a').text + '\n')
	file.write (link.find_element_by_xpath('.//a').get_attribute('href') + '\n \n')


file.close()
