# 大体的思路，二分法，先找到整个数组里最高的点，然后依此再找左边的最高点，依次左边向左，右边向右


def my_trap(heights):
    water_sum = 0
    left_max = right_max = get_max(heights)

    # 左边只往左走
    l_max = get_max(heights[:left_max])

    while l_max >= 0:
        for i in heights[l_max + 1:left_max]:
            water_sum = water_sum + (heights[l_max] - i)
        left_max = l_max
        if l_max == 0:
            break
        l_max = get_max(heights[:left_max])

    # 右边往右走
    r_max = right_max + get_max(heights[right_max + 1:]) + 1

    while r_max <= len(heights) - 1:
        for i in heights[right_max + 1:r_max]:
            water_sum = water_sum + (heights[r_max] - i)
        right_max = r_max
        if r_max == len(heights) - 1:
            break
        r_max = right_max + get_max(heights[right_max + 1:]) + 1

    return water_sum


def get_max(heights):
    height_max = 0
    if heights:
        for i in range(len(heights)):
            if heights[i] >= heights[height_max]:
                height_max = i
    return height_max


if __name__ == '__main__':
    a = [3, 3, 2, 4, 2, 1, 9, 3, 1, 6, 4, 2, 1, 5]
    print(my_trap(a))
