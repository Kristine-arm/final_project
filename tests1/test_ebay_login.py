
from selenium import webdriver
from pages.ebay_home_page import EbayHomePage
from host import page_address
import pytest
@pytest.mark.login
def test_ebay_login(driver):
    driver.get(page_address)  # Opening eBay main page directly

    ebay_home_page = EbayHomePage(driver)
    ebay_home_page.click_sign_in_link()
    ebay_home_page.enter_credentials("kristinesargsyants@gmail.com", "Ebay1111!")

    kristine_name_present = ebay_home_page.is_kristine_name_present()
    assert kristine_name_present, "Login was unsuccessful or kristine not found after login."

    print('success')
