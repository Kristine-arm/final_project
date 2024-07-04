from selenium.common import TimeoutException
from src.config.config import TestData
from src.pages.base_element import BaseElement
from src.pages.base_page import BasePage
import allure
import random
@allure.story("Checking cases page functionality")
class Cases(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.test_cases_button = BaseElement(driver, '//a[@href = "/test_cases"]')
        self.test_cases_note = BaseElement(driver, '//h2[@class="title text-center"]')
        self.feedback_for_us_button = BaseElement(driver, '//*[@href="#feedback"]')
        self.subscription_field = BaseElement(driver, '//*[@id = "susbscribe_email"]')
        self.subscription_button = BaseElement(driver, '//*[@class="fa fa-arrow-circle-o-right"]')
        self.copyright = BaseElement(driver, '//*[@class="pull-left"]')
        self.automation_exercise_logo = BaseElement(driver, '//img[@src="/static/images/home/logo.png"]')


    @allure.step("Click on the random test case")
    def select_random_test_case(self):
        try:
            n = random.randint(1, 26)
            self.random_case = BaseElement(self.driver, '(//*[@class="panel-group"])[' + str(n) + ']')
            self.random_case.click()
        except TimeoutException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="error_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Random test case could not be clicked.") from e

    @allure.step("Navigate to the bottom of the page")
    def navigate_and_scroll_to_bottom(self):
        self.copyright.scroll_into_view()

    @allure.step("Make a subscription with provided email")
    def make_subscription(self):
        self.subscription_field.send_keys(TestData.email_incorrect)
        self.subscription_button.click()

    @allure.step("Verify if the 'Test Cases' note is visible on the page")
    def is_test_case_visible(self):
        return self.test_cases_note.is_visible()

    @allure.step("Scroll to and click the automation exercise logo")
    def scroll_to_and_click_logo(self):
        self.automation_exercise_logo.scroll_into_view()
        self.automation_exercise_logo.click()