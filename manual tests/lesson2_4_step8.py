import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html" 
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100") ) 
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value' )
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, '#answer')
    input.send_keys(y)
    
    button2 = browser.find_element(By.ID, 'solve')
    button2.click()

    alert = browser.switch_to.alert
    text = alert.text
    print(text)

finally:
    time.sleep(10)
    browser.quit()
