import sys
from pathlib import Path

sys.path[0] = str(Path(sys.path[0]).parent)

import pytest
from selenium import webdriver
from POM import page

@pytest.fixture()
def setup_fixture():
    """ Connect driver, maximize window, modify settings and access website"""
    driver = webdriver.Chrome(executable_path = './chromedriver')
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get("https://www.demoblaze.com/")
    yield driver
    """ Quit """
    driver.close()
    driver.quit()

@pytest.fixture()
def login_page_fixture(setup_fixture):
    driver = setup_fixture
    main_page = page.MainPage(driver)
    main_page.click_login_button()
    return driver

@pytest.fixture()
def login_fixture(login_page_fixture):
    driver = login_page_fixture
    main_page = page.MainPage(driver)
    main_page.username_text_element = "selenium_test"
    main_page.password_text_element = "test123"
    main_page.click_sub_login_button()
    return driver

@pytest.fixture()
def laptops_fixture(login_fixture):
    driver = login_fixture
    main_page = page.MainPage(driver)
    main_page.refresh_page()
    main_page.click_laptops_button()
    return driver

@pytest.fixture()
def delli7_fixture(laptops_fixture):
    driver = laptops_fixture
    main_page = page.MainPage(driver)
    main_page.click_dell_i7_button()
    return driver

@pytest.fixture()
def add_cart_fixture(delli7_fixture):
    driver = delli7_fixture
    laptop_page = page.DellI7Page(driver)
    laptop_page.click_add_to_cart_button()
    return driver

@pytest.fixture()
def order_fixture(add_cart_fixture):
    driver = add_cart_fixture
    laptop_page = page.DellI7Page(driver)
    laptop_page.accept_pop_up()
    laptop_page.click_cart_button()
    cart_page = page.CartPage(driver)
    cart_page.place_order_button()
    return driver

def test_login_page(login_page_fixture):
    """ Check clicking login button """
    main_page = page.MainPage(login_page_fixture)
    assert main_page.is_log_in()

def test_login(login_fixture):
    """ Check log in """
    main_page = page.MainPage(login_fixture)
    assert main_page.is_logged_in()

def test_category(laptops_fixture):
    """ Check selecting laptop category """
    main_page = page.MainPage(laptops_fixture)
    assert main_page.is_laptops_page()

def test_select(delli7_fixture):
    """ Check DellI7 page """ 
    laptop_page = page.DellI7Page(delli7_fixture)
    assert laptop_page.check_page()

def test_add_cart(add_cart_fixture):
    """ Check adding laptop to cart """ 
    laptop_page = page.DellI7Page(add_cart_fixture)
    assert laptop_page.check_add_to_cart()
    laptop_page.accept_pop_up()

def test_order(order_fixture):
    """ Check placing order """
    cart_page = page.CartPage(order_fixture)
    assert cart_page.is_placed_order()

def test_purchase(order_fixture):
    """ Check entering information and making purchase """
    cart_page = page.CartPage(order_fixture)
    cart_page.name_text_element = "Name"
    cart_page.country_text_element = "Country"
    cart_page.city_text_element = "City"
    cart_page.card_text_element = "1234-1234-1234-1234"
    cart_page.month_text_element = "December"
    cart_page.year_text_element = "2022"
    cart_page.click_purchase_button()
    assert cart_page.is_successful_purchase()