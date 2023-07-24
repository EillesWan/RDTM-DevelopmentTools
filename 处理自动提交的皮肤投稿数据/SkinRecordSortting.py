import requests
import os,shutil
import datetime
import json
import threading
import random
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




cookie = ipt("Cookie: ",password=True)
if os.path.isfile(cookie):
    cookie = open(cookie, "r").read()
else:
    cookie = cookie


base_dataFolder = ipt("数据存储目录：")

base_folder_list = {}

for dirname in os.listdir(base_dataFolder):
    if "（" in dirname:
        base_folder_list[dirname.lower()[:len(dirname)-dirname[::-1].index("（")-1]] = os.path.join(base_dataFolder, dirname)


category = "pe"
limit = 16




if category == "pe":
    platform = "pe"
elif category == "comp":
    platform = "pc"

# category 可以是 comp 和 pe
# platform 可以是 pc 和 pe


data_headers = {
    "Host": "mc-launcher.webapp.163.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Origin": "https://mcdev.webapp.163.com",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://mcdev.webapp.163.com/",
    "Cookie": cookie,
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "TE": "trailers"
}



get_items_url = "https://mc-launcher.webapp.163.com/items/categories/{category}/?start=0&span=999999999"


items_list: dict = requests.get(get_items_url.format(category="pe"), headers=data_headers).json()
pc_items_list: dict = requests.get(get_items_url.format(category="comp"), headers=data_headers).json()

if items_list["status"] != "ok":
    prt(items_list)
    exit()

with open("items_list_result.json",'w',encoding="utf-8") as f:
    json.dump(items_list,f,ensure_ascii=False,indent=4)

with open("pc_items_list_result.json",'w',encoding="utf-8") as f:
    json.dump(pc_items_list,f,ensure_ascii=False,indent=4)


# status 商品状态:
#   reject:未过审  online:已上架  init:待提审  accept:已过审
# ori_weak_offline 弱下架状态
#   true || false

statistic = [(item['status'].lower() if not item['ori_weak_offline'] else "off_line") for item in items_list['data']['item']]

MainConsole.rule(title="[bold #AB70FF]统计", characters="=", style="#26E2FF")

from rich.table import Table
table = Table()
table.add_column('[bold #F2F4F6]项目')
table.add_column('[bold #F2F4F6]信息')
table.add_row('[bold #F2F4F6]商品总数', f'{items_list["data"]["count"]}')
table.add_row('[bold #F2F4F6]在线商品总数', f'{statistic.count("online")}')
table.add_row('[bold #F2F4F6]未过审商品总数', f'{statistic.count("reject")}')
table.add_row('[bold #F2F4F6]弱下架商品总数', f'{statistic.count("off_line")}')
MainConsole.print(table)

MainConsole.rule(title="", characters="=", style="#26E2FF")


item_statuts_list = dict([(item['item_name'].lower(),(item['status'].lower() if not item['ori_weak_offline'] else "off_line"),) for item in items_list['data']['item']])

pc_item_statuts_list = dict([(item['item_name'].lower(),(item['status'].lower() if not item['ori_weak_offline'] else "off_line"),) for item in pc_items_list['data']['item']])



MainConsole.rule(title="[bold #AB70FF]移动端组件操作中", characters="=", style="#26E2FF")

ori_delt = set()

for name, stt in item_statuts_list.items():
    name_ = name.replace("?","？").replace(":","：")
    if name_ in base_folder_list.keys():
        prt(f"\t++正在移动 {name_}")
        if not os.path.exists(f"./{stt}/"):
            os.makedirs(f"./{stt}/")
        try:
            shutil.copytree(base_folder_list[name_],f"./{stt}/{os.path.split(base_folder_list[name_])[-1]}")
            # shutil.move(base_folder_list[name],"./DELT/")
            ori_delt.add(base_folder_list[name_])
        except Exception as E:
            prt(f"\n\nERROR 操作{base_folder_list[name_]}发生错误：{E}\n\n")
    else:
        prt(name_,"非目录文件。")

MainConsole.rule(title="[bold #AB70FF]主机端组件操作中", characters="=", style="#26E2FF")


for name, stt in pc_item_statuts_list.items():
    name_ = name.replace("?","？").replace(":","：")
    if name_ in base_folder_list.keys():
        prt(f"\t++正在移动 {name_}")
        if not os.path.exists(f"./pc-{stt}/"):
            os.makedirs(f"./pc-{stt}/")
        try:
            shutil.copytree(base_folder_list[name_],f"./pc-{stt}/{os.path.split(base_folder_list[name_])[-1]}")
            # shutil.move(base_folder_list[name],"./DELT/")
            ori_delt.add(base_folder_list[name_])
        except Exception as E:
            prt(f"\n\nERROR 操作{base_folder_list[name_]}发生错误：{E}\n\n")
    else:
        prt(name_,"非目录文件。")

for i in ori_delt:
    shutil.move(i,"./DELT/")


# {
#     "DAU": ,                            # 日活
#     "cnt_buy": ,                        # 新增购买
#     "dateid": "",                   # 日期
#     "diamond": 0,                           # 当日钻石收入
#     "download_num": ,                # 下载总下载数
#     "iid": "",           # 组件ID
#     "platform": "PE",                       # 平台
#     "points": 0,                            # 当日绿宝石收入
#     "res_name": "",                 # 组件名称
#     "upload_time": "2022-01-18 17:49:11"    # 组件上传日期
# },

