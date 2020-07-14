# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 21:15
# @Author  : G.M
# @FileName: asyncio_create.py
# @Software: PyCharm
import time
import asyncio


# asyncio.create_task() 函数用来并发运行作为 asyncio 任务 的多个协程。
# 让我们修改以上示例，并发 运行两个 say_after 协程:

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
