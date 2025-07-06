from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element(By.ID, "robotCheckbox")
    button1.click()
    button2 = browser.find_element(By.ID, "robotsRule")
    button2.click()


    x_element = browser.find_element(By.ID, "treasure")
    x_element = x_element.get_attribute("valuex")
    x = x_element
    y = calc(x)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)


    button3 = browser.find_element(By.CLASS_NAME, "btn-default")
    #button3 = browser.find_element(By.CLASS_NAME, "btn btn-default")
    button3.click()

        

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()