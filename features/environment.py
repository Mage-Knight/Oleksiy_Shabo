from selenium import webdriver

def before_scenario(context, scenario):
    """ Connect driver, maximize window, modify settings and access website"""
    context.driver = webdriver.Chrome(executable_path = './chromedriver')
    context.driver.implicitly_wait(3)
    context.driver.maximize_window()
    context.driver.get("https://www.demoblaze.com/")


def after_scenario(context, scenario):
    """ Quit """
    context.driver.close()
    context.driver.quit()