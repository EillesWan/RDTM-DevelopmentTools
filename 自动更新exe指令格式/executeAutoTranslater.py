# -*- coding: utf-8 -*-


'''

   Copyright © 2022 Team-Ryoun

   Licensed under the Apache License, Version 2.0 (the "License");
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0


'''

# 自动转换exe指令格式
import uuid


def isWordsinside(string):
    '''判断字符串是否包含字母
    :param string: 字符串
    :return: bool
    '''
    for i in string:
        if i.isalpha():
            return True
    return False


def isfloatable(sth: str) -> bool:
    try:
        float(sth)
        return True
    except:
        return False    


# 极限挑战
# execute @a[name="abc 123"] ~~ ~ execute @s ~9 346 ~-8 detect ^6 ^7 ^2 concrete 18 execute @p[r=3,scores={a=3}] 324 ~324 5 scoreboard players add @s[tag="999 888aasd asd "] QWE_AS 2

# /execute @a~~~/w @s aaa

# execute@s[tag="[][]  你妈死了"]~ 1~576detect^6^^66concrete 1 execute @s         [scores={n=0}] ~ ~ ~0.09 execute@s~~~detect 0 0 0 bedrock -1 execute@a [name="999去他奶奶的 jjj"]~~ ~/execute@s[tag="℃♞"]~ 32 ~5423give @s command_block 1 1 {"name_tag":["a":"b操你妈逼"]}

# 感谢 尘风、籽怼、Happy2018New 为本程序的试错提供了非常有效的支持
# 也感谢 尘风、Happy2018New、Dislink Sforza 为作者提供相关参考意见


def autoTranslate(sentence):
    '''传入一行旧的execute指令，则将其转换为新格式
    :param sentence: 旧的execute指令
    :return: 新的execute指令
    '''


    if not 'execute' in sentence:
        return sentence
    elif 'run' in sentence:
        return autoTranslate(sentence[sentence.find('run')+4:])

    # 避免不规范的语法
    # 如果选择器的中括号包括空格
    sentence = ((sentence[:sentence.find("@")+2]+sentence[sentence.find('['):]) if (sum(0 if i == ' ' else 1 for i in sentence[sentence.find('@')+2:sentence.find('[')])==0) else sentence).replace("/"," ").lower()

    

    # 如果有字符串包含其中
    # 我们可以看作一个神奇的pattern
    startcatch = False
    strings = []
    tempstring = ""
    for i in sentence:
        if i == '"':
            startcatch = not startcatch
            if not startcatch:
                tpp = '{}"'.format(tempstring)
                tag = str(uuid.uuid4())
                sentence = sentence.replace(tpp,tag)
                strings.append((tpp,tag))
                tempstring = ""
        if startcatch:
            tempstring += i

    


    sentence = list(sentence)
    # 如果有神奇的东西在坐标后面，那就神奇了
    for i in range(len(sentence)):
        if sentence[i] in ('^','~') and sentence[i+1] != ' ':
            j = i + 1
            while isfloatable("".join(sentence[i+1:j+1])):
                j+=1
            if sentence[j] == " ":
                continue
            else:
                sentence.insert(j,' ')
    sentence = "".join(sentence)
    
    def backSentence(a):
        for tpp,tag in strings:
            a = a.replace(tag,tpp)
        return a

    # 下面是重点，只有我和老天爷看得懂
    if 'detect' in sentence[:sentence.find("execute",8) if "execute" in sentence[8:] else -1]:

        orign = sentence[sentence.find("execute")+7:(sentence.find("]") if "[" in sentence[:sentence.find("@")+5] else sentence.find("@")+1)+1].strip()

        position = sentence[(sentence.find("]") if "[" in sentence[:sentence.find("@")+3] else sentence.find("@")+1)+1:sentence.find("detect")-1].strip()

        ___ = [ j for i in [[i,] if isWordsinside(i) else ((["~"+j for j in i[1:].split("~")] if i.startswith("~") else ["~"+j for j in i.split("~")]) if "~" in i else ([i,] if not "^" in i else (["^"+j for j in i[1:].split("^")] if i.startswith("^") else ["^"+j for j in i.split("^")]))) for i in sentence[sentence.find("detect")+6:].strip().split(" ",4)] for j in i ]
        
        blockpos = " ".join(___[0:3])

        ____ = " ".join(___[3:]).split(" ")

        blockname = ____[0]

        blockdata = ____[1]

        command = " ".join(____[2:])

        return backSentence('execute as {} positioned as @s positioned {} if block {} {} {} at @s positioned {} run {}'.format(orign,position,blockpos,blockname,blockdata,position,autoTranslate(command)))
        
    else:


        ___ = [ j for i in [[i,] if isWordsinside(i) else ((["~"+j for j in i[1:].split("~")] if i.startswith("~") else ["~"+j for j in i.split("~")]) if "~" in i else ([i,] if not "^" in i else (["^"+j for j in i[1:].split("^")] if i.startswith("^") else ["^"+j for j in i.split("^")]))) for i in sentence[(sentence.find("]") if "]" in sentence else sentence.find("@")+1)+1:].strip().split(" ",4)] for j in i ]

        

        return backSentence('execute as {} positioned as @s positioned {} at @s positioned {} run {}'.format(sentence[sentence.find("execute")+7:(sentence.find("]") if "[" in sentence[:sentence.find("@")+5] else sentence.find("@")+1)+1].strip()," ".join(___[0:3])," ".join(___[0:3]),autoTranslate(" ".join(___[3:]))))
        
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
            print("="*10)
        except EOFError:
            break
        except Exception as e:
            print(e)
            continue


if __name__ == "__main__":
    __main__()

# 没写完，我也不知道咋写，但是总得写不是吗