# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 11:03
# @Author  : G.M
# @FileName: section_sort.py
# @Software: PyCharm


def selection_sort(un_list: list) -> list:
    if not un_list:
        return un_list
    cur_min = 0
    for i in range(len(un_list)-1):
        for j in range(i, len(un_list)):
            if un_list[j] < un_list[cur_min]:
                cur_min = j
        un_list[i], un_list[cur_min] = un_list[cur_min], un_list[i]
        cur_min = i + 1

    return un_list


if __name__ == "__main__":
    a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
    print(selection_sort(a))
