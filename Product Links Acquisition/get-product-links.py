from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)
driver.get('https://www.realcanadiansuperstore.ca/')

try:
    search_bar = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'search-input__input'))
    )

    search_bar.clear()
    search_bar.send_keys('Suraj')
    search_bar.send_keys(Keys.RETURN)

except:
    driver.quit()

time.sleep(10)

while(True):
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        load_more_btn = driver.find_element_by_class_name('primary-button--load-more-button')
        ActionChains(driver).move_to_element(load_more_btn).click(load_more_btn).perform()
        
        time.sleep(3)
    except:
        break


time.sleep(10)

products = driver.find_elements_by_class_name('product-tile__details__info__name__link')

links_file = open('Data Acquisition/product_links.txt', 'w')

driver.find_elements

links_file.write(f'Number of results: {len(products)}\n')

for product in products:
    product_name = product.find_element_by_class_name('product-name__item--name').text
    product_link = product.get_attribute('href')
    links_file.write(f'{product_name}: {product_link}\n')

links_file.close()

driver.quit()