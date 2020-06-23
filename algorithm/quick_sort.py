# 快速排序

# 1、不计内存占用

import time
from functools import wraps


def fn_timer(function):
     @wraps(function)
     def function_timer(*args, **kwargs):
         t0=time.time()
         result = function(*args, **kwargs)
         t1=time.time()
         print("算法%s 执行占用时间:%s" %(function.__name__,str(t1-t0)))
         return result
     return function_timer



@fn_timer
def quick_sort(list):
    if not list:
        return []
    else:
        pivot = list[0]
        lower = [x for x in list[1:] if x < pivot]
        higher = [x for x in list[1:] if x >= pivot]
        return quick_sort(lower) + [pivot] + quick_sort(higher)


if __name__ == "__main__":
    a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
    print(quick_sort(a))
