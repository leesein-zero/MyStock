import pywencai as wc
from prompt import *


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


if __name__ == '__main__':
    print(acquire_top_num())
    print(acquire_not_one_top_num())
    print(acquire_down_num())
