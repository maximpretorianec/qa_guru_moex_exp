import allure

from moex_project_tests.utils import TypeTag, Severity
from moex_project_tests.pages.web import main_lib, school_lib


@allure.epic('Страница обучения')
@allure.story('Открытие раздела сайта - Обучение')
@allure.title('Страница обучения должна быть открыта в новой вкладке')
@allure.feature('Страница обучения')
@allure.label('owner', 'mgolubev')
@allure.label('layer', TypeTag.UI)
@allure.tag(TypeTag.REGRESS, TypeTag.UI, Severity.MINOR)
@allure.severity(Severity.MINOR)
def test_open_school_tab():
    main_lib.open_core_site()
    main_lib.open_new_tab_school()

    school_lib.check_visibility_page()
