# python 里面很少出现链表这种数据结构，以list实现


def reverse(my_list):
    r_list = []
    for i in range(len(my_list)):
        r_list.append(my_list[-1 - i])
    return r_list


def reverse_list(my_list, n):
    if len(my_list) <= n:
        return reverse(my_list)
    else:
        i = 0
        while i + n <= len(my_list):
            my_list[i:i + n] = reverse(my_list[i:i + n])
            i = i + n
        if i < len(my_list):
            my_list[i:len(my_list) - 1] = reverse(my_list[i:len(my_list) - 1])
        return my_list


if __name__ == "__main__":
    a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
    print(reverse_list(a, 4))
