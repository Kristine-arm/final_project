import pytest
from pages.ebay_home_page import EbayHomePage


@pytest.mark.gift_category
def test_gift_cards(driver):
    ebay_home_page = EbayHomePage(driver)
    ebay_home_page.navigate_to_ebay()
    ebay_home_page.gift_cards()
    ebay_home_page.amount_button()
    ebay_home_page.gift_card_delivery()
    ebay_home_page.gift_card_details("Anna", "kristinesargsyants@gmail.com", "This is a gift message.","Me" )


    assert "eBay" in driver.title, "Page title does not contain 'eBay'"
    assert "ebay.com" in driver.current_url, "Current URL is not 'ebay.com'"
