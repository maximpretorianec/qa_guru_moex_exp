from moex_project_tests.utils import base_lib
from moex_project_tests.test_data import MoexUrl
from selene import be, browser
from allure import step


class SchoolPage:
    moex_school_logo = browser.element('//a[contains(@class,"nuxt-link-exact-active")]/div')

    def check_visibility_moex_school_logo(self, loc_moex_school_logo=moex_school_logo):
        with step('Иконка школы MOEX отображается в верхнем меню'):
            loc_moex_school_logo.should(be.visible)

    def check_visibility_page(self):
        with step('Проверка отображения страницы и верного адреса'):
            school_lib.check_visibility_moex_school_logo()
            base_lib.is_assert_equal_values(MoexUrl.SCHOOL_URL, base_lib.get_curr_url())


school_lib = SchoolPage()
