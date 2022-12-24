# -*- coding: utf-8 -*-

"""

   Copyright 2022 Team-Ryoun

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

"""


import json
import os
import shutil
import sys
import zipfile
import random

from rich.console import Console
from typing import Any, Optional, TextIO, Literal

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







def unzip(zipFile, targetDirection):
    if not os.path.exists(targetDirection):
        os.makedirs(targetDirection)
    fz = zipfile.ZipFile(zipFile, "r")
    for file in fz.namelist():
        fz.extract(file, targetDirection)


try:
    file = sys.argv[1]
    unzip(sys.argv[2], "./temp/")
except IndexError:
    file = ""
    zipf = ""
    prt("先excel再zip")
    while not (os.path.exists(file) and os.path.exists(zipf)):
        file, zipf = ipt().split(" ")
    unzip(zipf, "./temp/")


# 导入xlwings模块
import xlwings as xw

# 打开Excel程序，默认设置：程序不可见，只打开不新建工作薄
app = xw.App(visible=False, add_book=False)
app.display_alerts = False

# 文件位置：filepath，打开test文档，然后保存，关闭，结束程序

book = app.books.open(file, read_only=True)


lines = book.sheets(1).range("A1:AG50").value

# open('result.txt','w',encoding='utf-8')

cookie = ipt("Cookie: ")
if os.path.isfile(cookie):
    cookie = open(cookie, "r").read()
else:
    cookie = cookie

def inputDire(tip:str) -> str:
    '''输入一个目录'''
    while True:
        res = ipt(tip)
        if os.path.isdir(res):
            break
        else:
            prt(f"|{res}|错误，请重新输入。")
    return res


def getAllFiles(dirPath:str, endn:str = '.blend') -> list:
    '''获取目录{dirPath}中全部后缀为{endn}的文件列表'''
    flist = []
    for root, dirs, fs in os.walk(dirPath):
        for f in fs:
            f_fullpath = os.path.join(root, f)
            if f_fullpath.endswith(endn):
                flist.append(f_fullpath)
    return flist


def inputModelDir(type:str) -> list:
    '''让用户输入一个{type}的模板目录，返回其中的所有blend模板'''
    modelDire = inputDire(f"{type}模板目录：")
    return getAllFiles(modelDire,'.blend')
    


RenderModelTAlst = inputModelDir("TA")
RenderModelTBlst = inputModelDir("TB")

prt(f"\n已获取TA模板\n{RenderModelTAlst}\n\n已获取TB模板\n{RenderModelTBlst}\n\n")


import time


def randerImage(imagePath:str, blendFile: str,finalPath: str = '渲染结果###.png', logFile:str = './RenderLog.log'):

    prt(f"开始渲染文件：{os.path.basename(imagePath)}  录入日志{os.path.abspath(logFile)}")
    startTime = time.time()
    
    
    renderCMD = f"""blender -b -y --log * --log-file "{logFile}" -d "{blendFile}" --python-expr "import bpy;bpy.ops.image.open(filepath='//{os.path.basename(imagePath)}', directory='"""+os.path.abspath(os.path.dirname(imagePath)).replace('\\','\\\\')+"""', files=["""+"{"+f"""'name':'{os.path.basename(imagePath)}', 'name':'"""+os.path.basename(imagePath)+"'}"+f"""], relative_path=False, show_multiview=False);bpy.data.materials['MaterialA'].node_tree.nodes['图像纹理'].image = bpy.data.images['{os.path.basename(imagePath)}']" -o \""""+os.path.abspath(finalPath).replace('\\','\\\\')+"""\" -f 0"""
    

    r = os.system(renderCMD)

    prt(f"渲染已结束 文件{finalPath}已保存 耗时{int((time.time()-startTime)*100)/100}秒")

    return r

    


    





