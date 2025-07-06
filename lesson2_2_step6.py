from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Получаем значение x и вычисляем y
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.CLASS_NAME, "form-control")
    answer_input.send_keys(y)

    # Прокручиваем к чекбоксу и отмечаем его
    checkbox = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    # Прокручиваем к radiobutton и выбираем его
    radiobutton = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    # Нажимаем Submit
    submit_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()