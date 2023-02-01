from selenium.webdriver.common.by import By

class MainPageLocators:
    """Главная страница банка"""

    # Кнопка "Новый платеж"
    new_payment_button  = (By.CSS_SELECTOR, '.account_actions button:first-child')

    # Кнопка "Пополнить"
    top_up_button = (By.CSS_SELECTOR, '.account_actions button:nth-child(2)')

    # Кнопка "Выписка"
    statements_button = (By.CSS_SELECTOR, '.account_actions button:nth-child(3)')

    # Кнопка "Реквизиты"
    account_details_button = (By.CSS_SELECTOR, '.account_actions button:nth-child(4)')
