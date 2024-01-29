import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException  # Import TimeoutException
from pages.ebay_home_page import EbayHomePage

def test_check_basket(driver):
    ebay_home_page = EbayHomePage(driver)

    # Check if items are present in the basket and get the count
    item_count = ebay_home_page.check_basket_items()
    if item_count > 0:
        print(f"Items found in the basket: {item_count}")
    else:
        print("No items in the basket")
