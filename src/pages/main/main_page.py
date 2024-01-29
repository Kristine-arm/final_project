from src.pages.base_element import BaseElement
from src.pages.base_page import BasePage
import allure

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.signup_login_button = BaseElement(driver, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')

    @allure.step('Check if signup/login button is visible')
    def is_signup_login_button_visible(self):
        return self.signup_login_button.is_visible()


