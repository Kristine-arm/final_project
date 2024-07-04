import time
import pytest
from src.pages.all_pages.main_page import MainPage
from allure_commons.types import Severity
import allure

@pytest.mark.usefixtures("driver")
@allure.feature('Scroll up and down')
class TestVerifyScrollupAndScrolldownUsingArrow:

    @allure.story('Verify Scroll Up using "Arrow" button and Scroll Down functionality')
    @allure.severity(Severity.TRIVIAL)
    @allure.description("""
        This test case verifies the functionality of scrolling up using the "Arrow" button and scrolling down on a webpage.
        Steps:
        1. Navigate to the home page.
        2. Verify that the home page is visible successfully.
        3. Scroll down the page to the bottom.
        4. Verify the visibility of the 'SUBSCRIPTION' note.
        5. Click on the arrow button at the bottom right side to move upward.
        6. Verify that the page is scrolled up.
        7. Verify that the text 'Full-Fledged practice website for Automation Engineers' is visible on the screen after scrolling up.
        Notes:
        - The scrolling actions are accompanied by sleep statements to allow time for page elements to load.
        - Assertion errors will be raised if any of the expected elements are not found or if the scrolling actions fail.
    """)

    def test_scrollup_and_scrolldown_functionality(self, driver):
        main_page = MainPage(driver)

        with allure.step('Verify that home page is visible successfully'):
            assert main_page.is_home_button_visible(), "'Home' button was not visible after navigating to the Main Page."
        with allure.step("Scroll down page to bottom"):
            main_page.navigate_and_scroll_to_bottom()
        with allure.step("Verify text 'SUBSCRIPTION'"):
            time.sleep(1)
            assert main_page.is_subscription_note_visible(), "'SUBSCRIPTION' note was not visible after scrolling down."
        with allure.step('Click on arrow at bottom right side to move upward'):
            main_page.click_on_bottom_arrow()
            time.sleep(1)
        with allure.step('Verify that page is scrolled up and "Full-Fledged practice website" text is visible on screen'):
            assert main_page.is_page_scrolled_up(), "Page was not scrolled up successfully."
            assert main_page.is_full_fledged_text_visible(), "'Full-Fledged practice website for Automation Engineers' text was not visible after scrolling up."




