def find_reversal(r_list):
    start = 0
    end = len(r_list) - 1
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
    my_list = [4, 5, 1, 2, 3]
    print(my_list[find_reversal(my_list)])
