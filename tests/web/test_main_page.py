import allure

from moex_project_tests.utils import TypeTag, Severity
from moex_project_tests.test_data import MoexVariables
from moex_project_tests.pages.web import MainPage, BiddingPage


@allure.epic('Главная страница')
class TestMainPage:
    @allure.story('Открыть главную страницу')
    @allure.title('Стартовая страница, проверка базовых элементов страницы')
    @allure.feature('Главная страница')
    @allure.label('owner', 'mgolubev')
    @allure.label('layer', TypeTag.UI)
    @allure.tag(TypeTag.SMOKE, TypeTag.REGRESS, TypeTag.UI, Severity.CRITICAL)
    @allure.severity(Severity.CRITICAL)
    def test_open_main_page(self):
        main_page = MainPage()
        main_page.check_visibility_moex_icon()
        main_page.check_visibility_cart_button_at_top_menu()
        main_page.check_visibility_lang_switch_at_top_menu()
        main_page.check_visibility_search_at_top_menu()

    @allure.story('Смена языков')
    @allure.title('Смена языка на странице на английский')
    @allure.feature('Смена языков')
    @allure.label('owner', 'mgolubev')
    @allure.label('layer', TypeTag.UI)
    @allure.tag(TypeTag.REGRESS, TypeTag.UI, Severity.TRIVIAL)
    @allure.severity(Severity.TRIVIAL)
    def test_switch_language(self):
        main_page = MainPage()
        main_page.check_rus_name_at_top_menu(MoexVariables.rus_text)

        main_page.click_switch_lang_at_top_menu()
        main_page.check_eng_name_at_top_menu(MoexVariables.eng_text)

    @allure.story('Поиск')
    @allure.title('Поиск новостей, статей, прочей информации')
    @allure.feature('Строка поиска')
    @allure.label('owner', 'mgolubev')
    @allure.label('layer', TypeTag.UI)
    @allure.tag(TypeTag.REGRESS, TypeTag.UI, Severity.TRIVIAL)
    @allure.severity(Severity.TRIVIAL)
    def test_search_field(self):
        main_page = MainPage()
        main_page.filling_search_field()
        main_page.check_visibility_search_result()

    @allure.story('Время')
    @allure.title('Сверка времени на сайте')
    @allure.feature('Время в верхнем меню')
    @allure.label('owner', 'mgolubev')
    @allure.label('layer', TypeTag.UI)
    @allure.tag(TypeTag.REGRESS, TypeTag.UI, Severity.MAJOR)
    @allure.severity(Severity.MAJOR)
    def test_time_on_page(self):
        main_page = MainPage()
        main_page.check_time_on_site()

    @allure.story('Итоги торгов')
    @allure.title('Открытие раздела "итоги торгов" в текущей вкладке')
    @allure.feature('Открытие "Итоги торгов"')
    @allure.label('owner', 'mgolubev')
    @allure.label('layer', TypeTag.UI)
    @allure.tag(TypeTag.REGRESS, TypeTag.UI, Severity.MAJOR)
    @allure.severity(Severity.MAJOR)
    def test_open_page_in_current_tab(self):
        main_page = MainPage()
        main_page.open_bidding_results()
        bidd_results = BiddingPage()
        bidd_results.check_visibility_bidding_results()

    @allure.story('Итоги торгов')
    @allure.title('Открытие раздела "итоги торгов" в текущей вкладке')
    @allure.feature('Открытие "Итоги торгов"')
    @allure.label('owner', 'mgolubev')
    @allure.label('layer', TypeTag.UI)
    @allure.tag(TypeTag.REGRESS, TypeTag.UI, Severity.MAJOR)
    @allure.severity(Severity.MAJOR)
    def test_open_pop_up_window(self):
        main_page = MainPage()
        main_page.check_open_visibility_pop_up_menu()
