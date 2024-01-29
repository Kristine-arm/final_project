from selenium.common import TimeoutException
from src.config.config import TestData
from src.pages.base_element import BaseElement
from src.pages.base_page import BasePage
import allure

class LoginPage(BasePage):
    """Page object for the login page."""
    def __init__(self, driver):
        """Initialize the LoginPage."""
        super().__init__(driver)

        self.name_field = BaseElement(driver, '//*[@id="form"]/div/div/div[3]/div/form/input[2]')
        self.email_field = BaseElement(driver, '//*[@id="form"]/div/div/div[3]/div/form/input[3]')
        self.signup_button = BaseElement(driver, '//*[@id="form"]/div/div/div[3]/div/form/button')

        self.enter_account_info = BaseElement(driver, '//*[@id="form"]/div/div/div/div[1]/h2/b')
        self.gender_mrs = BaseElement(driver, '//*[@id="id_gender2"]')
        self.password = BaseElement(driver, '//*[@id="password"]')
        self.day_of_bird_button = BaseElement(driver, '//*[@id="days"]')
        self.choose_day_button = BaseElement(driver, '//*[@id="days"]/option[8]')
        self.month_button = BaseElement(driver, '//*[@id="months"]')
        self.choose_months = BaseElement(driver, '//*[@id="months"]/option[8]')
        self.year_button = BaseElement(driver, '//*[@id="years"]')
        self.choose_year = BaseElement(driver, '//*[@id="years"]/option[19]')
        self.first_name_field = BaseElement(driver, '//*[@id="first_name"]')
        self.last_name_filed = BaseElement(driver, '//*[@id="last_name"]')
        self.address_field = BaseElement(driver, '//*[@id="address1"]')
        self.county_button = BaseElement(driver, '//*[@id="country"]')
        self.choose_country = BaseElement(driver, '//*[@id="country"]/option[2]')
        self.state_field = BaseElement(driver, '//*[@id="state"]')
        self.city_filed = BaseElement(driver, '//*[@id="city"]')
        self.zipcode_filed = BaseElement(driver, '//*[@id="zipcode"]')
        self.mobile_number_filed = BaseElement(driver, '//*[@id="mobile_number"]')
        self.create_account_button = BaseElement(driver, "//button[@type='submit' and @data-qa='create-account' and contains(@class, 'btn btn-default')]")
        self.account_created = BaseElement(driver, '//*[@id="form"]/div/div/div/h2/b')
        self.continue_button = BaseElement(driver, '//*[@id="form"]/div/div/div/div/a')
        self.logout_button = BaseElement(driver, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
        self.delete_account_button = BaseElement(driver, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a')
        self.account_deleted_note = BaseElement(driver, '//*[@id="form"]/div/div/div/h2/b')
        self.login_your_account = BaseElement(driver, '//*[@id="form"]/div/div/div[1]/div/h2')

    @allure.story('User Registration')
    @allure.step('Make registration with name and email.Expected Result: User should be registered successfully.')
    def make_registration(self):
        """Perform user registration."""
        name = TestData.name
        email = TestData.email

        self.name_field.send_keys(name)
        self.email_field.send_keys(email)
        self.signup_button.click()

    @allure.story('Account Information')
    @allure.step('Fill account info with password, first name, etc.Expected Result: Account information should be filled successfully.')
    def fill_account_info(self):
        """Fill account information."""
        password = TestData.password
        first_name = TestData.first_name
        last_name = TestData.last_name
        address = TestData.address
        state = TestData.state
        city = TestData.city
        zipcode = TestData.zipcode
        mobile_number = TestData.mobile_number

        self.gender_mrs.click()
        self.password.send_keys(password)
        self.day_of_bird_button.click()
        self.choose_day_button.click()
        self.month_button.click()
        self.choose_months.click()
        self.year_button.click()
        self.choose_year.click()
        self.first_name_field.send_keys(first_name)
        self.last_name_filed.send_keys(last_name)
        self.address_field.send_keys(address)
        self.county_button.click()
        self.choose_country.click()
        self.state_field.send_keys(state)
        self.city_filed.send_keys(city)
        self.zipcode_filed.send_keys(zipcode)
        self.mobile_number_filed.send_keys(mobile_number)
        self.create_account_button.click()
        self.continue_button.click()

    @allure.story('Account Deletion')
    @allure.step('Deleting created account.Expected Result:The account should be successfully deleted.')
    def delete_account(self):
        """Perform user account delete."""
        try:
            self.delete_account_button.click()
        except TimeoutException:
            return False
    @allure.step('Check if login to your account visble')
    def is_login_your_account_visible(self):
        return self.login_your_account.is_visible()

class UserCorrectLogin(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.email1_field = BaseElement(driver, '//*[@id="form"]/div/div/div[1]/div/form/input[2]')
        self.password1 = BaseElement(driver, '//*[@id="form"]/div/div/div[1]/div/form/input[3]')
        self.login_button = BaseElement(driver, '//*[@id="form"]/div/div/div[1]/div/form/button')
        self.logout_button = BaseElement(driver, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
        self.login_your_account = BaseElement(driver, '//*[@id="form"]/div/div/div[1]/div/h2')
    @allure.story('Login account')
    @allure.step('Fill login info with email and password. Expected result: Login to account successfully.')
    def make_login(self):
        password1 = TestData.password1
        email1 = TestData.email1

        self.email1_field.send_keys(email1)
        self.password1.send_keys(password1)
        self.login_button.click()

    @allure.step('Check if login to your account visible')
    def is_login_your_account_visible(self):
        is_visible = self.login_your_account.is_visible()
        if is_visible:
            print("Login your account text is visible")
        else:
            print("Login your account text is not visible")
        return is_visible

    @allure.story('Logout account')
    @allure.step('Click logout button. Expected result: Logged out from account successfully.')
    def make_logout(self):
        try:
            self.logout_button.click()
        except TimeoutException:
            return False
class UserIncorrectLogin(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.invalid_email = BaseElement(driver, '//*[@id="form"]/div/div/div[1]/div/form/input[2]')
        self.invalid_password = BaseElement(driver, '//*[@id="form"]/div/div/div[1]/div/form/input[3]')
        self.login_button = BaseElement(driver, '//*[@id="form"]/div/div/div[1]/div/form/button')
        self.login_error_message = BaseElement(driver, '//*[@id="form"]/div/div/div[1]/div/form/p')

    @allure.story('Login account with incorrect data')
    @allure.step('Enter incorrect email and password. Expected result: Your email or password is incorrect.')
    def make_incorrect_login(self, email, password):
        self.invalid_email.send_keys(email)
        self.invalid_password.send_keys(password)
        self.login_button.click()

    @allure.step('Verify error: Your email or password is incorrect! is visible')
    def is_error_message_visible(self):
        is_visible = self.login_error_message.is_visible()
        if is_visible:
            print("Login your account text is visible")
        else:
            print("Login your account text is not visible")
        return is_visible