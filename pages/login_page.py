
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginPageLocators()

    def fill_phone_field(self):
        self.element_is_visible(self.locators.phone_field).send_keys('8482932984')
        self.element_is_visible(self.locators.submit_button).click()
        self.element_is_visible(self.locators.sms_field).send_keys('11111')
        self.element_is_visible(self.locators.password_field).send_keys('Qq111111')
        self.element_is_visible(self.locators.password_submit).click()




