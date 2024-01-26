import allure

from moex_project_tests.utils import TypeTag, Severity
from moex_project_tests.pages.web import main_lib


@allure.epic('Главная страница')
@allure.story('Открыть главную страницу')
@allure.title('Стартовая страница, проверка базовых элементов страницы')
@allure.feature('Главная страница')
@allure.label('owner', 'mgolubev')
@allure.label('layer', TypeTag.UI)
@allure.tag(TypeTag.SMOKE, TypeTag.REGRESS, TypeTag.UI, Severity.CRITICAL)
@allure.severity(Severity.CRITICAL)
def test_open_main_page():
    main_lib.open_core_site()

    main_lib.check_visibility_base_page_elements()


@allure.epic('Главная страница')
@allure.story('Смена языков')
@allure.title('Смена языка на странице на английский')
@allure.feature('Смена языков')
@allure.label('owner', 'mgolubev')
@allure.label('layer', TypeTag.UI)
@allure.tag(TypeTag.REGRESS, TypeTag.UI, Severity.TRIVIAL)
@allure.severity(Severity.TRIVIAL)
def test_switch_language():
    main_lib.open_core_site()
    main_lib.check_rus_name_at_top_menu()

    main_lib.click_switch_lang()
    main_lib.check_eng_name_at_top_menu()


@allure.epic('Главная страница')
@allure.story('Поиск')
@allure.title('Поиск новостей, статей, прочей информации')
@allure.feature('Строка поиска')
@allure.label('owner', 'mgolubev')
@allure.label('layer', TypeTag.UI)
@allure.tag(TypeTag.REGRESS, TypeTag.UI, Severity.TRIVIAL)
@allure.severity(Severity.TRIVIAL)
def test_search_field():
    main_lib.open_core_site()

    main_lib.filling_search_field()
    main_lib.check_visibility_search_result()

@allure.epic('Главная страница')
@allure.story('Время')
@allure.title('Сверка времени на сайте')
@allure.feature('Время в верхнем меню')
@allure.label('owner', 'mgolubev')
@allure.label('layer', TypeTag.UI)
@allure.tag(TypeTag.REGRESS, TypeTag.UI, Severity.MAJOR)
@allure.severity(Severity.MAJOR)
def test_time_on_page():
    main_lib.open_core_site()

    main_lib.check_time_on_site()


@allure.epic('Главная страница')
@allure.story('Вспывающее меню')
@allure.title('Проверка открытия всплывающего меню')
@allure.feature('Раскрытие меню')
@allure.label('owner', 'mgolubev')
@allure.label('layer', TypeTag.UI)
@allure.tag(TypeTag.REGRESS, TypeTag.UI, Severity.MAJOR)
@allure.severity(Severity.MAJOR)
def test_open_pop_up_window():
    main_lib.open_core_site()

    main_lib.check_open_visibility_pop_up_menu()
