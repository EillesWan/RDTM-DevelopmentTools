import requests
import os
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

if items_list["status"] != "ok":
    prt(items_list)
    exit()

with open("items_list_result.json",'w',encoding="utf-8") as f:
    json.dump(items_list,f,ensure_ascii=False,indent=4)


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


item_data_list = dict(zip([item['item_id'].lower() for item in items_list['data']['item']], [{"name":item['item_name'].lower(),"data":[]} for item in items_list['data']['item']]))

# prt(item_data_list)

# 2021年1月1日以后的
get_data_url = "https://mc-launcher.webapp.163.com/data_analysis/day_detail/?platform={platform}&category={category}&start_date={start_date}&end_date={end_date}&item_list_str={item_id}&sort=dateid&order=ASC&start=0&span=999999999"
# item_id 用逗号分隔，开始与结束时间之间的间隔不得大于180

def get_data(item_id: str, progress: Progress, semaphore: threading.BoundedSemaphore):
    
    semaphore.acquire()   #加锁
    global item_data_list

    nowdate = datetime.datetime(2021,1,1)
    single_task = progress.add_task(f'[#26E2FF on #121110]正在处理 {item_data_list[item_id]["name"]}', total=(datetime.datetime.now()-nowdate).days)
    while (datetime.datetime.now()-nowdate).days > 0:
        end_date = (nowdate + datetime.timedelta(days=128))
        end_date = end_date if (datetime.datetime.now()-end_date).days > 0 else datetime.datetime.now()

        item_data: dict = requests.get(get_data_url.format(category="pe",platform=platform,item_id=item_id,start_date=nowdate.date().isoformat().replace("-",''),end_date=end_date.date().isoformat().replace("-",'')), headers=data_headers).json()
        if not item_data['status'] == 'ok':
            prt(item_data)
            exit()
        item_data_list[item_id]["data"] += item_data['data']["data"]
        progress.update(single_task, advance=(end_date-nowdate).days)
        nowdate = end_date
    progress.reset(single_task,visible=False)
    semaphore.release()     #释放


thread_pool: List[threading.Thread] = []

with Progress() as progress:
    
    total_task_start = progress.add_task('[#0089F2 on #121110]启动数据获取单元', total=len(item_data_list))
    total_task_finish = progress.add_task('[#0089F2 on #121110]数据已获取', total=len(item_data_list))
    semaphore = threading.BoundedSemaphore(limit)

    for item_id in [item['item_id'].lower() for item in items_list['data']['item']]:
        progress.update(total_task_start, advance=1)
        thread_pool.append(threading.Thread(target=get_data, args=(item_id,progress,semaphore,)))
        thread_pool[-1].start()
    
    for t in thread_pool:
        t.join()
        progress.update(total_task_finish, advance=1)

    


with open("items_data_result.json",'w',encoding="utf-8") as f:
    json.dump(item_data_list,f,ensure_ascii=False,indent=4)

prt("[#F2F4F6 on #121110]正在绘制曲线")


import matplotlib.pyplot as plt
plt.ion()
color = (18, 17, 16)

items_line_data = {}

with Progress() as progress:
    
    total_task_finish = progress.add_task('[#0089F2 on #121110]绘制数据', total=len(item_data_list))


    for item_id,item_data in item_data_list.items():
        num_array = []
        ok = False
        for i in [single_data['download_num'] for single_data in item_data_list[item_id]['data']]:
            if i:
                ok = True
            if ok:
                num_array.append(i)

        plt.plot(range(len(num_array)), [num_array[i]/(i+1) for i in range(len(num_array))], lw=1, color="#{}".format("".join(str(hex(i))[2:].rjust(2,'0') for i in color)))

        items_line_data[item_id] = {
            "name":item_data_list[item_id]['name'],
            "color":color,
            "down_array":num_array,
        }

        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

        plt.pause(0.01)
        plt.ioff()
        progress.update(total_task_finish, advance=1,)
        
        f"[#26E2FF on #121110]正在处理 "



with open("items_draw_result.json",'w',encoding="utf-8") as f:
    json.dump(items_line_data,f,ensure_ascii=False,indent=4)


plt.show()






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