from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactUsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_contact_us_page(self):
        contact_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Contact us")))
        print("Contact Us link is clickable, now clicking.")
        contact_link.click()

    def submit_contact_form(self, name, email, subject, message):
        self.wait.until(EC.presence_of_element_located((By.NAME, "name"))).send_keys(name)
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "subject").send_keys(subject)
        self.driver.find_element(By.NAME, "message").send_keys(message)
        self.driver.find_element(By.NAME, "submit").click()
        #alert = self.driver.switch_to.alert
        #alert.accept()