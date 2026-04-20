from behave import given, when, then
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.driver_factory import DriverFactory
from selenium.common.exceptions import NoSuchElementException

@given("user is on login page")
def step_impl(context): #launch browser and navigate to login page
    context.driver = DriverFactory().get_driver()
    context.page = LoginPage(context.driver)
    context.page.open_url("https://v2.zenclass.in/login")

@when("user enters valid username and password")
def step_impl(context): #user enters valid login details
    context.page.enter_username("draj56403@gmail.com")
    context.page.enter_password("Ramesh@1#")

@when("user enters invalid username and password")
def step_impl(context): #user enters invalid details
    context.page.enter_username("wrong@gmail.com")
    context.page.enter_password("wrong")

@when("clicks login button")
def step_impl(context): #user clicks login button
    context.page.click_login()

@then("user should be logged in successfully")
def step_impl(context): #checks whether users logged in successfully
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.url_contains("dashboard"))
    assert "dashboard" in context.driver.current_url

@then("error message should be displayed")
def step_impl(context): #checks error message if user enters invalid details
    try:
        error = context.driver.find_element(By.XPATH, "//p[text()='*Invalid email!']")
        assert error.is_displayed()
    except NoSuchElementException:
        assert False, "Error message not found"

@then("username and password fields should be visible")
def step_impl(context): #checks username and password fields are displayed
    assert context.driver.find_element(By.XPATH, "//input[@placeholder='Enter your mail']").is_displayed()
    assert context.driver.find_element(By.XPATH, "//input[@placeholder='Enter your password ']").is_displayed()

@when("user clicks logout")
def step_impl(context): #user clicks logout button
    context.page.click_logout()

@then("user should be logged out successfully")
def step_impl(context): #checks user logged out successfully
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.url_contains("login"))  # change this based on real URL
    assert "login" in context.driver.current_url

@given("user is logged in")
def step_impl(context): #performs login and logout
    context.driver = DriverFactory().get_driver()
    context.page = LoginPage(context.driver)

    context.page.open_url("https://v2.zenclass.in/login")

    context.page.enter_username("draj56403@gmail.com")
    context.page.enter_password("Ramesh@1#")
    context.page.click_login()