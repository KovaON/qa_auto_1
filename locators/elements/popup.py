from selenium.webdriver.common.by import By


class Popups:
    # Получайте мгновенные уведомления прямо в браузере
    moment_notify_in_browser = (By.CSS_SELECTOR, '.popup_web_push a')