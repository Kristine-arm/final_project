
from src.config.config import TestData
from src.pages.base_element import BaseElement
from src.pages.base_page import BasePage
import allure

@allure.story("Checking contact us page functionality")
class ContactUsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.get_in_touch_text = BaseElement(driver, "//h2[contains(text(), 'Get In Touch')]")
        self.contact_name = BaseElement(driver, '//input[@type="text" and @data-qa="name"]')
        self.contact_email = BaseElement(driver, '//input[@type="email" and @data-qa="email"]')
        self.subject_button = BaseElement(driver, '//input[@name="subject"]')
        self.message_text = BaseElement(driver, '//*[@name="message"]')
        self.choose_file = BaseElement(driver, "//*[@name='upload_file']")
        self.submit_button = BaseElement(driver, '//input[@type="submit" and @data-qa="submit-button"]')
        self.success_message = BaseElement(driver, '//*[@class="status alert alert-success"]')
        self.home_page_button = BaseElement(driver, '//*[@class="btn btn-success"]')

    @allure.step('Check if "get in touch" note is visible')
    def is_get_in_touch_visible(self):
        return self.get_in_touch_text.is_visible()

    def contact_info_form(self):
        self.contact_name.send_keys(TestData.name_contact)
        self.contact_email.send_keys(TestData.email_contact)
        self.subject_button.send_keys(TestData.contact_subject)
        self.message_text.send_keys(TestData.message_info)
        self.choose_file.send_keys(TestData.file_path)
        self.submit_button.click()

    def ok_button_click(self):
        alert = self.driver.switch_to.alert
        alert.accept()
        return self

    @allure.step('Check if success message is visible after form submission')
    def is_success_message_visible(self):
        return self.success_message.is_visible()
    def click_home_button(self):
        self.home_page_button.click()
