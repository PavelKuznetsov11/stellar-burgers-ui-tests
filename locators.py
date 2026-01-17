import random
from selenium.webdriver.common.by import By

class Locators:
    
    NAME_REGISTER_INPUT = (By.XPATH, "//form[contains(@class, '3qKeq')]/fieldset[1]//input")  # Поле имени на странице регистрации
    EMAIL_REGISTER_INPUT = (By.XPATH, "//form[contains(@class, '3qKeq')]/fieldset[2]//input") # Поле email на странице регистрации
    PASSWORD_REGISTER_INPUT = (By.XPATH, "//form[contains(@class, '3qKeq')]/fieldset[3]//input") # Поле пароля на странице регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка регистрации на странице регистрации
    INCORRECT_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']") # Сообщение об ошибке некорректного пароля
   
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']") # Надпись Вход на странице входа
    LOGIN_HOMEPAGE_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") # Кнопка входа в аккаунт на главной странице
    PROFILE_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']/parent::a") # Кнопка перехода в личный кабинет
    LOGIN_MINORPAGE_BUTTON = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Войти']") # Кнопка входа в окне регистрации и в окне восстановление пароля
    EMAIL_LOGIN_BUTTON = (By.XPATH, "//form[contains(@class, '3qKeq')]/fieldset[1]//input") # Поле email на странице входа
    PASSWORD_LOGIN_BUTTON = (By.XPATH, "//form[contains(@class, '3qKeq')]/fieldset[2]//input") # Поле пароля на странице входа
    ENTER_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']") # Кнопка войти на странице входа


    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # Кнопка оформления заказа на главной странице
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX'][1]//p") # Кнопка перехода в конструктор
    STELLAR_BURGERS_LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a") # Логотип Stellar Burgers
    LOGOUT_BUTTON = (By.XPATH,
                      "//button[contains(@class, 'Account_button__14Yp3') and text()='Выход']") # Кнопка выхода из аккаунта в окне личного кабинета
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']") # Секция Булки в конструкторе
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']") # Секция Соусы в конструкторе
    TOPPINGS_SECTION = (By.XPATH, "//span[text()='Начинки']") # Секция Начинки в конструкторе
    SELECT_BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div[contains(@class, 'tab_tab_type_current__2BEPc')]") # Выбранная секция в конструкторе булки
    SELECT_SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div[contains(@class, 'tab_tab_type_current__2BEPc')]") # Выбранная секция в конструкторе соусы
    SELECT_TOPPINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div[contains(@class, 'tab_tab_type_current__2BEPc')]") # Выбранная секция в конструкторе начинки