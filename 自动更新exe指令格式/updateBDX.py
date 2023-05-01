# -*- coding: utf-8 -*-
'''
   Copyright © 2023 Eilles Wan & Team-Ryoun

   Licensed under the Apache License, Version 2.0
   You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
'''
import brotli as ____B;import uuid as ____U
def _(________):
    if not 'execute' in ________:return ________
    elif 'run' in ________:return ________[:________.find('run')+4]+_(________[________.find('run')+4:])
    ________ = ((__ := str(____U.uuid4()),___:=[(r"\"",__),], ________.replace(r"\"",__)) if r"\"" in ________ else (None,___:=[],________))[2];__ = False;______ = ""
    for i in ________:
        if i == '"':
            __ = not __;
            if not __:______ = '{}"'.format(______);____________ = str(____U.uuid4());________ = ________.replace(______,____________);___.append((______,____________));______ = ""
        if __:______ += i
    ________ = ((________[:________.find("@")+2]+________[________.find('['):]) if (sum(0 if i == ' ' else 1 for i in ________[________.find('@')+2:________.find('[')])==0) else ________).replace("/"," ").lower()
    ________ = list(________)
    for i in range(len(________)):
        if ________[i] in ('^','~') and ________[i+1] != ' ':
            j = i + 1
            def __(_):
                try:float(_);return True;
                except:return False    
            while __("".join(________[i+1:j+1])):j += 1
            if ________[j] == " ":continue
            else:________.insert(j,' ')
    ________ = "".join(________)
    return (lambda __________________________________________: ([(__________________________________________ := __________________________________________.replace(__,_)) for _,__ in ___[::-1] ][-1] if ___ else __________________________________________))('execute as {0} positioned as @s positioned {1} if block {2} {3} {4} at @s positioned {1} run {5}'.format(________[________.find("execute")+7:(________.find("]") if "[" in ________[:________.find("@")+5] else ________.find("@")+1)+1].strip(),________[(________.find("]") if "[" in ________[:________.find("@")+3] else ________.find("@")+1)+1:________.find("detect")-1].strip()," ".join([ j for i in [[i,] if sum([_.isalpha() for _ in i]) else ((["~"+j for j in i[1:].split("~")] if i.startswith("~") else ["~"+j for j in i.split("~")]) if "~" in i else ([i,] if not "^" in i else (["^"+j for j in i[1:].split("^")] if i.startswith("^") else ["^"+j for j in i.split("^")]))) for i in ________[________.find("detect")+6:].strip().split(" ",4)] for j in i ][0:3])," ".join([ j for i in [[i,] if sum([_.isalpha() for _ in i]) else ((["~"+j for j in i[1:].split("~")] if i.startswith("~") else ["~"+j for j in i.split("~")]) if "~" in i else ([i,] if not "^" in i else (["^"+j for j in i[1:].split("^")] if i.startswith("^") else ["^"+j for j in i.split("^")]))) for i in ________[________.find("detect")+6:].strip().split(" ",4)] for j in i ][3:]).split(" ")[0]," ".join([ j for i in [[i,] if sum([_.isalpha() for _ in i]) else ((["~"+j for j in i[1:].split("~")] if i.startswith("~") else ["~"+j for j in i.split("~")]) if "~" in i else ([i,] if not "^" in i else (["^"+j for j in i[1:].split("^")] if i.startswith("^") else ["^"+j for j in i.split("^")]))) for i in ________[________.find("detect")+6:].strip().split(" ",4)] for j in i ][3:]).split(" ")[1],_(" ".join(" ".join([ j for i in [[i,] if sum([_.isalpha() for _ in i]) else ((["~"+j for j in i[1:].split("~")] if i.startswith("~") else ["~"+j for j in i.split("~")]) if "~" in i else ([i,] if not "^" in i else (["^"+j for j in i[1:].split("^")] if i.startswith("^") else ["^"+j for j in i.split("^")]))) for i in ________[________.find("detect")+6:].strip().split(" ",4)] for j in i ][3:]).split(" ")[2:]))) if 'detect' in ________[:________.find("execute",8) if "execute" in ________[8:] else -1] else 'execute as {0} positioned as @s positioned {1} at @s positioned {1} run {2}'.format(________[________.find("execute")+7:(________.find("]") if "[" in ________[:________.find("@")+5] else ________.find("@")+1)+1].strip(), " ".join([ j for i in [[i,] if sum([_.isalpha() for _ in i]) else ((["~"+j for j in i[1:].split("~")] if i.startswith("~") else ["~"+j for j in i.split("~")]) if "~" in i else ([i,] if not "^" in i else (["^"+j for j in i[1:].split("^")] if i.startswith("^") else ["^"+j for j in i.split("^")]))) for i in ________[(________.find("]") if "]" in ________ else ________.find("@")+1)+1:].strip().split(" ",4)] for j in i ][0:3]),_(" ".join([ j for i in [[i,] if sum([_.isalpha() for _ in i]) else ((["~"+j for j in i[1:].split("~")] if i.startswith("~") else ["~"+j for j in i.split("~")]) if "~" in i else ([i,] if not "^" in i else (["^"+j for j in i[1:].split("^")] if i.startswith("^") else ["^"+j for j in i.split("^")]))) for i in ________[(________.find("]") if "]" in ________ else ________.find("@")+1)+1:].strip().split(" ",4)] for j in i ][3:]))))
while True:
    ____ = open(__:=input("请输入BDX文件地址："),"rb+").read();_____ = ____B.decompress(____[3:]);________________________________________________ = _____ if not b"-----BEGIN RSA PUBLIC KEY-----" in _____ else _____[:_____.find(b"-----BEGIN RSA PUBLIC KEY-----")-_____[:_____.find(b"-----BEGIN RSA PUBLIC KEY-----")][::-1].find(b'X')]+b'E';______ = []
    while b'execute' in ________________________________________________:
        __________ = str(____U.uuid4()).encode("utf-8");____________________________ = ________________________________________________[________________________________________________.find(b"execute"):][:________________________________________________[________________________________________________.find(b"execute"):].find(b'\x00')];________________________________________________ = ________________________________________________.replace(____________________________,__________)
        ______.append((____________________________,__________))
    for ____________________________,__________ in ______:
        ________________________________________________ = ________________________________________________.replace(__________,_(____________________________.decode("utf-8")).encode("utf-8"))
    with open(__,'wb+') as ____________________________________:
        ____________________________________.write(b"BD@"+____B.compress(________________________________________________))
    print('完成')
