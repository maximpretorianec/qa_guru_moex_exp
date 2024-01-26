from moex_project_tests.utils import base_lib, get_current_time
from moex_project_tests.test_data import MoexUrl, MoexVariables
from selene import be, have, browser
from allure import step


class MainPage:
    core_url = browser.element('')
    moex_school = browser.element(f'//a[contains(@href, "{MoexUrl.SCHOOL_URL}") and @class="site-header-menu__top-link"]')
    burger_button = browser.element('//button[@aria-label="Открыть бургер-меню"]')
    cart_button = browser.element('//button[contains(@class, "cart-button")]')
    search_field_icon = browser.element('//label[@for="moex-search-input"]')
    pop_up_menu = browser.element('//div[contains(@class, "header-burger__desktop")]')
    search_field = browser.element('//div/input[contains(@id, "moex-search-input")]')
    search_result_list = browser.element('//div/ul[contains(@class, "search-titles-list")]')
    lang_section = browser.element('//div[contains(@class, "lang-switch")]')
    moex_logo = browser.element(
        '//div[contains(@class, "header__logo")]//div[contains(@class, "app-logo--standard")]//child::img[@alt="Logo"]')
    time_on_site = browser.element('//div[@class="header-nav__date"]')
    header_obj_with_rus_text = browser.element(
        f'//ul[@class="site-header-menu__main-list"]/*[contains(.,"Продукты и услуги")]')
    header_obj_with_eng_text = browser.element(
        f'//ul[@class="site-header-menu__main-list"]/*[contains(.,"Markets")]')
    switch_lang_button = browser.element(
        '//span[contains(@class, "lang-switch__lang") and not(contains(@class, "lang-switch__lang--active"))]')
    exchange_button = browser.element('//ul[@class="site-header-menu__main-list"]/li[2]')
    bidding_results = browser.element('//div[contains(.,"По всем рынкам Московской биржи")]/ancestor::li[1]')

    def open_core_site(self):
        with step('Открыть главную страницу'):
            base_lib.open_site('')

    def check_visibility_moex_icon(self, loc_moex_logo=moex_logo):
        with step('Проверка отображения лого MOEX в верхнем меню'):
            loc_moex_logo.should(be.visible)

    def check_visibility_lang_switch_at_top_menu(self, loc_lang_section=lang_section):
        with step('Проверка отображения перключения языков в верхнем меню'):
            loc_lang_section.should(be.visible)

    def check_visibility_search_at_top_menu(self, loc_search_field_icon=search_field_icon):
        with step('Проверка отображения поиска в верхнем меню'):
            loc_search_field_icon.should(be.visible)

    def check_visibility_cart_button_at_top_menu(self, loc_cart_button=cart_button):
        with step('Проверка отображения корзины в верхнем меню'):
            loc_cart_button.should(be.visible)

    def check_visibility_open_pop_up_menu(self, loc_pop_up_menu=pop_up_menu):
        with step('Проверить наличие всплывающего окна'):
            loc_pop_up_menu.should(be.visible)

    def check_visibility_search_result(self, loc_search_result_list=search_result_list):
        with step('Проверить наличие отображения результатов поиска'):
            loc_search_result_list.should(be.visible)

    def check_rus_name_at_top_menu(self, loc_header_obj_with_text=header_obj_with_rus_text):
        with step('В верхнем меню отображаются элементы на русском языке'):
            loc_header_obj_with_text.should(be.visible)

    def check_eng_name_at_top_menu(self, loc_header_obj_with_text=header_obj_with_eng_text):
        with step('В верхнем меню отображаются элементы на английском языке'):
            loc_header_obj_with_text.should(be.visible)

    def check_time_on_site(self, loc_time_on_site=time_on_site):
        with step('Проверка времени на сайте'):
            loc_time_on_site.should(be.visible).should(have.text(get_current_time()))

    def check_moex_school(self, loc_moex_school=moex_school):
        with step('Проверить наличие раздела обучения'):
            loc_moex_school.should(be.visible)

    def click_moex_school(self, loc_moex_school=moex_school):
        with step('Открыть раздел обучения'):
            loc_moex_school.click()

    def filling_search_field(self, loc_search_field=search_field):
        with step('Заполнить строку поиска'):
            loc_search_field.type(MoexVariables.search_text)

    def click_switch_lang(self, loc_switch_lang_button=switch_lang_button):
        with step('Переключение языков'):
            loc_switch_lang_button.click()

    def click_exchange_information(self, loc_exchange_button=exchange_button):
        with step('Открыть раздел биржевой информации'):
            loc_exchange_button.should(be.visible).click()

    def click_bidding_results(self, loc_bidding_results=bidding_results):
        with step('Нажать на кнопку "Итоги торгов"'):
            loc_bidding_results.should(be.visible).click()

    def click_burger_button(self, loc_burger_button=burger_button):
        with step('Нажать на кнопку меню'):
            loc_burger_button.should(be.visible).click()

    def open_bidding_results(self):
        with step('Открыть раздел "Итоги торгов"'):
            self.click_exchange_information()
            self.click_bidding_results()

    def check_open_visibility_pop_up_menu(self):
        with step('Проверить открытие всплывающего окна'):
            self.click_burger_button()
            self.check_visibility_open_pop_up_menu()

    def open_new_tab_school(self):
        with step('Открыть новую вкладку - Обучение'):
            self.check_moex_school()
            self.click_moex_school()
            base_lib.switch_tab()

    def check_visibility_base_page_elements(self):
        with step('Проверка базовых элементов страницы'):
            self.check_visibility_moex_icon()
            self.check_visibility_cart_button_at_top_menu()
            self.check_visibility_lang_switch_at_top_menu()
            self.check_visibility_search_at_top_menu()


main_lib = MainPage()
