import pytest
from selenium import webdriver
from pages.ebay_home_page import EbayHomePage
from host import page_address

def test_ebay_login(driver):
    driver.get(page_address)  # Opening eBay main page directly

    ebay_home_page = EbayHomePage(driver)
    ebay_home_page.click_sign_in_link()
    ebay_home_page.enter_credentials("kristinesargsyants@gmail.com", "Ebay1111!")
    #ebay_home_page.click_sign_in_button()
    print('succes')


# def test_ebay_incorrect_password(driver):
#     driver.get(page_address)
#     ebay_home_page = EbayHomePage(driver)
#     ebay_home_page.click_sign_in_link()
#     ebay_home_page.enter_credentials("kristinesargsyants@gmail.com", "Ebay11!")
#     ebay_home_page.error_message()
#     print('bad')

# Assertion - Check if a logout link appears after successful login
#     logout_link = driver.find_element_by_xpath("//a[contains(text(), 'Logout')]")
#     assert logout_link.is_displayed(), "Login was unsuccessful or Logout link not found after login."




