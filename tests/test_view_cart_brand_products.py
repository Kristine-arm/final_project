
import pytest
from src.pages.all_pages.all_products_page import AllProducts
from src.pages.all_pages.main_page import MainPage
from allure_commons.types import Severity
import allure

@pytest.mark.usefixtures("driver")
@allure.feature('Products')
class TestViewCartBrandProducts:

    @allure.story('View & Cart Brand Products')
    @allure.severity(Severity.CRITICAL)
    @allure.description("""
    This test verifies the functionality related to viewing and carting brand products.
    It includes the following steps:
    1. Verify that the home page is visible successfully.
    2. Click on the "Products" button.
    3. Verify that Brands are visible on the left side bar.
    4. Click on any brand name.
    5. Verify that the user is navigated to the brand page and click on any other brand link.
    6. Verify that the user is navigated to the brand page.
    """)

    def test_view_cart_brand_products(self, driver):
        main_page = MainPage(driver)
        all_products_page = AllProducts(driver)

        with allure.step('Verify that home page is visible successfully'):
            assert main_page.is_home_button_visible(), "'Home' button was not visible after navigating to the Main Page."
        with allure.step('Click on "Products" button'):
            main_page.go_to_products_page()
        with allure.step('Verify that Brands are visible on left side bar'):
            assert all_products_page.brands_are_visible(), "Brands section is not visible on the all products page."
        with allure.step('Click on any brand name'):
            all_products_page.select_random_brand()
        with allure.step('Verify that user is navigated to brand page and click on any other brand link'):
            assert all_products_page.is_brand_note_visible()
            all_products_page.select_random_brand()
        with allure.step('Verify that user is navigated to brand page'):
            assert all_products_page.is_product_name_visible()



