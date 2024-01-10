# import pytest
# from selenium import webdriver
# from pages.ebay_home_page import EbayHomePage
#
# def test_search_item_and_add_to_basket(driver):
#     ebay_home_page = EbayHomePage(driver)
#
#     # Search for an item and click the second search result
#     ebay_home_page.navigate_to_ebay()
#     ebay_home_page.search_for_item("laptop")
#     ebay_home_page.click_nth_search_result(2)
#
#     # Add the item to the basket
#     item_added = ebay_home_page.add_to_basket()  # Create this method in your EbayHomePage class
#     item_count = ebay_home_page.check_basket_items()
#     if item_count > 0:
#         print(f"Items found in the basket: {item_count}")
#     else:
#         print("No items in the basket")

import time
from telnetlib import EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.ebay_home_page import EbayHomePage
from selenium.webdriver.support import expected_conditions as EC

# def test_search_item_and_add_to_basket(driver):
#     ebay_home_page = EbayHomePage(driver)
#
#     # Search for an item and click the second search result
#     ebay_home_page.navigate_to_ebay()
#     ebay_home_page.search_for_item("laptop")
#     ebay_home_page.click_nth_search_result(2)
#
#     # Add the item to the basket
#     item_added = ebay_home_page.add_to_basket() # Create this method in your EbayHomePage class
#     time.sleep(10)
#     item_go_to_cart = ebay_home_page.check_go_to_cart()
#     # Check the basket's item count after adding the item
#     ebay_home_page.check_basket_items()
# '''
#     if item_added:
#         if item_count > 0:
#             print(f"Item successfully added to the basket. Items found in the basket: {item_count}")
#         else:
#             print("Item added, but there are no items in the basket")
#     else:
#         print("Failed to add the item to the basket")
#
#     # Additional console logs for debugging
#     print(f"Item added to basket: {item_added}")
#     print(f"Current item count in basket: {item_count}")
# '''
def test_search_item_and_add_to_basket(driver):
    ebay_home_page = EbayHomePage(driver)

    # Search for an item and click the second search result
    ebay_home_page.navigate_to_ebay()
    ebay_home_page.search_for_item("laptop")
    ebay_home_page.click_nth_search_result(2)

    # Add the item to the basket
    item_added = ebay_home_page.add_to_basket()  # Create this method in your EbayHomePage class
    #time.sleep(10)

    # Check the basket's item count after adding the item
    item_count = ebay_home_page.check_basket_items()
    print(f"Current item count in basket: {item_count}")