from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_login_page(self):
        login_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login")))
        login_link.click()

    def login(self, email, password):
        self.wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(email)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()

    def is_login_successful(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Logged in as')]")))

    def logout(self):
        logout_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Logout')]")))
        logout_link.click()

    def is_logout_successful(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Login to your account')]")))
