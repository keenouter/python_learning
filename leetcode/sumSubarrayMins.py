# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 9:58
# @Author  : G.M
# @FileName: sumSubarrayMins.py
# @Software: PyCharm

# 给定一个整数数组 A，找到 min(B) 的总和，其中 B 的范围为 A 的每个（连续）子数组。
#
# 由于答案可能很大，因此返回答案模 10^9 + 7。

# 示例
# 输入：[3,1,2,4]
# 输出：17
# 解释：
# 子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
# 最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。


import sys
import time
import numpy as np

sys.setrecursionlimit(9000000)


def sumSubarrayMins(a_list):
    # 最直观简单的解法 时间可能会出问题
    sum_b = 0
    if not a_list:
        return 0
    for i in range(1, len(a_list) + 1):
        for j in range(len(a_list) - i + 1):
            # print(a_list[j:j + i])
            sum_b += min(a_list[j:j + i])
    return sum_b


def sumSubarrayMins_1(a_list):
    sum_b = 0
    if not a_list:
        return 0

    cur_min = 0
    for i in range(len(a_list)):
        if a_list[cur_min] > a_list[i]:
            cur_min = i
        sum_b += a_list[cur_min]
    return sum_b + sumSubarrayMins(a_list[1:])


if __name__ == '__main__':
    test = list(np.random.permutation(200))
    time_1 = time.time()
    print(sumSubarrayMins(test), time.time()-time_1)

    time_1 = time.time()
    print(sumSubarrayMins_1(test), time.time() - time_1)
