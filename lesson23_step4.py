from selenium import webdriver
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('.btn')
    input1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_css_selector(".nowrap#input_value")
    x = x_element.text
    y = calc(x)
    
    input2 = browser.find_element_by_css_selector('.form-control')
    input2.send_keys(y)
    
    option1 = browser.find_element_by_css_selector(".btn")
    option1.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
