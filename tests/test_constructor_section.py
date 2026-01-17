import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators as locs

class TestConstructorSection:


    def test_toppings_section_transit_from_buns_section(self, driver_login, email, password):
        
        driver_login.find_element(*locs.EMAIL_LOGIN_BUTTON).send_keys(email)
        driver_login.find_element(*locs.PASSWORD_LOGIN_BUTTON).send_keys(password)
        driver_login.find_element(*locs.ENTER_LOGIN_BUTTON).click()    
    
        WebDriverWait(driver_login, 5).until(
            expected_conditions.visibility_of_element_located(locs.ORDER_BUTTON))
    
        driver_login.find_element(*locs.PROFILE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver_login, 5).until(
            expected_conditions.visibility_of_element_located(locs.LOGOUT_BUTTON))
        
        driver_login.find_element(*locs.CONSTRUCTOR_BUTTON).click()

        WebDriverWait(driver_login, 5).until(
            expected_conditions.visibility_of_element_located(locs.BUNS_SECTION))
        
        driver_login.find_element(*locs.TOPPINGS_SECTION).click()

        WebDriverWait(driver_login, 5).until(
            expected_conditions.visibility_of_element_located(locs.SELECT_TOPPINGS_SECTION))

        select_toppings_section = driver_login.find_element(*locs.SELECT_TOPPINGS_SECTION)
        assert "Начинки" in select_toppings_section.text


    def test_sauces_section_transit_from_buns_section(self, driver_login, email, password):
        
        driver_login.find_element(*locs.EMAIL_LOGIN_BUTTON).send_keys(email)
        driver_login.find_element(*locs.PASSWORD_LOGIN_BUTTON).send_keys(password)
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

        select_sauces_section = driver_login.find_element(*locs.SELECT_SAUCES_SECTION)
        assert "Соусы" in select_sauces_section.text


    def test_buns_section_transit_from_sauces_section(self, driver_login, email, password):
        
        driver_login.find_element(*locs.EMAIL_LOGIN_BUTTON).send_keys(email)
        driver_login.find_element(*locs.PASSWORD_LOGIN_BUTTON).send_keys(password)
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

