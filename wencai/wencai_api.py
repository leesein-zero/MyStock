from collections import Counter

import settings
import wencai.wencai as wc
from settings import *


def acquire_top_num():
    """
    今天涨停数
    :return: num
    """
    res = wc.get(query=TODAY_TOP_NUM, perpage=100, loop=True)
    return len(res)


def acquire_not_one_top_num():
    """
    今天非一字涨停
    :return: num
    """
    res = wc.get(query=TODAY_NOT_ONE_TOP_NUM, perpage=100, loop=True)
    return len(res)


def acquire_down_num():
    """
    今天跌停数
    :return:num
    """
    res = wc.get(query=TODAY_DOWN_NUM, perpage=100, loop=True)
    return len(res)


def acquire_boom_num():
    """
    今天炸板数
    :return: num
    """
    res = wc.get(query=TODAY_BOOM_NUM, perpage=100, loop=True)
    return len(res)


def acquire_continue_num():
    """
    今天连板数（包含二板及以上）
    :return: num
    """
    res = wc.get(query=TODAY_CONTINUE_TOP_NUM, perpage=100, loop=True)
    return len(res)


def acquire_first_top_num():
    """
    今天首板数
    :return: num
    """
    res = wc.get(query=TODAY_FIRST_TOP_NUM, perpage=100, loop=True)
    return len(res)


def acquire_second_top_num():
    """
    今天二连板数
    :return: num
    """
    res = wc.get(query=TODAY_SECOND_TOP_NUM, perpage=100, loop=True)
    return len(res)


def acquire_third_top_num():
    """
    今天三连板数
    :return: num
    """
    res = wc.get(query=TODAY_THIRD_TOP_NUM, perpage=100, loop=True)
    return len(res)


def acquire_many_top_num():
    """
    今天三连板以上数
    :return: num
    """
    res = wc.get(query=TODAY_MANY_TOP_NUM, perpage=100, loop=True)
    return len(res)


def analysis_by_prompt(prompt, topn):
    analysis_hy_by_prompt(prompt, topn)
    analysis_gn_by_prompt(prompt, topn)


def analysis_gn_by_prompt(prompt, topn):
    """
    分析 prompt 选出股票的概念
    :param prompt:
    :param topn:
    :return:
    """
    print(">>>>>>>>>> 概念分布：{} >>>>>>>>>>".format(prompt))

    gn_res = wc.get(query=prompt, perpage=100, loop=True, add_info=tech_condition, analysis=True)
    print("共{}只股票".format(len(gn_res.get("xuangu_tableV1"))))

    flattened_list = []
    for i in gn_res.get("xuangu_tableV1")["所属概念"]:
        flattened_list.extend(i.split(";"))

    # 过滤不需要的概念关键字
    flattened_list = [i for i in flattened_list if i not in settings.gn_filter]

    element_counts = Counter(flattened_list)

    print("概念top10: ")
    for x in element_counts.most_common(topn):
        print(x)


def analysis_hy_by_prompt(prompt, topn):
    """
    分析 prompt 选出股票的行业
    :param prompt:
    :param topn:
    :return:
    """
    print(">>>>>>>>>> 行业分布：{} >>>>>>>>>>".format(prompt))

    hy_res = wc.get(query=prompt, perpage=100, loop=True, add_info=summary_condition, analysis=True)
    print("共{}只股票".format(len(hy_res.get("xuangu_tableV1"))))

    flattened_list = []
    for i in hy_res.get("xuangu_tableV1")["所属同花顺行业"]:
        hy = i.split("-")[1]
        if hy in settings.hy_filter:
            continue
        flattened_list.append(hy)
    element_counts = Counter(flattened_list)

    print("行业top10: ")
    for x in element_counts.most_common(topn):
        print(x)
