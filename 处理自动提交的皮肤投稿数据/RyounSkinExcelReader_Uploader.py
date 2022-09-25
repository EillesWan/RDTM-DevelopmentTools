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
import requests


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
    print("先excel再zip")
    while not (os.path.exists(file) and os.path.exists(zipf)):
        file, zipf = input().split(" ")
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

cookie = input("Cookie: ")
if os.path.isfile(cookie):
    cookie = open(cookie, "r").read()
else:
    cookie = cookie


firsturl = "https://mc-launcher.webapp.163.com/items/categories/pe/upload"

firstheaders = {
    "Host": "mc-launcher.webapp.163.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Access-Control-Request-Method": "POST",
    "Access-Control-Request-Headers": "content-type",
    "Referer": "https://mcdev.webapp.163.com/",
    "Origin": "https://mcdev.webapp.163.com",
    "DNT": "1",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
}

aGETurl = (
    "https://mc-launcher.webapp.163.com/filepicker/token?file_type=png&secure=false"
)

getHeader = {
    "Host": "mc-launcher.webapp.163.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
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
    "TE": "trailers",
}

# 统计数据定义
allProjrcts = {
    "成功": [],
    "失败": [],
    "错误": [],
    "未知": [],
}
maxProjectNameLength = 0
maxAuthorNameLength = 0


