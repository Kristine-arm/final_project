from src.pages.all_pages.main_page import MainPage
from src.pages.all_pages.login_page import LoginPage
from allure_commons.types import Severity
import allure
import pytest

@pytest.mark.usefixtures("driver")
@allure.feature('Registration With existing Email')
class TestRegistrationWithExistEmail:

    @allure.story('User Registration With Existing Email')
    @allure.severity(Severity.CRITICAL)
    @allure.description("""
    Test the registration process using an already registered email address.
    This test will:
    - Ensure that the home page is visible upon navigation.
    - Navigate to the signup/login page.
    - Confirm that the 'New User Signup!' section is visible.
    - Attempt to register with a name and an email that is already in use.
    - Verify that an error message stating 'Email Address already exist!' is displayed.
    """)

    def test_user_registration_and_deleting(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        with allure.step("Verify that home page is visible successfully"):
            assert main_page.is_signup_login_button_visible(), "Home page is not visible successfully"
        with allure.step("Click on signup/login button"):
            main_page.signup_login_button.click()
        with allure.step("Verify 'New User Signup!' is visible"):
            assert login_page.is_new_user_signup_note_visible(), "'New User Signup!' is not visible"
        with allure.step("Enter name and already registered email address, and press signup"):
            login_page.registration_with_existing_email()
        with allure.step("Verify error 'Email Address already exist!' is visible"):
            assert login_page.is_email_exist_note_visible(), "'Email Address already exist!' is not visible"







