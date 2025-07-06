import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
import pyperclip


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)



    submit_button1 = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit_button1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Получаем значение x и вычисляем y
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    submit_button2 = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit_button2.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)


finally:
    time.sleep(5)
    browser.quit()