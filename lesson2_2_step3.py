import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html" 

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'num1' )
    x = x_element.text
    y_element = browser.find_element(By.ID, 'num2' )
    y = y_element.text
    sum = int(x) + int(y)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))
    
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
         
finally:
    time.sleep(10)
    browser.quit()
