#
#
# import pytest
# from pages.ebay_home_page import EbayHomePage
# from host import page_address
#
# class TestEbayLoginPage:
#     @pytest.mark.parametrize("username, password", [("kristinesargsyants@gmail.com", "Wrongpassword1"),
#                                                      ("kristinesargsyants@gmail.com", "Wrongpassword2"),  ("kristinesargsyants@gmail.com", "abdrakadabraaaaa")])
#     def test_ebay_login_incorrect_password(self, driver, username, password):
#         ebay_home_page = EbayHomePage(driver)
#
#         ebay_home_page.navigate_to_ebay()
#         ebay_home_page.click_sign_in_link()
#         ebay_home_page.enter_credentials(username, password)
#
#         error_message = ebay_home_page.error_message()
#
#         assert "Incorrect Login" in error_message, f"Expected 'Incorrect Login' in error message, but got: {error_message}"

import pytest
from selenium import webdriver
from pages.ebay_home_page import EbayHomePage

class TestEbayLoginPage:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.ebay_home_page = EbayHomePage(self.driver)

    def teardown_method(self, method):
        self.driver.quit()

    @pytest.mark.parametrize("username, password", [
        ("kristinesargsyants@gmail.com", "Wrongpassword1"),
        ("kristinesargsyants@gmail.com", "wrongpassword2"),
        ("kristinesargsyants@gmail.com", "abdrakadabraaaaa")])
    def test_ebay_login_incorrect_password(self, username, password):
        self.ebay_home_page.navigate_to_ebay()
        self.ebay_home_page.click_sign_in_link()
        self.ebay_home_page.enter_credentials(username, password)

        error_message = self.ebay_home_page.error_message()
        assert "Incorrect Login" in error_message, f"Expected 'Incorrect Login' in error message, but got: {error_message}"