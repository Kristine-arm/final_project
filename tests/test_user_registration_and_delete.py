
from src.pages.main.main_page import MainPage
from src.pages.login.login_page import LoginPage
import allure


class Test_Registration_Delete():
    @allure.story('User Registration and Deletion')
    def test_user_registration_and_deleting(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        with allure.step("Click on signup/login button"):
            main_page.signup_login_button.click()

        with allure.step("Perform user registration"):
            login_page.make_registration()
            print("Registration done")

        with allure.step("Fill account information"):
            login_page.fill_account_info()
            print("Account filled")

        driver.get('https://automationexercise.com/')

        with allure.step("Delete user account"):
            login_page.delete_account()
            print('Deleted account')

        assert main_page.is_signup_login_button_visible(), "Signup/Login button is not visible after deleting the account"
