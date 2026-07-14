import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import time
from locators.locators import MainPageLocators, LoginPageLocators

import sys
import os

@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания и закрытия драйвера"""
    options = Options()
    # options.add_argument("--headless")  # Раскомментируйте для безголового режима
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://qa-desk.education-services.ru/")
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    """Фикстура для WebDriverWait"""
    return WebDriverWait(driver, 10)

@pytest.fixture
def test_user_email():
    """Генерация уникального email для каждого теста"""
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{random_string}@test.com"

@pytest.fixture
def test_password():
    return "TestPassword123"

@pytest.fixture
def existing_user():
    """Данные существующего пользователя"""
    return {
        "email": "existing@test.com",  # Замените на реальные данные
        "password": "ExistingPass123"
    }

@pytest.fixture
def login_existing_user(driver, wait, existing_user):
    """Фикстура для авторизации существующего пользователя"""
    
    # Нажимаем кнопку входа
    wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
    
    # Заполняем форму авторизации
    wait.until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(existing_user["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(existing_user["password"])
    driver.find_element(*LoginPageLocators.LOGIN_SUBMIT).click()
    
    # Ждем загрузки главной страницы
    wait.until(EC.presence_of_element_located(MainPageLocators.USER_AVATAR))