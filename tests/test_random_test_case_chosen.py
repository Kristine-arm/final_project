
from src.pages.all_pages.main_page import MainPage
from src.pages.all_pages.cases_page import Cases
from allure_commons.types import Severity
import allure
import pytest

@allure.feature('Choose Random test Case')
@pytest.mark.usefixtures("driver")
class TestRandomTestCase:
    @allure.story('Choose and Verify Random Test Case')
    @allure.severity(Severity.NORMAL)
    @allure.description("""
        This test validates the functionality of selecting a random test case from the 'Test Cases' page.
        Steps include:
        - Navigating to the 'Test Cases' section from the main page.
        - Verifying that the 'Test Cases' section is correctly displayed.
        - Selecting a random test case to view its details.
        - Scrolling down to the bottom of the page to subscribe to the newsletter.
        - Returning to the top of the page and clicking the automation exercise logo to navigate back to the main page.
        - Verifying successful navigation back to the home page.
        """)
    def test_random_case(self, driver):
        main_page = MainPage(driver)
        cases_page = Cases(driver)

        with allure.step("Click 'Test Cases' button"):
            main_page.test_cases_button.click()
        with allure.step("Verify 'Test Cases' note visibility"):
            assert cases_page.is_test_case_visible(), "'Test Cases' note was not visible after clicking Test Cases."
        with allure.step("Select a random test case"):
            cases_page.select_random_test_case()
        with allure.step("Navigate to the Copyright button of the page"):
            cases_page.navigate_and_scroll_to_bottom()
        with allure.step("Subscribe to newsletter"):
            cases_page.make_subscription()
        with allure.step("Scroll up and click the automation exercise logo"):
            cases_page.scroll_to_and_click_logo()
        with allure.step("Verify landing on the home page"):
            assert main_page.is_on_main_page(), "Did not navigate back to the home page successfully."

