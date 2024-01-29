
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.ebay_home_page import EbayHomePage
from conftest import driver
import time

class TestEbayWatchlist:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.ebay_home_page = EbayHomePage(self.driver)

    def teardown_method(self, method):
        self.driver.quit()
def test_filters_watchlist(driver):
    ebay_home_page = EbayHomePage(driver)
    ebay_home_page.navigate_to_ebay()
    ebay_home_page.search_for_item("bag" )
    ebay_home_page.filter_by_brand_style_material_color()
    #ebay_home_page.go_second_page()
    ebay_home_page.take_first_item()
    ebay_home_page.add_to_watchlist()
    ebay_home_page.enter_credentials("kristinesargsyants@gmail.com", "Ebay1111!")
    time.sleep(5)
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="watchWrapperId"]')))

    ebay_home_page.check_watchlist()

    element_xpath = '//*[@id="s0-0-35-0-6-m-carousel-list"]/li[1]/a'
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, element_xpath)))

    assert driver.find_element(By.XPATH, element_xpath).is_displayed(), "Element is not present on the page"