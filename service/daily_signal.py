from data_source.ak.data import *


class Signal:
    def __init__(self):
        self.hy_line = get_hy_lines()
        self.all_line = get_all_lines()

    def get_zhengquan_line(self):
        """
        获取证券板块涨幅
        :return: float
        """
        df_origin = self.hy_line[self.hy_line['板块'] == '证券']["涨跌幅"]
        result = float(df_origin.iloc[0]) / 100  # 计算涨跌幅
        return round(result, 4)  # 保留四位小数

    def get_shangzheng_line(self):
        """
        上证指数涨幅
        :return:
        """
        df_origin = self.all_line[self.all_line["名称"] == "上证指数"]["涨跌幅"]
        result = float(df_origin.iloc[0]) / 100  # 计算涨跌幅
        return round(result, 4)  # 保留四位小数

    def get_cyb_line(self):
        """
        创业板涨幅
        :return:
        """
        df_origin = self.all_line[self.all_line["名称"] == "创业板指"]["涨跌幅"]
        result = float(df_origin.iloc[0]) / 100  # 计算涨跌幅
        return round(result, 4)  # 保留四位小数
        # return df_origin

    def get_zz2000_line(self):
        """
        中证2000涨幅
        :return:
        """
        df_origin = self.all_line[self.all_line["名称"] == "中证2000"]["涨跌幅"]
        result = float(df_origin.iloc[0]) / 100  # 计算涨跌幅
        return round(result, 4)  # 保留四位小数

    def get_sz50_line(self):
        """
        上证50涨幅
        :return:
        """
        df_origin = self.all_line[self.all_line["名称"] == "上证50"]["涨跌幅"]
        result = float(df_origin.iloc[0]) / 100  # 计算涨跌幅
        return round(result, 4)  # 保留四位小数

    def get_hs300_line(self):
        """
        沪深300涨幅
        :return:
        """
        df_origin = self.all_line[self.all_line["名称"] == "沪深300"]["涨跌幅"]
        result = float(df_origin.iloc[0]) / 100  # 计算涨跌幅
        return round(result, 4)  # 保留四位小数

    def get_daily_signal(self):
        res = """
        上证指数: {}
        创业板指: {}
        沪深300: {}
        中证2000: {}
        上证50: {}
        证券: {}
        """.format(self.get_shangzheng_line(),
                   self.get_cyb_line(),
                   self.get_hs300_line(),
                   self.get_zz2000_line(),
                   self.get_sz50_line(),
                   self.get_zhengquan_line())
        return res


if __name__ == '__main__':
    signal = Signal()
    # print(signal.all_line)
    # print(signal.get_cyb_line())
    print(signal.get_daily_signal())
