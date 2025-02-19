import akshare as ak
import pandas as pd

# pd.set_option('display.max_columns', None)

stock_zh_index_spot_em_df = ak.stock_zh_index_spot_em(symbol="上证系列指数")
print(float(stock_zh_index_spot_em_df.loc[stock_zh_index_spot_em_df['代码'] == "000300"]["涨跌幅"].iloc[0]))

# 有点东西
# 创新高和新低的股票数量
