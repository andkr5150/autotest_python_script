from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    # link = " http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)


    num1 = browser.find_element_by_id("num1")
    x = int(num1.text)

    num2 = browser.find_element_by_id("num2")
    y = int(num2.text)

    sum = str(x + y)

    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector("[value='" + sum + "']").click()

    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
