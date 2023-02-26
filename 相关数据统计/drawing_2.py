

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
 
def func(x,w,h,k,a,b,c):#需要拟合的函数
    return np.exp(k*(a*np.sin(x+c)+b)/(x+w)+h)


import json
import threading
from rich.console import Console
from rich.progress import Progress
from typing import Any, Optional, TextIO, Literal, List

JustifyMethod = Literal["default", "left", "center", "right", "full"]
OverflowMethod = Literal["fold", "crop", "ellipsis", "ignore"]



MainConsole = Console()



def prt(
    *objects: Any,
    sep: str = " ",
    end: str = "\n",
    justify: Optional[JustifyMethod] = None,
    overflow: Optional[OverflowMethod] = None,
    no_wrap: Optional[bool] = None,
    emoji: Optional[bool] = None,
    markup: Optional[bool] = None,
    highlight: Optional[bool] = None,
    width: Optional[int] = None,
    height: Optional[int] = None,
    crop: bool = True,
    soft_wrap: Optional[bool] = None,
    new_line_start: bool = False,
) -> None:
    """打印到控制台。

    Args:
        objects (位置性的args): 要记录到终端的对象。
        sep (str, 可选): 要在打印数据之间写入的字符串。默认为""。
        end (str, optio可选nal): 在打印数据结束时写入的字符串。默认值为"\\\\n"。
        style (Union[str, Style], 可选): 应用于输出的样式。默认为`None`。
        justify (str, 可选): 校正位置，可为"default", "left", "right", "center" 或 "full". 默认为`None`。
        overflow (str, 可选): 控制溢出："ignore"忽略, "crop"裁剪, "fold"折叠, "ellipsis"省略号。默认为`None`。
        no_wrap (Optional[bool], 可选): 禁用文字包装。默认为`None`。
        emoji (Optional[bool], 可选): 启用表情符号代码，或使用控制台默认的`None`。默认为`None`。
        markup (Optional[bool], 可选): 启用标记，或`None`使用控制台默认值。默认为`None`。
        highlight (Optional[bool], 可选): 启用自动高亮，或`None`使用控制台默认值。默认为`None`。
        width (Optional[int], 可选): 输出的宽度，或`None`自动检测。默认为`None`。
        crop (Optional[bool], 可选): 裁剪输出到终端的宽度。默认为`True`。
        soft_wrap (bool, 可选): 启用软包装模式，禁止文字包装和裁剪，或`None``用于 控制台默认值。默认为`None`。
        new_line_start (bool, False): 如果输出包含多行，在开始时插入一个新行。默认值为`False`。
    """
    MainConsole.print(
        *objects,
        sep=sep,
        end=end,
        style="#F0F2F4 on #121110",
        justify=justify,
        overflow=overflow,
        no_wrap=no_wrap,
        emoji=emoji,
        markup=markup,
        highlight=highlight,
        width=width,
        height=height,
        crop=crop,
        soft_wrap=soft_wrap,
        new_line_start=new_line_start,
    )

