from allure import step
from selene import be, browser


class BiddingPage():
    bidding_results = browser.element('.headermain')

    def check_visibility_bidding_results(self, loc_bidding_results=bidding_results):
        with step('Проверить отображение раздела "Итоги торгов"'):
            loc_bidding_results.should(be.visible)


bidding_lib = BiddingPage()
