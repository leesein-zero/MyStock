from native import native_api
from settings import *
from wencai import wencai_api

if __name__ == '__main__':
    # 市场晴雨表
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

    # 板块晴雨表
    # 总涨停
    wencai_api.analysis_by_prompt(TODAY_TOP_NUM, 10)
    wencai_api.analysis_by_prompt(TODAY_FIRST_TOP_NUM, 10)
    wencai_api.analysis_by_prompt(TODAY_SECOND_TOP_NUM, 10)
    wencai_api.analysis_by_prompt(TODAY_THIRD_TOP_NUM, 10)
    wencai_api.analysis_by_prompt(TODAY_MANY_TOP_NUM, 10)

    wencai_api.analysis_by_prompt(TODAY_DOWN_NUM, 10)
    wencai_api.analysis_by_prompt(TODAY_BOOM_NUM, 10)
