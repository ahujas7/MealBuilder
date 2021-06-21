from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)


def retrieve_nutrition_data(driver, product_link):
    driver.get(product_link)

    time.sleep(5)

    driver.execute_script("window.scrollTo(0, 800)")

    try: 
        nutrition_button = driver.find_element_by_class_name('product-details-page-nutrition-info__title')
        ActionChains(driver).move_to_element(nutrition_button).click(nutrition_button).perform()
    except:
        return None
    
    time.sleep(3)

    nutrition_facts = driver.find_element_by_class_name('product-nutrition').text

    return nutrition_facts


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


product_links = open('Product Links Acquisition/product_links.txt', 'r')

products = []

for line in product_links:
    split = line.split(': ')
    products.append((split[0], split[1][:-1]))


for name, link in products:
    nutrition_data = retrieve_nutrition_data(driver, link)

    if nutrition_data is None:
        print(name, '\n')
        continue

    f = open(f'Nutrition Data/{format_name(name)}', 'a')

    f.write(nutrition_data)

    f.close()


driver.quit()

