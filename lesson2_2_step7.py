import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    input3.send_keys("a@a.com")


    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, '222.txt')
    element = browser.find_element(By.ID, "file")      # добавляем к этому пути имя файла 
    element.send_keys(file_path)
    # Нажимаем Submit


    submit_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit_button.click()


finally:
    time.sleep(5)
    browser.quit()