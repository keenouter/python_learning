# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 12:10
# @Author  : G.M
# @FileName: orangeRotting.py
# @Software: PyCharm


# 腐烂的橘子
# 在给定的网格中，每个单元格可以有以下三个值之一：
#
# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
# 每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
#
# 返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/rotting-oranges
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import math


class Solution:
    def orangesRotting(self, grid):
        if not grid or not grid[0]:
            return 0
        minitues = 0
        height = len(grid)
        length = len(grid[0])
        is_rotting = False
        max_minitues = math.ceil(math.sqrt(height * height + length * length))
        k = 0
        while k < max_minitues:
            is_rot = [[False] * height] * length
            for i in range(height):
                for j in range(length):
                    if grid[i][j] == 2 and not is_rot[i][j]:
                        if i + 1 <= height - 1:
                            if grid[i + 1][j] == 1:
                                grid[i + 1][j] = 2
                                is_rotting = True
                                is_rot[i + 1][j] = True
                        if i - 1 >= 0:
                            if grid[i - 1][j] == 1:
                                grid[i - 1][j] = 2
                                is_rotting = True
                                is_rot[i - 1][j] = True
                        if j - 1 >= 0:
                            if grid[i][j - 1] == 1:
                                grid[i][j - 1] = 2
                                is_rotting = True
                                is_rot[i][j - 1] = True
                        if j + 1 <= length - 1:
                            if grid[i][j + 1] == 1:
                                grid[i][j + 1] = 2
                                is_rotting = True
                                is_rot[i][j + 1] = True
            if is_rotting:
                minitues += 1
            k += 1
        return minitues


if __name__ == '__main__':
    test = [[False] * 5] * 4
    print(test)
