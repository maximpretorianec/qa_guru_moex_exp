from utils import BaseActions, step
from test_data import LocationsBiddingPage


class BiddingPage(BaseActions):
    def check_visibility_bidding_results(self):
        with step('Проверить отображение раздела "Итоги торгов"'):
            self.click_button(LocationsBiddingPage.bidding_results)
