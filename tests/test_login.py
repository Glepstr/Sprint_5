import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators, LoginPageLocators

class TestLogin:

    def test_successful_login(self, driver, wait, existing_user):
        # Нажимаем кнопку «Вход и регистрация»
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
        
        # Заполняем форму авторизации
        wait.until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(existing_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(existing_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT).click()
        
        # Проверяем переход на главную и отображение аватара
        wait.until(EC.presence_of_element_located(MainPageLocators.USER_AVATAR))
        assert driver.find_element(*MainPageLocators.USER_AVATAR).is_displayed(), "Аватар не отображается"