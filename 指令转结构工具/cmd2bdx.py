# -*- coding: utf-8 -*-

"""
Copyright 2022 Team-Ryoun
"""


import os
import math
import brotli


'''声明：
此文件中
函数 `__formCMDblk`、`__fillSquareSideLength` 直接拷贝自 音·创库版本
函数 `toBDXfile`、`formatipt` 拷贝并修改自 音·创库版本

音·创 库版本代码仓库地址为：
https://gitee.com/EillesWan/Musicreater/tree/pkgver/

本程序依照 Apache2.0 协议标明其作者，并附源协议文件位于 `./MSCTpkgver LICENSE.md`
'''


def __formCMDblk(
    self,
    command: str,
    particularValue: int,
    impluse: int = 0,
    condition: bool = False,
    needRedstone: bool = True,
    tickDelay: int = 0,
    customName: str = "",
    executeOnFirstTick: bool = False,
    trackOutput: bool = True,
):
    """
    使用指定项目返回指定的指令方块放置指令项
    :param command: `str`
        指令
    :param particularValue:
        方块特殊值，即朝向
            :0	下	无条件
            :1	上	无条件
            :2	z轴负方向	无条件
            :3	z轴正方向	无条件
            :4	x轴负方向	无条件
            :5	x轴正方向	无条件
            :6	下	无条件
            :7	下	无条件

            :8	下	有条件
            :9	上	有条件
            :10	z轴负方向	有条件
            :11	z轴正方向	有条件
            :12	x轴负方向	有条件
            :13	x轴正方向	有条件
            :14	下	有条件
            :14	下	有条件
        注意！此处特殊值中的条件会被下面condition参数覆写
    :param impluse: `int 0|1|2`
        方块类型
            0脉冲 1循环 2连锁
    :param condition: `bool`
        是否有条件
    :param needRedstone: `bool`
        是否需要红石
    :param tickDelay: `int`
        执行延时
    :param customName: `str`
        悬浮字
    lastOutput: `str`
        上次输出字符串，注意此处需要留空
    :param executeOnFirstTick: `bool`
        执行第一个已选项(循环指令方块是否激活后立即执行，若为False，则从激活时起延迟后第一次执行)
    :param trackOutput: `bool`
        是否输出

    :return:str
    """
    block = b"\x24" + particularValue.to_bytes(2, byteorder="big", signed=False)

    for i in [
        impluse.to_bytes(4, byteorder="big", signed=False),
        bytes(command, encoding="utf-8") + b"\x00",
        bytes(customName, encoding="utf-8") + b"\x00",
        bytes("", encoding="utf-8") + b"\x00",
        tickDelay.to_bytes(4, byteorder="big", signed=True),
        executeOnFirstTick.to_bytes(1, byteorder="big"),
        trackOutput.to_bytes(1, byteorder="big"),
        condition.to_bytes(1, byteorder="big"),
        needRedstone.to_bytes(1, byteorder="big"),
    ]:
        block += i
    return block


def __fillSquareSideLength(self, total: int, maxHeight: int):
    """给定总方块数量和最大高度，返回所构成的图形外切正方形的边长
    :param total: 总方块数量
    :param maxHeight: 最大高度
    :return: 外切正方形的边长 int"""
    return math.ceil(math.sqrt(math.ceil(total / maxHeight)))


def toBDXfile(
    commands: list,
    author: str = "Eilles",
    maxheight: int = 64,
    outfile: str = "./test.bdx",
):
    """
    :param author: 作者名称
    :param maxheight: 生成结构最大高度
    :return 成功与否，成功返回(True,未经过压缩的源,结构占用大小)，失败返回(False,str失败原因)
    """

    outputPath = os.path.dirname(outfile)
    if not os.path.exists(outputPath):
        os.makedirs(outputPath)

    with open(
        outfile,
        "w+",
    ) as f:
        f.write("BD@")

    _bytes = (
        b"BDX\x00" + author.encode("utf-8") + b" & Musicreater\x00\x01command_block\x00"
    )

    key = {
        "x": (b"\x0f", b"\x0e"),
        "y": (b"\x11", b"\x10"),
        "z": (b"\x13", b"\x12"),
    }
    """key存储了方块移动指令的数据，其中可以用key[x|y|z][0|1]来表示xyz的减或增"""
    x = "x"
    y = "y"
    z = "z"

    _sideLength = __fillSquareSideLength(len(commands), maxheight)

    yforward = True
    zforward = True

    nowy = 0
    nowz = 0
    nowx = 0

    for cmd in commands:
        _bytes += __formCMDblk(
            cmd,
            (1 if yforward else 0)
            if (
                ((nowy != 0) and (not yforward))
                or ((yforward) and (nowy != (maxheight - 1)))
            )
            else (3 if zforward else 2)
            if (
                ((nowz != 0) and (not zforward))
                or ((zforward) and (nowz != _sideLength))
            )
            else 5,
            impluse=2,
            condition=False,
            needRedstone=False,
            tickDelay=0,
            customName="",
            executeOnFirstTick=False,
            trackOutput=True,
        )

        nowy += 1 if yforward else -1

        if ((nowy >= maxheight) and (yforward)) or ((nowy < 0) and (not yforward)):
            nowy -= 1 if yforward else -1

            yforward = not yforward

            nowz += 1 if zforward else -1

            if ((nowz > _sideLength) and (zforward)) or ((nowz < 0) and (not zforward)):
                nowz -= 1 if zforward else -1
                zforward = not zforward
                _bytes += key[x][1]
                nowx += 1
            else:

                _bytes += key[z][int(zforward)]

        else:

            _bytes += key[y][int(yforward)]

    with open(
        outfile,
        "ab+",
    ) as f:
        f.write(brotli.compress(_bytes + b"XE"))

    return (True, (nowx, maxheight, _sideLength))


def formatipt(notice: str, fun, errnote: str = "", *extraArg):
    '''循环输入，以某种格式
    notice: 输入时的提示
    fun: 格式函数
    errnote: 输入不符格式时的提示
    *extraArg: 对于函数的其他参数'''
    while True:
        result = input(notice)
        try:
            funresult = fun(result, *extraArg)
            break
        except:
            print(errnote)
            continue
    return result, funresult


path = formatipt("请输入函数文件地址：", os.path.isfile, "地址无效，请重新输入")[0]

# 用双换行分割每段
functions = open(path, 'r', encoding="utf-8").read().split("\n\n")

# 单换行分每行
functionList = [[j for j in i.split("\n")] for i in functions]


toBDXfile(
    functionList,
    input("请输入作者："),
    formatipt("请输入生成结构的最大高度：", int, "输入数据应为数字。")[1],
    path[: len(path) - path[::-1].find('.')] + 'bdx',
)
# print(functionList)
