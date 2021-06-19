from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


PATH = 'C:\Program Files (x86)\chromedriver.exe'
URL = 'https://www.realcanadiansuperstore.ca/cumin-seeds-whole/p/20618061_EA'


driver = webdriver.Chrome(PATH)

driver.get(URL)


try:
    nutrition_facts = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "nutrient-per-serving__label--calories"))
    )

    print(nutrition_facts)

    # nutrition_file = open('nutrition.txt', 'w')
    # nutrition_file.write(nutrition_facts.text)
    # nutrition_file.close

finally:
    driver.quit()