import pytest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from locators.locators import MainPageLocators, AdCreationLocators, ProfilePageLocators
from data import AUTH_MESSAGE

class TestAdCreation:

    def test_create_ad_unauthorized(self, driver):
        wait = WebDriverWait(driver, 10)

        # Нажимаем кнопку «Разместить объявление» неавторизованным пользователем
        wait.until(EC.element_to_be_clickable(MainPageLocators.CREATE_AD_BUTTON)).click()
        
        # Проверяем отображение модального окна
        wait.until(EC.visibility_of_element_located(MainPageLocators.MODAL_WINDOW))
        assert driver.find_element(*MainPageLocators.MODAL_WINDOW).is_displayed(), "Модальное окно не отображается"
        
        modal_title = driver.find_element(*MainPageLocators.MODAL_TITLE).text
        assert AUTH_MESSAGE in modal_title.lower(), "Неверный текст в модальном окне"

    def test_create_ad_authorized(self, driver, login_existing_user):
        wait = WebDriverWait(driver, 10)

        # Генерируем уникальное название объявления
        ad_title = f"Test Ad {int(time.time())}"
        
        # Нажимаем кнопку «Разместить объявление»
        wait.until(EC.element_to_be_clickable(MainPageLocators.CREATE_AD_BUTTON)).click()
        
        # Заполняем форму
        wait.until(EC.presence_of_element_located(AdCreationLocators.TITLE_INPUT)).send_keys(ad_title)
        driver.find_element(*AdCreationLocators.DESCRIPTION_INPUT).send_keys("Test description")
        driver.find_element(*AdCreationLocators.PRICE_INPUT).send_keys("1000")
        
        # Выбираем категорию (если это dropdown)
        driver.find_element(*AdCreationLocators.CATEGORY_DROPDOWN).click()
        driver.find_element(*AdCreationLocators.CATEGORY_OPTION).click()

        # Выбираем город
        driver.find_element(*AdCreationLocators.CITY_DROPDOWN).click()
        driver.find_element(*AdCreationLocators.CITY_OPTION).click()
        
        # Выбираем состояние товара
        driver.find_element(*AdCreationLocators.CONDITION_RADIO_NEW).click()
        
        # Публикуем объявление
        publish_button = driver.find_element(*AdCreationLocators.PUBLISH_BUTTON)
        publish_button.click()

        wait.until(EC.staleness_of(publish_button))

        # Переходим в профиль пользователя 
        wait.until(EC.element_to_be_clickable(MainPageLocators.USER_AVATAR)).click()
        
        # Проверяем, что объявление появилось в блоке "Мои объявления"
        wait.until(EC.presence_of_element_located(ProfilePageLocators.MY_ADS_SECTION))

        card = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(AdCreationLocators.card_by_title(ad_title))
        )
        assert ad_title in card.text, f"Название '{ad_title}' не найдено в карточке"