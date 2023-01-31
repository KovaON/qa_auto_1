
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginPageLocators()

    def open_login_page(self):
        self.open()

    def fill_phone_field(self):
        self.element_is_visible(self.locators.phone_field).send_keys('8482932984')
        self.element_is_visible(self.locators.submit_button).click()




