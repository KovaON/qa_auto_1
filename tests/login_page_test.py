from pages.login_page import LoginPage
from data.url_of_pages import AdresPages as url
import time

class TestLoginPage:

    def test_enter_lk(self, driver):
        login_page = LoginPage(driver, url.login_page)
        login_page.open()
        login_page.fill_phone_field()
        time.sleep(20)

    def test_payroll_open(self, driver):
        login_page = LoginPage(driver, url.payroll_page)
        login_page.open()
        time.sleep(5)




