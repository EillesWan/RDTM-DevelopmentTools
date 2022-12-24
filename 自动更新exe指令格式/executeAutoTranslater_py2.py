# -*- coding: utf-8 -*-
#python27

'''

   Copyright © 2022 Team-Ryoun

   Licensed under the Apache License, Version 2.0 (the "License");
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0


'''

# 自动转换exe指令格式


def isWordsinside(string):
    '''判断字符串是否包含字母
    :param string: 字符串
    :return: bool
    '''
    for i in string:
        if i.isalpha():
            return True
    return False
    
# 极限挑战
# execute @a[name="abc 123"] ~~ ~ execute @s ~9 346 ~-8 detect ^6 ^7 ^2 concrete 18 execute @p[r=3,scores={a=3}] 324 ~324 5 scoreboard players add @s[tag="999 888aasd asd "] QWE_AS 2


def autoTranslate(sentence = ''):
    '''传入一行旧的execute指令，则将其转换为新格式
    :param sentence: 旧的execute指令
    :return: 新的execute指令
    '''


    sentence = sentence.replace("/","")

    if not 'execute' in sentence:
        return sentence
    if 'run' in sentence:
        return autoTranslate(sentence[sentence.find('run')+4:])
    

    # 下面是重点，只有我和老天爷看得懂
    if 'detect' in sentence[:sentence.find("execute",8) if "execute" in sentence[8:] else -1]:

        # print(f"检测到{sentence}含有detect")

        orign = sentence[sentence.find("execute")+8:(sentence.find("]") if "[" in sentence[:sentence.find("@")+3] else sentence.find("@")+1)+1]

        position = sentence[(sentence.find("]") if "[" in sentence[:sentence.find("@")+3] else sentence.find("@")+1)+2:sentence.find("detect")-1]

        ___ = [ j for i in [[i,] if isWordsinside(i) else ((["~"+j for j in i[1:].split("~")] if i.startswith("~") else ["~"+j for j in i.split("~")]) if "~" in i else ([i,] if not "^" in i else (["^"+j for j in i[1:].split("^")] if i.startswith("^") else ["^"+j for j in i.split("^")]))) for i in sentence[sentence.find("detect")+7:].split(" ",4)] for j in i ]
        
        blockpos = " ".join(___[0:3])

        ____ = " ".join(___[3:]).split(" ")

        blockname = ____[0]

        blockdata = ____[1]

        command = " ".join(____[2:])

        return 'execute as '+orign+' positioned as @s positioned '+position+' if block '+blockpos+' '+blockname+' '+blockdata+' at @s positioned '+position+' run '+autoTranslate(command)
        
    else:

        # print(f"检测到{sentence}不含有detect")

        ___ = [ j for i in [[i,] if isWordsinside(i) else ((["~"+j for j in i[1:].split("~")] if i.startswith("~") else ["~"+j for j in i.split("~")]) if "~" in i else ([i,] if not "^" in i else (["^"+j for j in i[1:].split("^")] if i.startswith("^") else ["^"+j for j in i.split("^")]))) for i in sentence[(sentence.find("]") if "]" in sentence else sentence.find("@")+1)+2:].split(" ",4)] for j in i ]

        return 'execute as '+sentence[sentence.find("execute")+8:(sentence.find("]") if "]" in sentence else sentence.find("@")+1)+1]+' positioned as @s positioned '+" ".join(___[0:3])+' at @s positioned '+" ".join(___[0:3])+' run '+autoTranslate(" ".join(___[3:]))
        
        # 我是一个善良的人，没有用下面这个恶心你们
        # f'execute as {sentence[sentence.find("execute")+8:(sentence.find("]") if "]" in sentence else sentence.find("@")+1)+1]} positioned as @s positioned {" ".join([ j for i in [[i,] if " " in i else ((["~"+j for j in i[1:].split("~")] if i.startswith("~") else ["~"+j for j in i.split("~")]) if "~" in i else ([i,] if not "^" in i else (["^"+j for j in i[1:].split("^")] if i.startswith("^") else ["^"+j for j in i.split("^")]))) for i in sentence[(sentence.find("]") if "]" in sentence else sentence.find("@")+1)+2:].split(" ",4)] for j in i ][0:3])} at @s positioned {" ".join([ j for i in [[i,] if " " in i else ((["~"+j for j in i[1:].split("~")] if i.startswith("~") else ["~"+j for j in i.split("~")]) if "~" in i else ([i,] if not "^" in i else (["^"+j for j in i[1:].split("^")] if i.startswith("^") else ["^"+j for j in i.split("^")]))) for i in sentence[(sentence.find("]") if "]" in sentence else sentence.find("@")+1)+2:].split(" ",4)] for j in i ][0:3])} run {autoTranslate(" ".join([ j for i in [[i,] if " " in i else ((["~"+j for j in i[1:].split("~")] if i.startswith("~") else ["~"+j for j in i.split("~")]) if "~" in i else ([i,] if not "^" in i else (["^"+j for j in i[1:].split("^")] if i.startswith("^") else ["^"+j for j in i.split("^")]))) for i in sentence[(sentence.find("]") if "]" in sentence else sentence.find("@")+1)+2:].split(" ",4)] for j in i ][3:]))}'



        
def __main__():
    '''主函数
    '''
    while True:
        try:
            sentence = input()
            print
            print (autoTranslate(sentence))
        except EOFError:
            break


if __name__ == "__main__":
    __main__()

# 没写完，我也不知道咋写，但是总得写不是吗