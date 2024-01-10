import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class EbayHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.ebay.com"

    def navigate_to_ebay(self):
        self.driver.get(self.base_url)

    def click_sign_in_link(self):
        sign_in_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Sign in']"))
        )
        sign_in_link.click()

    def enter_credentials(self, username, password):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "userid"))
        )

        username_input.send_keys(username)

        continue_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id = 'signin-continue-btn']")))
        continue_link.click()

        time.sleep(10)

        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "pass")))
        password_input.send_keys(password)
        password_continue_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id = 'sgnBt']")))
        password_continue_link.click()

    def error_message(self):
        #error_comm = WebDriverWait(self.driver, 10).until(
        #    EC.visibility_of_element_located((By.XPATH, "//*[@id = 'errormsg']")))
        time.sleep(5)
        error_element = self.driver.find_element(By.XPATH, "//*[@id = 'errormsg']")
        if error_element:
            return 'Great Succes. Incorrect Login'
        else:
            return 'Not a great success. Error comm not found.'

    def search_for_item(self, item):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id = 'gh-ac']")))
        search_input.send_keys(item)

        search_button= WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id = 'gh-btn']")))
        search_button.click()

    def click_nth_search_result(self, n):
        #xpath = f"(//li[contains(@class, 's-item')])[{n}]"
        # search_results = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[4]/div[4]/div[2]/div[1]/div[2]/ul/li[" + str(n-1) +"]")))
        # print('ffffffff', search_results)
        # for element in search_results:
        #     print(element)

        #search_results = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_all_elements_located((By.XPATH, "//*[@class='srp-results srp-list clearfix']/*[contains(@id, 'item')]")))
        #nth_element = search_results[n-1]
        #info_div = nth_element.find_element_by_xpath('//*[@id="item1ae928af31"]/div/div[' + str(n-1) + ']')
        #link_element = info_div.find_element_by_xpath('.//a[@class="s-item__link"]')
        #href_value = link_element.get_attribute('href')
        #print(href_value)
        #nth_element.click()

        search_results = WebDriverWait(self.driver, 10).until(
             EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[4]/div[2]/div[1]/div[2]/ul/li[' + str(n+1) + ']/div/div[2]/a')))
        url = search_results.get_attribute('href')
        self.driver.get(url)
        #self.driver.switch_to.window(self.driver.window_handles[-1])

    def add_to_basket(self):
        try:
            add_to_cart_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'ux-call-to-action') and contains(@class, 'fake-btn') and contains(@class, 'fake-btn--large') and contains(@class, 'fake-btn--primary')]//span[@class='ux-call-to-action__text' and text()='Add to cart']"))
        )
            add_to_cart_button.click()
            return True  # Return True if the item is successfully added to the basket
        except TimeoutException:
            return False  # Return False if there's a TimeoutException, indicating failure to add the item

    def check_go_to_cart(self):
        try:
            go_to_cart_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@class='btn btn-scnd vi-VR-btnWdth-XL']"))
            )
            go_to_cart_button.click()
        except TimeoutException:
            print("Button not found or couldn't be clicked.")


    # def check_basket_items(self):
    #     try:
    #         basket_button = WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable((By.XPATH, "//*[@class='gh-cart-icon']"))
    #         )
    #         basket_button.click()
    #
    #         basket_items = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_all_elements_located((By.XPATH, "//*[@class='basket-item']"))
    #         )
    #
    #         no_of_items = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_all_elements_located((By.XPATH, "//*[@id = 'gh-cart-n']")))
    #         print('no_of_items', no_of_items)
    #         print('no_of_items.text', no_of_items.text)
    #         #return no_of_items.text
    #
    #         #return len(basket_items)
    #     except TimeoutException:
    #         return 0

    def check_basket_items(self):
        try:
            basket_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@class='gh-cart-icon']"))
            )
            basket_button.click()

            # Check for the presence of elements representing the individual items in the basket
            basket_items = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//*[@class='basket-item']"))
            )

            return len(basket_items)  # Return the count of items in the basket
        except TimeoutException:
            return 0  # Return 0 if there's a TimeoutException or no items found in the basket






