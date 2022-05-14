
from behave import given, when, then, fixture, use_fixture
from selenium import webdriver

from POM import page

# @fixture
# def setup_fixture(context):
#     """ Connect driver, maximize window, modify settings and access website"""
#     context.driver = webdriver.Chrome(executable_path = './chromedriver')
#     context.driver.implicitly_wait(3)
#     context.driver.maximize_window()
#     context.driver.get("https://www.demoblaze.com/")
#     yield context.driver
#     """ Quit """
#     context.driver.close()
#     context.driver.quit()

# @fixture
# def login_page_fixture(context):
#     main_page = page.MainPage(context.driver)
#     main_page.click_login_button()

# @fixture
# def login_fixture(context):
#     use_fixture(login_page_fixture, context)
#     main_page = page.MainPage(context.driver)
#     main_page.username_text_element = "selenium_test"
#     main_page.password_text_element = "test123"
#     main_page.click_sub_login_button()

# @fixture
# def laptops_fixture(context):
#     use_fixture(login_fixture, context)
#     main_page = page.MainPage(context.driver)
#     main_page.refresh_page()
#     main_page.click_laptops_button()

# @fixture
# def delli7_fixture(context):
#     use_fixture(laptops_fixture, context)
#     main_page = page.MainPage(context.driver)
#     main_page.click_dell_i7_button()

# @fixture
# def delli7_fixture(context):
#     use_fixture(login_page_fixture, context)
#     main_page = page.MainPage(context.driver)
#     main_page.click_dell_i7_button()

# @fixture
# def add_cart_fixture(context):
#     use_fixture(delli7_fixture, context)
#     laptop_page = page.DellI7Page(context.driver)
#     laptop_page.click_add_to_cart_button()

# @fixture
# def order_fixture(context):
#     use_fixture(add_cart_fixture, context)
#     laptop_page = page.DellI7Pagecontext(context.driver)
#     laptop_page.accept_pop_up()
#     laptop_page.click_cart_button()
#     cart_page = page.CartPage(context.driver)
#     cart_page.place_order_button()

@given('that I am on the home page')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path = './chromedriver')
    context.driver.implicitly_wait(3)
    context.driver.maximize_window()
    context.driver.get("https://www.demoblaze.com/")
    yield context.driver


@when('I click on the log in button')
def step_impl(context):
    main_page = page.MainPage(context.driver)
    main_page.click_login_button()


@then('I should see log in window')
def step_impl(context):
    main_page = page.MainPage(context.driver)
    assert main_page.is_log_in()
    """ Quit """
    context.driver.close()
    context.driver.quit()


@given(u'that I see log in window')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given that I see log in window')


@when(u'I enter "selenium_test" into username field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter "selenium_test" into username field')


@when(u'I enter "test123" into password field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter "test123" into password field')


@when(u'I click log in button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click log in button')


@then(u'I should log in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should log in')


@when(u'I click on the laptops category')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on the laptops category')


@then(u'I should see laptops category')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see laptops category')


@given(u'that I have laptops category opened')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given that I have laptops category opened')


@when(u'I click on the Dell i7 8gb')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on the Dell i7 8gb')


@then(u'I should see Dell i7 8gb page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see Dell i7 8gb page')


@given(u'that I have Dell i7 8gb page opened')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given that I have Dell i7 8gb page opened')


@when(u'I click on the add to cart button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on the add to cart button')


@then(u'Dell i7 8gb laptop should be added to cart')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Dell i7 8gb laptop should be added to cart')


@when(u'I click on the cart button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on the cart button')


@when(u'I click on the place order button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on the place order button')


@then(u'I should see place order window')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see place order window')


@given(u'that I see pace order window')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given that I see pace order window')


@when(u'I enter "Name" into name field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter "Name" into name field')


@when(u'I enter "Country" into country field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter "Country" into country field')


@when(u'I enter "City" into city field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter "City" into city field')


@when(u'I enter "1234-1234-1234-1234" into credit card field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter "1234-1234-1234-1234" into credit card field')


@when(u'I enter "December" into month field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter "December" into month field')


@when(u'I enter "2022" into year field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter "2022" into year field')


@when(u'I click on the purchase button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on the purchase button')


@then(u'I should see pop-up "Thank you for your purchase!"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see pop-up "Thank you for your purchase!"')