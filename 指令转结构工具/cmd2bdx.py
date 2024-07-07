# -*- coding: utf-8 -*-

"""
注意，此文件未经允许不得商用

此文件中
部分函数拷贝或修改自 音·创 的 utils.py https://gitee.com/TriM-Organization/Musicreater/blob/master/Musicreater/utils.py
音·创 库版本代码仓库地址为：
https://gitee.com/EillesWan/Musicreater/tree/pkgver/

本程序依照 Apache2.0 协议标明其作者，源协议文件位于 `https://gitee.com/TriM-Organization/Musicreater/blob/pkgver/LICENSE.md`
引用协议：

版权所有 © 2023 音·创 开发者
Copyright © 2023 all the developers of Musicreater

   Licensed under the Apache License, Version 2.0
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

继承协议：

Copyright 2022 Team-Ryoun: 金羿("Eilles Wan")

   Licensed under the Apache License, Version 2.0
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

"""


import os
import brotli


key = {
    "x": [b"\x0f", b"\x0e", b"\x1c", b"\x14", b"\x15"],
    "y": [b"\x11", b"\x10", b"\x1d", b"\x16", b"\x17"],
    "z": [b"\x13", b"\x12", b"\x1e", b"\x18", b"\x19"],
}
"""key存储了方块移动指令的数据，其中可以用key[x|y|z][0|1]来表示xyz的减或增
而key[][2+]是用来增加指定数目的"""

x = "x"
y = "y"
z = "z"


def move(axis: str, value: int):
    if value == 0:
        return b""
    if abs(value) == 1:
        return key[axis][0 if value == -1 else 1]

    pointer = sum(
        [
            1 if i else 0
            for i in (
                value != -1,
                value < -1 or value > 1,
                value < -128 or value > 127,
                value < -32768 or value > 32767,
            )
        ]
    )

    return key[axis][pointer] + value.to_bytes(2 ** (pointer - 2), "big", signed=True)


def formCMDblk(
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


axisParticularValue = {
    x: {
        True: 5,
        False: 4,
    },
    y: {
        True: 1,
        False: 0,
    },
    z: {
        True: 3,
        False: 2,
    },
}


def anti(axis: str):
    return z if axis == x else x


def goahead(forward: bool):
    return 1 if forward else -1


def toLineBDXbytes(
    commands: list,
    axis: str,
    forward: bool,
    limit: int = 128,
):
    _bytes = b""
    nowf = True
    nowgo = 0
    for cmd, condition, note in commands:
        is_point = ((nowgo != 0) and (not nowf)) or (nowf and (nowgo != (limit - 1)))
        _bytes += formCMDblk(
            cmd,
            axisParticularValue[axis][not forward ^ nowf]
            if is_point
            else axisParticularValue[anti(axis)][True],
            impluse=2,
            condition=condition,
            needRedstone=False,
            tickDelay=0,
            customName=note,
            executeOnFirstTick=False,
            trackOutput=True,
        )
        nowgo += goahead(nowf)

        if ((nowgo >= limit) and nowf) or ((nowgo < 0) and (not nowf)):
            nowgo -= goahead(nowf)

            nowf = not nowf

            _bytes += move(anti(axis), 1)

        else:
            _bytes += move(axis, goahead(not forward ^ nowf))
    
    _bytes += move(axis, goahead(forward ^ nowf)*nowgo)

    return _bytes


def toLineBDXfile(
    funcList: list,
    axis_: str,
    forward_: bool,
    limit_: int = 128,
    author: str = "Eilles",
    outfile: str = "./test.bdx",
):
    """
    Parameters
    ----------
    funcList: list
        指令集列表： 指令系统[  指令集[  单个指令( str指令, bool条件性 ),  ],  ]
    axis_: str
        坐标增值方向，只能是小写的 `x`,`y`,`z`
    forward_: bool
        是否沿着坐标轴的正方向
    limit_: int
        在延展方向上的长度限制
    author: str
        作者名称
    outfile: str
        输出文件

    Returns
    -------
        成功与否，指令总长度，指令结构总大小
    """

    with open(os.path.abspath(outfile), "w+", encoding="utf-8") as f:
        f.write("BD@")

    _bytes = (
        b"BDX\x00"
        + author.encode("utf-8")
        + b" & Team-Ryoun: BDX Generator\x00\x01command_block\x00"
    )
    totalSize = {x: 0, y: 1, z: 0}
    totalLen = 0

    # 非链延展方向，即系统延展方向
    antiaxis = anti(axis_)

    while funcList:
        func = funcList.pop(0)

        nowlen = len(func)

        totalLen += nowlen

        # 走一条链的指令方块，会自动复位
        _bytes += toLineBDXbytes(func, axis_, forward_, limit_)

        # 不是最后一组
        if funcList:
            # 计算系统延展方向的长度
            totalSize[antiaxis] += 2 + nowlen // limit_

            if totalSize[antiaxis] + 2 <= limit_:
                # 没到头，那就 向前走两步？
                _bytes += move(antiaxis, 2)
            else:
                # 到头了，那就退回去？
                _bytes += move("y", 2)
                _bytes += move(antiaxis, -totalSize[antiaxis])

            # _bytes += move(axis_, -len(func))

        else:
            totalSize[antiaxis] += 1 + nowlen // limit_

        # 计算链延展方向的长度
        totalSize[axis_] = min(max(totalSize[axis_], nowlen), limit_)

    with open(
        os.path.abspath(outfile),
        "ab+",
    ) as f:
        f.write(brotli.compress(_bytes + b"XE"))

    return (True, totalLen, list(totalSize.values()))


def formatipt(notice: str, fun, errnote: str = "", *extraArg):
    """循环输入，以某种格式
    notice: 输入时的提示
    fun: 格式函数
    errnote: 输入不符格式时的提示
    *extraArg: 对于函数的其他参数"""
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
# 单换行分每行
cdt = False
note = ""
functionList = []
for lines in open(path, "r", encoding="utf-8").read().split("\n\n"):
    funcGroup = []
    for line in lines.split("\n"):
        if line.strip().startswith("#"):
            if "cdt" in line.lower():
                cdt = True
            note = line[1:].replace("cdt", "").strip()
        else:
            if "#" not in line:
                funcGroup.append((line, cdt, note))
            else:
                funcGroup.append(
                    (
                        line[: line.find("#")].strip(),
                        cdt,
                        line[line.find("#") + 1 :].strip() + note,
                    )
                )
            cdt = False
            note = ""
    functionList.append(funcGroup)

# print(functionList)


def isinXYZ(sth):
    if len(sth) == 2 and sth.lower()[0] in (x, y, z) and sth[1] in ("-", "+"):
        return (sth.lower()[0], True if sth[1] == "+" else False)
    else:
        raise


toLineBDXfile(
    functionList,
    *(formatipt("请输入生成结构的生成方向(如x+、z-等)：", isinXYZ, "输入数据应符合 轴+正负符号 的格式。")[1]),
    formatipt("请输入长度限制：", int, "请输入数字，即您希望生成结构的最大延展长度。")[1],
    input("请输入作者："),
    path[: len(path) - path[::-1].find(".")] + "bdx",
)
# print(functionList)
