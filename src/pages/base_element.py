from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class BaseElement:
    def __init__(self, driver, xpath):
        self.driver = driver
        self.xpath = xpath
        self.locator = (By.XPATH, xpath)

    def click(self):
        element = self.driver.find_element(By.XPATH, self.xpath)
        element.click()

        # element.click()
    def hover(self):
        actions = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, self.xpath)
        actions.move_to_element(element).perform()

    @property
    def element(self):
        return self.driver.find_element(By.XPATH, self.locator)


    def assert_element(self, clickable = False, return_many = False):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.xpath)))
        if clickable:
            wait.until(EC.element_to_be_clickable((By.XPATH, self.xpath)))
        if return_many:
            result = self.driver.find_elements(By.XPATH, self.xpath)
        else:
            result = self.driver.find_element(By.XPATH, self.xpath)
        return result


    def find_element(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.locator)
            )
            return element
        except TimeoutException:
            return None

    def is_displayed(self):
        element = self.find_element()
        if element:
            return element.is_displayed()
        else:
            return False


    def send_keys(self, keys):
        element = self.assert_element(clickable=True)
        element.send_keys(keys)


    def clear(self):
        field = self.assert_element(clickable=True)
        field.clear()

    def set_text(self, text):
        element = self.assert_element(clickable=True)
        element.clear()  # Clear existing text in the element
        element.send_keys(text)

    def wait_until_visible(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath)))
        return bool(wait)  #hishel

    def is_visible(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.xpath)))
            return True
        except TimeoutException:
            return False
    def get_title (self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def wait_until_invisibility(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.xpath)))

    def wait_text_to_be_present(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.text_to_be_present_in_element((By.XPATH, self.xpath), text))

    def scroll_into_view(self):
        element = self.assert_element()
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def capture_screenshot(self, filename):
        element = self.assert_element()
        element.screenshot(filename)

    def double_click(self):
        element = self.assert_element()
        ActionChains(self.driver).double_click(element).perform()

    def right_click(self):
        element = self.assert_element()
        ActionChains(self.driver).context_click(element).perform()

    def drag_and_drop(self, target):
        source_element = self.assert_element()
        target_element = target.assert_element()
        ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()

    def switch_to_frame(self):
        element = self.assert_element()
        self.driver.switch_to.frame(element)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def input_text(self, text, clear_first=False):
        element = self.assert_element(clickable=True)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def find_element(self, wait_type='visible', timeout=10, multiple=False):
        wait = WebDriverWait(self.driver, timeout)
        try:
            if wait_type == 'visible':
                condition = EC.visibility_of_element_located(self.locator)
            elif wait_type == 'clickable':
                condition = EC.element_to_be_clickable(self.locator)
            elif wait_type == 'present':
                condition = EC.presence_of_element_located(self.locator)
            else:
                raise ValueError("Invalid wait_type specified")

            if multiple:
                return wait.until(lambda driver: driver.find_elements(*self.locator))
            else:
                return wait.until(condition)
        except TimeoutException:
            return None

    def is_visible(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.locator))
            return True
        except TimeoutException:
            return False

    def input_text(self, text, clear_first=False):
        element = self.find_element(wait_type='clickable')
        if element is None:
            raise NoSuchElementException(f"Element with locator {self.locator} not found or not clickable.")
        if clear_first:
            element.clear()
        element.send_keys(text)

    def get_elements_text(self):
        elements = self.locating_elements()
        return [element.text.strip() for element in elements]

    def locating_elements(self):
        return self.driver.find_elements(*self.locator)

    @property
    def text(self):
        return self.element.text

    def get_text(self):
        element = self.find_element(wait_type='visible')
        if element:
            return element.text.strip()
        else:
            return None