#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import sys
import argparse



# buff_price                    网易buff价格
# steam_sale_price              steam出售价格
# steam_purchase_price          steam购买价格
# quantity                      数量，默认等于1




class Calculator():
    def __init__(self, default_proportion=0.8697):
        self.default_proportion = default_proportion
        self.parser = argparse.ArgumentParser(prog='python3 KnifeHangingCalculator.py', 
                                              description = "steam挂刀计算器，为方便倒余额写的。", 
                                              epilog="感谢您的使用！祝您挂刀愉快，比例低低！", 
                                              formatter_class=argparse.ArgumentDefaultsHelpFormatter, 
                                              argument_default=argparse.SUPPRESS, 
                                              add_help=False, 
                                              # exit_on_error=False
                                              )
        self.parser.add_argument('-h', '--help', action='help',default=argparse.SUPPRESS, help='使用帮助.')

        self.parser.add_argument('-buff','--buff_price', nargs='?', type=float, required=True, help='网易buff购买价格(buff_price).')
        self.parser.add_argument('-spp','--steam_purchase_price', nargs='?', type=float, required=True, help='Steam 购买价格,也就是别的玩家购买饰品的价格(steam_purchase_price).')
        self.parser.add_argument('-q', '--quantity', nargs='?', type=int, default=1, help='默认数量为1.')

        self.parser.add_argument('-dp', '--default_proportion', type=float, default=0.8697, help='默认Steam比例(0.8697)，一般情况下无需更改.')
        self.parser.add_argument('-v', '--version',action='version',version='当前软件版本为: 1.0', help='显示软件当前版本.')

        self.args = self.parser.parse_args()

    # buff 价格
    def buff(self):
        buff_price = self.args.buff_price
        print("网易 BUFF 价格为: %.2f" % buff_price)

    # steam 出售价格
    def steam_sale_price(self):
        steam_purchase_price = self.args.steam_purchase_price
        steam_sale_price = (steam_purchase_price * self.args.default_proportion)
        steam_sale_price = round(steam_sale_price, 2)
        print("steam 出售价格为: %.2f" % steam_sale_price)

    # steam 购买价格
    def steam_purchase_price(self):
        steam_purchase_price = self.args.steam_purchase_price
        print("steam 购买价格为: %.2f" % steam_purchase_price)

    # 数量
    def quantity(self):
        print("数量为: %s 件" % self.args.quantity)

    # buff 总购买所需价格
    def total_purchase_price(self):
        total_purchase_price = self.args.buff_price * self.args.quantity
        print("buff总购买所需价格为: %.2f" % total_purchase_price)

    # steam 总出售获得余额
    def total_sales_price(self):
        steam_sale_price = (self.args.steam_purchase_price * self.args.default_proportion)
        steam_sale_price = round(steam_sale_price, 2)
        total_sales_price = steam_sale_price * self.args.quantity
        print("steam总出售获得余额为: %.2f" % total_sales_price)


    # 倒余额单个差值
    def single_price_difference(self):
        steam_sale_price = (self.args.steam_purchase_price * self.args.default_proportion)
        steam_sale_price = round(steam_sale_price, 2)
        single_price_difference = (steam_sale_price - self.args.buff_price)
        print("倒余额单个差值为: %.2f" % single_price_difference)

    # 倒余额总差值
    def total_price_differences(self):
        steam_sale_price = (self.args.steam_purchase_price * self.args.default_proportion)
        steam_sale_price = round(steam_sale_price, 2)
        total_sales_price = steam_sale_price * self.args.quantity
        total_purchase_price = self.args.buff_price * self.args.quantity
        total_price_differences = (total_sales_price - total_purchase_price)
        print("倒余额总差值为: %.2f" % total_price_differences)

    # 倒余额比例
    def proportion(self):
        steam_sale_price = (self.args.steam_purchase_price * self.args.default_proportion)
        steam_sale_price = round(steam_sale_price, 2)
        proportion = (self.args.buff_price / steam_sale_price)
        print("倒余额比例为: %.2f" % proportion)

    # 倒余额比例，无输出
    def proportion_no_out(self):
        steam_sale_price = (self.args.steam_purchase_price * self.args.default_proportion)
        steam_sale_price = round(steam_sale_price, 2)
        proportion = (self.args.buff_price / steam_sale_price)
        return proportion


def Calc():
    calc = Calculator()
    print("计算器带入参数为: " + str(calc.parser.parse_args()))
    print("-------------------------------")
    print("价格计算结果如下: ")
    calc.buff()                         # buff  价格
    calc.steam_sale_price()             # steam 出售价格
    calc.steam_purchase_price()         # steam 购买价格
    calc.quantity()                     # 数量
    print("--------")
    calc.total_purchase_price()         # buff 总购买所需价格
    calc.total_sales_price()            # steam 总出售获得余额
    calc.single_price_difference()      # 倒余额单个差值
    calc.total_price_differences()      # 倒余额总差值
    calc.proportion()                   # 倒余额比例
    print("-------------------------------")
    if calc.proportion_no_out() >= 1:
        print("请注意您的购买与出售价格比例，比例大于或等于 1 ，请核实您是否卖亏了！")
    elif calc.proportion_no_out() >= 0.9:
        print("您的比例看起来不太友好！请注意选择！")
    elif calc.proportion_no_out() >= 0.8:
        print("您的比例看起来一般！但可以考虑下！")
    elif calc.proportion_no_out() >= 0.7:
        print("您的比例看起来还可以！")
    elif calc.proportion_no_out() < 0.7:
        print("您的比例看起来非常不错哦！")
    print("-------------------------------")
    print("请注意: 因为小数默认2位原因，此价格可能与实际有一点点出入，会有一点点小误差！")

if __name__ == '__main__':
    print("您运行参数为: " + str(sys.argv))
    Calc()
