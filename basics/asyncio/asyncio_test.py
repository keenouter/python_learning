# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 21:08
# @Author  : G.M
# @FileName: asyncio_test.py
# @Software: PyCharm

# asyncio.run() 函数用来运行最高层级的入口点 "main()" 函数 (参见上面的示例。)
# 等待一个协程。以下代码段会在等待 1 秒后打印 "hello"，然后 再次 等待 2 秒后打印 "world":

import asyncio
import time


# async def main():
#     print('Hello ...')
#     await asyncio.sleep(4)
#     print('... World!')


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
# Python 3.7+
# asyncio.run(main())
