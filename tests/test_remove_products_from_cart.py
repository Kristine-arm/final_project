import pytest
from src.pages.all_pages.cart_page import CartPage
from src.pages.all_pages.main_page import MainPage
from allure_commons.types import Severity
import allure

@pytest.mark.usefixtures("driver")
@allure.feature('Remove Products')
class TestRemoveProductsFromCart:

    @allure.story('Remove Products From Cart')
    @allure.severity(Severity.CRITICAL)
    @allure.description("""
This test case validates the functionality of removing products from a shopping cart on an e-commerce platform.

The steps included in this test case are:
1. Verifying that the homepage is successfully visible upon navigating to the site.
2. Adding a product to the shopping cart, ensuring that users can add items as expected.
3. Adding another product to ensure multiple items can be handled.
4. Confirming that the cart page is displayed correctly after adding items, which involves navigating to the cart page and verifying its contents.
5. Removing all products from the cart to test the cart's remove functionality. This step checks that users can delete items from their cart, which is essential for a flexible shopping experience.
6. Verifying that the cart is empty after all products have been removed. This final step confirms that the cart's state updates correctly after item removal, providing clear feedback to the user that their cart is now empty.
""")

    def test_remove_products_from_cart(self, driver):
        main_page = MainPage(driver)
        cart_page = CartPage(driver)

        with allure.step('Verify that home page is visible successfully'):
            assert main_page.is_home_button_visible(), "'Home' button was not visible after navigating to the Main Page."
        with allure.step("Add product to cart"):
            main_page.hover_and_add_first_product_to_cart()
            main_page.hover_and_add_product_to_cart()
        with allure.step('Verify that cart page is displayed'):
            assert cart_page.is_on_cart_page(), "Cart page is not displayed"
        with allure.step('Remove all products from the cart'):
            cart_page.remove_all_products_from_cart()
        with allure.step('Verify cart is empty'):
            assert cart_page.get_empty_cart_text() == "Cart is empty! Click here to buy products.", "Cart is not empty after removing all products."

            


