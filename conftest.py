import random
from selenium import webdriver
import pytest

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
    driver.get("https://stellarburgers.education-services.ru/")
    return driver

@pytest.fixture
def driver_login(driver):
    driver.get("https://stellarburgers.education-services.ru/login")
    return driver



@pytest.fixture
def driver_register(driver):
    driver.get("https://stellarburgers.education-services.ru/register")
    return driver

@pytest.fixture
def driver_forgot_password(driver):
    driver.get("https://stellarburgers.education-services.ru/forgot-password")
    return driver

@pytest.fixture
def name_registration():
    return 'Павел'

@pytest.fixture
def random_email():
    return f'pavelkuznetsov39{random.randint(100, 999)}@gmail.com'

@pytest.fixture
def random_password():
    return str(random.randint(100000, 999999999))

@pytest.fixture
def invalid_random_password():
    return str(random.randint(0, 99999))  

@pytest.fixture
def email():
    return 'pavelkuznetsov39000@gmail.com'

@pytest.fixture
def password():
    return 'tngozp33'

