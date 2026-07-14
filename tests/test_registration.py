import pytest
import sys
import os
import time
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators

class TestRegistration:

    def test_successful_registration(self, driver, wait, test_user_email, test_password):
        # Нажимаем кнопку «Вход и регистрация»
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
        
        # Нажимаем кнопку «Нет аккаунта»
        wait.until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()
        
        # Заполняем форму регистрации
        wait.until(EC.presence_of_element_located(RegistrationPageLocators.EMAIL_INPUT)).send_keys(test_user_email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(test_password)
        driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT).send_keys(test_password)
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        # Проверяем переход на главную и отображение аватара
        wait.until(EC.presence_of_element_located(MainPageLocators.USER_AVATAR))
        assert driver.find_element(*MainPageLocators.USER_AVATAR).is_displayed(), "Аватар не отображается"
        

    def test_registration_invalid_email(self, driver, wait):
        # Нажимаем кнопку «Вход и регистрация»
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
        
        # Нажимаем кнопку «Нет аккаунта»
        wait.until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()
        
        # Заполняем поле Email невалидным значением
        wait.until(EC.presence_of_element_located(RegistrationPageLocators.EMAIL_INPUT)).send_keys("invalid-email")
        
        # Нажимаем кнопку создания аккаунта
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        # Проверяем, что поля подсвечены красным и отображается ошибка
        error_fields = wait.until(
            EC.presence_of_all_elements_located(RegistrationPageLocators.ERROR_FIELDS)
        )
        assert len(error_fields) >= 3, "Не все поля подсвечены красным"
        
        error_message = driver.find_element(*RegistrationPageLocators.EMAIL_ERROR_MESSAGE).text
        assert "Ошибка" in error_message, "Сообщение об ошибке не отображается"

    def test_registration_existing_user(self, driver, wait, existing_user):
        # Нажимаем кнопку «Вход и регистрация»
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
        
        # Нажимаем кнопку «Нет аккаунта»
        wait.until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()
        
        # Заполняем форму данными существующего пользователя
        wait.until(EC.presence_of_element_located(RegistrationPageLocators.EMAIL_INPUT)).send_keys(existing_user["email"])
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(existing_user["password"])
        driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT).send_keys(existing_user["password"])
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()
        
        # Проверяем, что поля подсвечены красным и отображается ошибка
        error_fields = wait.until(
            EC.presence_of_all_elements_located(RegistrationPageLocators.ERROR_FIELDS)
        )
        assert len(error_fields) >= 3, "Не все поля подсвечены красным"
        
        error_message = driver.find_element(*RegistrationPageLocators.EMAIL_ERROR_MESSAGE).text
        assert "Ошибка" in error_message, "Сообщение об ошибке не отображается"