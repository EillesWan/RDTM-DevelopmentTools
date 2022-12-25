# -*- coding: utf-8 -*-
#python27

'''

   Copyright © 2022 Team-Ryoun

   Licensed under the Apache License, Version 2.0 (the "License");
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0


'''

# 自动转换exe指令格式



    
# 极限挑战
# execute @a[name="abc 123"] ~~ ~ execute @s ~9 346 ~-8 detect ^6 ^7 ^2 concrete 18 execute @p[r=3,scores={a=3}] 324 ~324 5 scoreboard players add @s[tag="999 888aasd asd "] QWE_AS 2


def autoTranslate(sentence = ''):
    '''传入一行旧的execute指令，则将其转换为新格式
    :param sentence: 旧的execute指令
    :return: 新的execute指令
    '''

    def isWordsinside(string):
        '''判断字符串是否包含字母
        :param string: 字符串
        :return: bool
        '''
        for i in string:
            if i.isalpha():
                return True
        return False
    if not 'execute' in sentence:
        return sentence
    if 'run' in sentence:
        return autoTranslate(sentence[sentence.find('run')+4:])

    # 避免不规范的语法
    sentence = sentence.replace("/"," ").lower()

    # 如果选择器的中括号包括空格
    sentence = (sentence[:sentence.find("@")+2]+sentence[sentence.find('['):]) if '[' in sentence else sentence

    # 如果有字符串包含其中
    # 我们可以看作一个神奇的pattern
    startcatch = False
    strings = []
    tempstring = ""
    for i in sentence:
        if i == '"':
            startcatch = not startcatch
            if not startcatch:
                strings.append(f'{tempstring}"')
                tempstring = ""
        if startcatch:
            tempstring += i
    for i in strings:
        sentence = sentence.replace(i,f'我的天哪这是不行的士大夫萨拉发噶苏联官方撒发生官方首发数据库发金羿你永远也写不到这句话{strings.index(i)}')
    
    
    def backSentence(a):
        for i in strings:
            a = a.replace(f'我的天哪这是不行的士大夫萨拉发噶苏联官方撒发生官方首发数据库发金羿你永远也写不到这句话{strings.index(i)}',i)
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

        

        return backSentence('execute as {} positioned as @s positioned {} at @s positioned {} run {}'.format(sentence[sentence.find("execute")+7:(sentence.find("]") if "[" in sentence[:sentence.find("@")+5] else sentence.find("@")+1)+1]," ".join(___[0:3])," ".join(___[0:3]),autoTranslate(" ".join(___[3:]))))
        


        
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