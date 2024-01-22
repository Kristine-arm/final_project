from pages.ebay_home_page import EbayHomePage
import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call, __multicall__):
    outcome = __multicall__.execute()

    if outcome.get_result().outcome == 'failed':
        driver = item.funcargs['driver']
        screenshot_path = f"tests/screenshot_{item.nodeid.replace('::', '_')}.png"
        driver.save_screenshot(screenshot_path)
    return outcome
@pytest.mark.gift_category
def test_gift_cards(driver):
    ebay_home_page = EbayHomePage(driver)
    ebay_home_page.navigate_to_ebay()
    ebay_home_page.gift_cards()
    ebay_home_page.amount_button()
    ebay_home_page.gift_card_delivery()
    ebay_home_page.gift_card_details("Anna", "kristinesargsyants@gmail.com", "This is a gift message.", "Me")

    assert "eBay" in driver.title, "Page title does not contain 'eBay'"
    assert "ebay.com" in driver.current_url, "Current URL is not 'ebay.com'"