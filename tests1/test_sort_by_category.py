
import pytest
from pages.ebay_home_page import EbayHomePage

@pytest.mark.shop_category
def test_shop_by_random_category(driver):
    ebay_home_page = EbayHomePage(driver)
    ebay_home_page.navigate_to_shop_by_category()

    assert "ebay.com" in driver.current_url, "Failed to navigate to a random category page"