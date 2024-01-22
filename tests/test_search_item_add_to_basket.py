
import pytest
from selenium import webdriver
from pages.ebay_home_page import EbayHomePage

class TestEbayHomePage:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.ebay_home_page = EbayHomePage(self.driver)

    def teardown_method(self, method):
        self.driver.quit()

    @pytest.mark.parametrize("item_name", ["mouse", "phone"])
    def test_search_item_and_add_to_basket(self, item_name):
        self.ebay_home_page.navigate_to_ebay()
        self.ebay_home_page.search_for_item(item_name)
        self.ebay_home_page.click_nth_search_result(2)
        self.ebay_home_page.adding_item_mouse_to_cart()
        self.ebay_home_page.check_go_to_cart()
        self.ebay_home_page.check_basket_items()

        num_items_in_basket = self.ebay_home_page.check_basket_items()
        assert num_items_in_basket is not None and num_items_in_basket >= 1, f"Expected at least 1 item in the basket, but found {num_items_in_basket}"

