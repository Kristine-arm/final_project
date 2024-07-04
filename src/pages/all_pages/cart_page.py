import time
from src.config.config import TestData
from src.pages.base_element import BaseElement
from src.pages.base_page import BasePage
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.cart_button = BaseElement(driver, '//a[@href="/view_cart"]')
        self.copyright = BaseElement(driver, '//*[@class="pull-left"]')
        self.subscription_note = BaseElement(driver, '//*[contains(text(), "Subscription")]')
        self.subscription_field = BaseElement(driver, '//*[@id = "susbscribe_email"]')
        self.subscription_button = BaseElement(driver, '//*[@class="fa fa-arrow-circle-o-right"]')
        self.subscription_success = BaseElement(driver, '//*[@class="alert-success alert"]')
        self.product_names = BaseElement(driver, '//*[@class="cart_description"]')
        self.product_prices = BaseElement(driver, '//*[@class="cart_price"]')
        self.product_quantities = BaseElement(driver, '//*[@class="cart_quantity"]')
        self.total_prices = BaseElement(driver, '//*[@class="cart_total_price"]')
        self.final_product_quantity = BaseElement(driver, '//*[@class="disabled"]')
        self.proceed_to_checkout = BaseElement(driver, '//*[@class="btn btn-default check_out"]')
        self.register_login_button = BaseElement(driver, '//a[u/text()="Register / Login"]')
        self.x_button = BaseElement(driver,"//i[@class='fa fa-times']")
        self.product_removed_note = BaseElement(driver, '//p[@class="text-center" and contains(., "Cart is empty!")]')
        self.product_name = BaseElement(driver, '//*[@class="description"]')

    @allure.step('Click "Cart" button')
    def clicking_cart_button(self):
        self.cart_button.click()

    @allure.step('Check if it is a cart page')
    def is_on_cart_page(self):
        return self.driver.current_url == self.CART_URL

    @allure.step('Click "CheckOut" button')
    def clicking_checkout(self):
        self.proceed_to_checkout.click()

    @allure.step('Click "Register/Logout" button')
    def clicking_register_login(self):
        self.register_login_button.click()

    @allure.step('Verify text "SUBSCRIPTION"')
    def is_subscription_note_visible(self):
        return self.subscription_note.is_visible()

    @allure.step("Make a subscription with provided email")
    def make_subscription(self):
        self.subscription_field.send_keys(TestData.email_incorrect)
        self.subscription_button.click()

    @allure.step("Navigate to the bottom of the page")
    def navigate_and_scroll_to_bottom(self):
        self.copyright.scroll_into_view()


    @allure.step('Get names of products in cart')
    def get_product_names(self):
        return self.product_names.get_elements_text()

    def get_prices(self):
        price_texts = self.product_prices.get_elements_text()
        prices = [float(price_text.replace('Rs.', '').strip()) for price_text in price_texts]
        return prices

    @allure.step('Get quantities of products in cart')
    def get_quantities(self):
        return self.product_quantities.get_elements_text()

    def get_total_prices(self):
        total_price_texts = self.total_prices.get_elements_text()
        total_prices = [float(total_price_text.replace('Rs.', '').strip()) for total_price_text in total_price_texts]
        return total_prices

    @allure.step("Hover over the first product and click 'Add to Cart'")
    def hover_and_add_first_product_to_cart(self):
        self.first_product.hover()
        time.sleep(2)
        self.add_to_cart_first_product.click()
        time.sleep(2)
        self.continue_shopping_button.click()

    @allure.step('Remove all products from the cart')
    def remove_all_products_from_cart(self):
        x_buttons = self.x_button.locating_elements()
        for button in x_buttons:
            button.click()
            time.sleep(1)

    @allure.step('Get empty cart text')
    def get_empty_cart_text(self):
        return self.product_removed_note.get_text()

    @allure.step("Get product names")
    def get_product_names(self):
        product_name_elements = self.driver.find_elements(By.XPATH, "//td[contains(@class, 'cart_description')]//a")
        product_names = [element.text for element in product_name_elements]
        return product_names

    @allure.step("Click 'Cart' button and verify that products are visible in cart")
    def click_cart_button_and_verify_that_products_are_visible_in_cart(self, products_names):
        products_names_added = self.get_product_names()
        for product_name in products_names:
            assert product_name in products_names_added, f"Product '{product_name}' not found in cart"
            print(f"Product '{product_name}' is visible in cart")

    def get_subscription_alert_text(self):
        alert_element = self.driver.find_element(By.XPATH, '//*[@class="alert-success alert"]')
        return alert_element.text.strip() if alert_element else None

    def wait_for_subscription_alert_visibility(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@class="alert-success alert"]')))
            return True
        except TimeoutException:
            return False

