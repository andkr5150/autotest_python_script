from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    input_text = browser.find_element_by_id("answer")
    input_text.send_keys(str(y))

    checkbutton = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbutton.click()

    radiobutton = browser.find_element_by_css_selector("[for='robotsRule']")
    radiobutton.click()

    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
