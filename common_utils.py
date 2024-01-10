class EbayHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.ebay.com"

    def navigate_to_ebay(self):
        self.driver.get(self.base_url)