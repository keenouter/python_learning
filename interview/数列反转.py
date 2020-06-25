# 单调递增数列 [1,2,3,4,5]  数列反转 如[3,4,5,1,2] ,找出数列中最小值，二分法


def find_reversal(r_list):
    start = 0
    end = len(r_list) - 1
    # 先判断数列是否反转，没有反转，第一个就是最小值
    if r_list[end] > r_list[start]:
        return start

    median = int((start + end) / 2)

    while True:
        if r_list[median] < r_list[median - 1]:
            break
        if r_list[median] < r_list[start]:
            end = median
            median = int((start + end) / 2)
        elif r_list[median] > r_list[end]:
            start = median
            median = int((start + end) / 2)
    return median


if __name__ == "__main__":
    my_list = [1, 2, 3]
    print(my_list[find_reversal(my_list)])
