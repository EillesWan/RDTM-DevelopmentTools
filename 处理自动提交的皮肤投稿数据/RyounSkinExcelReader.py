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
import shutil
import sys
import zipfile


def unzip(zipFile, targetDirection):
    if not os.path.exists(targetDirection):
        os.makedirs(targetDirection)
    fz = zipfile.ZipFile(zipFile, 'r')
    for file in fz.namelist():
        fz.extract(file, targetDirection)



try:
    file = sys.argv[1]
    unzip(sys.argv[2], './temp/')
except IndexError:
    file = ''
    zipf = ''
    print("先excel再zip")
    while not (os.path.exists(file) and os.path.exists(zipf)):
        file, zipf = input().split(' ')
    unzip(zipf, './temp/')


# 导入xlwings模块
import xlwings as xw

# 打开Excel程序，默认设置：程序不可见，只打开不新建工作薄
app = xw.App(visible=False, add_book=False)
app.display_alerts = False

# 文件位置：filepath，打开test文档，然后保存，关闭，结束程序

book = app.books.open(file, read_only=True)


lines = book.sheets(1).range('A1:AG20').value

# open('result.txt','w',encoding='utf-8')

for line in lines:
    if lines.index(line) == 0:
        continue
    if line[0]:
        # open('result.txt','a',encoding='utf-8').write(str(tuple(enumerate(line)))+'\n\n')

        # 信息读入

        author = line[3].replace('\n', ' ')
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
        authorQQ = '作者QQ ' + str(line[6])
        projectName = line[7].replace('\n', ' ')
        projectType = line[8].replace('\n', ' ')
        projectCost = line[9].replace('\n', ' ')
        skinType = '粗手臂' if line[10] == 'Steve  （粗手臂）' else '细手臂'
        skin = line[11:17]
        projectDescription = line[17].replace('\n', ' ')
        projectPicture = line[18:24]
        projectCopyleftPic = line[24:30]  # 值得注意的是，第30号格子是一个空格，是已经删掉的
        projectCopyleftDescription = line[2].replace('\n', ' ')
        releasePlatform = (
            '仅网易'
            if line[31] == '仅发布网易'
            else ('允许其他平台' if line[31] == '可以发布其他平台' else '【注】')
        )
        releaseAuthor = line[32] if (line[32] != '无需作答' and line[32]) else '金羿'

        # 信息处理

        projectDirection = f'./result/{projectName}（{author}{isMember}）/'
        os.makedirs(projectDirection)

        open(
            f'{projectDirection}{releasePlatform} {releaseAuthor}.release.txt',
            'w',
            encoding='utf-8',
        ).write(f'{line[31]}')

        open(
            f'{projectDirection}{projectType} {skinType} {projectCost}.description.txt',
            'w',
            encoding='utf-8',
        ).write(f'{projectDescription}\n\n\n{authorQQ}')

        for i in skin:
            if i:
                n = i.replace(':', '-').replace('/', '-')
                try:
                    shutil.move(f'./temp/{n}', projectDirection)
                    os.rename(
                        f'{projectDirection}{n}',
                        f'{projectDirection}{n}'.replace(
                            n[: n.index('.')], f'展开图{skin.index(i)}'
                        ),
                    )
                except Exception as E:
                    print(f'文件\"{projectDirection}\"操作时发送错误\n{E}')

        for i in projectPicture:
            if i:
                n = i.replace(':', '-').replace('/', '-')
                try:
                    shutil.move(f'./temp/{n}', projectDirection)
                    os.rename(
                        f'{projectDirection}{n}',
                        f'{projectDirection}{n}'.replace(
                            n[: n.index('.')], f'展示图Show{projectPicture.index(i)}'
                        ),
                    )
                except Exception as E:
                    print(f'文件\"{projectDirection}\"操作时发送错误\n{E}')

        if projectCopyleftDescription != '未借鉴他人，皮肤是我自己的创新，完全是我做的':
            os.makedirs(f'{projectDirection}借鉴参考/')
            open(f'{projectDirection}借鉴参考/借鉴解释.txt', 'w', encoding='utf-8').write(
                projectCopyleftDescription
            )
            for i in projectCopyleftPic:
                if i:
                    n = i.replace(':', '-').replace('/', '-')
                    try:
                        shutil.move(f'./temp/{n}', f'{projectDirection}借鉴参考/')
                        os.rename(
                            f'{projectDirection}借鉴参考/{n}',
                            f'{projectDirection}借鉴参考/{n}'.replace(
                                n[: n.index('.')], f'参考图{projectCopyleftPic.index(i)}'
                            ),
                        )
                    except Exception as E:
                        print(f'文件\"{projectDirection}\"操作时发送错误\n{E}')

    else:
        break


shutil.rmtree('./temp/')

book.close()
app.quit()
