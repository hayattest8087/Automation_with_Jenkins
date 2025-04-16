import allure

def take_screenshot(driver, name="failure_screenshot"):
    screenshot = driver.get_screenshot_as_png()
    allure.attach(
        screenshot,
        name=name,
        attachment_type=allure.attachment_type.PNG
    )
