import wencai.wencai
from native import native_api
from settings import TODAY_MANY_TOP_NUM, tech_condition
from wencai import wencai_api

if __name__ == '__main__':
    print("上涨的股票个数：{}".format(native_api.acquire_red_num()))
    print("下跌的股票个数：{}".format(native_api.acquire_green_num()))
    print("实际涨停的股票个数：{}".format(wencai_api.acquire_top_num()))
    print("非一字板涨停的股票个数：{}".format(wencai_api.acquire_not_one_top_num()))
    print("跌停的股票个数：{}".format(wencai_api.acquire_down_num()))
    print("炸板的股票个数：{}".format(wencai_api.acquire_boom_num()))
    print("连板的股票个数：{}".format(wencai_api.acquire_continue_num()))
    print("首板的股票个数：{}".format(wencai_api.acquire_first_top_num()))
    print("二连板的股票个数：{}".format(wencai_api.acquire_second_top_num()))
    print("三连板的股票个数：{}".format(wencai_api.acquire_third_top_num()))
    print("三连板以上的股票个数：{}".format(wencai_api.acquire_many_top_num()))

    # todo 下面是获取行业概念等的范例
    res = wencai.wencai.get(query=TODAY_MANY_TOP_NUM, perpage=100, loop=True, add_info=tech_condition, analysis=True)
    print(res)
