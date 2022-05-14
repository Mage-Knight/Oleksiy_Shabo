import sys
sys.path.append("./POM")

from locators import *
from element import BasePageElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
wait_time = 5

# Defining classes, that represent different elements on the website.
class UsernameTextElement(BasePageElement):
    locator = MainPageLocators.USERNAME_FIELD

class PasswordTextElement(BasePageElement):
    locator = MainPageLocators.PASSWORD_FIELD

class NameOfUserTextElement(BasePageElement):
    locator = MainPageLocators.USERNAME_LABEL

class NameTextElement(BasePageElement):
    locator = CartLocators.NAME_FIELD

class CountryTextElement(BasePageElement):
    locator = CartLocators.COUNTRY_FIELD 

class CityTextElement(BasePageElement):
    locator = CartLocators.CITY_FIELD

class CardTextElement(BasePageElement):
    locator = CartLocators.CARD_FIELD

class MonthTextElement(BasePageElement):
    locator = CartLocators.MONTH_FIELD

class YearTextElement(BasePageElement):
    locator = CartLocators.YEAR_FIELD

class BasePage(object):
    """ Base class to initialize the base page that will be called from all pages """
    def __init__(self, driver):
        self.driver = driver

    def click_button(self, locator):
        WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable(locator)).click()

    def refresh_page(self):
        self.driver.refresh()

    def accept_pop_up(self):
        WebDriverWait(self.driver, wait_time).until(EC.alert_is_present())
        Alert(self.driver).accept()

    def check_pop_up(self, message):
        WebDriverWait(self.driver, wait_time).until(EC.alert_is_present())
        return Alert(self.driver).text == message

    def check_visibility(self, locator):
        return WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(locator)).is_displayed()

    def check_click(self, locator):
        return bool(WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable(locator)))

class MainPage(BasePage):
    """ Home page action methods and elements"""
    username_text_element = UsernameTextElement()
    password_text_element = PasswordTextElement()
    name_of_user_text_element = NameOfUserTextElement()

    def is_pop_up_appeared(self):
        return "Thank you for your purchase!" in self.driver.page_source
    
    def click_login_button(self):
        self.click_button(MainPageLocators.LOGIN_BUTTON)

    def click_sub_login_button(self):
        self.click_button(MainPageLocators.SUB_LOGIN_BUTTON)

    def click_laptops_button(self):
        self.click_button(MainPageLocators.LAPTOPS_BUTTON)

    def click_dell_i7_button(self):
        self.click_button(MainPageLocators.DELL_I7_BUTTON)

    def is_log_in(self):
        return self.check_visibility(MainPageLocators.LOGIN_LABEL) and self.check_click(MainPageLocators.SUB_LOGIN_BUTTON)

    def is_logged_in(self):
        WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(MainPageLocators.USERNAME_LABEL))
        return self.name_of_user_text_element == "Welcome selenium_test"

    def is_laptops_page(self):
        return self.check_visibility(MainPageLocators.DELL_I7_BUTTON)

class DellI7Page(BasePage):
    """ DellI7 page action methods """
    def click_add_to_cart_button(self):
        self.click_button(DellI7Locators.ADD_TO_CART_BUTTON)

    def click_cart_button(self):
        self.click_button(DellI7Locators.CART_BUTTON)

    def check_page(self):
        return self.check_visibility(DellI7Locators.DELL_I7_LABEL) and self.check_click(DellI7Locators.ADD_TO_CART_BUTTON)

    def check_add_to_cart(self):
        return self.check_pop_up("Product added")

class CartPage(BasePage):
    """ Cart page action methods and elements"""
    name_text_element = NameTextElement()
    country_text_element = CountryTextElement()
    city_text_element = CityTextElement()
    card_text_element = CardTextElement()
    month_text_element = MonthTextElement()
    year_text_element = YearTextElement()

    def place_order_button(self):
        self.click_button(CartLocators.PLACE_ORDER_BUTTON)

    def click_purchase_button(self):
        self.click_button(CartLocators.PURCHASE_BUTTON)

    def is_placed_order(self):
        return self.check_visibility(CartLocators.PLACE_ORDER_LABEL) and self.check_click(CartLocators.PLACE_ORDER_BUTTON)

    def is_successful_purchase(self):
        return self.check_visibility(CartLocators.SUCESSFUL_PURCHASE)
