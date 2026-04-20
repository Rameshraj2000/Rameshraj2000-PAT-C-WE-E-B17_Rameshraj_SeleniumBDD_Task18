from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage): #Page Object Model class for Login Page.

    # Contains all locators and actions related to login/logout.
    username = (By.XPATH, "//input[@placeholder='Enter your mail']")
    password = (By.XPATH, "//input[@placeholder='Enter your password ']")
    login_btn = (By.XPATH, "//button[@type='submit']")
    drop_down_dash = (By.XPATH, "//img[@id='profile-click-icon']")
    logout_btn = (By.XPATH, "//div[contains(text(),'Log out')]")
    close_popup_btn = (By.XPATH, "//button[@aria-label='Close popup']")

    def enter_username(self, user): #Enter username into username field
        self.driver.find_element(*self.username).send_keys(user)

    def enter_password(self, pwd): #Enter password into username field
        self.driver.find_element(*self.password).send_keys(pwd)

    def click_login(self): #Click on login button
        self.driver.find_element(*self.login_btn).click()

    def click_logout(self):
        wait = WebDriverWait(self.driver, 20)

        # Handle popup (optional)
        try:
            popup = wait.until(EC.element_to_be_clickable(self.close_popup_btn))
            popup.click()
        except:
            print("No popup appeared")

        # Click dropdown/profile
        dropdown = wait.until(EC.element_to_be_clickable(self.drop_down_dash))
        dropdown.click()

        # Click logout
        logout = wait.until(EC.element_to_be_clickable(self.logout_btn))
        logout.click()