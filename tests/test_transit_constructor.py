import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators as locs
from data import Data

class TestTransitConstructor:


    def test_constructor_button_transit_from_profile_account(self, driver_login):

        email = Data.get_email()
        password = Data.get_password()
        
        driver_login.find_element(*locs.EMAIL_INPUT).send_keys(email)
        driver_login.find_element(*locs.PASSWORD_INPUT).send_keys(password)
        driver_login.find_element(*locs.ENTER_LOGIN_BUTTON).click()    
    
        WebDriverWait(driver_login, 5).until(
            expected_conditions.visibility_of_element_located(locs.ORDER_BUTTON))
    
        driver_login.find_element(*locs.PROFILE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver_login, 5).until(
            expected_conditions.visibility_of_element_located(locs.LOGOUT_BUTTON))
        
        driver_login.find_element(*locs.CONSTRUCTOR_BUTTON).click()

        WebDriverWait(driver_login, 5).until(
            expected_conditions.visibility_of_element_located(locs.BUNS_SECTION))

        buns_section = driver_login.find_element(*locs.BUNS_SECTION)
        assert "Булки" in buns_section.text

    def test_stellar_burgers_logo_transit_from_profile_account(self, driver_login):

        email = Data.get_email()
        password = Data.get_password()
        
        driver_login.find_element(*locs.EMAIL_INPUT).send_keys(email)
        driver_login.find_element(*locs.PASSWORD_INPUT).send_keys(password)
        driver_login.find_element(*locs.ENTER_LOGIN_BUTTON).click()    
    
        WebDriverWait(driver_login, 5).until(
            expected_conditions.visibility_of_element_located(locs.ORDER_BUTTON))
    
        driver_login.find_element(*locs.PROFILE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver_login, 5).until(
            expected_conditions.visibility_of_element_located(locs.LOGOUT_BUTTON))
        
        driver_login.find_element(*locs.STELLAR_BURGERS_LOGO).click()

        WebDriverWait(driver_login, 5).until(
            expected_conditions.visibility_of_element_located(locs.BUNS_SECTION))

        buns_section = driver_login.find_element(*locs.BUNS_SECTION)
        assert "Булки" in buns_section.text