for line in lines:
    if lines.index(line) == 0:
        continue
    if line[0]:
        # open('result.txt','a',encoding='utf-8').write(str(tuple(enumerate(line)))+'\n\n')

        # 信息读入
        prt("正在获取组件信息")



        author = line[3].replace("\n", " ")
        isMember_ = (
            "【非本团队成员】"
            if line[4] == "以上皆非"
            else (
                "【星河团队成员】"
                if "星河" in line[4]
                else (
                    "【ICW团队成员】"
                    if "ICW" in line[4]
                    else ("【凌创工作室成员】" if "工作室" in line[4] else "")
                )
            )
        )
        isMember = (
            '【外】'
            if line[4] == '以上皆非'
            else (
                '【星河】'
                if '星河' in line[4]
                else (
                    '【ICW】'
                    if 'ICW' in line[4]
                    else ('【工作室】' if '工作室' in line[4] else '')
                )
            )
        )
        authorQQ = "作者QQ " + str(line[6])
        projectName = line[7].replace("\n", " ")
        projectType = line[8].replace("\n", " ")

        # 资源定价所需要的资源类型 免费free|绿宝石point|钻石diamond|礼包gift
        projectCost = line[9].replace("\n", " ").replace("*", "")

        CostErr = False

        if "免费" in projectCost:
            cost_ = ("free", 0)
        elif "绿宝石" in projectCost:
            costNum_ = ""
            for i in projectCost:
                try:
                    int(i)
                    costNum_ += i
                except:
                    pass
            if costNum_ == "":
                costNum_ = random.randint(2,9)*10
            elif not costNum_ in projectCost:
                CostErr = True
            cost_ = ("point", int(costNum_))
        elif "钻石" in projectCost:
            costNum_ = ""
            for i in projectCost:
                try:
                    int(i)
                    costNum_ += i
                except:
                    pass
            if not costNum_ in projectCost:
                CostErr = True
            cost_ = ("diamond", int(costNum_))
        else:
            cost_ = ("free", "0")
            CostErr = True

        # 皮肤类型
        skinType_ = '粗手臂' if line[10].replace("\n", " ") in ('Steve  （粗手臂）','标准 （粗手臂）') else '细手臂'
        skinType = "normal" if line[10].replace("\n", " ") in ('Steve  （粗手臂）','标准  （粗手臂）') else "slim"

        # 皮肤地址
        skin = line[11:17]

        projectDescription = line[17].replace("\n", " ")
        projectPicture = line[18:24]
        projectCopyleftPic = line[24:30]  # 值得注意的是，第30号格子是一个空格，是已经删掉的
        projectCopyleftDescription = line[2].replace("\n", " ")
        releasePlatform = (
            "仅网易"
            if line[31] == "仅发布网易"
            else ("允许其他平台" if line[31] == "可以发布其他平台" else "【注】")
        )
        releaseAuthor = line[32] if (line[32] != "无需作答" and line[32]) else "金羿"

        # 信息处理


        prt("正在移动组件资源")



        projectDirection = f"./result/{projectName}（{author}{isMember}）/"

        try:
            os.makedirs(projectDirection)
        except FileExistsError:
            prt(f"\n\n目录已存在 {projectDirection} 此组件(之一)已被跳过\n\n")
        except Exception as E:
            prt(f"\n\n创建目录时发生未知错误 {E} 此组件已被跳过\n\n")

        open(
            f"{projectDirection}{releasePlatform} {releaseAuthor}.release.txt",
            "w",
            encoding="utf-8",
        ).write(f"{line[31]}")

        open(
            f"{projectDirection}{projectType} {skinType_} {projectCost}.description.txt",
            "w",
            encoding="utf-8",
        ).write(f"{projectDescription}\n\n\n{authorQQ}")

        for i in skin:
            if i:
                n = i.replace(":", "-").replace("/", "-")
                try:
                    shutil.move(f"./temp/{n}", projectDirection)
                    os.rename(
                        f"{projectDirection}{n}",
                        f"{projectDirection}{n}".replace(
                            n[: n.index(".")], f"展开图{skin.index(i)}"
                        ),
                    )
                    picturePath = f"{projectDirection}{n}".replace(
                        n[: n.index(".")], f"展开图{skin.index(i)}"
                    )
                except Exception as E:
                    prt(f'文件"{projectDirection}"操作时发送错误\n{E}')

        for i in projectPicture:
            if i:
                n = i.replace(":", "-").replace("/", "-")
                try:
                    shutil.move(f"./temp/{n}", projectDirection)
                    os.rename(
                        f"{projectDirection}{n}",
                        f"{projectDirection}{n}".replace(
                            n[: n.index(".")], f"展示图Show{projectPicture.index(i)}"
                        ),
                    )
                except Exception as E:
                    prt(f'文件"{projectDirection}"操作时发送错误\n{E}')

        if projectCopyleftDescription != "未借鉴他人，皮肤是我自己的创新，完全是我做的":
            os.makedirs(f"{projectDirection}借鉴参考/")
            open(f"{projectDirection}借鉴参考/借鉴解释.txt", "w", encoding="utf-8").write(
                projectCopyleftDescription
            )
            for i in projectCopyleftPic:
                if i:
                    n = i.replace(":", "-").replace("/", "-")
                    try:
                        shutil.move(f"./temp/{n}", f"{projectDirection}借鉴参考/")
                        os.rename(
                            f"{projectDirection}借鉴参考/{n}",
                            f"{projectDirection}借鉴参考/{n}".replace(
                                n[: n.index(".")], f"参考图{projectCopyleftPic.index(i)}"
                            ),
                        )
                    except Exception as E:
                        prt(f'文件"{projectDirection}"操作时发送错误\n{E}')

        # 渲染图片

        prt("正在制作渲染图")

        randerImage(picturePath,random.choice(RenderModelTAlst),f"{projectDirection}渲染图TA_生成###.png",f"{projectDirection}TA渲染日志.log")

        randerImage(picturePath,random.choice(RenderModelTBlst),f"{projectDirection}渲染图TB_生成###.png",f"{projectDirection}TB渲染日志.log")



    else:
        break




shutil.rmtree("./temp/")

book.close()
app.quit()
