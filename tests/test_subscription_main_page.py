
import pytest
from src.pages.all_pages.main_page import MainPage
from allure_commons.types import Severity
import allure

@pytest.mark.usefixtures("driver")
@allure.feature('Subscription in main page')
class TestMainPageSubscription:

    @allure.story('Verify Subscription in home page')
    @allure.severity(Severity.MINOR)
    @allure.description("""
        Verifies the functionality of the subscription feature on the main page.
        This test covers:
        - Ensuring the visibility of the 'Home' button, confirming the user is on the Main Page.
        - Scrolling to the bottom of the page to locate the 'SUBSCRIPTION' section.
        - Verifying that the 'SUBSCRIPTION' note is visible to the user.
        - Subscribing to the newsletter and waiting for a response.
        - Confirming that the success message 'You have been successfully subscribed!' is displayed after subscription.
        """)
    def test_subscription_main_page(self, driver):
        main_page = MainPage(driver)

        with allure.step('Verify that home page is visible successfully'):
            assert main_page.is_home_button_visible(), "'Home' button was not visible after navigating to the Main Page."
        with allure.step("Navigate to the Copyright button of the page"):
            main_page.navigate_and_scroll_to_bottom()
        with allure.step("Verify text 'SUBSCRIPTION'"):
            assert main_page.is_subscription_note_visible(), "'SUBSCRIPTION' note was not visible after scrolling down."
        with allure.step("Subscribe to newsletter"):
            main_page.make_subscription()
        with allure.step('Wait for success message "You have been successfully subscribed!" to become visible'):
            assert main_page.wait_for_subscription_alert_visibility(), "Subscription success message was not visible."
        with allure.step('Verify success message "You have been successfully subscribed!" is visible and correct'):
            assert main_page.get_subscription_alert_text() == "You have been successfully subscribed!", \
                "Subscription success message is incorrect or not visible."

