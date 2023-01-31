from selenium.webdriver.common.by import By


class LoginPageLocators:
    """ тут у нас локаторы странички ввода телефона при авторизации в ЛК банка"""

    phone_field = (By.CSS_SELECTOR, '#form [type="tel"]')
    submit_button = (By.CSS_SELECTOR, '#form [type="submit"]')

    left_up_logo = (By.CSS_SELECTOR, 'a.logo')
    right_up_tel = (By.CSS_SELECTOR, 'a.auth__phone')
