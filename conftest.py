from selenium import webdriver
import pytest
from urls import Urls

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    try:
        driver.quit()
    except:
        pass

@pytest.fixture
def driver_home(driver):
    driver.get(Urls.HOME_URL)
    return driver

@pytest.fixture
def driver_login(driver):
    driver.get(Urls.LOGIN_URL)
    return driver

@pytest.fixture
def driver_register(driver):
    driver.get(Urls.REGISTER_URL)
    return driver

@pytest.fixture
def driver_forgot_password(driver):
    driver.get(Urls.FORGOT_PASSWORD_URL)
    return driver



