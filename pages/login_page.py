from pages.Base_Page import Page
from selenium.webdriver.common.by import By

class Login(Page):
    email = (By.XPATH, "//p[contains(text(), '7PM)Email:')]")

    def open_url(self):
        self.driver.get('https://shop.cureskin.com/account/login')

    def verify_element_text(self):
        expected_text = 'Email: hello@cureskin.com'
        actual_text = self.driver.find_element(*self.email).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'