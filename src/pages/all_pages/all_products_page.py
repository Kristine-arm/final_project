import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from src.pages.base_element import BaseElement
from src.pages.base_page import BasePage
import allure
import random

@allure.story("Checking the functionality of all products page")
class AllProducts(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.test_cases_button = BaseElement(driver, '//a[@href = "/test_cases"]')
        self.all_products_note = BaseElement(driver, '//*[@class="title text-center"]')
        self.products_list = BaseElement(driver, '//*[@class="features_items"]')
        self.view_product_button = BaseElement(driver, '(//*[@class="fa fa-plus-square"])[1]')
        self.product_search_field = BaseElement(driver, '//*[@id="search_product"]')
        self.search_button = BaseElement(driver, '//*[@class="fa fa-search"]')
        self.search_products_note = BaseElement(driver, '//*[@class="title text-center"]')
        self.product_names = BaseElement(driver, '//*[@class="product-image-wrapper"]')
        self.first_product = BaseElement(driver, '(//*[@class="col-sm-4"])[2]')
        self.add_to_cart_first_product = BaseElement(driver, "(//a[@data-product-id='1'])[2]")
        self.continue_shopping_button = BaseElement(driver, '//button[contains(@class, "close-modal") and contains(text(), "Continue Shopping")]')
        self.second_product = BaseElement(driver, '(//*[@class="col-sm-4"])[3]')
        self.add_to_cart_second_product = BaseElement(driver, "(//a[@data-product-id='2'])[2]")
        self.view_cart_button = BaseElement(driver,'//u[contains(text(), "View Cart")]')
        self.woman_products_note = BaseElement(driver, '//h2[@class="title text-center"]')
        self.category_woman_x = BaseElement(driver, '//*[@id="accordian"]/div[1]/div[1]/h4/a/span/i')
        self.category_man_x = BaseElement(driver, '//*[@id="accordian"]/div[2]/div[1]/h4/a/span/i')
        self.category_kids_x = BaseElement(driver, '//*[@id="accordian"]/div[3]/div[1]/h4/a/span/i')
        self.dress_button = BaseElement(driver, '//a[contains(@href, "/category_products/1")]')
        self.tops_button = BaseElement(driver, '//a[contains(@href, "/category_products/2")]')
        self.random_category = BaseElement(driver, '(//a[@href="/category_products/1" and normalize-space()="Dress"]')
        self.men_products_note = BaseElement(driver, '//h2[@class="title text-center"]')
        self.brand_note = BaseElement(driver, '//*[@class="title text-center"]')
        self.product_brand_name = BaseElement(driver, '// *[ @class ="active"]')
        self.cart_button = BaseElement(driver, '//a[@href="/view_cart"]')


    @allure.step('Verify user is navigated to ALL PRODUCTS page successfully')
    def is_all_products_note_visible(self):
        return self.all_products_note.is_visible()

    @allure.step('Verify the products list is visible')
    def is_products_list_visible(self):
        return self.products_list.is_visible()

    @allure.step('Click on "View Product" of first product')
    def view_product(self):
        self.view_product_button.click()

    @allure.step('Search for a product "{product_name}"')
    def search_for_product(self, product_name):
        self.product_search_field.input_text(product_name)
        self.search_button.click()

    @allure.step("Verify 'SEARCHED PRODUCTS' text is visible")
    def is_searched_products_visible(self):
        return self.search_products_note.is_visible()

    @allure.step("Verify search results are relevant to the search query")
    def are_search_results_relevant(self, query):
        product_names = self.product_names.get_elements_text()
        query = query.lower()
        relevant_products = [name for name in product_names if query in name.lower()]
        irrelevant_products = [name for name in product_names if query not in name.lower()]
        return relevant_products, irrelevant_products

    @allure.step("Hover over the first product and click 'Add to Cart'")
    def hover_and_add_first_product_to_cart(self):
        self.first_product.hover()
        time.sleep(2)
        self.add_to_cart_first_product.click()
        time.sleep(2)
        self.continue_shopping_button.click()


    @allure.step("Hover over the second product and click 'Add to Cart'")
    def hover_and_add_second_product_to_cart(self):
        self.second_product.hover()
        self.add_to_cart_second_product.click()
        self.view_cart_button.click()

    @allure.step('Verify that category page is displayed and text "WOMEN PRODUCTS" visible')
    def is_woman_products_note_visible(self):
        return self.woman_products_note.is_visible()

    @allure.step('Verify that user is navigated to that category page')
    def is_man_products_note_visible(self):
        return self.men_products_note.is_visible()

    @allure.step('Click on "Men" category')
    def click_men_button(self):
        self.category_man_x.click()

    @allure.step('Randomly click on any category')
    def click_random_men_subcategory(self):
        n = random.randint(1, 2)
        self.choose_random_men_category = BaseElement(self.driver, '//*[@id="Men"]/div/ul/li['+ str(n) +']/a')
        self.choose_random_men_category.click()

    @allure.step('Verify that Brands are visible on left side bar')
    def brands_are_visible(self):
        for n in range(1, 9):
            try:
                brands_section = BaseElement(self.driver, f'(//*[@class="pull-right"])[{n}]')
                if not brands_section.is_visible():
                    print(f'Brand at index {n} is not visible on the all products page')
                    return False
            except:
                print(f'Brand section at index {n} not found on the all products page')
                return False
        return True

    @allure.step("Click random brand")
    def select_random_brand(self):
        n = random.randint(1, 8)
        self.random_brand = BaseElement(self.driver, '(//*[@class="pull-right"])[' + str(n) + ']')
        self.random_brand.click()

    @allure.step('Verify that user is navigated to brand page and brand products are displayed')
    def is_brand_note_visible(self):
        return self.brand_note.is_visible()

    @allure.step(' Verify that user is navigated to that brand page')
    def is_product_name_visible(self):
        return self.product_brand_name.is_visible

    @allure.step("Add those products to cart")
    def hover_and_add_top_product_to_cart(self):
        y = 2
        p = 1
        for x in range(2,16):
            x = y
            w = 2*p
            actions = ActionChains(self.driver)
            element = self.driver.find_element(By.XPATH,'(//*[@class="col-sm-4"])[' + str(x) +']')
            actions.move_to_element(element).perform()
            add_to_cart_btn = self.driver.find_element(By.XPATH,'(//a[contains(@class, "add-to-cart")])[' + str(w) + ']')
            add_to_cart_btn.click()
            y += 1
            p += 1
            continue_button = self.driver.find_element(By.XPATH, '//*[@class="btn btn-success close-modal btn-block"]')
            continue_button.click()

    @allure.step('Click "Cart Button" on main page')
    def click_cart_button(self):
        self.cart_button.click()

