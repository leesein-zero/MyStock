import os
import subprocess
from settings import *

import requests

request_data = {
    'perpage': 10,
    'page': 1,
    'source': 'Ths_iwencai_Xuangu',
    'secondary_intent': "stock",
    "question": "今天上涨的数量",
}

request_url = "https://www.iwencai.com/customized/chart/get-robot-data"


def count_stocks_num(prompt):
    """
    对查询条件筛选出的个股计数
    :param prompt:
    :return:
    """
    request_data["question"] = prompt
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
    request_data[
        "add_info"] = "{\"urp\":{\"scene\":1,\"company\":1,\"business\":1,\"addheaderindexes\":\"竞价量;竞价金额;换手率;主力资金流向;个股热度;dde散户数量;集中度90;所属概念;技术形态\",\"indexnamelimit\":\"股票代码;股票简称;最新价;最新涨跌幅;竞价量;竞价金额;换手率;主力资金流向;个股热度;dde散户数量;集中度90;所属概念;技术形态\"},\"contentType\":\"json\"}"
    request_data["question"] = TODAY_FIRST_TOP_NUM
    request_data["rsh"] = "Ths_iwencai_Xuangu_phz6l4wqivfibtymqs6loxxes80xmv1t"
    request_data["token"] = "0ac9529b17010981510355638"
    res = requests.post(request_url, json=request_data, headers=headers())
    print(len(res.json()["data"]["answer"][0]["txt"][0]["content"]["components"][0]["data"]["datas"]))
    print(res.json()["data"]["answer"][0]["txt"][0]["content"]["components"][0]["data"]["datas"][0])
