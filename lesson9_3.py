from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # browser.implicitly_wait(15)

    WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    but = browser.find_element_by_id("book")
    but.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input_text = browser.find_element_by_id("answer")
    input_text.send_keys(str(y))

    button = browser.find_element_by_id("solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
