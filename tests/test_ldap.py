import allure
from data.data import Data
from pages.ldap_page import LdapPage

@allure.parent_suite("Автоматизация UI")
@allure.suite("Страница LDAP")
@allure.sub_suite("Основные проверки")
class TestLdapPage:
    @allure.title('Успешное создание LDAP объекта')
    def test_create_ldap(self, driver):
        page = LdapPage(driver)
        page.authorize()
        page.wait_button_create_ldap()
        page.click_button_create_ldap()
        page.wait_main_menu_ldap()
        page.clear_user_ldap()
        page.input_data_ldap()
        page.click_button_save_ldap()
        text = page.wait_text_save_ldap()
        excepted = text.text
        page.go_to_ldap_page()
        page.wait_button_delete_ldap()
        page.click_button_delete_ldap()
        page.use_enter()

        assert excepted == Data.access_created_ldap

    @allure.title('Создание дубля LDAP объекта')
    def test_create_duplicate_ldap(self, driver):
        page = LdapPage(driver)
        page.authorize()
        page.wait_button_create_ldap()
        page.click_button_create_ldap()
        page.wait_main_menu_ldap()
        page.clear_user_ldap()
        page.input_data_ldap()
        page.click_button_save_ldap()
        page.go_to_ldap_page()
        page.wait_button_create_ldap()
        page.click_button_create_ldap()
        page.wait_main_menu_ldap()
        page.clear_user_ldap()
        page.input_data_ldap()
        page.click_button_save_ldap()
        text = page.wait_error_duplicate_ldap()
        excepted = text.text
        page.go_to_ldap_page()
        page.wait_button_delete_ldap()
        page.click_button_delete_ldap()
        page.use_enter()

        assert excepted == Data.error_duplicate_ldap

    @allure.title('Успешное удаление LDAP объекта')
    def test_delete_ldap(self, driver):
        page = LdapPage(driver)
        page.authorize()
        page.wait_button_create_ldap()
        page.click_button_create_ldap()
        page.wait_main_menu_ldap()
        page.clear_user_ldap()
        page.input_data_ldap()
        page.click_button_save_ldap()
        page.go_to_ldap_page()
        page.wait_button_delete_ldap()
        page.click_button_delete_ldap()
        page.use_enter()
        text = page.wait_text_deleted_ldap()
        excepted = text.text

        assert excepted == Data.access_deleted_ldap

    @allure.title('Успешное редактирование LDAP объекта')
    def test_edit_ldap(self, driver):
        page = LdapPage(driver)
        page.authorize()
        page.wait_button_create_ldap()
        page.click_button_create_ldap()
        page.wait_main_menu_ldap()
        page.clear_user_ldap()
        page.input_data_ldap()
        page.click_button_save_ldap()
        page.go_to_ldap_page()
        page.wait_button_edit_ldap()
        page.click_button_edit_ldap()
        page.wait_main_menu_ldap()
        page.input_description_ldap()
        page.click_button_save_ldap()
        page.go_to_ldap_page()
        text = page.wait_description_ldap()
        excepted = text.text
        page.go_to_ldap_page()
        page.wait_button_delete_ldap()
        page.click_button_delete_ldap()
        page.use_enter()

        assert excepted == Data.ldap_description

    @allure.title('Успешное копирование LDAP объекта')
    def test_copy_ldap(self, driver):
        page = LdapPage(driver)
        page.authorize()
        page.wait_button_create_ldap()
        page.click_button_create_ldap()
        page.wait_main_menu_ldap()
        page.clear_user_ldap()
        page.input_data_ldap()
        page.click_button_save_ldap()
        page.go_to_ldap_page()
        page.wait_button_create_ldap()
        page.click_button_copy_ldap()
        text_message = page.wait_text_copy_ldap()
        excepted_message = text_message.text
        page.wait_button_delete_ldap()
        page.click_button_delete_ldap()
        page.use_enter()
        text_name = page.wait_copy_name_ldap()
        excepted_name = text_name.text
        page.wait_button_delete_ldap()
        page.click_button_delete_ldap()
        page.use_enter()

        assert excepted_message == Data.access_copy_ldap and Data.name_copy_ldap in excepted_name
