# -*- coding: utf-8 -*-

'''

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

'''

import os

import sys


try:
    file = sys.argv[1]

except IndexError:
    file =''
    print("先excel再zip")
    while not (os.path.exists(file)):
        file = input()


# 导入xlwings模块
import xlwings as xw

# 打开Excel程序，默认设置：程序不可见，只打开不新建工作薄
app=xw.App(visible=False,add_book=False)
app.display_alerts=False

# 文件位置：filepath，打开test文档，然后保存，关闭，结束程序

book=app.books.open(file)



lines = book.sheets(1).range('A1:AG15').value

open('result.txt','w',encoding='utf-8')

for line in lines:
    if lines.index(line) == 0:
        continue
    if line[0]:
        open('result.txt','a',encoding='utf-8').write(str(tuple(enumerate(line)))+'\n\n')


book.close()
app.quit()