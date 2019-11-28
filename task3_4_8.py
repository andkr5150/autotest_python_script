from selenium import webdriver
import time
import random

# Test1
# Checking logging
# 1. go to “http://selenium1py.pythonanywhere.com/ru/” link
# 2. enter to "Войти или зарегистрироваться"
# 3. form "Войти"
#  enter Адрес электронной почты "..."
#  enter Пароль "...."
# 4. Press button "Войти"
#  RESULT - Open main page "Отображается Имя и сообщение об успешном входе"

# Test2
# Checking Register
# 1. go to “http://selenium1py.pythonanywhere.com/ru/” link
# 2. enter to "Войти или зарегистрироваться"
# 3. form "Зарегистрироваться"
#  enter Адрес электронной почты "..."
#  enter Пароль "...."
#        enter Повторить пароль "...."
# 4. Press button "Зарегистрироваться"
# RESULT - Open main page "Отображается Имя и сообщение об успешной регистрации"

# Test3
# Language check
# 1. go to “http://selenium1py.pythonanywhere.com/” link
# 2. click on "Русский"
# 3. selection language “British English”
# 4. Press button "Выполнить"
# 5. Проверка на изменение URL
# RESULT - Translation of the page with the selected language

# Test4
# View All products
# 1. go to “http://selenium1py.pythonanywhere.com/” link
# 2. click on "Просмотр магазина"
# 3. selection “Все товары”
# 4. Press "Все товары"
# 5. проверка на отображение товаров в корзине
# RESULT - go to the page with all the products

# Test5-6
# View All products
# 1. go to “http://selenium1py.pythonanywhere.com/” link
# 2. click on "Просмотр магазина"
# 3. selection “Clothing / Books”
# 4. Press "Clothing / Books"
# 5. проверка на отображение товаров в корзине
# RESULT - go to the page with Clothing the products

try:
    browser = webdriver.Chrome()
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)

    # Test 1
    button = browser.find_element_by_id("login_link")
    button.click()
    time.sleep(5)

    username = browser.find_element_by_id("id_login-username")
    username.send_keys("qwerty@gmail.com")

    password = browser.find_element_by_id("id_login-password")
    password.send_keys("asdqwe123#")

    button_send = browser.find_element_by_name("login_submit")
    button_send.click()
    time.sleep(5)

    link_logout = browser.find_element_by_id("logout_link").click()
    time.sleep(5)

    # Test 2
    browser.get(link)
    button = browser.find_element_by_id("login_link")
    button.click()
    time.sleep(5)

    ran = str(random.randint(1, 10001))
    username_new = "qwerty_" + ran + "@gmail.com"
    password1_reg_new = "asdqwe123#_" + ran
    password2_reg_new = "asdqwe123#_" + ran

    username_reg = browser.find_element_by_id("id_registration-email")
    username_reg.send_keys(username_new)

    password1_reg = browser.find_element_by_id("id_registration-password1")
    password1_reg.send_keys(password1_reg_new)

    password1_reg = browser.find_element_by_id("id_registration-password2")
    password1_reg.send_keys(password2_reg_new)

    button_send2 = browser.find_element_by_name("registration_submit")
    button_send2.click()
    time.sleep(5)

    link_logout_reg = browser.find_element_by_id("logout_link").click()
    time.sleep(5)

    # Test 3
    browser.get(link)

    lang = 'ru'

    curretnurlpage = browser.current_url
    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector("[value='" + lang + "']").click()

    button_ch = browser.find_element_by_css_selector(".navbar-left .btn.btn-default")
    button_ch.click()
    time.sleep(5)
    currenturlnew = browser.current_url
    assert (curretnurlpage != currenturlnew)
    time.sleep(5)

    # Test 4
    browser.get(link)

    browser.find_element_by_css_selector("[data-navigation='dropdown-menu'] a:nth-child(1)").click()
    time.sleep(5)

    # Проверка на количество обязательных полей в блоке
    elements = browser.find_elements_by_css_selector("ol.row li")
    time.sleep(5)
    # проверка на количество отображений товаров
    assert len(elements) >= 3

    browser.find_element_by_css_selector(".col-sm-7.h1 a").click()

    # Test 5

    time.sleep(5)
    browser.find_element_by_css_selector("[data-navigation='dropdown-menu'] li:nth-child(3) a").click()
    time.sleep(5)

    # Проверка на количество обязательных полей в блоке
    elements = browser.find_elements_by_css_selector("ol.row li")
    time.sleep(5)
    # проверка на количество отображений товаров
    assert len(elements) >= 3

    browser.find_element_by_css_selector(".col-sm-7.h1 a").click()

    # Test 6

    time.sleep(5)
    browser.find_element_by_css_selector("[data-navigation='dropdown-menu'] li:nth-child(4) a").click()
    time.sleep(5)

    # Проверка на количество обязательных полей в блоке
    elements = browser.find_elements_by_css_selector("ol.row li")
    time.sleep(5)
    # проверка на количество отображений товаров
    assert len(elements) >= 3

    browser.find_element_by_css_selector(".col-sm-7.h1 a").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

