
import pytest
from src.pages.all_pages.cart_page import CartPage
from src.pages.all_pages.checkout_page import CheckOutPage
from src.pages.all_pages.login_page import LoginPage
from src.pages.all_pages.main_page import MainPage
from src.pages.all_pages.payment_page import PaymentPage
from allure_commons.types import Severity
import allure

@pytest.mark.usefixtures("driver")
@allure.feature('download')
class TestDownloadInvoiceAfterPurchaseOrder:

    @allure.story('Download Invoice after purchase order')
    @allure.severity(Severity.CRITICAL)
    @allure.description("""
This test verifies the complete purchase process on a web application, from adding products to the cart to downloading the invoice after purchase, and finally deleting the account. The test sequence includes:
1. Verifying visibility of the home page.
2. Adding a product to the cart and checking the cart page is visible.
3. Proceeding to checkout and performing user registration and login.
4. Verifying that the account is created and proceeding.
5. Confirming logged-in status and accessing the checkout via the cart.
6. Verifying that delivery and billing addresses are the same and reviewing order details.
7. Entering a description, placing the order, and entering payment details.
8. Confirming the order with payment details and verifying a success message.
9. Downloading the invoice and checking that the file is correctly downloaded.
10. Continuing after download, deleting the user account, and confirming the account has been deleted.
This test ensures that the user can not only purchase and confirm orders but also handle account management actions like deleting an account post-purchase.
""")

    def test_download_and_verify_invoice(self, driver):
        main_page = MainPage(driver)
        cart_page = CartPage(driver)
        login_page = LoginPage(driver)
        checkout_page = CheckOutPage(driver)
        payment_page = PaymentPage(driver)


        with allure.step('Verify that home page is visible successfully'):
            assert main_page.is_home_button_visible(), "'Home' button was not visible after navigating to the Main Page."
        with allure.step("Add product to cart and click cart button"):
            main_page.hover_and_add_product_to_cart()
            main_page.click_cart_button()
        with allure.step('Verify that cart page is displayed'):
            assert cart_page.is_on_cart_page(), "Cart page is not displayed"
        with allure.step('Click "Proceed To Checkout" button'):
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
        with allure.step('Click "Download Invoice" button and verify invoice is downloaded successfully.'):
            assert payment_page.download_and_verify_invoice("C:/Users/TOSHIBA TOUCHSCREEN/Downloads"), "Invoice download failed"
        with allure.step('Click "Continue" button'):
            payment_page.clicking_continue_button()
        with allure.step('Click "Delete Account" button'):
            payment_page.clicking_account_delete_button()
        with allure.step(' Verify "ACCOUNT DELETED!" and click "Continue" button'):
            assert payment_page.is_account_deleted_note_visible()
            payment_page.clicking_continue_button()


