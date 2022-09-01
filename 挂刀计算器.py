#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import sys
import argparse


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# buff_price                    网易buff价格
# steam_sale_price              steam出售价格
# steam_purchase_price          steam购买价格
# quantity                      数量，默认等于1

def gd_calc(buff_price, steam_purchase_price, quantity=1, default_proportion=0.8697):
    buff_price = buff_price
    print("-------------------------------")
    print("价格计算结果如下：")
    print("网易 BUFF 价格为：%s" % buff_price)

    steam_purchase_price = steam_purchase_price
    print("steam 购买价格为：%s" % steam_purchase_price)

    steam_sale_price = (steam_purchase_price * default_proportion)
    steam_sale_price = round(steam_sale_price, 2)
    print("steam 出售价格为：%.2f" % steam_sale_price)

    quantity = quantity
    print("数量为：%s" % quantity)
    print("--------")
    steam_sale_price * 1.15 == steam_purchase_price

    total_purchase_price = buff_price * quantity
    print("buff总购买所需价格为：%.2f" % total_purchase_price)


    total_sales_price = (steam_sale_price * quantity)
    print("steam总出售余额为：%.2f" % total_sales_price)

    single_price_difference = (steam_sale_price - buff_price)
    print("倒余额单个差值为：%.2f" % single_price_difference)

    total_price_differences = (total_sales_price - total_purchase_price)
    print("倒余额差值为：%.2f" % total_price_differences)

    proportion = (buff_price / steam_sale_price)
    print("倒余额比例为：%.2f" % proportion)
    print("-------------------------------")


# print '参数个数为:', len(sys.argv), '个参数。'
# print '参数列表:', str(sys.argv)

print("运行参数为：" + str(sys.argv))

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
    # gd_calc(7.3, 10.5, 3)
    gd_calc(float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]))

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
