import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators as locs
from data import Data

class TestLogin:


    def test_login_homepage_login_button(self, driver_home):

        email = Data.get_email()
        password = Data.get_password()

        driver_home.find_element(*locs.LOGIN_HOMEPAGE_BUTTON).click()

        WebDriverWait(driver_home, 5).until(
            expected_conditions.visibility_of_element_located(locs.LOGIN_TITLE))
        
        driver_home.find_element(*locs.EMAIL_INPUT).send_keys(email)
        driver_home.find_element(*locs.PASSWORD_INPUT).send_keys(password)
        driver_home.find_element(*locs.ENTER_LOGIN_BUTTON).click()    
    
        WebDriverWait(driver_home, 5).until(
            expected_conditions.visibility_of_element_located(locs.ORDER_BUTTON))
    
        order_button = driver_home.find_element(*locs.ORDER_BUTTON)
        assert "Оформить заказ" in order_button.text


    def test_login_homepage_profile_button(self, driver_home):

        email = Data.get_email()
        password = Data.get_password()

        driver_home.find_element(*locs.PROFILE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver_home, 5).until(
            expected_conditions.visibility_of_element_located(locs.LOGIN_TITLE))
        
        driver_home.find_element(*locs.EMAIL_INPUT).send_keys(email)
        driver_home.find_element(*locs.PASSWORD_INPUT).send_keys(password)
        driver_home.find_element(*locs.ENTER_LOGIN_BUTTON).click()    
    
        WebDriverWait(driver_home, 5).until(
            expected_conditions.visibility_of_element_located(locs.ORDER_BUTTON))
    
        order_button = driver_home.find_element(*locs.ORDER_BUTTON)
        assert "Оформить заказ" in order_button.text


    def test_login_button_from_register_page(self, driver_register):

        email = Data.get_email()
        password = Data.get_password()

        driver_register.find_element(*locs.LOGIN_MINORPAGE_BUTTON).click()

        WebDriverWait(driver_register, 5).until(
            expected_conditions.visibility_of_element_located(locs.LOGIN_TITLE))
        
        driver_register.find_element(*locs.EMAIL_INPUT).send_keys(email)
        driver_register.find_element(*locs.PASSWORD_INPUT).send_keys(password)
        driver_register.find_element(*locs.ENTER_LOGIN_BUTTON).click()    
    
        WebDriverWait(driver_register, 5).until(
            expected_conditions.visibility_of_element_located(locs.ORDER_BUTTON))
    
        order_button = driver_register.find_element(*locs.ORDER_BUTTON)
        assert "Оформить заказ" in order_button.text    


    def test_login_button_from_forgot_password_page(self, driver_forgot_password):

        email = Data.get_email()
        password = Data.get_password()

        driver_forgot_password.find_element(*locs.LOGIN_MINORPAGE_BUTTON).click()

        WebDriverWait(driver_forgot_password, 5).until(
            expected_conditions.visibility_of_element_located(locs.LOGIN_TITLE))
        
        driver_forgot_password.find_element(*locs.EMAIL_INPUT).send_keys(email)
        driver_forgot_password.find_element(*locs.PASSWORD_INPUT).send_keys(password)
        driver_forgot_password.find_element(*locs.ENTER_LOGIN_BUTTON).click()    
    
        WebDriverWait(driver_forgot_password, 5).until(
            expected_conditions.visibility_of_element_located(locs.ORDER_BUTTON))
    
        order_button = driver_forgot_password.find_element(*locs.ORDER_BUTTON)
        assert "Оформить заказ" in order_button.text

