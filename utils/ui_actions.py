from selene import browser, be
from allure import step


class BaseActions:
    def open_site(self, url):
        browser.open(url)

    def type_text(self, location, text):
        browser.element(location).should(be.visible).type(text)

    def click_button(self, location):
        browser.element(location).should(be.visible).click()

    def check_visibility(self, location):
        browser.element(location).should(be.visible)

    def switch_tab(self):
        browser.switch_to_next_tab()

    def is_assert_equal_values(self, first_el, second_el):
        with step('Сравнение равенства элементов'):
            assert first_el == second_el

    def get_curr_url(self):
        with step('Вернуть текущий url'):
            return browser.driver.current_url
