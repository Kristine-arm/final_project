import time
import pytest
from src.pages.all_pages.all_products_page import AllProducts
from src.pages.all_pages.cart_page import CartPage
from src.pages.all_pages.main_page import MainPage
from allure_commons.types import Severity
import allure


@pytest.mark.usefixtures("driver")
@allure.feature('Products in Cart')
class TestProductInCart:

    @allure.story('Add Products in Cart')
    @allure.severity(Severity.CRITICAL)
    @allure.description("""
        This test case verifies the functionality of adding products to the cart and ensuring they are correctly added with the appropriate details.
        Steps:
        1. Verify that the home page is visible.
        2. Navigate to the products page.
        3. Add the first product to the cart.
        4. Add the second product to the cart.
        5. Verify that both products are present in the cart.
        6. Verify the prices, quantities, and total prices of the products in the cart.
        """)

    def test_add_product_in_cart(self, driver):
        main_page = MainPage(driver)
        all_products_page = AllProducts(driver)
        cart_page = CartPage(driver)

        with allure.step('Verify that home page is visible successfully'):
            assert main_page.is_home_button_visible(), "'Home' button was not visible after navigating to the Main Page."
            time.sleep(1)
        with allure.step('Click on "Products" button'):
            main_page.go_to_products_page()
            time.sleep(2)
        with allure.step('Hover over first product, click "Add to cart" and click "Continue Shopping"'):
            all_products_page.hover_and_add_first_product_to_cart()
        with allure.step('Hover over the second product, click "Add to Cart" and click "View Cart"'):
            all_products_page.hover_and_add_second_product_to_cart()
        with allure.step('Verify both products are added to Cart'):
            product_names = cart_page.get_product_names()
            assert len(product_names) == 2, "Expected two products in the cart, found {}".format(len(product_names))
        with allure.step('Verify their prices, quantity and total price'):
            prices = cart_page.get_prices()
            quantities = cart_page.get_quantities()
            total_prices = cart_page.get_total_prices()

            for price, quantity, total_price in zip(prices, quantities, total_prices):
                assert float(total_price) == float(price) * int(quantity), "Price calculation does not match for one of the products"
                assert int(quantity) == 1, "Product quantity is not as expected"  # Assuming you expect 1 item each



