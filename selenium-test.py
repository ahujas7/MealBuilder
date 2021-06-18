from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)

driver.get('https://www.realcanadiansuperstore.ca/')

time.sleep(30)

search = driver.find_element_by_class_name('search-input__input')
search.send_keys('Suraj')
search.send_keys(Keys.ENTER)

time.sleep(20)

driver.quit()

