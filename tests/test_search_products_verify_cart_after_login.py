
import re
import pytest
from src.pages.all_pages.login_page import LoginPage
from src.pages.all_pages.all_products_page import AllProducts
from src.pages.all_pages.main_page import MainPage
from allure_commons.types import Severity
from src.pages.all_pages.cart_page import CartPage
import allure

@pytest.mark.usefixtures("driver")
@allure.feature('Products')
class TestViewCartBrandProducts:

    @allure.story('Search Products and Verify Cart After Login')
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.parametrize("product_name", ["Top"])
    @allure.description("""
    This test case verifies the functionality of searching for products, adding them to the cart,
    and verifying the contents of the cart after login. It follows these steps:
    
    1. Navigate to the main page.
    2. Click on the "Products" button.
    3. Verify that the user is navigated to the "ALL PRODUCTS" page.
    4. Search for the specified product name.
    5. Verify that the "SEARCHED PRODUCTS" text is visible.
    6. Verify that all the products related to the search are visible.
    7. Add the products to the cart and click on the cart button.
    8. Verify that the products are visible in the cart.
    9. Click on the signup/login button.
    10. Perform login.
    11. Verify that the products are still visible in the cart after login.
    12. Logout from the account.
    """)

    def test_search_products_with_cart_verification(self, driver, product_name):
        main_page = MainPage(driver)
        all_products_page = AllProducts(driver)
        cart_page = CartPage(driver)
        login_page = LoginPage(driver)

        with allure.step('Verify that home page is visible successfully'):
            assert main_page.is_home_button_visible(), "'Home' button was not visible after navigating to the Main Page."
        with allure.step('Click on "Products" button'):
            main_page.go_to_products_page()
        with allure.step('Verify user is navigated to ALL PRODUCTS page successfully'):
            assert all_products_page.is_all_products_note_visible(), "'All Products' text was not visible after navigating to Products Page."
        with allure.step(f'Search for product name "{product_name}"'):
            all_products_page.search_for_product(product_name)
        with allure.step("Verify 'SEARCHED PRODUCTS' text is visible"):
            assert all_products_page.is_searched_products_visible(), "'SEARCHED PRODUCTS' text was not visible after searching."
        with allure.step('Verify all the products related to search are visible'):
            assert all_products_page.are_search_results_relevant(
                product_name), f"Some products were not relevant to the search query for '{product_name}'."
        with allure.step('Add those products to cart and click cart button'):
            all_products_page.hover_and_add_top_product_to_cart()
            all_products_page.click_cart_button()
        with allure.step('verify products are visible in cart'):
            actual_product_names = cart_page.get_product_names()
            pattern = re.compile(r'Top', re.IGNORECASE)
            expected_product_names = [name for name in actual_product_names if pattern.search(name)]
            for expected_name in expected_product_names:
                assert expected_name in actual_product_names, f"Expected product '{expected_name}' not found in cart"
        with allure.step("Click on signup/login button"):
            main_page.signup_login_button.click()
        with allure.step("Perform login"):
            login_page.make_login()
        with allure.step('Verify that the products are still visible in the cart after login'):
            main_page.click_cart_button()
            actual_product_names = cart_page.get_product_names()
            pattern = re.compile(r'Top', re.IGNORECASE)
            expected_product_names = [name for name in actual_product_names if pattern.search(name)]
            for expected_name in expected_product_names:
                assert expected_name in actual_product_names, f"Expected product '{expected_name}' not found in cart"
        with allure.step("Log out from account"):
            login_page.make_logout()

