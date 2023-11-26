import os
import subprocess
from prompt import *

import requests

request_data = {
    'perpage': 10,
    'page': 1,
    'source': 'Ths_iwencai_Xuangu',
    'secondary_intent': "stock",
    "question": "今天上涨的数量",
}

request_url = "https://www.iwencai.com/customized/chart/get-robot-data"


def acquire_red_num():
    request_data["question"] = TODAY_RED_NUM
    res = requests.post(request_url, json=request_data, headers=headers())
    return res.json()["data"]["answer"][0]["txt"][0]["content"]["components"][0]["data"]["meta"]["extra"]["code_count"]


def acquire_green_num():
    request_data["question"] = TODAY_GREEN_NUM
    res = requests.post(request_url, json=request_data, headers=headers())
    return res.json()["data"]["answer"][0]["txt"][0]["content"]["components"][0]["data"]["meta"]["extra"]["code_count"]


def get_token():
    # 获取token
    result = subprocess.run(['node', os.path.join(os.path.dirname(__file__), 'hexin-v.bundle.js')],
                            stdout=subprocess.PIPE)
    return result.stdout.decode().strip()  # context.call("v")


def headers(cookie=None, user_agent=None):
    if user_agent is None:
        from fake_useragent import UserAgent
        ua = UserAgent()
        user_agent = ua.random

    return {
        'hexin-v': get_token(),
        'User-Agent': user_agent,
        'cookie': cookie,
        'Content-Type': "application/json"
    }


if __name__ == '__main__':
    print(acquire_red_num())
