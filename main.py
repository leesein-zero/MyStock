from native import native_api
from settings import *
from wencai import wencai_api

if __name__ == '__main__':
    # 市场晴雨表
    print("上涨的股票个数：{}".format(native_api.count_stocks_num(TODAY_RED_NUM)))
    print("下跌的股票个数：{}".format(native_api.count_stocks_num(TODAY_GREEN_NUM)))
    print("实际涨停的股票个数：{}".format(native_api.count_stocks_num(TODAY_TOP_NUM)))
    print("非一字板涨停的股票个数：{}".format(native_api.count_stocks_num(TODAY_NOT_ONE_TOP_NUM)))
    print("跌停的股票个数：{}".format(native_api.count_stocks_num(TODAY_DOWN_NUM)))
    print("炸板的股票个数：{}".format(native_api.count_stocks_num(TODAY_BOOM_NUM)))
    print("连板的股票个数：{}".format(native_api.count_stocks_num(TODAY_CONTINUE_TOP_NUM)))
    print("首板的股票个数：{}".format(native_api.count_stocks_num(TODAY_FIRST_TOP_NUM)))
    print("二连板的股票个数：{}".format(native_api.count_stocks_num(TODAY_SECOND_TOP_NUM)))
    print("三连板的股票个数：{}".format(native_api.count_stocks_num(TODAY_THIRD_TOP_NUM)))
    print("三连板以上的股票个数：{}".format(native_api.count_stocks_num(TODAY_MANY_TOP_NUM)))

    # 板块/概念晴雨表
    # 总涨停
    wencai_api.analysis_by_prompt(TODAY_TOP_NUM, 10)
    wencai_api.analysis_by_prompt(TODAY_FIRST_TOP_NUM, 10)
    wencai_api.analysis_by_prompt(TODAY_SECOND_TOP_NUM, 10)
    wencai_api.analysis_by_prompt(TODAY_THIRD_TOP_NUM, 10)
    wencai_api.analysis_by_prompt(TODAY_MANY_TOP_NUM, 10)

    wencai_api.analysis_by_prompt(TODAY_DOWN_NUM, 10)
    wencai_api.analysis_by_prompt(TODAY_BOOM_NUM, 10)

    # 高标统计
    wencai_api.analysis_leader()
