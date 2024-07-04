from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    MAIN_URL = 'https://automationexercise.com/'
    CART_URL = 'https://automationexercise.com/view_cart'
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def open_main_page(self):
        self.open_url(self.MAIN_URL)

    def open_cart_page(self):
        self.open_cart_page(self.CART_URL)



