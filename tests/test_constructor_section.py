import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators as locs
from data import Data

class TestConstructorSection:

    @pytest.mark.parametrize("transit_section, transit_select_section, ingredient", [
        (locs.TOPPINGS_SECTION, locs.SELECT_TOPPINGS_SECTION, 'Начинки'),
        (locs.SAUCES_SECTION, locs.SELECT_SAUCES_SECTION, 'Соусы')])
    def test_toppings_and_sauces_section_transit_from_buns_section(
        self, driver_login, transit_section, transit_select_section, ingredient):

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
        
        driver_login.find_element(*transit_section).click()

        WebDriverWait(driver_login, 5).until(
            expected_conditions.visibility_of_element_located(transit_select_section))

        select_toppings_section = driver_login.find_element(*transit_select_section)
        assert ingredient in select_toppings_section.text


    def test_buns_section_transit_from_sauces_section(self, driver_login):

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
        
        driver_login.find_element(*locs.SAUCES_SECTION).click()

        WebDriverWait(driver_login, 5).until(
            expected_conditions.visibility_of_element_located(locs.SELECT_SAUCES_SECTION))
        
        driver_login.find_element(*locs.BUNS_SECTION).click()

        WebDriverWait(driver_login, 5).until(
            expected_conditions.visibility_of_element_located(locs.SELECT_BUNS_SECTION))

        select_buns_section = driver_login.find_element(*locs.SELECT_BUNS_SECTION)
        assert "Булки" in select_buns_section.text

