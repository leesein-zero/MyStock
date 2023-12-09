from collections import Counter

import settings
import wencai.wencai as wc
from settings import *


def analysis_by_prompt(prompt, topn):
    """
    根据prompt，分析相应股票的行业与概念
    :param prompt:
    :param topn:
    :return:
    """
    prompt = prompt + "，股票简称不包含st"
    stocks = __acquire_stock_list(prompt, hy_condition)
    __analysis_hy(stocks, topn)

    stocks = __acquire_stock_list(prompt, gn_condition)
    __analysis_gn(stocks, topn)


def analysis_leader():
    """
    主要统计市场高标
    1）市场高度是多少
    2）前五个吧，高标有哪些，分别有什么行业，概念
    :return:
    """
    print("正在获取高标名称>>>>>>>>>>>")
    headers = __acquire_stock_list(TODAY_HEADERS_SORT, normal_condition)
    print("正在获取高标行业数据>>>>>>>>>>>")
    headers_with_hy = __acquire_stock_list(TODAY_HEADERS_SORT, hy_condition)
    print("正在获取高标概念数据>>>>>>>>>>>")
    headers_with_gn = __acquire_stock_list(TODAY_HEADERS_SORT, gn_condition)

    output = "名称：{}  板数：{}  行业：{}  概念：{}"
    ban_num_columns = headers.columns[5]
    for i in range(5):
        print(output.format(headers.get("股票简称")[i],
                            headers.get(ban_num_columns)[i],
                            headers_with_hy.get("xuangu_tableV1")["所属同花顺行业"][i],
                            headers_with_gn.get("xuangu_tableV1")["所属概念"][i]
                            ))


def __acquire_stock_list(prompt, condition):
    """
    根据prompt与查询条件获取个股初始数据
    :param prompt: 提示语
    :return: list
    """
    if condition == "" or condition == normal_condition:
        return wc.get(query=prompt, perpage=100, loop=True)
    return wc.get(query=prompt, perpage=100, loop=True, add_info=condition, analysis=True)


def __analysis_hy(stock_list, topn):
    """
    根据传入的股票列表，分析行业
    :param stock_list:
    :param topn:
    :return:
    """
    flattened_list = []
    for i in stock_list.get("xuangu_tableV1")["所属同花顺行业"]:
        hy = i.split("-")[1]
        if hy in settings.hy_filter:
            continue
        flattened_list.append(hy)
    element_counts = Counter(flattened_list)

    print("行业top10: ")
    for x in element_counts.most_common(topn):
        print(x)


def __analysis_gn(stock_list, topn):
    """
    根据传入的股票列表，分析概念
    :param stock_list:
    :param topn:
    :return:
    """
    flattened_list = []
    for i in stock_list.get("xuangu_tableV1")["所属概念"]:
        flattened_list.extend(i.split(";"))

    # 过滤不需要的概念关键字
    flattened_list = [i for i in flattened_list if i not in settings.gn_filter]

    element_counts = Counter(flattened_list)

    print("概念top10: ")
    for x in element_counts.most_common(topn):
        print(x)
