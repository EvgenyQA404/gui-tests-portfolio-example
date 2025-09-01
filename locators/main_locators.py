from selenium.webdriver.common.by import By


class MainLocators:
    # Строка ввода
    LOGIN_FORM = [By.XPATH, "//input[@placeholder='Login']"]
    PASSWORD_FORM = [By.XPATH, "//input[@placeholder='Password']"]
    # Текст
    DASHBOARD = [By.XPATH, "//h1[normalize-space(text())='Welcome, ng-admin!']"]
    # Кнопки
    SIGN_IN_BUTTON = [By.XPATH, "//button[text()='Sign In']"]
