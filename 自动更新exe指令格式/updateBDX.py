# -*- coding: utf-8 -*-

'''
   Copyright © 2023 Eilles Wan & Team-Ryoun

   Licensed under the Apache License, Version 2.0
   You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
'''

import brotli
import uuid

from executeAutoTranslater import autoTranslate

from magicBeing import *



def __main__():
    while True:
        
        filepath, bdxfile = formatipt("请输入BDX文件地址：",open,"文件不存在或无法打开，请重新输入。","rb+")
        
        # 记得注释掉
        # bdxfile = open("","wb+")
        # -----BEGIN RSA PUBLIC KEY-----\n
        whole = bdxfile.read()
        bdxfile.close()
        
        context = brotli.decompress(whole[3:])
        
        a = context if not b"-----BEGIN RSA PUBLIC KEY-----" in context else context[:context.find(b"-----BEGIN RSA PUBLIC KEY-----")-context[:context.find(b"-----BEGIN RSA PUBLIC KEY-----")][::-1].find(b'X')]+b'E'
        replaceLst = []

        while b'execute' in a:
            tag = str(uuid.uuid4()).encode("utf-8")
            cmd = a[a.find(b"execute"):][:a[a.find(b"execute"):].find(b'\x00')]
            a = a.replace(cmd,tag)
            replaceLst.append((cmd,tag))
        
        for cmd,tag in replaceLst:
            a = a.replace(tag,autoTranslate(cmd.decode("utf-8")).encode("utf-8"))
        
        with open(filepath,'wb+') as gogogo:
            gogogo.write(b"BD@"+brotli.compress(a))

        prt('完成')

        
if __name__ == "__main__":
    __main__()

