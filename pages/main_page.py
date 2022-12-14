from pages.Base_Page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    phone_number = (By.XPATH, "//p[contains(text(), 'Call')]")

    def open_main(self):
        self.driver.get('https://shop.cureskin.com/')


    def verify_element_text(self):
        expected_text = '(800) 4680 9361'
        actual_text = self.driver.find_element(*self.phone_number).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'