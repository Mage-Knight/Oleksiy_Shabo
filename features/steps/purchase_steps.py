from behave import given, when, then, fixture, use_fixture
from POM import page

@fixture
def login_page_fixture(context):
    context.main_page = page.MainPage(context.driver)
    context.main_page.click_login_button()

@fixture
def login_fixture(context):
    use_fixture(login_page_fixture, context)
    context.main_page.username_text_element = "selenium_test"
    context.main_page.password_text_element = "test123"
    context.main_page.click_sub_login_button()

@fixture
def laptops_fixture(context):
    use_fixture(login_fixture, context)
    context.main_page.refresh_page()
    context.main_page.click_laptops_button()

@fixture
def delli7_fixture(context):
    use_fixture(laptops_fixture, context)
    context.main_page.click_dell_i7_button()

@fixture
def add_cart_fixture(context):
    use_fixture(delli7_fixture, context)
    context.laptop_page = page.DellI7Page(context.driver)
    context.laptop_page.click_add_to_cart_button()
    context.laptop_page.accept_pop_up()

@fixture
def order_fixture(context):
    use_fixture(add_cart_fixture, context)
    context.laptop_page.click_cart_button()
    context.cart_page = page.CartPage(context.driver)
    context.cart_page.place_order_button()

@given('that I am on the home page')
def step_impl(context):
    context.main_page = page.MainPage(context.driver)


@when('I click on the log in button')
def step_impl(context):
    context.main_page.click_login_button()


@then('I should see log in window')
def step_impl(context):
    assert context.main_page.is_log_in()


@given('that I see log in window')
def step_impl(context):
    use_fixture(login_page_fixture, context)
    context.main_page = page.MainPage(context.driver)
     
    
@when('I enter "selenium_test" into username field')
def step_impl(context):
    context.main_page.username_text_element = "selenium_test"


@when('I enter "test123" into password field')
def step_impl(context):
    context.main_page.password_text_element = "test123"


@when('I click log in button')
def step_impl(context):
    context.main_page.click_sub_login_button()


@then('I should log in as user')
def step_impl(context):
    assert context.main_page.is_logged_in()


@given('that I am on the home page logged in as user')
def step_impl(context):
    use_fixture(login_fixture, context)


@when('I click on the laptops category')
def step_impl(context):
    context.main_page.refresh_page()
    context.main_page.click_laptops_button()


@then('I should see laptops category')
def step_impl(context):
    assert context.main_page.is_laptops_page()


@given('that I have laptops category opened')
def step_impl(context):
    use_fixture(laptops_fixture, context)


@when('I click on the Dell i7 8gb')
def step_impl(context):
    context.main_page.click_dell_i7_button()


@then('I should see Dell i7 8gb page')
def step_impl(context):
    context.laptop_page = page.DellI7Page(context.driver)
    assert context.laptop_page.check_page()


@given('that I have Dell i7 8gb page opened')
def step_impl(context):
    use_fixture(delli7_fixture, context)


@when('I click on the add to cart button')
def step_impl(context):
    context.laptop_page = page.DellI7Page(context.driver)
    context.laptop_page.click_add_to_cart_button()


@then('Dell i7 8gb laptop should be added to cart')
def step_impl(context):
    assert context.laptop_page.check_add_to_cart()
    context.laptop_page.accept_pop_up()


@given('that I have Dell i7 8gb page opened with Dell i7 8gb in cart')
def step_impl(context):
    use_fixture(add_cart_fixture, context)


@when('I click on the cart button')
def step_impl(context):
    context.laptop_page.click_cart_button()


@when('I click on the place order button')
def step_impl(context):
    context.cart_page = page.CartPage(context.driver)
    context.cart_page.place_order_button()


@then('I should see place order window')
def step_impl(context):
    assert context.cart_page.is_placed_order()


@given('that I see pace order window')
def step_impl(context):
    use_fixture(order_fixture, context)
    

@when('I enter "Name" into name field')
def step_impl(context):
    context.cart_page.name_text_element = "Name"


@when('I enter "Country" into country field')
def step_impl(context):
    context.cart_page.country_text_element = "Country"


@when('I enter "City" into city field')
def step_impl(context):
    context.cart_page.city_text_element = "City"


@when('I enter "1234-1234-1234-1234" into credit card field')
def step_impl(context):
    context.cart_page.card_text_element = "1234-1234-1234-1234"


@when('I enter "December" into month field')
def step_impl(context):
    context.cart_page.month_text_element = "December"


@when('I enter "2022" into year field')
def step_impl(context):
    context.cart_page.year_text_element = "2022"


@when('I click on the purchase button')
def step_impl(context):
    context.cart_page.click_purchase_button()


@then('I should see pop-up "Thank you for your purchase!"')
def step_impl(context):
    assert context.cart_page.is_successful_purchase()