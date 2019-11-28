from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input_text = browser.find_element_by_id("answer")
    input_text.send_keys(str(y))

    checkbutton = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbutton.click()

    radiobutton = browser.find_element_by_css_selector("[for='robotsRule']")
    radiobutton.click()

    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
