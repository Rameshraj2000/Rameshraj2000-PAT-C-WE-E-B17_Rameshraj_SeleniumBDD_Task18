from selenium import webdriver

class DriverFactory: #Factory class to initialize and return WebDriver instance

    def get_driver(self): #Initialize Chrome driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver