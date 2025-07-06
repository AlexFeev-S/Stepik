from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math 
import pyperclip
import time

browser = webdriver.Chrome()

try:
    
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    submit_button1 = browser.find_element(By.ID, "book")
    submit_button1.click()


    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Получаем значение x и вычисляем y
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    submit_button2 = browser.find_element(By.ID, "solve")
    submit_button2.click()


    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)


finally:
    time.sleep(5)
    browser.quit()
