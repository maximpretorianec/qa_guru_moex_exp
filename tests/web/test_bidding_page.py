import allure

from moex_project_tests.utils import TypeTag, Severity
from moex_project_tests.pages.web import main_lib, bidding_lib


@allure.epic('Главная страница')
class TestBiddingPage:
    @allure.story('Итоги торгов')
    @allure.title('Открытие раздела "итоги торгов" в текущей вкладке')
    @allure.feature('Открытие "Итоги торгов"')
    @allure.label('owner', 'mgolubev')
    @allure.label('layer', TypeTag.UI)
    @allure.tag(TypeTag.REGRESS, TypeTag.UI, Severity.MAJOR)
    @allure.severity(Severity.MAJOR)
    def test_open_page_in_current_tab(self):
        main_lib.open_core_site()
        main_lib.open_bidding_results()
        bidding_lib.check_visibility_bidding_results()
