from moex_project_tests.utils import BaseActions, step, get_current_time
from moex_project_tests.test_data import LocationsMainPage, MoexUrl, MoexVariables


class MainPage(BaseActions):
    def open_core_site(self):
        with step('Открыть главную страницу'):
            self.open_site('')

    def check_visibility_base_page_elements(self):
        with step('Проверка базовых элементов страницы'):
            self.check_visibility_moex_icon()
            self.check_visibility_cart_button_at_top_menu()
            self.check_visibility_lang_switch_at_top_menu()
            self.check_visibility_search_at_top_menu()

    def check_visibility_moex_icon(self):
        with step('Проверка отображения лого MOEX в верхнем меню'):
            self.check_visibility(LocationsMainPage.moex_logo)

    def check_visibility_lang_switch_at_top_menu(self):
        with step('Проверка отображения перключения языков в верхнем меню'):
            self.check_visibility(LocationsMainPage.lang_section)

    def check_visibility_search_at_top_menu(self):
        with step('Проверка отображения поиска в верхнем меню'):
            self.check_visibility(LocationsMainPage.search_field_icon)

    def open_new_tab_school(self):
        with step('Открыть новую вкладку - Обучение'):
            self.click_href(MoexUrl.SCHOOL_URL)
            self.switch_tab()

    def check_visibility_cart_button_at_top_menu(self):
        with step('Проверка отображения корзины в верхнем меню'):
            self.check_visibility(LocationsMainPage.cart_button)


    def click_href(self, link_href):
        with step('Открыть раздел обучения'):
            self.click_button(LocationsMainPage(link_href).page_href_by_text)

    def filling_search_field(self):
        with step('Заполнить строку поиска'):
            self.type_text(LocationsMainPage.search_field, MoexVariables.search_text)

    def check_time_on_site(self):
        with step('Проверка времени на сайте'):
            self.check_visibility(LocationsMainPage(get_current_time()).time_on_site)

    def check_visibility_search_result(self):
        with step('Проверить наличие отображения результатов поиска'):
            self.check_visibility(LocationsMainPage.search_result_list)

    def check_rus_name_at_top_menu(self, rus_text):
        with step('В верхнем меню отображаются элементы на русском языке'):
            self.check_visibility(LocationsMainPage(rus_text).header_obj_with_text)

    def check_eng_name_at_top_menu(self, eng_text):
        with step('В верхнем меню отображаются элементы на английском языке'):
            self.check_visibility(LocationsMainPage(eng_text).header_obj_with_text)

    def click_switch_lang_at_top_menu(self):
        with step('Переключение языков'):
            self.click_button(LocationsMainPage.switch_lang_button)

    def click_exchange_information(self):
        with step('Открыть раздел биржевой информации'):
            self.click_button(LocationsMainPage.exchange_button)

    def click_bidding_results(self):
        with step('Нажать на кнопку "Итоги торгов"'):
            self.click_button(LocationsMainPage.bidding_results)

    def open_bidding_results(self):
        with step('Открыть раздел "Итоги торгов"'):
            self.click_exchange_information()
            self.click_bidding_results()

    def click_burger_button(self):
        with step('Нажать на кнопку меню'):
            self.click_button(LocationsMainPage.burger_button)

    def check_visibility_open_pop_up_menu(self):
        with step('Проверить наличие всплывающего окна'):
            self.check_visibility(LocationsMainPage.pop_up_menu)

    def check_open_visibility_pop_up_menu(self):
        with step('Проверить открытие всплывающего окна'):
            self.click_burger_button()
            self.check_visibility_open_pop_up_menu()


main_lib = MainPage()
