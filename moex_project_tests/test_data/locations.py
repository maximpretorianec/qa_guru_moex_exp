class LocationsMainPage:
    moex_logo = '.header__logo .nuxt-link-exact-active .app-logo img'
    lang_section = '.lang-switch'
    search_field_icon = 'label[for=moex-search-input] svg'
    cart_button = '.cart-button'
    switch_lang_button = '//span[contains(@class, "lang-switch__lang") and not(contains(@class, "lang-switch__lang--active"))]'
    search_field = 'div #moex-search-input'
    search_result_list = 'div .search-titles-list'
    exchange_button = '//ul[@class="site-header-menu__main-list"]/li[2]'
    bidding_results = '//div[contains(.,"По всем рынкам Московской биржи")]/ancestor::li[1]'
    burger_button = 'button[aria-label*="Открыть бургер-меню"]'
    pop_up_menu = '.header-burger__desktop'

    def __init__(self, text):
        self.page_href_by_text = f'a[href*="{text}"].site-header-menu__top-link'
        self.header_obj_with_text = f'//ul[@class="site-header-menu__main-list"]/*[contains(.,"{text}")]'
        self.time_on_site = f'//div[@class="header-nav__date" and contains(.,"{text}")]'


class LocationsBiddingPage:
    bidding_results = '.headermain'


class LocationsSchoolPage:
    moex_school_logo = '.nuxt-link-exact-active div'
