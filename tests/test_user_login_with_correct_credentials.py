from src.pages.main.main_page import MainPage
from src.pages.login.login_page import UserCorrectLogin
import allure

class Test_Login_Correct():
    @allure.story('User Login With Correct Credentials')
    def test_user_login_correct(self, driver):
        main_page = MainPage(driver)
        login_page = UserCorrectLogin(driver)

        assert main_page.is_signup_login_button_visible(), "Signup/Login button is not visible after deleting the account"

        with allure.step("Click on signup/login button"):
            main_page.signup_login_button.click()

        login_account_visible = login_page.is_login_your_account_visible()
        assert login_account_visible, "'Login your account' text is not visible after login"

        with allure.step("Perform login"):
            login_page.make_login()
            print("login done")

        with allure.step("Log out from account"):
            login_page.make_logout()
            print('logged out success')

        assert main_page.is_signup_login_button_visible(), "Signup/Login button is not visible after deleting the account"
