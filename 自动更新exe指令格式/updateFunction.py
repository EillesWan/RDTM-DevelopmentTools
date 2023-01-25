# -*- coding: utf-8 -*-

'''
   Copyright © 2023 Eilles Wan & Team-Ryoun

   Licensed under the Apache License, Version 2.0
   You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
'''

import os
import shutil
import uuid
import zipfile


from executeAutoTranslater import autoTranslate
from magicBeing import *


def makeZip(sourceDir, outFilename):
    zipf = zipfile.ZipFile(outFilename, "w", 8)
    pre_len = len(os.path.dirname(sourceDir))
    for parent, dirnames, filenames in os.walk(sourceDir):
        for filename in filenames:
            pathfile = os.path.join(parent, filename)
            arcname = pathfile[pre_len:].strip(os.path.sep)  # 相对路径
            zipf.write(pathfile, arcname)
    zipf.close()

def extractZip(targetFile, outPath):
    zipf = zipfile.ZipFile(targetFile, "r", 8)
    zipf.extractall(outPath)


def dododoSingle(filePath: str):
    with open(filePath,'r',encoding="utf-8") as f:
        context = f.read()
    
    a = context
    replaceLst = []

    while 'execute' in a:
        tag = uuid.uuid4()
        cmd = a[a.find("execute"):][:a[a.find("execute"):].find('\n')]
        a = a.replace(cmd,tag)
        replaceLst.append((cmd,tag))
    
    for cmd,tag in replaceLst:
        a = a.replace(tag,autoTranslate(cmd.decode("utf-8")).encode("utf-8"))
    



def forfile(pathIndex: str):
    pass


def __main__():
    while True:
        
        filepath, _ = formatipt("请输入MCFUNCTION文件或MCPACK文件地址(可以键入文件夹名)\n：",os.path.exists,"文件不存在或无法打开，请重新输入。",)

        if os.path.isdir:
            pass
        elif os.path.isfile:
            if filepath.endswith(".mcpack"):
                if os.path.exists(r"./temp/"):
                    shutil.rmtree(r"./temp/")
                os.makedirs(r"./temp/")
                extractZip(filepath,r"./temp/")

                shutil.rmtree(r"./temp/")
        


        prt('完成')

        
if __name__ == "__main__":
    __main__()