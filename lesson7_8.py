from selenium import webdriver
import time
import math
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input_name = browser.find_element_by_name("firstname")
    input_name.send_keys("Vasya")

    input_name = browser.find_element_by_name("lastname")
    input_name.send_keys("Petrov")

    input_name = browser.find_element_by_name("email")
    input_name.send_keys("v.p@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

    element = browser.find_element_by_css_selector('[type="file"]')
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
