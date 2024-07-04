
#aaaaaaaaaa

import pytest
from selenium import webdriver
from src.pages.all_pages.main_page import MainPage
from src.pages.all_pages.cases_page import Cases
import pytest
from datetime import datetime
import os
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from src.pages.all_pages.main_page import MainPage
# from src.pages.all_pages.cases_page import Cases
# from datetime import datetime
# import os

#added by Pawel
# @pytest.fixture
# def driver():
#     adblock_path = r'C:\Users\TOSHIBA TOUCHSCREEN\AppData\Local\Google\Chrome\User Data\Default\Extensions\lgblnfidahcdcjddiepkckcfdhpknnjh\1.573_0'
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument(f'--load-extension={adblock_path}')
#
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#     driver.get('https://www.onet.pl')
#     driver.quit()
#     options = webdriver.ChromeOptions()
#     options.add_argument("window-size=1920,1080")  # Corrected syntax
#     options.add_argument("--disable-geolocation")  # Corrected flag
#     options.add_argument("--disable-notifications")
#     with webdriver.Chrome(options=options) as driver:
#         driver.implicitly_wait(10)
#         yield driver


#Fixture for initializing the WebDriver with uBlock Origin extension
# @pytest.fixture
# def driver():
#     # Path to the uBlock Origin extension
#     ublock_extension_path = '/path/to/ublock_origin_extension.crx'
#
#     # Set up Chrome options
#     options = webdriver.ChromeOptions()
#     options.add_argument("window-size=1920,1080")
#     options.add_argument("--disable-geolocation")
#     options.add_argument("--disable-notifications")
#
#     # Add uBlock Origin extension
#     options.add_extension(ublock_extension_path)
#
#     # Set up Chrome driver
#     driver_path = '/path/to/chromedriver'  # Set your Chrome driver path
#     service = Service(driver_path)
#     driver = webdriver.Chrome(service=service, options=options)
#
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()


# @pytest.fixture    #temporary, till checking add blocker
# def driver():
#     options = webdriver.ChromeOptions()
#     options.add_argument("window-size=1920,1080")  # Corrected syntax
#     options.add_argument("--disable-geolocation")  # Corrected flag
#     options.add_argument("--disable-notifications")
#     with webdriver.Chrome(options=options) as driver:
#         driver.implicitly_wait(10)
#         yield driver

# @pytest.fixture
# def driver():
#     options = webdriver.ChromeOptions()
#     options.add_argument("window-size=1920,1080")
#     options.add_argument("--disable-geolocation")
#     options.add_argument("--disable-notifications")
#     # Disable images
#     prefs = {"profile.managed_default_content_settings.images": 2}
#     # Disable JavaScript - Warning: This might break a lot of sites
#     # prefs["profile.managed_default_content_settings.javascript"] = 2
#     options.add_experimental_option("prefs", prefs)
#
#     with webdriver.Chrome(options=options) as driver:
#         driver.implicitly_wait(10)
#         yield driver

# @pytest.fixture(autouse=True)   #temporary, till checking add blocker
# def open_main_page(driver):
#     main_page = MainPage(driver)
#     main_page.open_main_page()

# @pytest.fixture   #temporary, till checking add blocker
# def navigate_to_main_page(driver):
#     main_page = MainPage(driver)
#     main_page.open_main_page()
#     return main_page

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.when == "call" and rep.failed:
#         mode = "a" if os.path.exists("failures.txt") else "w"
#         try:
#             web_driver = item.funcargs['driver']
#             if web_driver:
#                 timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#                 screenshot_name = f"screenshot_{timestamp}.png"
#                 web_driver.save_screenshot(screenshot_name)
#                 with open("failures.txt", mode) as f:
#                     f.write(f"FAIL: {item.nodeid} with {screenshot_name}\n")
#         except Exception as e:
#             print(f"Failed to capture screenshot: {e}")

#BBBBBBBB


#fROM HERE

# ZABEZPIECZENIE
# from selenium import webdriver
# from src.pages.all_pages.main_page import MainPage
# from src.pages.all_pages.cases_page import Cases
# import pytest
# from datetime import datetime
# import os
# from selenium.webdriver.chrome.service import Service
#
# @pytest.fixture    #temporary, till checking add blocker
# def driver():
#     options = webdriver.ChromeOptions()
#     options.add_argument("window-size=1920,1080")  # Corrected syntax
#     options.add_argument("--disable-geolocation")  # Corrected flag
#     options.add_argument("--disable-notifications")
#     with webdriver.Chrome(options=options) as driver:
#         driver.implicitly_wait(10)
#         yield driver
#
# @pytest.fixture(autouse=True)   #temporary, till checking add blocker
# def open_main_page(driver):
#     main_page = MainPage(driver)
#     main_page.open_main_page()
#
# @pytest.fixture   #temporary, till checking add blocker
# def navigate_to_main_page(driver):
#     main_page = MainPage(driver)
#     main_page.open_main_page()
#     return main_page


#uncomment anel stexic, arel em comment for conftesty stugem

# #commenting from here the Pawels code
# from selenium import webdriver
# from src.pages.all_pages.main_page import MainPage
# from src.pages.all_pages.cases_page import Cases
# import pytest
# from datetime import datetime
# import os
# from selenium.webdriver.chrome.service import Service
#
# @pytest.fixture    #temporary, till checking add blocker
# def driver():
#     options = webdriver.ChromeOptions()
#     options.add_argument("window-size=1920,1080")  # Corrected syntax
#     options.add_argument("--disable-geolocation")  # Corrected flag
#     options.add_argument("--disable-notifications")
#
#     #### THIS MAKES ADBLOCK WORKS
#     # options.add_argument("--no-sandbox")
#     # options.add_argument('--load-extension=C:/Users/TOSHIBA TOUCHSCREEN/AppData/Local/Google/Chrome/User Data/Default/Extensions/lgblnfidahcdcjddiepkckcfdhpknnjh/1.573_0')
#     # options.add_experimental_option('useAutomationExtension', False)
#     # options.add_experimental_option('excludeSwitches', ['enable-automation'])
#     #### END OF WHAT MAKES ADBLOCK WORKS
#
#
#     with webdriver.Chrome(options=options) as driver:
#         driver.implicitly_wait(10)
#         yield driver
#
# @pytest.fixture(autouse=True)   #temporary, till checking add blocker
# def open_main_page(driver):
#     main_page = MainPage(driver)
#     main_page.open_main_page()
#
# @pytest.fixture   #temporary, till checking add blocker
# def navigate_to_main_page(driver):
#     main_page = MainPage(driver)
#     main_page.open_main_page()
#     return main_page
# #ending here the comment of Pawels code
#