for line in lines:
    if lines.index(line) == 0:
        continue
    if line[0]:
        # open('result.txt','a',encoding='utf-8').write(str(tuple(enumerate(line)))+'\n\n')

        # 信息读入

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
        skinType_ = '粗手臂' if line[10] == 'Steve  （粗手臂）' else '细手臂'
        skinType = "normal" if line[10] == "Steve  （粗手臂）" else "slim"

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

        projectDirection = f"./result/{projectName}（{author}{isMember}）/"
        os.makedirs(projectDirection)

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
                    print(f'文件"{projectDirection}"操作时发送错误\n{E}')

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
                    print(f'文件"{projectDirection}"操作时发送错误\n{E}')

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
                        print(f'文件"{projectDirection}"操作时发送错误\n{E}')

        # 以下是发送组件

        print(f"正在操作组件{projectDirection}")

        print("====================开始获取图片上传密钥")

        firstResult = requests.get(aGETurl, headers=getHeader).json()

        if firstResult["status"] == "ok":
            print("成功！已获取密钥")
            token = firstResult["data"]["token"]
        else:
            print("获取密钥失败！")
            print(firstResult)
            continue

        print(f"====================开始上传图片:{picturePath}")

        aPOSTurl = "https://fp.ps.netease.com/x19/file/new/"

        boundary = "---------------------------" + "".join(
            [str(random.randint(0, 9)) for i in range(29)]
        )

        payload = (
            f"""--{boundary}
Content-Disposition: form-data; name="Authorization"

{token}
--{boundary}
Content-Disposition: form-data; name="fpfile"; filename="{projectName}.png"
Content-Type: image/png

""".encode()
            + open(
                picturePath,
                "rb",
            ).read()
            + f"""
--{boundary}--""".encode()
        )

        # print(f"负载已读取：\n{payload}")

        postHeader = {
            "Host": "fp.ps.netease.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "Content-Length": str(len(payload)),
            "Origin": "https://mcdev.webapp.163.com",
            "DNT": "1",
            "Connection": "keep-alive",
            "Referer": "https://mcdev.webapp.163.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "TE": "trailers",
        }

        postresult = requests.post(aPOSTurl, data=payload, headers=postHeader)

        responseHeader = postresult.headers
        responseData = postresult.text

        signature = responseHeader["X-Ntes-Signature"]

        # print(f"响应头({type(responseHeader)})：\n{responseHeader}\n\n响应内容({type(responseData)})：\n{responseData}\n")
        # print(f'已获取网易签名：{signature}\n已获取资源url地址：{responseData}')
        print("图片上传成功")

        print("====================开始投稿资源：获取投稿许可")

        requests.options(firsturl, headers=firstheaders)

        print("成功通告服务端")

        print("====================开始投稿资源：提交资源信息")
        isMember_ = (
            f'<strong style="color: green;" class="ql-size-small">{isMember_}</strong>'
            if isMember_
            else ""
        )
        datadict = {
            "update_summary": "",  # 更新纪要，就是网易给你留的日志
            "item_name": projectName,  # 上传组件名称
            "game_type": "",
            "mc_version": [[]],
            "online_platform": ["pe"],  # 当前的上传平台
            "pri_type": 4,  # 上传组件类型 地图1 模组2 材质光影3 皮肤4 联机大厅5
            "sub_type": 13
            if projectType == "原版"
            else (
                14 if projectType == "科幻" else (15 if projectType == "神话" else 16)
            ),  # 上传组件子类型 地图-闯关1 RPG2 PVP3 建筑4 其他5 | 模组-玩法6 道具7 生物8 其他9 一键生成10 | 材质光影-材质11 光影12 | 皮肤-原版13 科幻14 神话15 其他16 | 联机大厅- 未考证
            "pc_pri_type": None,
            "pc_sub_type": None,
            "info": f'<p><img src="https://x19.fp.ps.netease.com/file/627020d4442e29577c303660uydAI6HY04"></p><p><span class="ql-size-large">本组件作者：</span><strong class="ql-size-huge" style="color: blue;">{author}</strong>{isMember_}</p><p>{projectDescription}</p><p class="ql-align-center"><strong style="color: blue;" class="ql-size-huge">凌天之云创新我的世界开发团队</strong></p><p class="ql-align-center"><span style="color: blue;" class="ql-size-huge">Ryoun Development Team for Minecraft</span></p><p class="ql-align-center"><strong style="color: orange;" class="ql-size-huge">玩家至上</strong></p><p><span class="ql-size-large">代发各种优秀稿件！皮肤、组件、地图、材质、光影皆可！</span></p><p><em class="ql-size-large">欢迎前来探讨您在游玩时遇到的问题以及提供信息反馈：</em><strong class="ql-size-huge"><em>946419613</em></strong></p>',  # 详情简介
            "pc_info": "",
            "rarity": 0,
            "lobby_min_num": 0,
            "lobby_max_num": 0,
            "lobby_tags": [],
            "host": [],
            "test_host": [],
            "include_map": False,  # 是否包含地图（仅PC）
            "tag": [],
            "multi_tags": [],
            "requirement": [],
            "mod_id": 0,
            "available_scope": "",
            "force_encrypt": False,
            "price_type": cost_[0],  # 资源定价所需要的资源类型 免费free|绿宝石point|钻石diamond|礼包gift
            "trial_duration": 0,
            "price": cost_[1],  # 价格
            "ios_price": 0,
            "ios_price_type": "",
            "ios_jelly_id": "",
            "android_price": 0,
            "android_price_type": "",
            "adv_obtain_num": 0,
            "brief": "",
            "game_host": "",
            "pure": False,
            "java_version": "",
            "charge_type": "skin packs",  # 付费类型
            "charge_desc": "免费",  # 付费备注
            "activity_desc": "",
            "claim_item_enabled": False,
            "body_type": skinType,  # 皮肤材质类型 slim | normal
            "current_change_log": "",
            "pe_item_id": [],
            "pe_home_cash": [],
            "pe_frame_id": [],
            "pe_furniture_id": [],
            "pe_six_month_vip_id": [],
            "pe_passport_ten_id": [],
            "pe_user_background_id": [],
            "pe_activity_coupon": [],
            "pe_chat_bubble_id": [],
            "pe_one_month_vip_id": [],
            "pe_lottery_chance": [],
            "has_mod_version": False,
            "mod_version": "2.2",  # 网易ModAPI版本
            "is_lobby_competitive": False,
            "is_asymmetric": False,
            "lobby_player_num": 0,
            "lobby_camps": [],
            "lobby_normal_mode": False,
            "lobby_reconnect_time": 0,
            "subject_id": None,
            "is_sync": False,
            "vip_only": False,
            "is_season_mod": False,
            "activity_only": False,
            "searchable": True,
            "is_original": True,
            "lobby_commercialize": False,
            "season_begin": 0,
            "is_lottery_reward": False,
            "lottery_id": 0,
            "is_persona": False,
            "is_recommend": False,
            "exchange_currency": 0,
            "exchange_currency_type": "ordinary",
            "decompose_currency": 0,
            "decompose_currency_type": "ordinary",
            "persona_mtypeid": 0,
            "persona_stypeid": 0,
            "dyeing": "",
            "discount": [],
            "need_method_uuid": False,
            "need_behaviour_uuid": False,
            "is_vip_benefit": False,
            "is_test_server": False,
            "is_access_by_uid": False,
            "is_can_comment": False,
            "weak_offline": False,
            "weak_offline_reason": "",
            "is_quick_upload": False,
            "running_status": "normal",
            "white_list": [],
            "silent_white_list": [],
            "is_joint_activity": False,
            "joint_activity_detail": {},
            "joint_activity_name": "",
            "joint_activity_tag": [],
            "collection_id": 0,
            "collection_name": "",
            "res": [
                {
                    "res_url": {
                        "body": responseData,
                        "file_type": "png",
                        "sign": signature,
                    },
                    "res_name": f"{projectName}.png",
                    "mc_version": [],
                    "add_version": True,
                }
            ],
            "channel": [
                {
                    "channel_id": 5,
                    "channel_url": {
                        "body": '{"url": "https://x19.fp.ps.netease.com/file/6281287e2ef6ee847a2806d29bOEEKqu04", "mime": "image/png; charset=binary", "fsize": 423480, "md5": "acda3ea7a04a7348b3c8f800cb93307a", "picSize": [1000, 1000]}',
                        "file_type": "image",
                        "sign": "h7x9mkkslt7o5tYs1vS4RgRvCpY=",
                    },
                    "channel_required": True,
                    "version": 2,
                },
                {
                    "channel_id": 6,
                    "channel_url": {
                        "body": '{"url": "https://x19.fp.ps.netease.com/file/628128822ef6ee9b09f0372fEs51Kqk504", "mime": "image/png; charset=binary", "fsize": 346267, "md5": "c4cccee7ed2d50f9f075d5116f1707f8", "picSize": [900, 580]}',
                        "file_type": "image",
                        "sign": "9Ygz7oDrmnEsvh9t6+gAPETcTvs=",
                    },
                    "channel_required": True,
                    "version": 1,
                },
            ],
        }

        headers = {
            "Host": "mc-launcher.webapp.163.com",  # 访问地址
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",  # 模拟浏览器
            "Accept": "application/json, text/plain, */*",  # 接受数据类型
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",  # 接受语种
            "Accept-Encoding": "gzip, deflate, br",  # 接受的压缩编码格式
            "Content-Type": "application/json;charset=utf-8",  # 发送数据类型
            "Content-Length": f"{len(datadict)}",  # 发送数据长度（即下方的json字符串的长度）
            "Origin": "https://mcdev.webapp.163.com",  # 发送来源
            "DNT": "1",  # 是否支持DNT
            "Connection": "keep-alive",  # 连接类型
            "Referer": "https://mcdev.webapp.163.com/",  # 来源地址
            "Cookie": cookie,  # cookie
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
        }

        result = requests.post(firsturl, headers=headers, json=datadict)
        result = result.json()
        print(f"组件名称：{projectName}, 作者：{author}")
        print(
            f'失败：{result["msg"]}'
            if result["status"] == "fail"
            else (
                f'成功\n组件ID：{result["data"]["item_id"]}'
                if result["status"] == "ok"
                else f"未知{result}"
            )
        )
        print()

        maxAuthorNameLength = max(len(author), maxAuthorNameLength)
        maxProjectNameLength = max(len(projectName), maxProjectNameLength)

        status = (
            "失败"
            if result["status"] == "fail"
            else (
                "成功"
                if result["status"] == "ok"
                else ("错误" if result["status"] == "params error" else "未知")
            )
        )
        allProjrcts[status].append(
            {
                "name": projectName,
                "author": author,
                "status": status,
                "msg": result,
                "DEAL": CostErr,
            }
        )

    else:
        break


print("=====-----=====-----统计数据-----=====-----=====")
print(
    "\t" * int(maxProjectNameLength / 8 - 1)
    + "组件名称"
    + "\t" * int(maxProjectNameLength / 8),
    end="|",
)
print(
    "\t" * int(maxAuthorNameLength / 8 - 1)
    + "作者"
    + "\t" * int(maxAuthorNameLength / 8),
    end="|",
)
print("状态", end="|")
print(
    "信息",
)


for key, subj in allProjrcts.items():
    print(f"{key}x{len(subj)}")
    for context in subj:
        print(
            ("■" if context["DEAL"] else '')
            + str(context["name"])
            + "\t" * int((maxProjectNameLength - len(context["name"])) / 4)
            + "|"
            + str(context["author"])
            + "\t" * int((maxAuthorNameLength - len(context["author"])) / 4)
            + "|"
            + str(context["status"])
            + "|"
            + str(context["msg"])
        )
        if context["DEAL"]:
            print(f"定价：{projectCost} ;解析结果：{cost_}")
    print()


shutil.rmtree("./temp/")

book.close()
app.quit()
