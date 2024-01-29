import pytest
from selenium import webdriver
from src.pages.main.main_page import MainPage
from src.pages.login.login_page import LoginPage

@pytest.fixture
def driver():
    with webdriver.Chrome() as driver:
        yield driver

@pytest.fixture(autouse=True)
def open_main_page(driver):
    main_page = MainPage(driver)
    main_page.driver.get("https://automationexercise.com/")

@pytest.fixture(scope="module", autouse=True)
def teardown_module(request):
    yield
    print("all is done")

@pytest.fixture
def setup():
    yield


