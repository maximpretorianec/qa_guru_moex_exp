import os
from dotenv import load_dotenv

load_dotenv()

resources_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../schemas'))
tmp_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tmp'))


class ExpectedMessagesMOEX:
    iss_engines = 'engines'
    iss_securities = 'securities'
    iss_markets = 'markets'
    iss_boards = 'boards'
    iss_trades = 'trades'


class MoexDataVariables:
    engine_by_stock = 'stock'
    market_by_index = 'index'


class FileTypes:
    xml = 'xml'
    json = 'json'
    html = 'html'
    non_type = ''


class Method:
    GET = 'get'


class StatusCode:
    SUCCESS = 200


class MoexUrl:
    BASE_URL = 'https://iss.moex.com'
    SCHOOL_URL = 'https://school.moex.com/'


class MoexVariables:
    rus_text = 'Продукты и услуги'
    eng_text = 'Markets'
    search_text = 'Вклад'


class CoreEndpoints:
    ISS = '/iss'


class EngineEndpoints(CoreEndpoints):
    def __init__(self, add_first_node=None, add_sec_node=None):
        self.ENGINE_LIST = f'{super().ISS}/engines.'
        self.MARKETS_LIST = f'{super().ISS}/engines/{add_first_node}/markets.'
        self.BOARDS_LIST = f'{super().ISS}/engines/{add_first_node}/markets/{add_sec_node}/boards.'
        self.TRADES_LIST = f'{super().ISS}/engines/{add_first_node}/markets/{add_sec_node}/trades.'


class SecuritiesEndpoints(CoreEndpoints):
    def __init__(self):
        self.SECURITIES_LIST = super().ISS + '/securities.'
