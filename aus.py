from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

import time

def sleep(milliseconds):
    time.sleep(milliseconds / 1000)

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Navigate to the webpage
driver.get('https://otv.verwalt-berlin.de/ams/TerminBuchen/wizardng/68959171-2916-4caa-9525-7b4c9c91e7f6?dswid=4045&dsrid=159&st=2&v=1686405547773')

# Wait for the elements to be present and interactable
wait = WebDriverWait(driver, 10)

# Set values and trigger change event for xi-sel-400
select_element = wait.until(EC.element_to_be_clickable((By.ID, 'xi-sel-400')))
driver.execute_script("arguments[0].value = '436'; arguments[0].dispatchEvent(new Event('change'))", select_element)
sleep(1000)

# Set values and trigger change event for xi-sel-422
select_element = wait.until(EC.element_to_be_clickable((By.ID, 'xi-sel-422')))
driver.execute_script("arguments[0].value = '1'; arguments[0].dispatchEvent(new Event('change'))", select_element)
sleep(1000)

# Set values and trigger change event for xi-sel-427
select_element = wait.until(EC.element_to_be_clickable((By.ID, 'xi-sel-427')))
driver.execute_script("arguments[0].value = '2'; arguments[0].dispatchEvent(new Event('change'))", select_element)
sleep(1000)

# TODO
# Click on SERVICEWAHL_DE3436-0-2
# service_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="SERVICEWAHL_DE3436-0-2"]')))
# service_element.click()
# sleep(1000)

# Click on SERVICEWAHL_DE_436-0-2-3
service_element = wait.until(EC.element_to_be_clickable((By.ID, 'SERVICEWAHL_DE_436-0-2-3')))
service_element.click()
sleep(1000)

# Click on SERVICEWAHL_DE436-0-2-3-305244
service_element = wait.until(EC.element_to_be_clickable((By.ID, 'SERVICEWAHL_DE436-0-2-3-305244')))
service_element.click()
sleep(1000)

# Check for error message and reload the page if it exists
error_message = driver.find_elements_by_class_name('errorMessage')
if error_message:
    print('An error occurred. Reloading the page...')
    sleep(5000)
    driver.refresh()

# Continue processing or extract data from the updated page
