from selenium.webdriver.common.by import By
from locators.main_locators import MainLocators


class LoginLocators(MainLocators):
    ## Inputs
    ## Texts
    # Ошибка при вводе некорректного логина или пароля
    TEXT_ERROR_INCORRECT_LOGIN_DATE = [By.XPATH, "//section[@class='error']"]
    # Главный текст на странице логина
    TEXT_ERROR_USER_LOGGED_OUT = [By.XPATH, "//h3[normalize-space(.)='NGate Web Console Authentication']"]

    ## Buttons
    # Кнопка выхода из профиля
    BUTTON_SIGN_OUT = [By.XPATH, "//button[text()='Logout']"]
    # Кнопка профиля пользователя
    BUTTON_PROFILE_USER = [By.XPATH, "//li[contains(@class, 'action') and contains(normalize-space(.), 'ng-admin')]"]
    BUTTON_PANEL_NGATE = [By.XPATH, "//span[2]"]
