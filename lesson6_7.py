from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id("treasure")
    vall = x_element.get_attribute("valuex")
    y = calc(vall)

    input_text = browser.find_element_by_id("answer")
    input_text.send_keys(str(y))

    checkbutton = browser.find_element_by_id("robotCheckbox")
    checkbutton.click()

    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()

    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
