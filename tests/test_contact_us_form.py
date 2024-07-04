
from src.pages.all_pages.main_page import MainPage
from src.pages.all_pages.contact_us_page import ContactUsPage
import allure
import pytest
from allure_commons.types import Severity

@pytest.mark.usefixtures("driver")
@allure.feature('Contact Us Form')
class TestContactUs:

    @allure.story('Submission Verification')
    @allure.severity(Severity.MINOR)
    @allure.description("""
        This test case verifies the functionality of the 'Contact Us' form on the website.
        The steps included are:
        - Navigating to the 'Contact Us' section from the main page.
        - Verifying that the 'Get in touch' header is visible to ensure the user is on the correct page.
        - Filling out the 'Contact Us' form with predefined information.
        - Submitting the form and confirming the submission by clicking the OK button.
        - Checking for a success message to confirm that the form was submitted properly.
        - Returning to the home page to ensure the website navigation remains intact after form submission.
        """)
    def test_contact_us(self, driver):
        main_page = MainPage(driver)
        contact_us_page = ContactUsPage(driver)

        with allure.step("Click 'Contact Us' button"):
            main_page.contact_us_button.click()
        with allure.step('Verify "Get in touch" note is visible'):
            assert contact_us_page.is_get_in_touch_visible(), "'Get in touch' note is not visible after pressing Contact Us"
        with allure.step("Fill 'Contact Us' form"):
            contact_us_page.contact_info_form()
        with allure.step("Clicking OK button"):
            contact_us_page.ok_button_click()
        with allure.step("Verify success message visibility"):
            assert contact_us_page.is_success_message_visible(), "Success message was not visible after form submission."
        with allure.step("Click 'Home' button and verify landing on the home page"):
            contact_us_page.click_home_button()
        with allure.step("Verify landing on the home page"):
            assert main_page.is_on_main_page(), "Did not navigate back to the home page successfully."
