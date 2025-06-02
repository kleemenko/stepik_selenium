import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html" 

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.NAME, 'firstname' )
    name.send_keys("Dima")

    surname = browser.find_element(By.NAME, 'lastname')
    surname.send_keys("klim")

    email = browser.find_element(By.NAME, 'email')
    email.send_keys('sdfs@dsf.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))    
    file_path = file_path = os.path.join(current_dir, 'text.txt')
    file = browser.find_element(By.NAME, 'file')
    file.send_keys(file_path)
    time.sleep(2)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
         
finally:
    time.sleep(10)
    browser.quit()
