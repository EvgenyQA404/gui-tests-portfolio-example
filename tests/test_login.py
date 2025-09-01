import allure
from data.data import Data
from pages.login_page import AuthenticationPage

@allure.parent_suite("Автоматизация UI")
@allure.suite("Страница логина")
@allure.sub_suite("Основные проверки")
class TestAuthPage:
    @allure.title('Успешная аутентификация по логину и паролю')
    def test_auth_login_password(self, driver):
        page = AuthenticationPage(driver)
        page.go_auth_site()
        page.input_login()
        page.input_password()
        page.button_of_authorization()
        excepted = page.wait_text_dashboard()

        assert excepted.text == Data.dashboard

    @allure.title('Аутентификация - неверный логин')
    def test_auth_incorrect_login(self, driver):
        page = AuthenticationPage(driver)
        page.go_auth_site()
        page.input_incorrect_login()
        page.input_password()
        page.button_of_authorization()
        excepted = page.wait_error_login()

        assert Data.error_login in excepted.text

    @allure.title('Аутентификация - неверный пароль')
    def test_auth_incorrect_password(self, driver):
        page = AuthenticationPage(driver)
        page.go_auth_site()
        page.input_login()
        page.input_incorrect_password()
        page.button_of_authorization()
        excepted = page.wait_error_login()

        assert Data.error_login in excepted.text

    @allure.title('Выход из учётной записи')
    def test_sign_out(self, driver):
        page = AuthenticationPage(driver)
        page.go_auth_site()
        page.input_login()
        page.input_password()
        page.button_of_authorization()
        page.wait_text_dashboard()
        page.click_profile_user_button()
        page.wait_sign_out_profile_user_button()
        page.click_sign_out_profile_user_button()
        excepted = page.wait_error_login_sign_out()

        assert Data.error_sign_out_profile in excepted.text
