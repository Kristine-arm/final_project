
import pytest
from src.pages.all_pages.cart_page import CartPage
from src.pages.all_pages.main_page import MainPage
from allure_commons.types import Severity
import allure
import re

@pytest.mark.usefixtures("driver")
@allure.feature('Cart')
class TestAddToCartRecommendedProducts:

    @allure.story('Add to cart from Recommended items')
    @allure.severity(Severity.CRITICAL)
    @allure.description("""
This test verifies the process of adding recommended products to the shopping cart. Steps include:
1. Navigate to the bottom of the main page to access 'RECOMMENDED ITEMS'.
2. Confirm visibility of 'RECOMMENDED ITEMS'.
3. Add a product to the cart.
4. Check the cart to ensure the added product is correctly listed.
""")

    def test_add_to_cart_recommended_items(self, driver):
        main_page = MainPage(driver)
        cart_page = CartPage(driver)

        with allure.step(" Scroll to bottom of page"):
            main_page.navigate_and_scroll_to_bottom()
        with allure.step('Verify "RECOMMENDED ITEMS" are visible'):
            assert main_page.is_recommended_items_visible(), '"RECOMMENDED ITEMS" are not visible'
        with allure.step(' Click on "Add To Cart" on Recommended product'):
            main_page.click_on_rec_product()
        with allure.step('verify products are visible in cart'):
            actual_product_names = cart_page.get_product_names()
            pattern = re.compile(r'Top|Dress', re.IGNORECASE)
            expected_product_names = [name for name in actual_product_names if pattern.search(name)]
            for expected_name in expected_product_names:
                assert expected_name in actual_product_names, f"Expected product '{expected_name}' not found in cart"






