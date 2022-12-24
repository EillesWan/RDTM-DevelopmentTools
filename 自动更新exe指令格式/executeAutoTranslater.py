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

# 自动转换exe指令格式

def getMapBlock(startPos: tuple = (0,0,0), endPos: tuple = (0,0,0)):
    '''传入起始和终止坐标，返回一个区块中的方块
    :param startPos: 起始坐标
    :param endPos: 终止坐标
    :return: list[全部方块]
    '''
    pass


def isWordsinside(string: str):
    '''判断字符串是否包含字母
    :param string: 字符串
    :return: bool
    '''
    for i in string:
        if i.isalpha():
            return True
    return False
    

def autoTranslate(sentence: str = ''):
    '''传入一行旧的execute指令，则将其转换为新格式
    :param sentence: 旧的execute指令
    :return: 新的execute指令
    '''
    if not 'execute' in sentence:
        return sentence
    if 'run' in sentence:
        return autoTranslate(sentence[sentence.find('run')+4:])
    

    # 下面是重点，只有我和老天爷看得懂
    if 'detect' in sentence:
        orign = sentence[sentence.find("execute")+8:(sentence.find("]") if "]" in sentence else sentence.find("@")+1)+1]

        position = sentence[(sentence.find("]") if "]" in sentence else sentence.find("@")+1)+1:sentence.find("detect")]

        ___ = [ j for i in [[i,] if isWordsinside(i) else ((["~"+j for j in i[1:].split("~")] if i.startswith("~") else ["~"+j for j in i.split("~")]) if "~" in i else ([i,] if not "^" in i else (["^"+j for j in i[1:].split("^")] if i.startswith("^") else ["^"+j for j in i.split("^")]))) for i in sentence[sentence.find("detect")+7:].split(" ",4)] for j in i ]
        
        blockpos = " ".join(___[0:3])

        ____ = " ".join(___[4:]).split(" ")

        blockname = ____[0]

        blockdata = ____[1]

        command = " ".join(____[2:])

        return f'execute as {orign} positioned as @s positioned {position} if block {blockpos} {blockname} {blockdata} at @s positioned {position} run {autoTranslate(command)}'
        
    else:
        ___ = [ j for i in [[i,] if isWordsinside(i) else ((["~"+j for j in i[1:].split("~")] if i.startswith("~") else ["~"+j for j in i.split("~")]) if "~" in i else ([i,] if not "^" in i else (["^"+j for j in i[1:].split("^")] if i.startswith("^") else ["^"+j for j in i.split("^")]))) for i in sentence[(sentence.find("]") if "]" in sentence else sentence.find("@")+1)+2:].split(" ",4)] for j in i ]

        return f'execute as {sentence[sentence.find("execute")+8:(sentence.find("]") if "]" in sentence else sentence.find("@")+1)+1]} positioned as @s positioned {" ".join(___[0:3])} at @s positioned {" ".join(___[0:3])} run {autoTranslate(" ".join(___[3:]))}'
        
        # 我是一个善良的人，没有用下面这个恶心你们
        # f'execute as {sentence[sentence.find("execute")+8:(sentence.find("]") if "]" in sentence else sentence.find("@")+1)+1]} positioned as @s positioned {" ".join([ j for i in [[i,] if " " in i else ((["~"+j for j in i[1:].split("~")] if i.startswith("~") else ["~"+j for j in i.split("~")]) if "~" in i else ([i,] if not "^" in i else (["^"+j for j in i[1:].split("^")] if i.startswith("^") else ["^"+j for j in i.split("^")]))) for i in sentence[(sentence.find("]") if "]" in sentence else sentence.find("@")+1)+2:].split(" ",4)] for j in i ][0:3])} at @s positioned {" ".join([ j for i in [[i,] if " " in i else ((["~"+j for j in i[1:].split("~")] if i.startswith("~") else ["~"+j for j in i.split("~")]) if "~" in i else ([i,] if not "^" in i else (["^"+j for j in i[1:].split("^")] if i.startswith("^") else ["^"+j for j in i.split("^")]))) for i in sentence[(sentence.find("]") if "]" in sentence else sentence.find("@")+1)+2:].split(" ",4)] for j in i ][0:3])} run {autoTranslate(" ".join([ j for i in [[i,] if " " in i else ((["~"+j for j in i[1:].split("~")] if i.startswith("~") else ["~"+j for j in i.split("~")]) if "~" in i else ([i,] if not "^" in i else (["^"+j for j in i[1:].split("^")] if i.startswith("^") else ["^"+j for j in i.split("^")]))) for i in sentence[(sentence.find("]") if "]" in sentence else sentence.find("@")+1)+2:].split(" ",4)] for j in i ][3:]))}'



        
def __main__():
    '''主函数
    '''
    while True:
        try:
            sentence = input()
            print()
            print(autoTranslate(sentence))
        except EOFError:
            break
        except Exception as e:
            print(e)
            continue


if __name__ == "__main__":
    __main__()

# 没写完，我也不知道咋写，但是总得写不是吗