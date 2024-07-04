import pytest
from src.pages.all_pages.all_products_page import AllProducts
from src.pages.all_pages.main_page import MainPage
from allure_commons.types import Severity
import allure
from src.pages.all_pages.product_detail_page import ProductDetailPage

@pytest.mark.usefixtures("driver")
@allure.feature('Products')
class TestProductSearch:

    @allure.story('Add review on product')
    @allure.severity(Severity.MINOR)
    @allure.description("""
    This test case verifies the functionality of adding a review on a product.
    Steps:
    Navigate to the main page.
    Navigate to the products page.
    Select a product from the list of products.
    Fill in the review details (name, email, review text).
    Submit the review.
    Verify that the success message "Thank you for your review" is displayed.
    """)
    def test_add_review_on_product(self, driver):
        main_page = MainPage(driver)
        all_products_page = AllProducts(driver)
        product_detail_page = ProductDetailPage(driver)

        with allure.step('Verify that home page is visible successfully'):
            assert main_page.is_home_button_visible(), "'Home' button was not visible after navigating to the Main Page."
        with allure.step('Click on Products button'):
            main_page.go_to_products_page()
        with allure.step('Verify user is navigated to ALL PRODUCTS page successfully'):
            assert all_products_page.is_all_products_note_visible(), "'All Products' text was not visible after navigating to the Products Page."
        with allure.step('Click on "View Product" of first product'):
            all_products_page.view_product()
        with allure.step('Verify "Write Your Review" is visible'):
            product_detail_page.is_write_your_review_note_visible()
        with allure.step('Enter name, email and review'):
            product_detail_page.fill_review()
        with allure.step("Verify success message 'Thank you for your review.'"):
            assert product_detail_page.is_thank_you_message_visible(), "Success message 'Thank you for your review.' is not visible"



