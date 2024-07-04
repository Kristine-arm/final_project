from src.pages.all_pages.main_page import MainPage
from src.pages.all_pages.login_page import LoginPage
import allure
import pytest
from allure_commons.types import Severity

@pytest.mark.usefixtures("driver")
@allure.feature('Login')
class TestLoginLogout:
    @allure.story('User Login With Correct Credentials')
    @allure.severity(Severity.CRITICAL)
    @allure.description("""
    Verifies the login and logout process with correct user credentials.
    This test covers:
    - Navigating to the login page by clicking the signup/login button.
    - Checking if the 'Login your account' text is visible to ensure the user is on the correct page.
    - Performing the login operation with valid credentials.
    - Logging out from the account after a successful login.
    - Ensuring that the Signup/Login button is visible post-logout, indicating the user was successfully logged out.
    """)
    def test_user_login_logout(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        with allure.step("Click on signup/login button"):
            main_page.signup_login_button.click()
        with allure.step("'Login your account' text is visible"):
            assert login_page.is_login_your_account_visible(), "'Login your account' text is not visible after press login"
        with allure.step("Perform login"):
            login_page.make_login()
        with allure.step("Log out from account"):
            login_page.make_logout()
        with allure.step("Signup/Login button is visible"):
            assert main_page.is_signup_login_button_visible(), "Signup/Login button is not visible after deleting the account"
