import allure
from data.data import Data
from pages.basic_page import BasePage
from locators.ldap_locators import LdapLocators
from locators.login_locators import LoginLocators

class LdapPage(BasePage):
    @allure.step('Авторизация на сайте')
    def authorize(self):
        self.go_to_site(Data.ldap_page)
        self.input_text(LoginLocators.LOGIN_FORM, Data.user_login)
        self.input_text(LoginLocators.PASSWORD_FORM, Data.user_password)
        self.click_on_element(LoginLocators.SIGN_IN_BUTTON)

    @allure.step('Переход на страницу LDAP')
    def go_to_ldap_page(self):
        self.go_to_site(Data.ldap_page)

    @allure.step('Нажатие на кнопку создания LDAP')
    def click_button_create_ldap(self):
        self.click_on_element(LdapLocators.BUTTON_CREATE_LDAP)

    @allure.step('Ожидание кликабельности кнопки создания LDAP')
    def wait_button_create_ldap(self):
        self.wait_element_clickable(LdapLocators.BUTTON_CREATE_LDAP)

    @allure.step('Нажатие на кнопку сохранения LDAP')
    def click_button_save_ldap(self):
        self.click_on_element(LdapLocators.BUTTON_SAVE_LDAP)

    @allure.step('Ожидание кликабельности кнопки сохранения LDAP')
    def wait_button_save_ldap(self):
        self.wait_element_clickable(LdapLocators.BUTTON_SAVE_LDAP)

    @allure.step('Ожидание появления текста главного меню LDAP')
    def wait_main_menu_ldap(self):
        text = self.wait_element_located(LdapLocators.TEXT_MAIN_LDAP)
        return text

    @allure.step('Очистить строку ввода пользователя LDAP')
    def clear_user_ldap(self):
        self.clear_input(LdapLocators.INPUT_USER_LDAP)

    @allure.step('Заполнение данных LDAP')
    def input_data_ldap(self):
        self.input_text(LdapLocators.INPUT_NAME_LDAP, Data.ldap_name)
        self.input_text(LdapLocators.INPUT_LDAP_BIND_URI, Data.ldap_bind_uri)
        self.input_text(LdapLocators.INPUT_USER_LDAP, Data.ldap_bind_user)
        self.input_text(LdapLocators.INPUT_PASSWORD_LDAP, Data.ldap_password)
        self.input_text(LdapLocators.INPUT_GROUP_DN_LDAP, Data.ldap_base_dn)
        self.input_text(LdapLocators.INPUT_USER_DN_LDAP, Data.ldap_base_dn)

    @allure.step('Ожидание успешного сохранения LDAP')
    def wait_text_save_ldap(self):
        text = self.wait_element_located(LdapLocators.TEXT_ACCESS_CREATE_LDAP )
        return text

    @allure.step('Ожидание кликабельности кнопки удаления LDAP')
    def wait_button_delete_ldap(self):
        self.wait_element_clickable(LdapLocators.BUTTON_DELETE_LDAP)

    @allure.step('Нажатие на кнопку удаления LDAP')
    def click_button_delete_ldap(self):
        self.click_on_element(LdapLocators.BUTTON_DELETE_LDAP)

    @allure.step('Нажатие на кнопку Enter для удаления')
    def use_enter(self):
        self.enter(LdapLocators.BUTTON_FOR_DELETE)

    @allure.step('Ожидание успешного удаления LDAP')
    def wait_text_deleted_ldap(self):
        text = self.wait_element_located(LdapLocators.TEXT_ACCESS_DELETE_LDAP)
        return text

    @allure.step('Ожидание ошибки дубля LDAP')
    def wait_error_duplicate_ldap(self):
        text = self.wait_element_located(LdapLocators.TEXT_ERROR_DUPLICATE_LDAP)
        return text

    @allure.step('Ожидание кликабельности кнопки редактирования LDAP')
    def wait_button_edit_ldap(self):
        self.wait_element_clickable(LdapLocators.BUTTON_EDIT_LDAP)

    @allure.step('Нажатие на кнопку редактирования LDAP')
    def click_button_edit_ldap(self):
        self.click_on_element(LdapLocators.BUTTON_EDIT_LDAP)

    @allure.step('Ожидание описания LDAP')
    def wait_description_ldap(self):
        text = self.wait_element_located(LdapLocators.TEXT_DESCRIPTION_LDAP)
        return text

    @allure.step('Заполнение описания LDAP')
    def input_description_ldap(self):
        self.input_text(LdapLocators.INPUT_DESCRIPTION_LDAP, Data.ldap_description)
        self.input_text(LdapLocators.INPUT_PASSWORD_LDAP, Data.ldap_password)

    @allure.step('Нажатие на кнопку копирования LDAP')
    def click_button_copy_ldap(self):
        self.click_on_element(LdapLocators.BUTTON_COPY_LDAP)

    @allure.step('Ожидание успешного копирования LDAP')
    def wait_text_copy_ldap(self):
        text = self.wait_element_located(LdapLocators.TEXT_ACCESS_COPY_LDAP)
        return text

    @allure.step('Ожидание копии имени LDAP')
    def wait_copy_name_ldap(self):
        text = self.wait_element_located(LdapLocators.TEXT_NAME_LDAP)
        return text

