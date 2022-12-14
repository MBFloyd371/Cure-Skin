from pages.login_page import Login
from pages.main_page import MainPage



class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.login_page = Login(self.driver)
