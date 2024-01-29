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

    def find(self):
        return self.driver.find_element(self.locator)

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

    def hover(self):
        actions = ActionChains(self.driver)
        element = self.find_element()
        actions.move_to_element(element).perform()


    def send_keys(self, keys):
        element = self.assert_element(clickable=True)
        element.send_keys(keys)

    def text(self):
        element = self.assert_element()
        return element.text

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
        """Scrolls the element into view."""
        element = self.assert_element()
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # def select_option(self, option):
    #     """Selects an option from a dropdown menu."""
    #     element = self.assert_element()
    #     select = Select(element)
    #     select.select_by_visible_text(option)

    def capture_screenshot(self, filename):
        """Captures a screenshot of the element."""
        element = self.assert_element()
        element.screenshot(filename)

    def double_click(self):
        """Double clicks on the element."""
        element = self.assert_element()
        ActionChains(self.driver).double_click(element).perform()

    def right_click(self):
        """Right clicks on the element."""
        element = self.assert_element()
        ActionChains(self.driver).context_click(element).perform()

    def drag_and_drop(self, target):
        """Drags the element and drops it onto the target element."""
        source_element = self.assert_element()
        target_element = target.assert_element()
        ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()

    def switch_to_frame(self):
        """Switches to the frame containing the element."""
        element = self.assert_element()
        self.driver.switch_to.frame(element)

    def switch_to_default_content(self):
        """Switches back to the default content from the frame."""
        self.driver.switch_to.default_content()

    def find_element(self):
        pass
