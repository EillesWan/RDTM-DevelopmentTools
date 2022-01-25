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

import zipfile
import os
import shutil

def unzip(zipFile, targetDirection):
    if not os.path.exists(targetDirection):
        os.makedirs(targetDirection)
    fz = zipfile.ZipFile(zipFile, 'r')
    for file in fz.namelist():
        fz.extract(file, targetDirection)  


import sys

file = sys.argv[1]

unzip(sys.argv[2],'./temp/')

# 导入xlwings模块
import xlwings as xw

# 打开Excel程序，默认设置：程序可见，只打开不新建工作薄
app=xw.App(visible=True,add_book=False)
app.display_alerts=False

# 文件位置：filepath，打开test文档，然后保存，关闭，结束程序

book=app.books.open(file)



i = 1

lines = book.sheets(i).range('A1:AE10').value

open('result.txt','w',encoding='utf-8')

for line in lines:
    if lines.index(line) == 0:
        continue
    if line[0]:
        open('result.txt','a',encoding='utf-8').write(str(tuple(enumerate(line)))+'\n\n')
        
        # 信息读入

        author = line[3]
        isMember = '【外】' if line[4] == '不是' else ''
        authorQQ = '' if isMember == '' else line[6] 
        projectName = line[7]
        projectType = line[8]
        projectCost = line[9]
        skinType = '粗手臂' if line[10] == 'Steve  （粗手臂）' else '细手臂'
        skin = line[11:17]
        projectDescription = line[17]
        projectPicture = line[18:24]
        projectCopyleftPic = line[24:]
        projectCopyleftDescription = line[2]

        # 信息处理

        projectDirection = f'./result/{projectName}（{author}{isMember}）/'
        
        os.makedirs(projectDirection)

        open(f'{projectDirection}{projectType} {skinType} {projectCost}.txt','w').write(f'{projectDescription}\n\n\n{authorQQ}')

        for i in skin:
            if i:
                n = i.replace(':','_').replace('/','-')
                shutil.move(f'./temp/{n}',projectDirection)
                os.rename(f'{projectDirection}{n}',f'{projectDirection}{n}'.replace(n[:n.index('.')],f'展开图{skin.index(i)}'))
        
        for i in projectPicture:
            if i:
                n = i.replace(':','_').replace('/','-')
                shutil.move(f'./temp/{n}',projectDirection)
                os.rename(f'{projectDirection}{n}',f'{projectDirection}{n}'.replace(n[:n.index('.')],f'展示图Show{projectPicture.index(i)}'))

        
        if projectCopyleftDescription != '未借鉴他人，皮肤是我自己的创新，完全是我做的':
            os.makedirs(f'{projectDirection}借鉴参考/')
            for i in projectCopyleftPic:
                if i:
                    n = i.replace(':','_').replace('/','-')
                    shutil.move(f'./temp/{n}',f'{projectDirection}借鉴参考/')
                    os.rename(f'{projectDirection}借鉴参考/{n}',f'{projectDirection}借鉴参考/{n}'.replace(n[:n.index('.')],f'参考图{projectCopyleftPic.index(i)}'))

    else:
        break






shutil.rmtree('./temp/')

book.close()
app.quit()