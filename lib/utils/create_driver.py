import pytest
from selenium.webdriver import Chrome,Firefox


def get_driver_instance():
    browser = pytest.config.options.type.lower()
    if browser == 'chrome':
        driver = Chrome("./browser-ser/chromedriver.exe")
    elif browser == 'firefox':
        driver = Firefox("./browser-ser/geckodriver.exe")
    else:
        print("Invalid Browser option")
        return None
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get("http://localhost")
    return driver