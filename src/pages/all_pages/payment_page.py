
from src.config.config import TestData
from src.pages.base_element import BaseElement
from src.pages.base_page import BasePage
import allure
import os
@allure.story("Checking payment page functionality")
class PaymentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.name_on_card_field = BaseElement(driver, '//*[@name="name_on_card"]')
        self.card_number_field = BaseElement(driver, '//*[@name="card_number"]')
        self.cvc_field = BaseElement(driver, '//*[@name="cvc"]')
        self.expiry_month_field = BaseElement(driver, '//*[@name="expiry_month"]')
        self.expiry_year_field = BaseElement(driver, '//*[@name="expiry_year"]')
        self.pay_and_confirm_button = BaseElement(driver, '//*[@data-qa="pay-button"]')
        self.order_placed_success_note = BaseElement(driver, '//p[@style="font-size: 20px; font-family: garamond;" and contains(text(), "Congratulations! Your order has been confirmed!")]')
        self.delete_account_button = BaseElement(driver, '//a[contains(@href, "/delete_account")]')
        self.account_deleted_note = BaseElement(driver, '//b[contains(text(), "Account Deleted!")]')
        self.continue_button = BaseElement(driver, '//a[@data-qa="continue-button"]')
        self.download_invoice_button = BaseElement(driver, '//a[@href="/download_invoice/500"]')


    @allure.step('Enter payment details')
    def filling_card_field_and_paying(self):
        self.name_on_card_field.send_keys(TestData.card_name)
        self.card_number_field.send_keys(TestData.card_number)
        self.cvc_field.send_keys(TestData.cvc)
        self.expiry_month_field.send_keys(TestData.expiry_month)
        self.expiry_year_field.send_keys(TestData.expiry_year)

    @allure.step('Click "Pay and Confirm Order" button')
    def pay_and_click_confirm(self):
        self.pay_and_confirm_button.click()

    @allure.step('Verify success message "Your order has been placed successfully!"')
    def verify_order_success_message(self):
        self.order_placed_success_note.wait_until_visible()  # Utilize BaseElement's built-in wait functionality
        return self.order_placed_success_note.get_text()

    @allure.step('Click "Delete Account" button')
    def clicking_account_delete_button(self):
        self.delete_account_button.click()

    @allure.step('Verify "ACCOUNT DELETED!" and click "Continue" button')
    def is_account_deleted_note_visible(self):
        self.account_deleted_note.wait_until_visible()
        return self.account_deleted_note.is_visible()

    @allure.step('Click "Continue" button')
    def clicking_continue_button(self):
        self.continue_button.click()

    @allure.step('Download and verify the invoice is downloaded successfully')
    def download_and_verify_invoice(self, download_dir):
        self.download_invoice_button.click()
        expected_file_name = "invoice.txt"  # Updated to the correct file name
        file_path = os.path.join(download_dir, expected_file_name)
        for _ in range(30):
            if os.path.exists(file_path):
                print("Invoice downloaded successfully.")
                return True
        print("Failed to download the invoice.")
        return False


