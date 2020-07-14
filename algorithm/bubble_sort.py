# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 10:46
# @Author  : G.M
# @FileName: bubble_sort.py
# @Software: PyCharm


# noinspection PyMethodMayBeStatic
class Algorithm(object):
    def __init__(self):
        pass

    def bubble_sort(self, un_list: list) -> list:
        if not un_list:
            return un_list
        for j in range(len(un_list) - 1):
            for i in range(len(un_list) - 1 - j):
                if un_list[i] > un_list[i + 1]:
                    un_list[i], un_list[i + 1] = un_list[i + 1], un_list[i]
        return un_list


if __name__ == '__main__':
    test = [1, 2, 3, 1, 5, 1, 5, 6, 110, 10, 11]
    print(Algorithm().bubble_sort(test))
