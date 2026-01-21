import random
from selenium.webdriver.common.by import By

class Locators:
    
    NAME_REGISTER_INPUT = (By.XPATH, "//label[contains(text(),'Имя')]/..//input")  # Поле имени на странице регистрации
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(),'Email')]/..//input") # Поле email на странице регистрации и входа
    PASSWORD_INPUT = (By.XPATH, "//label[contains(text(),'Пароль')]/..//input") # Поле пароля на странице регистрации и входа
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]") # Кнопка регистрации на странице регистрации
    INCORRECT_PASSWORD = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]") # Сообщение об ошибке некорректного пароля
   
    LOGIN_TITLE = (By.XPATH, "//h2[contains(text(), 'Вход')]") # Надпись Вход на странице входа
    LOGIN_HOMEPAGE_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]") # Кнопка входа в аккаунт на главной странице
    PROFILE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "a[href='/account']") # Кнопка перехода в личный кабинет
    LOGIN_MINORPAGE_BUTTON = (By.CSS_SELECTOR, "a[href='/login']") # Кнопка входа в окне регистрации и в окне восстановление пароля
    ENTER_LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]") # Кнопка войти на странице входа


    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]") # Кнопка оформления заказа на главной странице
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]/parent::a") # Кнопка перехода в конструктор
    STELLAR_BURGERS_LOGO = (By.XPATH, "//div[contains(@class,'logo')]//a") # Логотип Stellar Burgers
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]") # Кнопка выхода из аккаунта в окне личного кабинета
    BUNS_SECTION = (By.XPATH, "//span[contains(text(),'Булки')]") # Секция Булки в конструкторе
    SAUCES_SECTION = (By.XPATH, "//span[contains(text(),'Соусы')]") # Секция Соусы в конструкторе
    TOPPINGS_SECTION = (By.XPATH, "//span[contains(text(),'Начинки')]") # Секция Начинки в конструкторе
    SELECT_BUNS_SECTION = (By.XPATH, "//span[contains(text(),'Булки')]/parent::div[contains(@class, 'current')]") # Выбранная секция в конструкторе булки
    SELECT_SAUCES_SECTION = (By.XPATH, "//span[contains(text(),'Соусы')]/parent::div[contains(@class, 'current')]") # Выбранная секция в конструкторе соусы
    SELECT_TOPPINGS_SECTION = (By.XPATH, "//span[contains(text(),'Начинки')]/parent::div[contains(@class, 'current')]") # Выбранная секция в конструкторе начинки

