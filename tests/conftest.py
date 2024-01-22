import pytest
from selenium import webdriver
from pages.ebay_home_page import EbayHomePage


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def ebay_home_page(driver):
    return EbayHomePage(driver)


@pytest.fixture
def setup_teardown(driver):
    ebay_home_page = EbayHomePage(driver)
    ebay_home_page.navigate_to_ebay()
    yield ebay_home_page