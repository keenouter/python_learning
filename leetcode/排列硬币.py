# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 14:18
# @Author  : G.M
# @FileName: 排列硬币.py
# @Software: PyCharm

# 你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。
#
# 给定一个数字 n，找出可形成完整阶梯行的总行数。
#
# n 是一个非负整数，并且在32位有符号整型的范围内。
#
# 示例 1:
#
# n = 5
#
# 硬币可排列成以下几行:
# ¤
# ¤ ¤
# ¤ ¤
#
# 因为第三行不完整，所以返回2.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/arranging-coins
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        m = int(math.sqrt(2 * n))
        m_sum = (m * m + m) / 2
        if n - m_sum >= 0:
            return m
        if n - m_sum < 0:
            return m - 1


if __name__ == '__main__':
    for i in range(1, 20):
        print(i, Solution().arrangeCoins(i))
