from selenium.webdriver.common.by import By
from locators.main_locators import MainLocators


class LdapLocators(MainLocators):
    ## Buttons
    # Кнопка создания LDAP
    BUTTON_CREATE_LDAP = [By.XPATH, "//button[text()='Create New']"]
    # Кнопка сохранить LDAP
    BUTTON_SAVE_LDAP = [By.XPATH, "//aside/button"]
    # Кнопка редактирования LDAP
    BUTTON_EDIT_LDAP = (
        By.XPATH,
        "//*[local-name()='svg' and @data-icon='pen']/*[local-name()='path']")
    # Кнопка копирования LDAP
    BUTTON_COPY_LDAP = [By.XPATH, "//*[local-name()='svg' and @data-icon='copy']/*[local-name()='path']"]
    # Кнопка удаления LDAP
    BUTTON_DELETE_LDAP = [By.XPATH, "//*[local-name()='button' and @data-ngui_joinable='true']/*[local-name()='svg' and @data-icon='trash']/*[local-name()='path']"]
    # Ползунок удаления
    BUTTON_FOR_DELETE = [By.XPATH, "//*[local-name()='path' and starts-with(@d,'M438.6 278.6c12.5-12.5')]"]


    ## Texts
    # Главное меню создания LDAP
    TEXT_MAIN_LDAP = [By.XPATH, "//h3[contains(text(), 'LDAP Server')]"]
    # Сообщение об успешном создании LDAP
    TEXT_ACCESS_CREATE_LDAP  = [
        By.CSS_SELECTOR,
        "aside.toaster-overlay.success > main.toast-content"]
    # Сообщение об успешном копировании LDAP
    TEXT_ACCESS_COPY_LDAP = [By.XPATH, "//main[text()='Object copied']"]
    # Сообщение об успешном удалении LDAP
    TEXT_ACCESS_DELETE_LDAP = [By.XPATH, "//main[contains(text(), 'deleted')]"]
    # Ошибка дубля при создании LDAP
    TEXT_ERROR_DUPLICATE_LDAP = [By.XPATH, "//li[text()='Field LDAP Name should not be repeated between objects. Please choose another value.']"]
    # Имя LDAP
    TEXT_NAME_LDAP = [By.XPATH, "//h4[@class='name']"]
    # Описание LDAP
    TEXT_DESCRIPTION_LDAP = [By.XPATH, "//p[@class='description']"]

    ## Inputs
    # Ввод Name
    INPUT_NAME_LDAP = [By.XPATH, "//input[@placeholder='Name']"]
    # Ввод LDAP bind URI
    INPUT_LDAP_BIND_URI = [By.XPATH, "//input[@placeholder='LDAP bind URI']"]
    # Ввод пользователя LDAP
    INPUT_USER_LDAP = [By.XPATH, "//input[@placeholder='LDAP bind user']"]
    # Ввод пароля LDAP
    INPUT_PASSWORD_LDAP = [By.XPATH, "//input[@placeholder='LDAP bind user password']"]
    # Ввод group base DN
    INPUT_GROUP_DN_LDAP = [By.XPATH, "//section[4]//input[@placeholder='dc=beaver,dc=ngate,dc=local']"]
    # Ввод user base DN
    INPUT_USER_DN_LDAP = [By.XPATH, "//section[5]//input[@placeholder='dc=beaver,dc=ngate,dc=local']"]
    # Ввод описания LDAP
    INPUT_DESCRIPTION_LDAP = [By.XPATH, "//textarea[contains(@class,'ngui-textarea-input') and @placeholder='Description' and @rows='2']"]
