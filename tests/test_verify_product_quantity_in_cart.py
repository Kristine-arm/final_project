
import pytest
from src.pages.all_pages.product_detail_page import ProductDetailPage
from src.pages.all_pages.cart_page import CartPage
from src.pages.all_pages.main_page import MainPage
from allure_commons.types import Severity
import allure

@pytest.mark.usefixtures("driver")
@allure.feature('Products Quantity In Cart')
class TestProductQuantityInCart:

    @allure.story('Verify Product quantity in Cart')
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.parametrize('quantity', [4, 100, 1005])
    @allure.description("""This test verifies that the quantity of a product added to the cart matches the expected quantity.
    The test goes through the process of navigating to the main page, selecting a random product,
    increasing its quantity, adding it to the cart, and then verifying the quantity in the cart.""")

    def test_product_quantity_in_cart(self, driver, quantity):
        main_page = MainPage(driver)
        product_detail_page = ProductDetailPage(driver)
        cart_page = CartPage(driver)

        with allure.step('Verify that home page is visible successfully'):
            assert main_page.is_home_button_visible(), "'Home' button was not visible after navigating to the Main Page."
        with allure.step(f'Click "View Product" of random product on main page and increase quantity to {quantity}'):
            main_page.select_random_view_product()
            assert product_detail_page.verify_product_details_opened(), "'Home' button was not visible after navigating to the Main Page."
            product_detail_page.increase_quantity(quantity)
        with allure.step('Click "Add to cart" button'):
            product_detail_page.add_to_cart_button_click()
        with allure.step('Click "View Cart" button'):
            product_detail_page.view_cart_button_click()
        with allure.step('Verify that product is displayed in cart page with exact quantity'):
            actual_quantities = cart_page.get_quantities()
            assert actual_quantities, "No product quantities found in the cart."
            actual_quantity = actual_quantities[0]
            assert actual_quantity == str(quantity), f"Product quantity in cart does not match, got '{actual_quantity}'"
