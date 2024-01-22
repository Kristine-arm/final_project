import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.ebay_home_page import EbayHomePage
from selenium.webdriver.common.by import By

def test_search_item(driver):
    ebay_home_page = EbayHomePage(driver)
    ebay_home_page.navigate_to_ebay()
    ebay_home_page.search_for_item("laptop")
    ebay_home_page.click_nth_search_result(2)