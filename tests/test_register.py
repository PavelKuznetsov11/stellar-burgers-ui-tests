import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators as locs
from data import Data

class TestRegister:

    def test_register_is_success(self, driver_register):

        name_registration = Data.get_name_registration()
        random_email = Data.get_random_email()
        random_password = Data.get_random_password()

        driver_register.find_element(*locs.NAME_REGISTER_INPUT).send_keys(
                            name_registration)
    
        driver_register.find_element(*locs.EMAIL_INPUT).send_keys(
                            random_email)

        driver_register.find_element(*locs.PASSWORD_INPUT).send_keys(
                            random_password)

        driver_register.find_element(*locs.REGISTER_BUTTON).click()    

        WebDriverWait(driver_register, 5).until(
                expected_conditions.visibility_of_element_located(locs.LOGIN_TITLE))
    
        driver_register.find_element(*locs.EMAIL_INPUT).send_keys(random_email)
        driver_register.find_element(*locs.PASSWORD_INPUT).send_keys(random_password)
        driver_register.find_element(*locs.ENTER_LOGIN_BUTTON).click()    

       
        WebDriverWait(driver_register, 5).until(
            expected_conditions.visibility_of_element_located(locs.ORDER_BUTTON))
        order_button = driver_register.find_element(*locs.ORDER_BUTTON)
        assert "Оформить заказ" in order_button.text






    def test_register_invalid_password(self, driver_register):
        
        name_registration = Data.get_name_registration()
        random_email = Data.get_random_email()
        invalid_random_password = Data.get_invalid_random_password()


        driver_register.find_element(*locs.NAME_REGISTER_INPUT).send_keys(
                            name_registration)
    
        driver_register.find_element(*locs.EMAIL_INPUT).send_keys(
                            random_email)

        driver_register.find_element(*locs.PASSWORD_INPUT).send_keys(
                            invalid_random_password)

        driver_register.find_element(*locs.REGISTER_BUTTON).click()    
    
        WebDriverWait(driver_register, 5).until(
            expected_conditions.visibility_of_element_located(locs.INCORRECT_PASSWORD))
    
        invalid_password_message = driver_register.find_element(*locs.INCORRECT_PASSWORD)
        assert 'Некорректный пароль' in invalid_password_message.text

