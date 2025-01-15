from native import native_api
from settings import *
from wencai import wencai_api
import psycopg2
from datetime import datetime

db_config = {
    'dbname': 'stock_daily',
    'user': 'postgres',
    'password': 'admin',
    'host': '127.0.0.1',
    'port': '5432'
}


def insert_daily_stock(
        shangzhang,
        xiedie,
        zhangting,
        dieting,
        lianban,
        hs300_20high,
        hs300_20low,
        zz2000_20high,
        zz2000_20low,
        date
):
    data = {
        'shangzhang': shangzhang,
        'xiadie': xiedie,
        'zhangting': zhangting,
        'dieting': dieting,
        'lianban': lianban,
        'hs300_20high': hs300_20high,
        'hs300_20low': hs300_20low,
        'zz2000_20high': zz2000_20high,
        'zz2000_20low': zz2000_20low,
        'date': date
    }

    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    # 插入数据的 SQL 语句
    insert_query = """
    INSERT INTO public.t_daily (shangzhang, xiadie, zhangting, dieting, lianban, hs300_20high, hs300_20low, zz2000_20high, zz2000_20low, date)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    # 执行插入操作
    cursor.execute(insert_query, (
        data['shangzhang'],
        data['xiadie'],
        data['zhangting'],
        data['dieting'],
        data['lianban'],
        data['hs300_20high'],
        data['hs300_20low'],
        data['zz2000_20high'],
        data['zz2000_20low'],
        data['date']
    ))

    # 提交事务
    conn.commit()

    # 关闭连接
    cursor.close()
    conn.close()

    print("数据插入成功！")


if __name__ == '__main__':
    # 不写则取今天
    expect_date = None
    # expect_date = "2025-01-13"

    parse_date = datetime.now().date()

    if expect_date:
        parse_date = expect_date
    insert_daily_stock(
        native_api.count_stocks_num(TODAY_RED_NUM.format(parse_date)),
        native_api.count_stocks_num(TODAY_GREEN_NUM.format(parse_date)),
        native_api.count_stocks_num(TODAY_TOP_NUM.format(parse_date)),
        native_api.count_stocks_num(TODAY_DOWN_NUM.format(parse_date)),
        native_api.count_stocks_num(TODAY_CONTINUE_TOP_NUM.format(parse_date)),
        native_api.count_stocks_num(BIG_HIGH_IN20.format(parse_date)),
        native_api.count_stocks_num(BIG_LOW_IN20.format(parse_date)),
        native_api.count_stocks_num(SMALL_HIGH_IN20.format(parse_date)),
        native_api.count_stocks_num(SMALL_LOW_IN20.format(parse_date)),
        parse_date
    )
    # 市场晴雨表
    # print("上涨的股票个数：{}".format(native_api.count_stocks_num(TODAY_RED_NUM)))
    # print("下跌的股票个数：{}".format(native_api.count_stocks_num(TODAY_GREEN_NUM)))
    # print("实际涨停的股票个数：{}".format(native_api.count_stocks_num(TODAY_TOP_NUM)))
    # # print("非一字板涨停的股票个数：{}".format(native_api.count_stocks_num(TODAY_NOT_ONE_TOP_NUM)))
    # print("跌停的股票个数：{}".format(native_api.count_stocks_num(TODAY_DOWN_NUM)))
    # # print("炸板的股票个数：{}".format(native_api.count_stocks_num(TODAY_BOOM_NUM)))
    # print("连板的股票个数：{}".format(native_api.count_stocks_num(TODAY_CONTINUE_TOP_NUM)))
    # # print("首板的股票个数：{}".format(native_api.count_stocks_num(TODAY_FIRST_TOP_NUM)))
    # # print("二连板的股票个数：{}".format(native_api.count_stocks_num(TODAY_SECOND_TOP_NUM)))
    # # print("三连板的股票个数：{}".format(native_api.count_stocks_num(TODAY_THIRD_TOP_NUM)))
    # # print("三连板以上的股票个数：{}".format(native_api.count_stocks_num(TODAY_MANY_TOP_NUM)))
    # print("沪深300创20新高股票个数：{}".format(native_api.count_stocks_num(BIG_HIGH_IN20)))
    # print("沪深300创20新低股票个数：{}".format(native_api.count_stocks_num(BIG_LOW_IN20)))
    # print("中证2000创20日新高股票个数：{}".format(native_api.count_stocks_num(SMALL_HIGH_IN20)))
    # print("中证2000创20日新低股票个数：{}".format(native_api.count_stocks_num(SMALL_LOW_IN20)))

    # 板块/概念晴雨表
    # 总涨停
    # wencai_api.analysis_by_prompt(TODAY_TOP_NUM, 30)
    # wencai_api.analysis_by_prompt(TODAY_FIRST_TOP_NUM, 30)
    # wencai_api.analysis_by_prompt(TODAY_SECOND_TOP_NUM, 15)
    # wencai_api.analysis_by_prompt(TODAY_THIRD_TOP_NUM, 10)
    # wencai_api.analysis_by_prompt(TODAY_MANY_TOP_NUM, 15)

    # wencai_api.analysis_by_prompt(TODAY_DOWN_NUM, 10)
    # wencai_api.analysis_by_prompt(TODAY_BOOM_NUM, 10)

    # wencai_api.analysis_by_prompt(BIG_HIGH_IN20, 20)
    # wencai_api.analysis_by_prompt(BIG_LOW_IN20, 20)
    # wencai_api.analysis_by_prompt(MID_HIGH_IN20, 20)

    # 高标统计
    # wencai_api.analysis_leader()