def ipt(
    *objects: Any,
    sep: str = " ",
    justify: Optional[JustifyMethod] = None,
    overflow: Optional[OverflowMethod] = None,
    no_wrap: Optional[bool] = None,
    emoji: Optional[bool] = None,
    markup: Optional[bool] = None,
    highlight: Optional[bool] = None,
    width: Optional[int] = None,
    height: Optional[int] = None,
    crop: bool = True,
    soft_wrap: Optional[bool] = None,
    new_line_start: bool = False,
    password: bool = False,
    stream: Optional[TextIO] = None,
) -> str:
    """显示一个提示并等待用户的输入。

    它的工作方式与Python内建的 :func:`ipt` 函数相同，如果Python内建的 :mod:`readline` 模块先前已经加载，则提供详细的行编辑和历史功能。

    Args:
        objects (位置性的args): 要记录到终端的对象。
        sep (str, 可选): 要在打印数据之间写入的字符串。默认为""。
        end (str, optio可选nal): 在打印数据结束时写入的字符串。默认值为"\\\\n"。
        style (Union[str, Style], 可选): 应用于输出的样式。默认为`None`。
        justify (str, 可选): 校正位置，可为"default", "left", "right", "center" 或 "full". 默认为`None`。
        overflow (str, 可选): 控制溢出："ignore"忽略, "crop"裁剪, "fold"折叠, "ellipsis"省略号。默认为`None`。
        no_wrap (Optional[bool], 可选): 禁用文字包装。默认为`None`。
        emoji (Optional[bool], 可选): 启用表情符号代码，或使用控制台默认的`None`。默认为`None`。
        markup (Optional[bool], 可选): 启用标记，或`None`使用控制台默认值。默认为`None`。
        highlight (Optional[bool], 可选): 启用自动高亮，或`None`使用控制台默认值。默认为`None`。
        width (Optional[int], 可选): 输出的宽度，或`None`自动检测。默认为`None`。
        crop (Optional[bool], 可选): 裁剪输出到终端的宽度。默认为`True`。
        soft_wrap (bool, 可选): 启用软包装模式，禁止文字包装和裁剪，或`None``用于 控制台默认值。默认为`None`。
        new_line_start (bool, False): 如果输出包含多行，在开始时插入一个新行。默认值为`False`。
        password (bool, 可选): 隐藏已经输入的文案，默认值为`False`。
        stream (TextIO, 可选): 可选从文件中读取（而非控制台），默认为 `None`。

    Returns:
        str: 从stdin读取的字符串
    """
    MainConsole.print(
        *objects,
        sep=sep,
        end="",
        style="#F0F2F4 on #121110",
        justify=justify,
        overflow=overflow,
        no_wrap=no_wrap,
        emoji=emoji,
        markup=markup,
        highlight=highlight,
        width=width,
        height=height,
        crop=crop,
        soft_wrap=soft_wrap,
        new_line_start=new_line_start,
    )

    return MainConsole.input("", password=password, stream=stream)


limit = 8

with open("items_draw_result.json",'r',encoding="utf-8") as f:
    item_draw_list: dict = json.load(f,)

prt("[#F2F4F6 on #121110]正在绘制曲线")


plt.ion()

with Progress() as progress:
    
    total_task_finish = progress.add_task('[#0089F2 on #121110]绘制数据', total=len(item_draw_list))


    for item_id,item_data in item_draw_list.items():
        
        # single_data = [i-item_data['down_array'][item_data['down_array'].index(i)-1] if not item_data['down_array'].index(i) == 0 else i for i in item_data['down_array'][:-1]]
        # single_data = item_data['down_array'][:-1]
        single_data = [i/(item_data['down_array'].index(i)+1) for i in item_data['down_array'][:-1]]
        if len(single_data) <= 3:
            progress.update(total_task_finish, advance=1,)
            continue
        x0 = list(range(len(single_data)))
        y0 = single_data.copy()

        # prt(x0,y0)

        try:
            funcArg, maparray= optimize.curve_fit(func, x0, y0, maxfev=131072)
        except TypeError:
            progress.update(total_task_finish, advance=1,)
            continue
        except RuntimeError as E:
            prt(f"\n数据错误 {E}\n\t{y0}")
            progress.update(total_task_finish, advance=1,)
            continue

        w4, h4, k4, a4, b4, c4 = funcArg
        x4 = np.arange(0, len(single_data), 1)
        y4 = np.exp(k4*(a4*np.sin(x4+c4)+b4)/(x4+w4)+h4)

        for i in y4:
            if i > 5 * max(y0):
                prt(f"\n拟合错误{y0}\n\t{y4}")
                progress.update(total_task_finish, advance=1,)
                continue

        plt.plot(x0[:], y0[:], 1.5, color="#{}".format("".join(str(hex(i))[2:].rjust(2,'0') for i in item_data['color'])))
        plt.scatter(x0[:], y0[:], 3, color="#{}".format("".join(str(hex(i))[2:].rjust(2,'0') for i in item_data['color'])))
        # plt.scatter(25, 25, 25, "red")
        plt.plot(x4, y4, 1, color="#{}".format("".join(str(hex((i+32) % 0xFF))[2:].rjust(2,'0') for i in item_data['color'])))

        plt.pause(0.01)
        plt.ioff()
        progress.update(total_task_finish, advance=1,)
        
        f"[#26E2FF on #121110]正在处理 {item_draw_list[item_id]['name']}"




plt.show()