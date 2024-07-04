
import pytest
from src.pages.all_pages.cart_page import CartPage
from src.pages.all_pages.main_page import MainPage
from allure_commons.types import Severity
import allure
@pytest.mark.usefixtures("driver")
@allure.feature('Subscription in cart page')
class TestCartPageSubscription:

    @allure.story('Verify Subscription in home page')
    @allure.severity(Severity.MINOR)
    @allure.description("""
        Verifies the newsletter subscription functionality on the cart page.
        This test covers:
        - Ensuring the home page is initially visible upon navigation.
        - Clicking on the 'Cart' button to navigate to the cart page.
        - Scrolling to the bottom of the cart page to find the 'Subscription' section.
        - Verifying that the 'Subscription' text is visible, indicating the subscription section is present.
        - Performing the subscription action by entering an email and submitting.
        - Verifying the success message "You have been successfully subscribed!" is visible and correct.
        """)
    def test_subscription_cart_page(self, driver):
        main_page = MainPage(driver)
        cart_page = CartPage(driver)

        with allure.step('Verify that home page is visible successfully'):
            assert main_page.is_home_button_visible(), "'Home' button was not visible after navigating to the Main Page."
        with allure.step("Click 'Cart' button"):
            cart_page.clicking_cart_button()
        with allure.step("Scroll down to footer"):
            cart_page.navigate_and_scroll_to_bottom()
        with allure.step("Verify text 'SUBSCRIPTION'"):
            assert cart_page.is_subscription_note_visible(), "'SUBSCRIPTION' note was not visible after scrolling down."
        with allure.step("Subscribe to newsletter"):
            cart_page.make_subscription()
        with allure.step('Wait for success message "You have been successfully subscribed!" to become visible'):
            assert cart_page.wait_for_subscription_alert_visibility(), "Subscription success message was not visible."
        with allure.step('Verify success message "You have been successfully subscribed!" is visible and correct'):
            assert cart_page.get_subscription_alert_text() == "You have been successfully subscribed!", \
                "Subscription success message is incorrect or not visible."
