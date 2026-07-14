import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators

class TestLogout:

    def test_logout(self, driver, wait, login_existing_user):
        # Проверяем, что пользователь авторизован
        wait.until(EC.presence_of_element_located(MainPageLocators.USER_AVATAR))
        assert driver.find_element(*MainPageLocators.USER_AVATAR).is_displayed(), "Пользователь не авторизован"
        
        # Нажимаем кнопку «Выйти»
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGOUT_BUTTON)).click()
        
        # Проверяем, что аватар и имя исчезли, появилась кнопка входа
        wait.until(EC.presence_of_element_located(MainPageLocators.LOGIN_BUTTON))
        assert driver.find_element(*MainPageLocators.LOGIN_BUTTON).is_displayed(), "Кнопка входа не отображается"
        
        # Проверяем, что аватар больше не отображается
        avatars = driver.find_elements(*MainPageLocators.USER_AVATAR)
        assert len(avatars) == 0, "Аватар все еще отображается"