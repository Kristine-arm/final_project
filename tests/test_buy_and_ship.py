
import time
from telnetlib import EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.ebay_home_page import EbayHomePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

test_data = [
    {
        "email": "ksargsyants@gmail.com",
        "first_name": "Ana",
        "last_name": "whatever",
        "street_line": "Bogkiego St 13",
        "city": "Rzeszow",
        "postal_code": "",
        "phone_number": "222-333-555"
    },
]
@pytest.mark.parametrize("user_data", test_data)
def test_buy_item_and_ship(driver, user_data):
    ebay_home_page = EbayHomePage(driver)
    ebay_home_page.navigate_to_ebay()
    ebay_home_page.search_for_item("mouse")
    ebay_home_page.go_fifth_page()
    ebay_home_page.take_item()
    ebay_home_page.buy_it_now()
    ebay_home_page.check_out_as_guest()
    ebay_home_page.shipping_credentials(**user_data)

    add_new_cart_button_locator = (By.XPATH, '//*[@id="mainContent"]/div[3]/div/div[1]/section[2]/div/div/div[1]/span/span/a')

    try:
        add_new_cart_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(add_new_cart_button_locator)
        )
        add_new_cart_button.click()
    except TimeoutException:
        pass
    #URL for debugging purposes
    print(driver.current_url)

    assert add_new_cart_button is not None, "Confirmation button not found on the page"

