from pages.login_page import LoginPage
import time

class TestLoginPage:

    def test_enter_lk(self, driver):
        print(type(driver))
        login_page = LoginPage(driver, 'https://dev.moduldev.ru')
        login_page.open()
        login_page.fill_phone_field()
        time.sleep(5)



