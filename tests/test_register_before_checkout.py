
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
class TestRegBeforeCheckout:

    @allure.story('Place Order: Register before Checkout')
    @allure.severity(Severity.NORMAL)
    @allure.description("""
This test case validates the complete flow from registration to order placement on the e-commerce platform:
1. Verify that the home page is properly displayed by checking the visibility of the 'Home' button.
2. Navigate to the sign-up/login page by clicking the appropriate button on the home page.
3. Complete the account registration form with necessary details and confirm the account creation.
4. Ensure that the new user is properly logged in by checking for a 'Logged In As' note.
5. Add a product to the shopping cart and proceed to view the cart.
6. Confirm that the correct cart page is displayed.
7. Proceed from the cart page to the checkout page.
8. Validate that the delivery and billing addresses are correctly displayed and match.
9. Review the order details to ensure all product names, prices, and quantities are correct.
10. Enter a comment for the order and proceed to place the order.
11. Fill in the payment details including card information and submit the payment.
12. Confirm that the order has been successfully placed by verifying the order success message.
13. Lastly, delete the newly created account to clean up after the test, and verify that the account has been successfully deleted.
""")

    def test_registration_before_checkout(self, driver):
        main_page = MainPage(driver)
        cart_page = CartPage(driver)
        login_page = LoginPage(driver)
        payment_page = PaymentPage(driver)
        checkout_page = CheckOutPage(driver)

        with allure.step('Verify that home page is visible successfully'):
            assert main_page.is_home_button_visible(), "'Home' button was not visible after navigating to the Main Page."
        with allure.step("Click on signup/login button"):
            main_page.signup_login_button.click()
        with allure.step('Fill all details in Signup and create account'):
            login_page.make_registration()
            login_page.fill_account_info()
        with allure.step('Verify "ACCOUNT CREATED!" and click "Continue" button'):
            assert login_page.is_account_created_note_visible(), "Account Created note is not visible"
            login_page.clicking_continue_button()
        with allure.step('Verify "Logged in as username" at top'):
            assert login_page.is_logged_in_as_note_visible(), "'Logged In As' note is not visible"
        with allure.step("Add product to cart"):
            main_page.hover_and_add_product_to_cart()
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
        with allure.step('Click "Delete Account" button'):
            payment_page.clicking_account_delete_button()
        with allure.step(' Verify "ACCOUNT DELETED!" and click "Continue" button'):
            assert payment_page.is_account_deleted_note_visible()
            payment_page.clicking_continue_button()

