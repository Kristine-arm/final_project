
import pytest
from src.pages.all_pages.cart_page import CartPage
from src.pages.all_pages.checkout_page import CheckOutPage
from src.pages.all_pages.login_page import LoginPage
from src.pages.all_pages.main_page import MainPage
from allure_commons.types import Severity
import allure

@pytest.mark.usefixtures("driver")
@allure.feature('Verify')
class TestVerifyAddressDetailsInCheckoutPage:

    @allure.story('Verify address details in checkout page')
    @allure.severity(Severity.NORMAL)
    @allure.description("""
This test verifies the address details on the checkout page after performing a series of actions from logging in to navigating through the cart and checkout process.
Steps include:
1. Confirming visibility and functionality of the 'Home' button on the main page.
2. Handling user registration and login procedures.
3. Checking the acknowledgment of successful account creation and the user's logged-in status.
4. Adding products to the cart and ensuring the cart page is displayed correctly.
5. Proceeding to checkout and comparing delivery and billing addresses to ensure they match.
6. Deleting the user account and confirming the account deletion notice.
This sequence tests the overall flow from user account handling to product checkout, focusing on the accuracy and visibility of critical information throughout the process.
""")

    def test_address_verification(self, driver):
        main_page = MainPage(driver)
        cart_page = CartPage(driver)
        login_page = LoginPage(driver)
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
        with allure.step("Add product to cart and click cart button"):
            main_page.hover_and_add_product_to_cart()
            main_page.click_cart_button()
        with allure.step('Verify that cart page is displayed'):
            assert cart_page.is_on_cart_page(), "Cart page is not displayed"
        with allure.step('Click "Proceed To Checkout" button'):
            cart_page.clicking_checkout()
        with allure.step('Verify delivery address nad billing address are the same'):
            delivery_addresses, billing_addresses = checkout_page.verify_address_details()
            assert delivery_addresses == billing_addresses, "Delivery and billing addresses do not match"
        with allure.step('Click "Delete Account" button'):
            checkout_page.clicking_account_delete_button()
        with allure.step(' Verify "ACCOUNT DELETED!"'):
            assert checkout_page.is_account_deleted_note_visible()