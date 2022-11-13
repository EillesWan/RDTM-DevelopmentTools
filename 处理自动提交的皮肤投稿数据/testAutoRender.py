
import subprocess
import time
import os


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





def randerImage(imagePath:str, blendFile: str,finalPath: str = '渲染结果###.png', logFile:str = './RenderLog.log', debugFile:str = './RenderDebug.log'):

    prt(f"开始渲染文件：{os.path.basename(imagePath)}  录入日志{os.path.abspath(logFile)}")
    startTime = time.time()
    
    
    renderCMD = f"""blender -b -y --log * --log-file "{logFile}" -d "{blendFile}" --python-expr "import bpy;bpy.ops.image.open(filepath='//{os.path.basename(imagePath)}', directory='{os.path.dirname(imagePath)}', files=["""+"{"+f"""'name':'{os.path.basename(imagePath)}', 'name':'{os.path.basename(imagePath)}'"""+"}"+f"""], relative_path=True, show_multiview=False);bpy.data.materials['MaterialA'].node_tree.nodes['图像纹理'].image = bpy.data.images['{os.path.basename(imagePath)}']" -o "{finalPath}" -f 0"""
    

    os.system(renderCMD)

    prt(f"渲染已结束 文件{finalPath}已保存 耗时{(int(time.time()-startTime)*100)/100}秒")

    

picturePath = ipt("皮肤路径：")


import random


randerImage(picturePath,random.choice(RenderModelTAlst),)

randerImage(picturePath,random.choice(RenderModelTBlst),)


