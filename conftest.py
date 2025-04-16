import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://automationexercise.com/")
    
    request.cls.driver = driver
    yield driver
    driver.quit()

