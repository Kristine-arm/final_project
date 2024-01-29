import pytest
from src.pages.main.main_page import MainPage
from src.pages.login.login_page import UserIncorrectLogin
import allure

class Test_Login_Incorrect():

    @allure.story('User Login With Incorrect Credentials')
    @pytest.mark.parametrize("email, password", [
        ("incorrect_email1@example.com", "incorrect_password1"),
        ("incorrect_email2@example.com", "incorrect_password2"),
        ("incorrect_email3@example.com", "incorrect_password3")])

    def test_user_login_incorrect(self, driver, email, password):
        main_page = MainPage(driver)
        login_page = UserIncorrectLogin(driver)

        assert main_page.is_signup_login_button_visible(), "Signup/Login button is not visible after deleting the account"
        with allure.step("Click on signup/login button"):
            main_page.signup_login_button.click()
        with allure.step("Enter incorrect login credentials"):
            login_page.make_incorrect_login(email, password)

        error_message_visible = login_page.is_error_message_visible()
        assert error_message_visible, "'Login your account' text is not visible after login"