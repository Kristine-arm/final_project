
from src.pages.base_element import BaseElement
from src.pages.base_page import BasePage
from src.config.config import TestData
import allure
import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.signup_login_button = BaseElement(driver, '//*[@class="fa fa-lock"]')
        self.contact_us_button = BaseElement(driver, '//a[@href= "/contact_us"]')
        self.test_cases_button = BaseElement(driver, '//a[@href = "/test_cases"]')
        self.home_button = BaseElement(driver, '//*[@class="fa fa-home"]')
        self.products_button = BaseElement(driver, '//a[@href= "/products"]')
        self.cart_button = BaseElement(driver, '//a[@href="/view_cart"]')
        self.copyright = BaseElement(driver, '//*[@class="pull-left"]')
        self.subscription_note = BaseElement(driver, '//*[contains(text(), "Subscription")]')
        self.subscription_field = BaseElement(driver, '//*[@id = "susbscribe_email"]')
        self.subscription_button = BaseElement(driver, '//*[@class="fa fa-arrow-circle-o-right"]')
        self.subscription_success = BaseElement(driver, '//*[@class="alert-success alert"]')
        self.first_product = BaseElement(driver, '(//*[@class="col-sm-4"])[2]')
        self.add_to_cart_first_product = BaseElement(driver, "(//a[@data-product-id='1'])[2]")
        self.continue_shopping_button = BaseElement(driver,'//button[contains(@class, "close-modal") and contains(text(), "Continue Shopping")]')
        self.view_cart_button = BaseElement(driver, '//u[contains(text(), "View Cart")]')
        self.categories = BaseElement(driver, '//*[@class="panel panel-default"]')
        self.category_woman_x = BaseElement(driver, '//*[@id="accordian"]/div[1]/div[1]/h4/a/span/i')
        self.category_man_x = BaseElement(driver, '//*[@id="accordian"]/div[2]/div[1]/h4/a/span/i')
        self.category_kids_x = BaseElement(driver, '//*[@id="accordian"]/div[3]/div[1]/h4/a/span/i')
        self.dress_button = BaseElement(driver, '//a[contains(@href, "/category_products/1")]')
        self.tops_button = BaseElement(driver, '//a[contains(@href, "/category_products/2")]')
        self.random_category = BaseElement(driver, '(//a[@href="/category_products/1" and normalize-space()="Dress"]')
        self.recommended_items = BaseElement(driver, '//*[@id="recommended-item-carousel"]')
        self.first_recommended_item = BaseElement(driver, '(//*[@data-product-id="4"])[3]')
        self.second_recommended_item = BaseElement(driver, '(//*[@data-product-id="1"])[3]')
        self.yellow_bottom_arrow = BaseElement(driver, '//*[@id="scrollUp"]')
        self.full_fledged_text = BaseElement(driver, '//h2[text()="Full-Fledged practice website for Automation Engineers"]' )
        self.permission_button = BaseElement (driver, '//p[@class="fc-button-label" and text()="Соглашаюсь"]')

    @allure.step('Check if signup/login button is visible')
    def is_signup_login_button_visible(self):
        return self.signup_login_button.is_visible()


    @allure.step('Check if it is a main page')
    def is_on_main_page(self):
        return self.driver.current_url == self.MAIN_URL

    @allure.step('Check if Home button is visible')
    def is_home_button_visible(self):
        return self.home_button.is_visible()

    @allure.step('Click on "Products" button')
    def go_to_products_page(self):
        self.products_button.click()

    @allure.step("Navigate to the bottom of the page")
    def navigate_and_scroll_to_bottom(self):
        self.copyright.scroll_into_view()

    @allure.step('Verify text "SUBSCRIPTION"')
    def is_subscription_note_visible(self):
        return self.subscription_note.is_visible()

    @allure.step("Make a subscription with provided email")
    def make_subscription(self):
        self.subscription_field.send_keys(TestData.email_incorrect)
        self.subscription_button.click()

    @allure.step('Get subscription success message')
    def get_subscription_success_message(self):
        try:
            return self.subscription_success.get_text()
        except TimeoutException:
            return None

    @allure.step('Click "View Product" of random product on main page')
    def select_random_view_product(self):
        try:
            n = random.randint(1, 34)
            self.random_view_product_button = BaseElement(self.driver, '(//*[@class="fa fa-plus-square"])[' + str(n) + ']')
            self.random_view_product_button.click()
        except TimeoutException as e:
            raise AssertionError("Random view product could not be clicked.") from e

    @allure.step('Click "Cart Button" on main page')
    def click_cart_button(self):
        self.cart_button.click()

    @allure.step("Hover over the first product and click 'Add to Cart'")
    def hover_and_add_first_product_to_cart(self):
        self.first_product.hover()
        time.sleep(2)
        self.add_to_cart_first_product.click()
        time.sleep(2)
        self.continue_shopping_button.click()

    @allure.step("Hover over the second product and click 'Add to Cart'")
    def hover_and_add_product_to_cart(self):
        self.first_product.hover()
        self.add_to_cart_first_product.click()
        self.view_cart_button.click()

    @allure.step('Verify product categories')
    def get_categories(self):
        return {
            "woman": self.category_woman_x,
            "man": self.category_man_x,
            "kids": self.category_kids_x}

    @allure.step('Click on "Women" category')
    def click_woman_button(self):
        self.category_woman_x.click()

    @allure.step('Randomly click on any category')
    def click_random_woman_subcategory(self):
        n = random.randint(1, 3)
        self.choose_random_category = BaseElement(self.driver, '//*[@id="Women"]/div/ul/li[' + str(n) + ']/a')
        self.choose_random_category.click()

    @allure.step("Navigate to the bottom of the page")
    def navigate_and_scroll_to_bottom(self):
        self.subscription_button.scroll_into_view()

    @allure.step('Verify text "SUBSCRIPTION"')
    def is_recommended_items_visible(self):
        return self.recommended_items.is_visible()

    @allure.step('Click on "Add To Cart" on Recommended product, later click "View Cart" button')
    def click_on_rec_product(self):
        if self.driver.find_element(By.XPATH, '(//*[@data-product-id="4"])[3]'):
            self.first_recommended_item.click()
        elif self.driver.find_element(By.XPATH, '(//*[@data-product-id="1"])[3]'):
            self.second_recommended_item.click()
        self.view_cart_button.click()

    @allure.step('Click on arrow at bottom right side to move upward')
    def click_on_bottom_arrow(self):
        self.yellow_bottom_arrow.click()

    @allure.step('Verify "Full-Fledged practice website for Automation Engineers" text is visible')
    def is_full_fledged_text_visible(self):
        return self.full_fledged_text.is_displayed()

    def is_page_scrolled_up(self):
        value = self.driver.execute_script("return window.pageYOffset;")
        return value < 2500

    @allure.step("Scroll up page to top")
    def navigate_and_scroll_to_top(self):
        self.home_button.scroll_into_view()

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


