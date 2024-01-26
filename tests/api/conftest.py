import pytest
import random
import shutil
import os

from moex_project_tests.test_data import MoexUrl, EngineEndpoints, FileTypes, tmp_path
from moex_project_tests.api_models import get_data_by_moex_api


@pytest.fixture(scope='module')
def tmp_dir_control():
    if not os.path.exists(tmp_path):
        os.mkdir(tmp_path)
    yield
    if os.listdir(tmp_path):
        shutil.rmtree(tmp_path)
    else:
        os.rmdir(tmp_path)


@pytest.fixture()
def base_url():
    return MoexUrl.BASE_URL


@pytest.fixture()
def get_engine_from_list(base_url):
    return random.choice(
        get_data_by_moex_api(base_url, EngineEndpoints().ENGINE_LIST, FileTypes.json).json()['engines']['data'])[1]


@pytest.fixture()
def get_market_from_list_by_engine(base_url, get_engine_from_list):
    engine = get_engine_from_list
    return engine, random.choice(
        get_data_by_moex_api(base_url,
                             EngineEndpoints(engine).MARKETS_LIST,
                             FileTypes.json).json()['markets']['data'])[1]
