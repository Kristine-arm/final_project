from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from src.pages.base_element import BaseElement
from src.pages.base_page import BasePage
import allure
from src.config.config import TestData

@allure.step('Checking product page functionality')
class ProductDetailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.product_information = BaseElement(driver, '//*[@class="product-information"]')
        self.product_name = BaseElement(driver, '//h2[text()="Blue Top"]')
        self.category = BaseElement(driver, '//p[contains(text(), "Category: Women > Tops")]')
        self.price = BaseElement(driver, '//span[text()="Rs. 500"]')
        self.availability = BaseElement(driver, '//*[contains(text(), "In Stock")]')
        self.condition = BaseElement(driver, '//*[contains(text(), "New")]')
        self.brand = BaseElement(driver, '//*[contains(text(), "Polo")]')
        self.quantity_field = BaseElement(driver, '//*[@id="quantity"]')
        self.add_to_cart_button = BaseElement(driver, '//button[@type="button"]')
        self.view_cart_button = BaseElement(driver, '//u[text()="View Cart"]')
        self.write_your_review_note = BaseElement(driver, '//a[text()="Write Your Review"]')
        self.name_review_field = BaseElement(driver, '//*[@id="name"]')
        self.email_review_field = BaseElement(driver, '//*[@id="email"]')
        self.add_review_field = BaseElement(driver, '//*[@id="review"]')
        self.review_submit_button = BaseElement(driver, '//*[@id="button-review"]')
        self.review_thanks_note = BaseElement(driver, '//span[@style="font-size: 20px;"]')


    # @allure.step('Verify product name, category, price, availability, condition, brand')
    # def get_product_details(self):
    #     return {
    #         "name": self.product_name.text(),
    #         "category": self.category.text(),
    #         "price": self.price.text(),
    #         "availability": self.availability.text(),
    #         "condition": self.condition.text(),
    #         "brand": self.brand.text()}

    def get_product_details(self):
        details = {}
        try:
            if self.product_name.is_visible():
                details["name"] = self.product_name.get_text()
            if self.category.is_visible():
                details["category"] = self.category.get_text()
            if self.price.is_visible():
                details["price"] = self.price.get_text()
            if self.availability.is_visible():
                details["availability"] = self.availability.get_text()
            if self.condition.is_visible():
                details["condition"] = self.condition.get_text()
            if self.brand.is_visible():
                details["brand"] = self.brand.get_text()
        except NoSuchElementException:
            pass
        return details

    @allure.step('Check if signup/login button is visible')
    def verify_product_details_opened(self):
        return self.product_information.is_visible()

    @allure.step('Increase quantity to 4')
    def increase_quantity(self, quantity):
        self.quantity_field.clear()
        self.quantity_field.send_keys(quantity)
        return self

    @allure.step('Click "Add to cart" button')
    def add_to_cart_button_click(self):
        self.add_to_cart_button.click()
        return self

    @allure.step('Click "View Cart" button')
    def view_cart_button_click(self):
        self.view_cart_button.click()
        return self

    @allure.step('Verify "Write Your Review" is visible')
    def is_write_your_review_note_visible(self):
        return self.write_your_review_note.is_visible()

    @allure.step('Enter name, email and review')
    def fill_review(self):
        self.name_review_field.send_keys(TestData.review_name)
        self.email_review_field.send_keys(TestData.review_email)
        self.add_review_field.send_keys(TestData.review_text)
        self.review_submit_button.click()

    def is_thank_you_message_visible(self):
        try:
            success_message = self.driver.find_element(By.XPATH, '//span[@style="font-size: 20px;"]')
            return "Thank you for your review." in success_message.text
        except NoSuchElementException:
            return False

