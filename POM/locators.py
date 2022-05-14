from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """ Locators for main page """
    LOGIN_BUTTON = (By.ID, "login2")
    LOGIN_LABEL = (By.ID, "logInModalLabel")
    USERNAME_LABEL = (By.ID, "nameofuser")
    USERNAME_FIELD = (By.ID, "loginusername")
    PASSWORD_FIELD = (By.ID, "loginpassword")
    SUB_LOGIN_BUTTON = (By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]")
    LAPTOPS_BUTTON = (By.LINK_TEXT, "Laptops")
    DELL_I7_BUTTON = (By.LINK_TEXT, "Dell i7 8gb")

class DellI7Locators(object):
    """ Locators for DellI7 page """
    ADD_TO_CART_BUTTON = (By.LINK_TEXT, "Add to cart")
    CART_BUTTON = (By.ID, "cartur")
    DELL_I7_LABEL = (By.XPATH, "/html/body/div[5]/div/div[2]/h2")

class CartLocators(object):
    """ Locators for cart page """
    PLACE_ORDER_BUTTON = (By.XPATH, "/html/body/div[6]/div/div[2]/button")
    NAME_FIELD = (By.ID, "name")
    COUNTRY_FIELD = (By.ID, "country")
    CITY_FIELD = (By.ID, "city")
    CARD_FIELD = (By.ID, "card")
    MONTH_FIELD = (By.ID, "month")
    YEAR_FIELD = (By.ID, "year")
    PURCHASE_BUTTON = (By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]")
    PLACE_ORDER_LABEL = (By.ID, "orderModalLabel")
    SUCESSFUL_PURCHASE = (By.XPATH, "/html/body/div[10]")