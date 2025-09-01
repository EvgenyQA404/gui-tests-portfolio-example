import allure
from data.data import Data
from pages.basic_page import BasePage
from locators.login_locators import LoginLocators


class AuthenticationPage(BasePage):

    @allure.step('Переход на страницу')
    def go_auth_site(self):
        self.go_to_site(Data.main_page)

    @allure.step('Ввод логина пользователя')
    def input_login(self):
        self.input_text(LoginLocators.LOGIN_FORM, Data.user_login)

    @allure.step('Ввод некорректного логина пользователя')
    def input_incorrect_login(self):
        self.input_text(LoginLocators.LOGIN_FORM, Data.bad_login)

    @allure.step('Ввод пароля пользователя')
    def input_password(self):
        self.input_text(LoginLocators.PASSWORD_FORM, Data.user_password)

    @allure.step('Ввод некорректного пароля пользователя')
    def input_incorrect_password(self):
        self.input_text(LoginLocators.PASSWORD_FORM, Data.bad_password)

    @allure.step('Нажатие на кнопку авторизации')
    def button_of_authorization(self):
        self.click_on_element(LoginLocators.SIGN_IN_BUTTON)

    @allure.step('Ожидание до кликабельной панели ngate')
    def wait_panel_ngate(self):
        self.wait_element_clickable(LoginLocators.BUTTON_PANEL_NGATE)

    @allure.step('Ожидание появления текста панели управления')
    def wait_text_dashboard(self):
        text = self.wait_element_located(LoginLocators.DASHBOARD)
        return text

    @allure.step('Ожидание появления ошибки логина и пароля')
    def wait_error_login(self):
        text = self.wait_element_located(LoginLocators.TEXT_ERROR_INCORRECT_LOGIN_DATE)
        return text

    @allure.step('Нажатие на кнопку профиля пользователя')
    def click_profile_user_button(self):
        self.click_on_element(LoginLocators.BUTTON_PROFILE_USER)

    @allure.step('Ожидание кнопки выхода из профиля пользователя')
    def wait_sign_out_profile_user_button(self):
        self.wait_element_clickable(LoginLocators.BUTTON_SIGN_OUT)

    @allure.step('Нажатие на кнопку выхода из профиля пользователя')
    def click_sign_out_profile_user_button(self):
        self.click_on_element(LoginLocators.BUTTON_SIGN_OUT)

    @allure.step('Ожидание появления ошибки выхода из профиля')
    def wait_error_login_sign_out(self):
        text = self.wait_element_located(LoginLocators.TEXT_ERROR_USER_LOGGED_OUT)
        return text

    @allure.step('Получить текст ошибки выхода из профиля')
    def get_text_error_login_sign_out(self):
        text = self.get_text_of_element(LoginLocators.TEXT_ERROR_USER_LOGGED_OUT)
        return text
