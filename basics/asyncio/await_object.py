# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 21:24
# @Author  : G.M
# @FileName: await_object.py
# @Software: PyCharm

import asyncio


async def nested():
    return 42


async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    # nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".


asyncio.run(main())
