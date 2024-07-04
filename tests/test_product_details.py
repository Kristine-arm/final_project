
from src.pages.all_pages.all_products_page import AllProducts
from src.pages.all_pages.main_page import MainPage
from src.pages.all_pages.product_detail_page import ProductDetailPage
from allure_commons.types import Severity
import allure
import pytest
@allure.feature('Products')
@pytest.mark.usefixtures("driver")
class TestProductDetails:
    @allure.story('Verify that product details are visible')
    @allure.severity(Severity.CRITICAL)
    @allure.description("""
    This test ensures that users can view details of a product from the 'All Products' page.
    Steps include:
    - Confirming the home page is visible after navigation.
    - Navigating to the 'All Products' page by clicking the 'Products' button.
    - Verifying the user is successfully navigated by checking the visibility of 'All Products' text.
    - Ensuring the list of products is visible.
    - Viewing the details of the first product by clicking on 'View Product'.
    - Checking that all essential product details are visible, including name, category, price, availability, condition, and brand.
    """)
    def test_product_details(self, driver):
        main_page = MainPage(driver)
        product_detail_page = ProductDetailPage(driver)
        all_products_page = AllProducts(driver)

        with allure.step('Verify that home page is visible successfully'):
            assert main_page.is_home_button_visible(), "'Home' button was not visible after navigating to Main Page."
        with allure.step('Click on Products button'):
            main_page.go_to_products_page()
        with allure.step('Verify user is navigated to ALL PRODUCTS page successfully'):
            assert all_products_page.is_all_products_note_visible(), "'All Products' text was not visible after navigating to Products Page."
        with allure.step('Verify the products list is visible'):
            assert all_products_page.is_products_list_visible(), "Products list was not visible after navigating to Products Page."
        with allure.step('Click on "View Product" of first product'):
            all_products_page.view_product()
        with allure.step('Verify that detail is visible'):
            details = product_detail_page.get_product_details()
            # print(f"Details found: {details}")
            assert details["name"], "Product name is not visible."
            assert details["category"], "Category is not visible."
            assert details["price"], "Price is not visible."
            assert details["availability"], "Availability is not visible."
            assert details["condition"], "Condition is not visible."
            assert details["brand"], "Brand is not visible."



