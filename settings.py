TODAY_RED_NUM = "{}上涨的个股数量"
TODAY_GREEN_NUM = "{}下跌的个股数量"
TODAY_TOP_NUM = "{}实际涨停数量"
TODAY_NOT_ONE_TOP_NUM = "{}不含一字涨停数量"
TODAY_DOWN_NUM = "{}跌停数量"
TODAY_BOOM_NUM = "{}炸板的股票数量"
TODAY_CONTINUE_TOP_NUM = "{}连板的股票数量"
TODAY_FIRST_TOP_NUM = "{}首板的股票数量"
TODAY_SECOND_TOP_NUM = "{}二连板的股票数量"
TODAY_THIRD_TOP_NUM = "{}三连板的股票数量"
TODAY_MANY_TOP_NUM = "{}的连续涨停天数大于三"

TODAY_HEADERS_SORT = "股票简称不包含st，{}涨停的股票数量，连续涨停天数从大到小排序前5个"

# 沪深300创20日新高
BIG_HIGH_IN20 = "{}沪深300成分股，最高价创20日新高"
# 沪深300创20日新低
BIG_LOW_IN20 = "{}沪深300成分股，最高价创20日新低"
# 中证500创20日新高
MID_HIGH_IN20 = "{}中证500成分股，最高价创20日新高"

SMALL_HIGH_IN20 = "{}中证2000成分股，最高价创20日新高"
SMALL_LOW_IN20 = "{}中证2000成分股，最高价创20日新低"

# add_info
# 相关
normal_condition = "{\"urp\":{\"scene\":1,\"company\":1,\"business\":1},\"contentType\":\"json\"}"
# 概览（有行业）
hy_condition = "{\"urp\":{\"scene\":1,\"company\":1,\"business\":1,\"addheaderindexes\":\"所属同花顺行业;公司简介;企业性质;最新在职员工人数;总市值;成交量;成交额;换手率;dde散户数量\",\"indexnamelimit\":\"股票代码;股票简称;最新价;最新涨跌幅;所属同花顺行业;公司简介;企业性质;最新在职员工人数;总市值;成交量;成交额;换手率;dde散户数量\"},\"contentType\":\"json\"}"
# 技术（有概念）
gn_condition = "{\"urp\":{\"scene\":1,\"company\":1,\"business\":1,\"addheaderindexes\":\"竞价量;竞价金额;换手率;主力资金流向;个股热度;dde散户数量;集中度90;所属概念;技术形态\",\"indexnamelimit\":\"股票代码;股票简称;最新价;最新涨跌幅;竞价量;竞价金额;换手率;主力资金流向;个股热度;dde散户数量;集中度90;所属概念;技术形态\"},\"contentType\":\"json\"}"

# 概念需要被剔除的关键字
gn_filter = ["融资融券", "转融券标的", "地方国企改革", "深股通", "沪股通", "央企国企改革", "标普道琼斯A股",
             "富时罗素概念股", "富时罗素概念", "粤港澳大湾区", "江苏国企改革", "上海国企改革", "广东国企改革"]
# 行业需要被剔除的关键字
hy_filter = ["综合"]
