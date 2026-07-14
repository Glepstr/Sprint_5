import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import MainPageLocators, LoginPageLocators
from data import EXISTING_USER

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
def login_existing_user(driver):
    """Фикстура для авторизации существующего пользователя"""
    wait = WebDriverWait(driver, 10)
    
    # Используем данные из data.py
    wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
    wait.until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(EXISTING_USER["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(EXISTING_USER["password"])
    driver.find_element(*LoginPageLocators.LOGIN_SUBMIT).click()
    wait.until(EC.presence_of_element_located(MainPageLocators.USER_AVATAR))