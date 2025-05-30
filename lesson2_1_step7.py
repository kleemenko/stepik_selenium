import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/get_attribute.html" 
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try: 
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#treasure' )
    x = x_element.get_attribute('valuex')
    print(x)
    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, '#answer')
    input.send_keys(y)
    time.sleep(2)
    
    option1 = browser.find_element(By.CSS_SELECTOR, 'input#robotCheckbox')
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, 'input#robotsRule')
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
         
finally:
    time.sleep(10)
    browser.quit()
