
import pytest
from src.pages.all_pages.login_page import LoginPage
from src.pages.all_pages.main_page import MainPage
from allure_commons.types import Severity
import allure

@pytest.mark.usefixtures("driver")
@allure.feature('Registration')
class TestUserRegistration:

    @allure.story('Register User')
    @allure.severity(Severity.CRITICAL)
    @allure.description("""
        This test case automates the user registration process on a web platform with the following steps:
        1. Verifying the visibility of the home page to ensure the initial landing page is correctly displayed.
        2. Navigating to the signup/login section to begin the registration process.
        3. Confirming the visibility of the 'New User Signup!' note, indicating the signup page is accessible.
        4. Filling out the registration form with user details and submitting it.
        5. Checking for a confirmation message that the account has been created successfully.
        6. Logging in with the newly created account to verify successful registration and session initiation.
        7. Deleting the newly created account to confirm the account deletion functionality and cleanup post-test.""")

    def test_user_registration(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)


        with allure.step('Verify that home page is visible successfully'):
            assert main_page.is_home_button_visible(), "'Home' button was not visible after navigating to the Main Page."
        with allure.step("Click on signup/login button"):
            main_page.signup_login_button.click()
        with allure.step('Verify "New User Signup!" is visible'):
            login_page.is_new_user_signup_note_visible(), "'New User Signup!' note is not visible"
        with allure.step('Fill all details in Signup and create account'):
            login_page.make_registration()
            login_page.fill_account_info()
        with allure.step('Verify "ACCOUNT CREATED!" and click "Continue" button'):
            assert login_page.is_account_created_note_visible(), "Account Created note is not visible"
            login_page.clicking_continue_button()
        with allure.step('Verify "Logged in as username" at top'):
            assert login_page.is_logged_in_as_note_visible(), "'Logged In As' note is not visible"
        with allure.step('Click "Delete Account" button'):
            login_page.delete_account()
        with allure.step(' Verify "ACCOUNT DELETED!" and click "Continue" button'):
            assert login_page.is_account_deleted_note_visible()