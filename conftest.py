
from selenium import webdriver
from src.pages.all_pages.main_page import MainPage
import pytest

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1920,1080")  # Corrected syntax
    options.add_argument("--disable-geolocation")  # Corrected flag
    options.add_argument("--disable-notifications")

    ### THIS MAKES ADBLOCK WORKS
    options.add_argument("--no-sandbox")
    options.add_argument('--load-extension=C:/Users/TOSHIBA TOUCHSCREEN/AppData/Local/Google/Chrome/User Data/Default/Extensions/lgblnfidahcdcjddiepkckcfdhpknnjh/2.1.20_0')
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    ### END OF WHAT MAKES ADBLOCK WORKS


    with webdriver.Chrome(options=options) as driver:
        driver.implicitly_wait(10)
        yield driver

@pytest.fixture(autouse=True)
def open_main_page(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()

@pytest.fixture
def navigate_to_main_page(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()
    return main_page
