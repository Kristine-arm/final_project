
from src.config.config import TestData
from src.pages.base_element import BaseElement
from src.pages.base_page import BasePage
import allure

class CheckOutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.address_delivery = BaseElement(driver, '//ul[@id="address_delivery"]/li')
        self.address_invoice = BaseElement(driver, '//ul[contains(@id, "address_invoice")]//li')
        self.comment_field = BaseElement(driver, '//*[@name="message"]')
        self.place_order_button = BaseElement(driver,'//a[@class="btn btn-default check_out" and text()="Place Order"]')
        self.total_amount = BaseElement(driver,'//some_xpath_for_total_amount')
        self.order_details = BaseElement(driver,'a[href="/payment"]')
        self.product_names = BaseElement(driver, '//*[@class="cart_description"]')
        self.product_prices = BaseElement(driver, '//*[@class="cart_price"]')
        self.product_quantities = BaseElement(driver, '//*[@class="cart_quantity"]')
        self.total_prices = BaseElement(driver, '//*[@class="cart_total_price"]')
        self.delete_account_button = BaseElement(driver, '//a[contains(@href, "/delete_account")]')
        self.account_deleted_note = BaseElement(driver, '//b[contains(text(), "Account Deleted!")]')

    @allure.step('Get delivery address')
    def get_address_delivery(self):
        elements = self.address_delivery.locating_elements()
        return [element.text for element in elements][1:]

    @allure.step('Get invoice address')
    def get_address_invoice(self):
        elements = self.address_invoice.locating_elements()
        return [element.text for element in elements][1:]

    @allure.step('Verify address details')
    def verify_address_details(self):
        delivery_addresses = self.get_address_delivery()
        billing_addresses = self.get_address_invoice()
        return delivery_addresses, billing_addresses

    @allure.step('Get names of products in cart')
    def get_product_names(self):
        return self.product_names.get_elements_text()

    @allure.step('Get prices of products in cart')
    def get_prices(self):
        price_texts = self.product_prices.get_elements_text()
        prices = [float(price_text.replace('Rs.', '').strip()) for price_text in price_texts]
        return prices

    @allure.step('Get quantities of products in cart')
    def get_quantities(self):
        return self.product_quantities.get_elements_text()

    @allure.step('Get total prices of products in cart')
    def get_total_prices(self):
        total_price_texts = self.total_prices.get_elements_text()
        total_prices = [float(total_price_text.replace('Rs.', '').strip()) for total_price_text in total_price_texts]
        return total_prices

    @allure.step('Review Your Order details')
    def review_order_details(self):
        product_names = self.get_product_names()
        product_prices = self.get_prices()
        product_quantities = [int(qty) for qty in self.get_quantities()]
        total_prices = self.get_total_prices()
        for name, price, quantity, total_price in zip(product_names, product_prices, product_quantities, total_prices):
            expected_total = quantity * price
            assert expected_total == total_price, f"Mismatch in total price for {name}. Expected: {expected_total}, Found: {total_price}"
        return {
            'product_names': product_names,
            'product_prices': product_prices,
            'product_quantities': product_quantities,
            'total_prices': total_prices}

    @allure.step('Enter description in comment text area and click "Place Order"')
    def write_comment_and_press_place_order(self):
        self.comment_field.send_keys(TestData.comment_message)
        self.place_order_button.click()

    @allure.step('Click "Delete Account" button')
    def clicking_account_delete_button(self):
        self.delete_account_button.click()

    @allure.step('Verify "ACCOUNT DELETED!" and click "Continue" button')
    def is_account_deleted_note_visible(self):
        self.account_deleted_note.wait_until_visible()
        return self.account_deleted_note.is_visible()





