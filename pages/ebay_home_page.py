import time
import random
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
    def is_kristine_name_present(self):
        try:
            kristine_name = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id = 'gh-eb-u']"
            )))
            return True
        except:
            return False

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

        time.sleep(10)

    def error_message(self):
        try:
            error_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='errormsg']"))
            )
            return 'Great Success. Incorrect Login'
        except:
            return 'Not a great success. Error message not found.'


    def search_for_item(self, item):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id = 'gh-ac']")))
        search_input.send_keys(item)

        search_button= WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id = 'gh-btn']")))
        search_button.click()

    def click_nth_search_result(self, n):
        print("startig nth")
        search_results = WebDriverWait(self.driver, 10).until(
             EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[4]/div[2]/div[1]/div[2]/ul/li[' + str(n+1) + ']/div/div[2]/a')))
        url = search_results.get_attribute('href')
        self.driver.get(url)
        self.driver.switch_to.window(self.driver.window_handles[-1])


    def add_to_basket(self):
        try:
            print('punkt pierwszy')
            select_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '(//*[@class ="ux-call-to-action__cell"])[1]')))

            if select_button is not None:
                select_button.click()
                time.sleep(2)
                print('between 1 and 2')

                print('Checking for color button...')
                color_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="x-msku__option-box-0"]')))
                color_button.click()
                time.sleep(2)
                print('punkt drugi')
            print('punkt trzeczy')
            add_to_cart_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'ux-call-to-action') and contains(@class, 'fake-btn') and contains(@class, 'fake-btn--large') and contains(@class, 'fake-btn--primary')]//span[@class='ux-call-to-action__text' and text()='Add to cart']")))
            add_to_cart_button.click()
            return True
        except TimeoutException:
            return False


    def adding_item_mouse_to_cart(self):
        try:
            print('punkt pierwszy')
            select_item_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="x-msku__select-box-1000"]')))
            if select_item_button is not None:
                select_item_button.click()
                time.sleep(2)
                print('Checking for color button...')
                color_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="x-msku__option-box-0"]')))
                color_button.click()
                time.sleep(2)
                print('punkt drugi')
            print('punkt trzeczy')
            add_to_cart_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,"//a[contains(@class, 'ux-call-to-action') and contains(@class, 'fake-btn') and contains(@class, 'fake-btn--large') and contains(@class, 'fake-btn--primary')]//span[@class='ux-call-to-action__text' and text()='Add to cart']")))
            add_to_cart_button.click()
            return True
        except TimeoutException:
            return False


    def check_go_to_cart(self):
        try:
            go_to_cart_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@class ='btn btn-scnd vi-VR-btnWdth-XL']"))
            )
            go_to_cart_button.click()
        except TimeoutException:
            print("Button not found or couldn't be clicked.")


    def check_basket_items(self):
        try:
            time.sleep(10)
            basket_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@class='gh-cart-icon']"))
            )
            basket_button.click()
            print('przelogowalam strone')
            time.sleep(3)
            basket_items = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//*[@id='gh-cart-n']"))
            )
            time.sleep(3)
            print('to jest basket items', basket_items)
            print('a to jest basket_items z metoda text, ', basket_items[0].text)
            print('wydrukuowalam basket items')
            return len(basket_items)  # Return the count of items in the basket
        except TimeoutException:
            print('poszlo zle')
            return 0

    def navigate_to_shop_by_category(self):
        self.navigate_to_ebay()

        time.sleep(3)

        try:
            accept_all = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="gdpr-banner-accept"]')))
            accept_all.click()

            time.sleep(3)

        except:
            pass

        time.sleep(3)

        try:
            shop_by_category_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='gh-shop-a']"))
            )
            shop_by_category_button.click()
            print("Clicked on 'Shop by category' button.")

            m = random.randint(1, 12)

            category_rnd = self.driver.find_element(By.XPATH, '(//*[@class="gh-sbc-parent"])[' + str(m) + ']' )
            href_value = category_rnd.find_element(By.TAG_NAME, 'a').get_attribute("href")
            self.driver.get(href_value)
            print(href_value)

            self.driver.get(href_value)
            print(f"Navigated to random category page: {href_value}")


        except TimeoutException:
            print("Failed to find or click 'Shop by category' button. XYZ")

    def filter_by_brand_style_material_color(self):
        try:
            n = random.randint(1, 3)
            brand_button = self.driver.find_element(By.XPATH, '(//*[@id="x-refine__group_1__0"]/ul/li[' + str(n) + ']/div/a/div)')
            brand_button.click()
            time.sleep(3)
            style_button = self.driver.find_element(By.XPATH, '(//*[@id="x-refine__group_1__1"]/ul/li[' + str(n) + '])')
            style_button.click()
            time.sleep(3)
            material_button =self.driver.find_element(By.XPATH, '(//*[@id="x-refine__group_1__2"]/ul/li[' + str(n) + '])')
            material_button.click()
            time.sleep(3)
            color_button = self.driver.find_element(By.XPATH, '(//*[@id="x-refine__group_1__3"]/div[1]/ul/li[' + str(n) + '])')
            color_button.click()
            time.sleep(13)
            print('Hura! Udalo sie')

        except TimeoutException:
            print("Failed to find or click 'Shop by category' button. XYZ")

    def go_second_page(self):
        second_page_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "(//*[@class='pagination__item'])[2]")))
        second_page_button.click()
        print("i am at 2nd page")


    def take_first_item(self):
        item_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@class="srp-river-results clearfix"]/ul/li[3]')))
        #item_button = self.driver.find_element(By.XPATH,'//*[@class="srp-river-results clearfix"]/ul/li[' + str(n) + ']')
        item_button.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(3)

        print("took 1st item")
        time.sleep(3)

    def add_to_watchlist(self):
        print('jestem w watchlist')

        add_to_watchlist_button_xpath = '//*[@id="vi-atl-lnk-99"]'

        add_to_watchlist_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, add_to_watchlist_button_xpath))
        )

        print('wzialam kodzik')

        add_to_watchlist_button.click()
        time.sleep(20)

        print("added watchlist")


    def check_watchlist(self):
        try:
            watchlist_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(@title, 'Watchlist')]")))
            watchlist_button.click()
            view_items_in_watchlist_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "// span[contains(text(), 'View all items you are watching')]")))
            view_items_in_watchlist_button.click()
            print('before count watchlist items')
            count_watchlist_items_button = self.driver.find_element(By.XPATH, '//*[@id="s0-0-35-0-6-m-carousel-list"]/li[2]/a/span/span')

            time.sleep(3)
            print('to jest basket items', count_watchlist_items_button)
            number_in_watchlist = count_watchlist_items_button.text

            if number_in_watchlist[-3] == '(':
                number_in_watchlist = number_in_watchlist[-2]
            elif number_in_watchlist[-4] == '(':
                number_in_watchlist = number_in_watchlist[-3:-1]
            elif number_in_watchlist[-5] == '(':
                number_in_watchlist = number_in_watchlist[-4:-1]

            print(number_in_watchlist)

        except TimeoutException:
            print('poszlo zle')
            return 0


    def go_fifth_page(self):
        second_page_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "(//*[@class='pagination__item'])[5]")))
        second_page_button.click()
        print("i am at 5th page")


    def click_random_item(self):
        n = random.randint(2, 60)
        search_results = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,'//*[@id="srp-river-results"]/ul/li[' + str(n + 1) + ']')))
        url = search_results.get_attribute('href')
        self.driver.get(url)

    def take_item(self):

        big_group = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@class="srp-river-results clearfix"]/ul/li[2]'))
        )
        item_info_div = big_group.find_element(By.XPATH, './/div[@class="s-item__info clearfix"]')
        link_tag = item_info_div.find_element(By.TAG_NAME, 'a')
        href_value = link_tag.get_attribute('href')
        print(href_value)
        self.driver.get(href_value)
        print('item taken')

    def buy_it_now(self):
        try:
            print('punkt pierwszy')
            select_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '(//*[@class ="ux-call-to-action__cell"])[1]')))
            print('punkt drugi')

            if select_button is not None:
                select_button.click()
                time.sleep(2)
                print('between 2 and 3')

                # Add debugging statement to check if color button is found
                print('Checking for color button...')
                color_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="x-msku__option-box-0"]')))
                color_button.click()
                time.sleep(2)
                print('punkt trzeci')

            print('Checking for buy_it_now_button...')
            buy_it_now_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '(//*[@class="vim x-bin-action vim-flex-cta"])[1]')))
            print('punkt czwarty')
            buy_it_now_button.click()
            print('after clicking buy it now')
            time.sleep(5)

        except TimeoutException:
            print('TimeoutException: Element not found or not clickable')
            return 0


    def check_out_as_guest(self):
        try:
            check_out_as_guest_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '(//*[@class="ux-bin-nudge__guestCheckOut"])[1]')))
            check_out_as_guest_button.click()
            print("punkt pionty")
            time.sleep(5)
            quantity_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@class="select select--large"]')))

            if quantity_button is not None:
                quantity_button.click()
                amount_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '//span[@class="select select--large"]/select/option[last()]')))
                amount_button.click()
                print('amount button clicked')
                adding_item_button =WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@class ="textbox__control"]')))
                print('punkt szusty')

                # if adding_item_button is not None:
                #     for i in range(1, 31):
                #         adding_item_button.click()
                #         print('adding item button clicked')

        except TimeoutException:
            print('poszlo zle2')
            return 0


    def shipping_credentials(self, email, first_name, last_name, street_line, city, postal_code, phone_number):
        try:
            select_country_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="country"]')))
            select_country_button.click()
            country_poland = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//select[@id='country']/option[text()='Poland']")))
            country_poland.click()
            email_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "email")))
            email_button.send_keys(email)
            first_name_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "firstName")))
            first_name_input.send_keys(first_name)
            last_name_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "lastName")))
            last_name_input.send_keys(last_name)
            street_line_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "addressLine1")))
            street_line_input.send_keys(street_line)
            city_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "city")))
            city_input.send_keys(city)
            print("city")
            postal_code_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "postalCode")))
            postal_code_input.send_keys(postal_code)
            print('post')
            phone_number_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "phoneNumber")))
            phone_number_input.send_keys(phone_number)
            print('phone')
            done_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@class="btn btn--primary"]')))
            done_button.click()
            print('after done')
        except TimeoutException:
            print('poszlo zle2')
            return 0

    def gift_cards(self):
        try:
            gift_cards_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="gh-p-6"]')))
            gift_cards_button.click()
            buy_card_now_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@class="page-nav__link btn is-blue"]')))
            buy_card_now_button.click()
            #self.driver.switch_to.window(self.driver.window_handles[-1])
        except TimeoutException:
            print('poszlo zle1')
            return 0
        try:
            time.sleep(10)
            self.driver.switch_to.window(self.driver.window_handles[-1])
            print('i am on the second try')
            occacision_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@class="gallery-categories-dropdown-select-label"]')))
            occacision_button.click()
            time.sleep(10)
            print('after occasion button')

            n = random.randint(1, 7)
            occasion_category_choose = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div[1]/div/ul/li[' + str(n) + ']')))
            occasion_category_choose.click()
            print('after choosing category')
        except TimeoutException:
            print('poszlo zle2')
            return 0


    def amount_button(self):
        try:
            time.sleep(5)
            amount_category_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div[2]')))
            amount_category_button.click()
            print('after choosing amount')
        except TimeoutException:
            print('poszlo zle3')
            return 0

    def gift_card_delivery(self):
        try:
            deliver_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@class="delivery-button delivery-button--selected"]')))
            deliver_button.click()
        except TimeoutException:
            print('poszlo zle4')
            return 0

    def gift_card_details(self, recipient_name, recipient_email, gift_message, sender_name):
        try:
            time.sleep(5)
            print('chce podac odbiorce')
            recipient_name_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'recipient_name')))
            recipient_name_input.send_keys(recipient_name)
            print("after recipient name")
            recipient_email_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "recipient_email")))
            recipient_email_input.send_keys(recipient_email)
            gift_message_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "gift_message")))
            gift_message_input.send_keys(gift_message)
            sender_name_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "sender_name")))
            sender_name_input.send_keys(sender_name)
            continue_gift_card = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@class="action-button filled"]')))
            continue_gift_card.click()
            print("all done")
            self.driver.switch_to.window(self.driver.window_handles[0])
            ebay_main_icon = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="gh-la"]')))
            ebay_main_icon.click()
        except TimeoutException:
            print('poszlo zle5')
            return 0






