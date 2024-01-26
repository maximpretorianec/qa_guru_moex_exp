import json
import logging
import os
import allure
import requests
import zoneinfo
import tzdata
from moex_project_tests.test_data import resources_path
from datetime import datetime


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - Response Code: %(response_code)s - URL: %(url)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def load_schema(file):
    with open(os.path.join(resources_path, file)) as file:
        return json.load(file)


def send_request(base_url, endpoint, method, **kwargs):
    method_func = getattr(requests, method.lower())
    response = method_func(base_url + endpoint, **kwargs)

    log_to_allure(response.request, response)
    log_to_console(response)
    return response


def log_to_allure(request, response):
    request_info = f"URL: {request.url}\nMethod: {request.method}\nHeaders: {request.headers}\n"
    if request.body:
        request_info += f"Body: {request.body}\n"
    allure.attach(
        body=request_info,
        name="Request",
        attachment_type=allure.attachment_type.TEXT,
        extension="txt",
    )
    response_info = f"Status code: {response.status_code}\nHeaders: {response.headers}\nBody:\n{response.text}"
    allure.attach(
        body=response_info,
        name="Response",
        attachment_type=allure.attachment_type.TEXT,
        extension="txt",
    )


def log_to_console(response):
    logging.info("Response Code: %s - URL: %s",
                 response.status_code, response.request.url)


def get_current_time():
    zone = zoneinfo.ZoneInfo("Europe/Moscow")
    return str(datetime.now(zone).strftime("%H:%M"))
