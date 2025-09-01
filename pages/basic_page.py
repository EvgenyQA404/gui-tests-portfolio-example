from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переход на страницу')
    def go_to_site(self, site):
        self.driver.get(site)

    @allure.step('Нажатие на кликабельный элемент')
    def click_on_element(self, element):
        self.driver.find_element(*element).click()

    @allure.step('Ожидание до видимого элемента')
    def wait_element_located(self, element):
        text = WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(element))
        return text

    @allure.step('Ожидание до кликабельного элемента')
    def wait_element_clickable(self, element):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(element))

    @allure.step('Получение текста элемента')
    def get_text_of_element(self, element):
        text = self.driver.find_element(*element).text
        return text

    @allure.step('Ввод сообщения в строку input')
    def input_text(self, string, message):
        self.driver.find_element(*string).send_keys(message)

    @allure.step('Очистка поля input')
    def clear_input(self, element):
        field = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(element))
        field.clear()

    @allure.step('Ожидание до видимости элемента')
    def wait_element_will_be_visible(self, element, text):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.text_to_be_present_in_element(element, text))

    @allure.step('Ожидание изменения элемента в тексте')
    def wait_another_text(self, element, text):
        # ожидание изменения текста
        WebDriverWait(self.driver, 30).until(lambda driver: self.driver.find_element(
            *element).text != text)
        # возврат нового текста
        new_text = self.driver.find_element(*element).text
        return new_text

    @allure.step('Получить текст списка')
    def get_text_list(self, list_text):
        text = self.driver.find_elements(*list_text)
        return text

    @allure.step('Нажатие на кнопку Enter')
    def enter(self, element):
        body = self.driver.find_element(*element)
        actions = ActionChains(self.driver)
        actions.click(body).key_down(Keys.ENTER).pause(2).key_up(Keys.ENTER).perform()
