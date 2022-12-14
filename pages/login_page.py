from Base_Page import Page
from selenium.webdriver.common.by import By

class ContactUS(Page):
    email_address = (By.CSS_SELECTOR, ".elementor-element.elementor-element-29df4de.elementor-view-default.elementor-vertical-align-top.elementor-widget.elementor-widget-icon-box")

def open_url(self):
    self.driver.get('https://cureskin.com/contact/')

def click(self):
    self.driver.find_element(*self.email_address).click()