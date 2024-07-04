from selenium.common import TimeoutException
from src.config.config import TestData
from src.pages.base_element import BaseElement
from src.pages.base_page import BasePage
import allure

@allure.story("Checking login page functionality")
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.new_user_signup_note = BaseElement(driver,'//h2[text()="New User Signup!"]')
        self.signup_name = BaseElement(driver, '//input[@type="text" and @data-qa="signup-name"]')
        self.signup_email = BaseElement(driver, '//input[@type="email" and @data-qa="signup-email"]')
        self.signup_button = BaseElement(driver, '//button[@type="submit" and @data-qa="signup-button"]')
        self.email_exist_note = BaseElement(driver, '//p[text()="Email Address already exist!"]')

        self.gender_mrs = BaseElement(driver, '//*[@id="id_gender2"]')
        self.password = BaseElement(driver, '//*[@id="password"]')
        self.day_of_bird_button = BaseElement(driver, '//*[@id="days"]')
        self.choose_day_button = BaseElement(driver, '//*[@id="days"]/option[8]')
        self.month_button = BaseElement(driver, '//*[@id="months"]')
        self.choose_months = BaseElement(driver, '//*[@id="months"]/option[8]')
        self.year_button = BaseElement(driver, '//*[@id="years"]')
        self.choose_year = BaseElement(driver, '//*[@id="years"]/option[19]')
        self.first_name_field = BaseElement(driver, '//*[@id="first_name"]')
        self.last_name_field = BaseElement(driver, '//*[@id="last_name"]')
        self.address_field = BaseElement(driver, '//*[@id="address1"]')
        self.county_button = BaseElement(driver, '//*[@id="country"]')
        self.choose_country = BaseElement(driver, '//*[@id="country"]/option[2]')
        self.state_field = BaseElement(driver, '//*[@id="state"]')
        self.city_field = BaseElement(driver, '//*[@id="city"]')
        self.zipcode_field = BaseElement(driver, '//*[@id="zipcode"]')
        self.mobile_number_field = BaseElement(driver, '//*[@id="mobile_number"]')
        self.create_account_button = BaseElement(driver, "//button[@type='submit' and @data-qa='create-account' and contains(@class,'btn btn-default')]")
        self.continue_button = BaseElement(driver, '//a[@class="btn btn-primary" and text()="Continue"]')
        self.delete_account_button = BaseElement(driver, "//a[@href='/delete_account']")
        self.account_deleted_note = BaseElement(driver, '//h2[@data-qa="account-deleted"]')
        self.continue_after_del_button = BaseElement(driver, '//a[@data-qa="continue-button"]')
        self.account_created_note = BaseElement(driver, '//h2[@data-qa="account-created"]')
        self.continue_after_account_created = BaseElement(driver, '//a[@data-qa="continue-button"]')

        self.login_your_account = BaseElement(driver, '//h2[text()="Login to your account"]')
        self.login_email = BaseElement(driver, '//input[@type="email" and @data-qa="login-email"]')
        self.login_password = BaseElement(driver, '//input[@type="password" and @data-qa="login-password"]')
        self.login_button = BaseElement(driver, '//button[@type="submit" and @data-qa="login-button"]')
        self.logout_button = BaseElement(driver, '//a[@href = "/logout"]')
        self.login_error_message = BaseElement(driver, '//*[text()="Your email or password is incorrect!"]')

        self.logged_in_as_note = BaseElement(driver, '//*[@class="fa fa-user"]')
        self.cart_button = BaseElement(driver, '//a[@href="/view_cart"]')

    @allure.step('Make registration with name and email.')
    def make_registration(self):
            self.signup_name.send_keys(TestData.name_signup)
            self.signup_email.send_keys(TestData.email_signup)
            self.signup_button.click()

    @allure.step('Make registration with existing email')
    def registration_with_existing_email(self):
            self.signup_name.send_keys(TestData.name_contact)
            self.signup_email.send_keys(TestData.backup_email)
            self.signup_button.click()

    @allure.step('Fill account info with password, first name, etc.')
    def fill_account_info(self):
            self.gender_mrs.click()
            self.password.send_keys(TestData.password_for_signin)
            self.day_of_bird_button.click()
            self.choose_day_button.click()
            self.month_button.click()
            self.choose_months.click()
            self.year_button.click()
            self.choose_year.click()
            self.first_name_field.send_keys(TestData.first_name)
            self.last_name_field.send_keys(TestData.last_name)
            self.address_field.send_keys(TestData.address)
            self.county_button.click()
            self.choose_country.click()
            self.state_field.send_keys(TestData.state)
            self.city_field.send_keys(TestData.city)
            self.zipcode_field.send_keys(TestData.zipcode)
            self.mobile_number_field.send_keys(TestData.mobile_number)
            self.create_account_button.click()
            # self.continue_button.click()

    @allure.step('Press continue button')
    def clicking_continue_button(self):
        self.continue_button.click()


    @allure.step('Deleting created account.')
    def delete_account(self):
        try:
            self.delete_account_button.click()
        except TimeoutException:
            return False

    @allure.step('Check if Account Deleted note is visible after deleting account')
    def is_account_deleted_note_visible(self):
        return self.account_deleted_note.is_visible()

    @allure.step('Verify "ACCOUNT CREATED"')
    def is_account_created_note_visible(self):
        return self.account_created_note.is_visible()

    @allure.step("Verify 'New User Signup!' is visible")
    def is_new_user_signup_note_visible(self):
        return self.new_user_signup_note.is_visible()

    @allure.step("Verify error 'Email Address already exist!' is visible")
    def is_email_exist_note_visible(self):
        return self.email_exist_note.is_visible()

    @allure.step('Check if login to your account visible')
    def is_login_your_account_visible(self):
        return self.login_your_account.is_visible()

    @allure.step('Fill login info with email and password.')
    def make_login(self):
        self.login_email.send_keys(TestData.email_login)
        self.login_password.send_keys(TestData.password_login)
        self.login_button.click()

    @allure.step('Click logout button.')
    def make_logout(self):
        try:
            self.logout_button.click()
        except TimeoutException:
            return False

    @allure.step('Enter incorrect email and password.')
    def make_incorrect_login(self, email, password):
        self.login_email.send_keys(email)
        self.login_password.send_keys(password)
        self.login_button.click()

    @allure.step('Verify error: Your email or password is incorrect! is visible')
    def is_error_message_visible(self):
        is_visible = self.login_error_message.is_visible()
        if is_visible:
            print("Login your account text is visible")
        else:
            print("Login your account text is not visible")
        return is_visible

    @allure.step('Verify "Logged in as username" at top')
    def is_logged_in_as_note_visible(self):
        return self.logged_in_as_note.is_visible()

    @allure.step('Click "Cart Button" on main page')
    def click_cart_button(self):
        self.cart_button.click()