from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EbayHomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_sign_in_link(self):
        sign_in_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Sign in']"))
        )
        sign_in_link.click()

    def enter_credentials(self, username, password):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "userid"))
        )
        password_input = self.driver.find_element(By.ID, "pass")

        username_input.send_keys(username)
        password_input.send_keys(password)

    def click_sign_in_button(self):
        sign_in_button = self.driver.find_element(By.ID, "sgnBt")
        sign_in_button.click()