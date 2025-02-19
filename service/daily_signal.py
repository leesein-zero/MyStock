from data_source.ak.data import *

class

def get_zhengquan_line():
    res = get_hy_lines()
    df_origin = res[res['板块'] == '证券']["涨跌幅"]
    return float(df_origin.iloc[0])/100

def get_zhangzheng_line():


def get_daily_signal():
    res = get_all_lines()


if __name__ == '__main__':
    print(get_zhengquan_line())
