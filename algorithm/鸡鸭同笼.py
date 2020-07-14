# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 17:13
# @Author  : G.M
# @FileName: 鸡鸭同笼.py
# @Software: PyCharm


def chicken_rabbit():
    try:
        foots = eval(input("请输入鸡和兔子脚的总数："))
        heads = eval(input("请输入鸡和兔子头的总数："))
        if foots % 2 != 0 and foots < 6:
            print('请重新输入鸡和兔子脚的总数>>>>')
        elif heads < 2:
            print('输入的鸡和兔子头的总数错误，请重新输入>>>>')
        else:
            chicken = 0

            while chicken < heads:
                chicken += 1
                rabbit = heads - chicken
                if foots == (chicken * 2 + rabbit * 4):
                    print("有鸡%d只,有兔子%d只" % (chicken, rabbit))

    except:
        print("能不能好好玩？！")


if __name__ == '__main__':
    chicken_rabbit()
