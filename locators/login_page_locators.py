from selenium.webdriver.common.by import By

class AuthorizationLocators:
    LOGIN_FIELD = (By.CSS_SELECTOR, "#form [name='login']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#form [type='submit']")



