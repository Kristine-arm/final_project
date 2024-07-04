
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
class TestRegWhileCheckout:

    @allure.story('Place Order: Register while Checkout')
    @allure.severity(Severity.NORMAL)
    @allure.description("""
This test case covers the end-to-end flow of a user placing an order on an e-commerce site. The steps include:
1. Verifying the visibility of the homepage upon navigating to the site.
2. Adding a product to the cart from the homepage.
3. Proceeding to view the cart and initiating the checkout process.
4. Opting to register or log in during the checkout process for new users.
5. Filling in all required details for account creation and continuing post account creation.
6. Verifying that the account has been successfully created and the user is logged in.
7. Re-accessing the cart to continue the checkout process post-login.
8. Validating the delivery and billing addresses during checkout.
9. Reviewing the order details, ensuring that product names, quantities, and prices are correct.
10. Writing a comment for the order and placing the order.
11. Entering payment details including the card information and confirming the payment.
12. Verifying the success message post-order placement to ensure the order has been confirmed.
13. Deleting the newly created account to maintain state and cleanliness of the test environment.
This test ensures that the user can successfully navigate through the site, add items to their cart, complete the checkout process, and finally, verify that the order has been placed and confirmed.
""")
    def test_registration_while_checkout(self, driver):
        main_page = MainPage(driver)
        cart_page = CartPage(driver)
        login_page = LoginPage(driver)
        payment_page = PaymentPage(driver)
        checkout_page = CheckOutPage(driver)


        with allure.step('Verify that home page is visible successfully'):
            assert main_page.is_home_button_visible(), "'Home' button was not visible after navigating to the Main Page."
        with allure.step("Add product to cart"):
            main_page.hover_and_add_first_product_to_cart()
        with allure.step("Click 'Cart' button and later clicking checkout"):
            main_page.click_cart_button()
            cart_page.clicking_checkout()
        with allure.step(' Click "Register / Login" button'):
            cart_page.clicking_register_login()
        with allure.step(' Fill all details in Signup and create account'):
            login_page.make_registration()
            login_page.fill_account_info()
        with allure.step('Verify "ACCOUNT CREATED!" and click "Continue" button'):
            assert login_page.is_account_created_note_visible(), "Account Created note is not visible"
            login_page.clicking_continue_button()
        with allure.step('Verify "Logged in as username" at top and click Cart button'):
            assert login_page.is_logged_in_as_note_visible(), "'Logged In As' note is not visible"
            login_page.click_cart_button()
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














