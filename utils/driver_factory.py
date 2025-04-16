from selenium import webdriver

class DriverFactory:
    @staticmethod
    def get_driver():
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.get("https://automationexercise.com/")
        return driver
