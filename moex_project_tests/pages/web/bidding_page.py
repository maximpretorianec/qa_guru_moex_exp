from moex_project_tests.utils import BaseActions, step
from moex_project_tests.test_data import LocationsBiddingPage


class BiddingPage(BaseActions):
    def check_visibility_bidding_results(self):
        with step('Проверить отображение раздела "Итоги торгов"'):
            self.click_button(LocationsBiddingPage.bidding_results)
