from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


PATH = 'C:\Program Files (x86)\chromedriver.exe'
URL = 'https://www.realcanadiansuperstore.ca/cumin-seeds-whole/p/20618061_EA'

driver = webdriver.Chrome(PATH)
driver.get(URL)

time.sleep(5)

driver.execute_script("window.scrollTo(0, 800)") 

nutrition_button = driver.find_element_by_class_name('product-details-page-nutrition-info__title')
ActionChains(driver).move_to_element(nutrition_button).click(nutrition_button).perform()

time.sleep(3)

nutrition_facts = driver.find_element_by_class_name('product-nutrition')

driver.quit()


def retrieve_nutrition_data(driver, product_name, product_link):
    driver.get(URL)

    time.sleep(5)

    driver.execute_script("window.scrollTo(0, 800)")

    nutrition_button = driver.find_element_by_class_name('product-details-page-nutrition-info__title')
    ActionChains(driver).move_to_element(nutrition_button).click(nutrition_button).perform()

    time.sleep(3)

    nutrition_facts = driver.find_element_by_class_name('product-nutrition')


def format_name(name):
    formatted = ''

    for char in name:
        if char.isalpha():
            formatted += char
        elif char == ' ':
            formatted += '_'
        else:
            continue
    
    formatted = formatted.lower()
    formatted += '.txt'

    return formatted
