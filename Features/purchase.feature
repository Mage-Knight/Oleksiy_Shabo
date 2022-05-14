#@fixture.setup_fixture
Feature: Making laptop purchase on www.demoblaze.com

  Scenario: Open the Log in window
    Given that I am on the home page
    When I click on the log in button
    Then I should see log in window

#  Scenario: Log in to the website
#     Given that I see log in window
#     When I enter "selenium_test" into username field
#     And I enter "test123" into password field
#     And I click log in button
#     Then I should log in

#   Scenario: Open laptops category
#     Given that I am on the home page
#     When I click on the laptops category
#     Then I should see laptops category

#   Scenario: Open Dell i7 8gb page
#     Given that I have laptops category opened
#     When I click on the Dell i7 8gb
#     Then I should see Dell i7 8gb page

#   Scenario: Add Dell i7 8gb to cart
#     Given that I have Dell i7 8gb page opened
#     When I click on the add to cart button
#     Then Dell i7 8gb laptop should be added to cart

#   Scenario: Add Dell i7 8gb to cart
#     Given that I have Dell i7 8gb page opened
#     When I click on the add to cart button
#     Then Dell i7 8gb laptop should be added to cart

#   Scenario: Open place order window
#     Given that I have Dell i7 8gb page opened
#     When I click on the cart button
#     And I click on the place order button
#     Then I should see place order window

#   Scenario: Make a purchase
#     Given that I see pace order window
#     When I enter "Name" into name field
#     And I enter "Country" into country field
#     And I enter "City" into city field
#     And I enter "1234-1234-1234-1234" into credit card field
#     And I enter "December" into month field
#     And I enter "2022" into year field
#     And I click on the purchase button
#     Then I should see pop-up "Thank you for your purchase!"