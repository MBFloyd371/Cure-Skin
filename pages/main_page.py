from pages.Base_Page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    phone_number = (By.XPATH, "//p[contains(text(), 'Call')]")
    headline_text = (By.XPATH, "//p[contains(text(),'Get your skin')]")
    title = (By.XPATH, "//h1[contains(text(),'We believe in')]")

    def open_main(self):
        self.driver.get('https://shop.cureskin.com/')


    def verify_element_text(self):
        expected_text = '(800) 4680 9361'
        actual_text = self.driver.find_element(*self.phone_number).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    def verify_element_text(self):
        expected_text = 'Get your skin festive ready with our CureSkin favorites'
        actual_text = self.driver.find_element(*self.headline_text).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    def verify_element_text(self):
        expected_text = 'We believe in Skin'
        actual_text = self.driver.find_element(*self.title).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'