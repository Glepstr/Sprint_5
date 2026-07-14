from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопки на главной
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    CREATE_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
    
    # Элементы авторизованного пользователя
    USER_AVATAR = (By.XPATH, "//button[@class='circleSmall']") 
    USER_NAME = (By.XPATH, "//h3[contains(text(), 'User')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")

    # Модальное окно
    MODAL_WINDOW = (By.XPATH, "//form[@class=('popUp_shell__LuyqR')]")
    MODAL_TITLE = (By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")

class LoginPageLocators:
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_SUBMIT = (By.XPATH, "//button[contains(text(), 'Войти')]")
    REGISTER_LINK = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")

class RegistrationPageLocators:
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    CONFIRM_PASSWORD_INPUT = (By.NAME, "submitPassword")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    
    # Элементы для проверки ошибок
    EMAIL_ERROR_MESSAGE = (By.XPATH, "//*[contains(text(), 'Ошибка')]")
    ERROR_FIELDS = (By.XPATH, "//div[@class=('input_inputError__fLUP9')]") 

class ProfilePageLocators:
    PROFILE_AVATAR = (By.CSS_SELECTOR, ".user-avatar")
    MY_ADS_SECTION = (By.XPATH, "//h1[contains(text(), 'Мои объявления')]")
    AD_TITLES = (By.XPATH, "//div[@class=('card')]")  # уточните селектор

class AdCreationLocators:
    TITLE_INPUT = (By.CSS_SELECTOR, 'input[name="name"]')
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, 'textarea[name="description"]')
    PRICE_INPUT = (By.CSS_SELECTOR, 'input[name="price"]')
    CATEGORY_DROPDOWN = (By.XPATH, "(//button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP'])[1]")
    CITY_DROPDOWN = (By.XPATH, "(//button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP'])[2]")
    CONDITION_RADIO_NEW = (By.XPATH, "(//div[@class='radioUnput_inputActive__eC-HY'])")
    PUBLISH_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")
    CARD = (By.CSS_SELECTOR, 'img[alt="test"]')

    @staticmethod
    def card_by_title(ad_title):
        return (By.XPATH, f".//div[contains(@class, 'about')][.//h2[normalize-space(text())='{ad_title}']]")