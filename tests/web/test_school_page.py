import allure

from moex_project_tests.utils import TypeTag, Severity
from moex_project_tests.test_data import MoexUrl
from moex_project_tests.pages.web import main_page, school_page


@allure.epic('Страница обучения')
class TestSchoolPage:
    @allure.story('Открытие раздела сайта - Обучение')
    @allure.title('Страница обучения должна быть открыта в новой вкладке')
    @allure.feature('Страница обучения')
    @allure.label('owner', 'mgolubev')
    @allure.label('layer', TypeTag.UI)
    @allure.tag(TypeTag.REGRESS, TypeTag.UI, Severity.MINOR)
    @allure.severity(Severity.MINOR)
    def test_open_school_tab(self):
        main_page.open_new_tab_school()

        school_page.check_visibility_moex_school_logo()
        school_page.is_assert_equal_values(MoexUrl.SCHOOL_URL, school_page.get_curr_url())
