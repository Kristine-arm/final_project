
import pytest
from src.pages.all_pages.cart_page import CartPage
from src.pages.all_pages.checkout_page import CheckOutPage
from src.pages.all_pages.login_page import LoginPage
from src.pages.all_pages.main_page import MainPage
from src.pages.all_pages.payment_page import PaymentPage
from allure_commons.types import Severity
import allure

@pytest.mark.usefixtures("driver")
@allure.feature('Place Order')
class TestLoginBeforeCheckout:

    @allure.story('Place Order: Login before Checkout')
    @allure.severity(Severity.NORMAL)
    @allure.description("""
This test automates the process of placing an order on an e-commerce platform, ensuring a seamless user journey:
1. Verify home page visibility to ensure user lands on the main page successfully.
2. Initiate and complete user login to authenticate and access user-specific functionalities.
3. Add a product to the cart and proceed to view the cart, confirming item addition.
4. Navigate to and verify the cart page, then click 'Proceed To Checkout'.
5. Confirm address details and review the order, ensuring all information is correct.
6. Enter any final comments and place the order, moving to the payment phase.
7. Fill out and submit payment details, then confirm the order placement.
8. Verify the success message post-order confirmation, ensuring the process completes.
9. Log out to clear session and confirm logout success by the visibility of the login button.
This streamlined procedure checks critical e-commerce functionalities from login to order completion.
""")

    def test_login_before_checkout(self, driver):
        main_page = MainPage(driver)
        cart_page = CartPage(driver)
        login_page = LoginPage(driver)
        payment_page = PaymentPage(driver)
        checkout_page = CheckOutPage(driver)

        with allure.step('Verify that home page is visible successfully'):
            assert main_page.is_home_button_visible(), "'Home' button was not visible after navigating to the Main Page."
        with allure.step("Click on signup/login button"):
            main_page.signup_login_button.click()
        with allure.step("Perform login"):
            login_page.make_login()
        with allure.step('Verify "Logged in as username" at top'):
            assert login_page.is_logged_in_as_note_visible(), "'Logged In As' note is not visible"
        with allure.step("Add product to cart and click cart button"):
            main_page.hover_and_add_product_to_cart()
            main_page.click_cart_button()
        with allure.step('Verify that cart page is displayed'):
            assert cart_page.is_on_cart_page(), "Cart page is not displayed"
        with allure.step('Click "Proceed To Checkout" button'):
            cart_page.clicking_checkout()
        with allure.step('Verify Address Details and Review Your Order'):
            delivery_addresses, billing_addresses = checkout_page.verify_address_details()
            assert delivery_addresses == billing_addresses, "Delivery and billing addresses do not match"
            order_details = checkout_page.review_order_details()
            assert order_details, "Order details could not be verified"
        with allure.step('Enter description in comment text area and click "Place Order"'):
            checkout_page.write_comment_and_press_place_order()
        with allure.step('Enter payment details: Name on Card, Card Number, CVC, Expiration date'):
            payment_page.filling_card_field_and_paying()
        with allure.step('Click "Pay and Confirm Order" button'):
            payment_page.pay_and_click_confirm()
        with allure.step('Verify order success message'):
            success_message = payment_page.verify_order_success_message()
            assert "Congratulations! Your order has been confirmed!" in success_message, f"Expected success message not found. Actual message: '{success_message}'"
        with allure.step("Log out from account"):
            login_page.make_logout()
        with allure.step("Signup/Login button is visible"):
            assert main_page.is_signup_login_button_visible(), "Signup/Login button is not visible after deleting the account"

