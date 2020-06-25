# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 9:07
# @Author  : GuoMin
# @FileName: 股票最大收益.py
# @Software: PyCharm


# 数列存储时间序列股票价格，交易一次的最大收益

def max_return(price_list):
    if not price_list:
        return 0
    current_min_price_index = 0
    m_return = 0

    for i in range(len(price_list)):
        cur_return = price_list[i] - price_list[current_min_price_index]
        if cur_return > m_return:
            m_return = cur_return

        if price_list[i] < price_list[current_min_price_index]:
            current_min_price_index = i

    return m_return


def main():
    test_list = [2, 1, 4, 4, 5, 10, 4, 6, 3, 5, 10, 15, 10]
    print(max_return(test_list))


if __name__ == '__main__':
    main()
