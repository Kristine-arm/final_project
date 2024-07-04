
import pytest
from src.pages.all_pages.all_products_page import AllProducts
from src.pages.all_pages.main_page import MainPage
from allure_commons.types import Severity
import allure

@pytest.mark.usefixtures("driver")
@allure.feature('Products')
class TestViewCategoryProducts:

    @allure.story('View Category Products')
    @allure.severity(Severity.CRITICAL)
    @allure.description("""
        This test case verifies the functionality of viewing category products on the website.
        1. It verifies that the categories are visible on the left sidebar of the main page.
        2. It clicks on the "Women" category and randomly selects a subcategory link under the "Women" category.
        3. It verifies that the category page is displayed and checks if the "WOMEN PRODUCTS" text is visible.
        4. It then clicks on the "Men" category and randomly selects a subcategory link under the "Men" category.
        5. Finally, it verifies that the user is navigated to the corresponding category page and checks if the "MEN PRODUCTS" text is visible.
    """)

    def test_view_category_products(self, driver):
        main_page = MainPage(driver)
        all_products_page = AllProducts(driver)

        with allure.step("Verify that categories are visible on left side bar"):
            categories_are_visible = main_page.get_categories().values()
            assert all([category.is_displayed() for category in categories_are_visible]), "Categories are not visible on left side bar"
        with allure.step('Click on "Women" category'):
            main_page.click_woman_button()
        with allure.step('Randomly click on any category link under "Women" category'):
            main_page.click_random_woman_subcategory()
        with allure.step('Verify that category page is displayed and text "WOMEN PRODUCTS" text visible'):
            assert all_products_page.is_woman_products_note_visible(), "WOMEN PRODUCTS text is not visible"
        with allure.step('Click on "Men" category'):
            all_products_page.click_men_button()
        with allure.step('Randomly click on any category link under "Men" category'):
            all_products_page.click_random_men_subcategory()
        with allure.step('Verify that user is navigated to that category page'):
            assert all_products_page.is_man_products_note_visible(), "MEN PRODUCTS text is not visible"









