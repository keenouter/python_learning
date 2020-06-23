## python 里面很少出现链表这种数据结构，以list实现

def reverse(list):
    reverse_list = []
    for i in range(len(list)):
        reverse_list.append(list[-1-i])
    return reverse_list

def reverse_list(list,n):
    if len(list)<=n:
        return reverse(list)
    else:
        i=0
        while i+n<=len(list):
            list[i:i+n]=reverse(list[i:i+n])
            i=i+n
        if i <len(list):
            list[i:len(list)-1]=reverse(list[i:len(list)-1])
        return list


if __name__ == "__main__":
    a= [4, 65, 2, -31, 0, 99, 83, 782, 1]
    print(reverse_list(a,4))