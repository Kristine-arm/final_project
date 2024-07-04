
import pytest
from src.pages.all_pages.all_products_page import AllProducts
from src.pages.all_pages.main_page import MainPage
from allure_commons.types import Severity
import allure

@pytest.mark.usefixtures("driver")
@allure.feature('Search Product')
class TestProductSearch:

    @allure.story('Search for products and verify results')
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.parametrize("product_name", ["Top", "Dress"])
    @allure.description("""
        This test verifies the product search functionality on the 'All Products' page.
        Steps include:
        - Ensuring the home page is visible upon navigation.
        - Navigating to the 'All Products' page by clicking on the 'Products' button.
        - Confirming the navigation by checking the visibility of the 'All Products' text.
        - Performing a search for a specific product using predefined names like 'Top' and 'Dress'.
        - Verifying that the 'SEARCHED PRODUCTS' section becomes visible following the search.
        - Ensuring all displayed search results are relevant to the searched product name.
        """)
    def test_search_product(self, driver, product_name):
        main_page = MainPage(driver)
        all_products_page = AllProducts(driver)

        with allure.step('Verify that home page is visible successfully'):
            assert main_page.is_home_button_visible(), "'Home' button was not visible after navigating to the Main Page."
        with allure.step('Click on Products button'):
            main_page.go_to_products_page()
        with allure.step('Verify user is navigated to ALL PRODUCTS page successfully'):
            assert all_products_page.is_all_products_note_visible(), "'All Products' text was not visible after navigating to the Products Page."
        with allure.step(f'Search for product name "{product_name}"'):
            all_products_page.search_for_product(product_name)
        with allure.step("Verify 'SEARCHED PRODUCTS' text is visible"):
            assert all_products_page.is_searched_products_visible(), "'SEARCHED PRODUCTS' text was not visible after searching."
        with allure.step('Verify all the products related to search are visible'):
            assert all_products_page.are_search_results_relevant(product_name), f"Some products were not relevant to the search query for '{product_name}'."


