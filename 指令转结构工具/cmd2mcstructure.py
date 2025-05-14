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

Copyright 2023 Team-Ryoun: 金羿("Eilles Wan")

   Licensed under the Apache License, Version 2.0
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

"""


import os
from TrimMCStruct import Structure, Block, TAG_Long, TAG_Byte

x = "x"
y = "y"
z = "z"


def form_command_block_in_NBT_struct(
    command: str,
    coordinate: tuple,
    particularValue: int,
    impluse: int = 0,
    condition: bool = False,
    alwaysRun: bool = True,
    tickDelay: int = 0,
    customName: str = "",
    executeOnFirstTick: bool = False,
    trackOutput: bool = True,
):
    """
    使用指定项目返回指定的指令方块结构
    :param command: `str`
        指令
    :param coordinate: `tuple[int,int,int]`
        此方块所在之相对坐标
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
    :param alwaysRun: `bool`
        是否始终执行
    :param tickDelay: `int`
        执行延时
    :param customName: `str`
        悬浮字
    :param executeOnFirstTick: `bool`
        首刻执行(循环指令方块是否激活后立即执行，若为False，则从激活时起延迟后第一次执行)
    :param trackOutput: `bool`
        是否输出

    :return:str
    """

    return Block(
        "minecraft",
        "command_block"
        if impluse == 0
        else ("repeating_command_block" if impluse == 1 else "chain_command_block"),
        states={"conditional_bit": condition, "facing_direction": particularValue},
        extra_data={
            "block_entity_data": {
                "Command": command,
                "CustomName": customName,
                "ExecuteOnFirstTick": executeOnFirstTick,
                "LPCommandMode": 0,
                "LPCondionalMode": False,
                "LPRedstoneMode": False,
                "LastExecution": TAG_Long(0),
                "LastOutput": "",
                "LastOutputParams": [],
                "SuccessCount": 0,
                "TickDelay": tickDelay,
                "TrackOutput": trackOutput,
                "Version": 25,
                "auto": alwaysRun,
                "conditionMet": False,  # 是否已经满足条件
                "conditionalMode": condition,
                "id": "CommandBlock",
                "isMovable": True,
                "powered": False,  # 是否已激活
                "x": coordinate[0],
                "y": coordinate[1],
                "z": coordinate[2],
            } # type: ignore
        },
        compability_version=17959425,
    )


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




def to_structure_lines(
    funcList: list,
    axis_: str,
    forward_: bool,
    limit: int = 100,
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
    limit: int
        在延展方向上的长度限制
    
    Returns
    -------
        成功与否，指令结构总大小
    """

    struct_size = {
        x: 0,
        y: 1,
        z: 0,
    }

    max_length = max([len(i) for i in funcList])

    struct_size[axis_] = max_length
    struct_size[x if axis_ == z else z] = len(funcList) * 2
    struct = Structure([i for i in struct_size.values()]) # type: ignore
    now_pos = {x: 1, y: 1, z: 1} if forward_ else struct_size.copy()
    for func in funcList:
        now_pos[axis_] = 1 if forward_ else max_length
        for cmd, cdt in func:
            actually_pos = [i - 1 for i in now_pos.values()]
            struct.set_block(
                actually_pos,# type: ignore
                form_command_block_in_NBT_struct(
                    command=cmd,
                    coordinate= actually_pos,# type: ignore
                    particularValue=axisParticularValue[axis_][forward_],
                    impluse=2,
                    condition=cdt,
                ),
            )
            now_pos[axis_] += 1 if forward_ else -1
        now_pos[x if axis_ == z else z] += 2 if forward_ else -2

    return struct, [i for i in struct_size.values()]


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
functionList = []
for lines in open(path, "r", encoding="utf-8").read().split("\n\n"):
    funcGroup = []
    for line in lines.split("\n"):
        if line.strip().startswith("#"):
            if "cdt" in line.lower():
                cdt = True
        else:
            funcGroup.append((line, cdt))
            cdt = False
    functionList.append(funcGroup)

# print(functionList)


def isinXYZ(sth):
    if len(sth) == 2 and sth.lower()[0] in (x, y, z) and sth[1] in ("-", "+"):
        return (sth.lower()[0], True if sth[1] == "+" else False)
    else:
        raise


struct, size = to_structure_lines(
    functionList,
    *(formatipt("请输入生成结构的生成方向(如x+、z-等)：", isinXYZ, "输入数据应符合 轴+正负符号 的格式。")[1]),
)

with open(path[: len(path) - path[::-1].find(".")] + "mcstructure",'wb') as f:
    struct.dump(f)

print("文件已保存，结构大小：",size)


# print(functionList)
