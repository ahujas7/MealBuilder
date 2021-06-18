from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd




PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)

driver.get('https://www.realcanadiansuperstore.ca/')

try:
    search_bar = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "search-input__input"))
    )

    search_bar.send_keys('Suraj')
    search_bar.send_keys(Keys.RETURN)
except:
    driver.quit()

time.sleep(30)

results = driver.find_elements_by_class_name('product-tile__details__info__name__link')

print('Number of results', len(results))

driver.quit()

