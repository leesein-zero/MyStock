import akshare as ak
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# stock_board_industry_summary_ths_df = ak.stock_board_industry_summary_ths()
# motor_df = stock_board_industry_summary_ths_df[stock_board_industry_summary_ths_df['板块'] == '证券']
#
# # 打印筛选后的数据
# print(motor_df)


def get_all_lines():
    """
    获取市场指数
    :return:
        序号      代码       名称       最新价   涨跌幅     涨跌额         成交量           成交额
        0    1  000001     上证指数   3351.54  0.81   27.05   502912965  6.751464e+11
        1    2  399001     深证成指  10772.65  1.46  155.39   750496631  1.045873e+12
        2    3  899050     北证50   1289.84  5.36   65.66    12353089  2.843457e+10
        3    4  399006     创业板指   2226.98  2.03   44.41   260631356  5.073394e+11
        4    5  000680     科创综指   1202.69  2.97   34.74    41785846  1.571039e+11
    """
    return ak.stock_zh_index_spot_em(symbol="沪深重要指数")


def get_hy_lines():
    """
    获取同花顺行业指数
    :return:
     序号       板块   涨跌幅     总成交量     总成交额     净流入  上涨家数  下跌家数     均价    领涨股
    0    1    自动化设备  5.70  2278.64   580.07   83.36    93     1  25.46   三丰智能
    1    2       电机  5.59   684.09   176.04   21.67    24     0  25.73   江南奕帆
    2    3      半导体  4.92  2674.83  1360.75  138.70   156     3  50.87    帝奥微
    3    4    汽车零部件  4.39  5135.60   800.59   81.42   234     6  15.59   骏创科技
    """
    return ak.stock_board_industry_summary_ths()


if __name__ == '__main__':
    print(get_hy_lines())
