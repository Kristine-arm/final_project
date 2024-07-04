import pytest
from src.pages.all_pages.main_page import MainPage
from src.pages.all_pages.login_page import LoginPage
import allure
from src.config.config import TestData
from allure_commons.types import Severity

@pytest.mark.usefixtures("driver")
@allure.feature('Incorrect Login')
class TestIncorrectLogin:

    @allure.story('User Login With Incorrect Password')
    @allure.severity(Severity.CRITICAL)
    @allure.description("""
    Tests the login functionality with incorrect credentials.
    This test will:
    - Navigate to the login page from the main page.
    - Attempt to log in using either an incorrect password with a correct email or a correct password with an incorrect email.
    - Verify that the appropriate error message is displayed for incorrect login attempts.
    """)
    @pytest.mark.parametrize("email,password", [
        (TestData.email_login, TestData.password_incorrect),  #Incorrect password
        (TestData.email_incorrect, TestData.password_login)])  #Incorrect email

    def test_user_incorrect_login(self, driver, email, password):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        with allure.step("Navigate to login page"):
            main_page.signup_login_button.click()
        with allure.step("Enter incorrect login credentials"):
            login_page.make_incorrect_login(email, password)
        with allure.step("Verify error message is visible"):
            assert login_page.is_error_message_visible(), "'Error message' text is not visible after login"