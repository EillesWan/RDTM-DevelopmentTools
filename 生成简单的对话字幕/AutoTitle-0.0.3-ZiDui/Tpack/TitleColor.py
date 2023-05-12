def InsertColor(Afterlist):
    colorlist=[]
    Standby_Str1=''
    Standby_Str2=''
    indexnum=0
    for Tergodic in range(Afterlist.__len__()):
        subscript = 0
        while True:
            print("回车继续给下一个字符效果\n"
                  "效果：k 英文乱码 l 粗体字 o 斜体字\n"
                  "颜色：1 深蓝色  2 绿色  3 海蓝色  4 红色\n"
                  "5 玫瑰红  6 橙色  7 银色  8 灰色  9 紫浅蓝\n"
                  "0 粗黑体  a 亮绿色  b 天蓝色  c 果红色\n"
                  "d 粉红色  e 金黄色  f 白色  r 黑色")
            Insert_inputColor = str(input("输入 " + Afterlist[indexnum]+ " 的颜色或效果(输入数字或字母):"))
            if Insert_inputColor=="k" or Insert_inputColor=="l" or  Insert_inputColor=="o" or Insert_inputColor=="1" or Insert_inputColor=="2" or Insert_inputColor=="3" or Insert_inputColor=="4" or Insert_inputColor=="5" or Insert_inputColor=="6" or Insert_inputColor=="7" or Insert_inputColor=="8" or  Insert_inputColor=="9" or Insert_inputColor=="0" or Insert_inputColor=="a" or Insert_inputColor=="b" or Insert_inputColor=="c" or Insert_inputColor=="d" or Insert_inputColor=="e" or Insert_inputColor=="f" or Insert_inputColor=="r":
                if subscript==0:
                    Standby_Str1 = "§" + Insert_inputColor + Afterlist[indexnum]
                    subscript+=1
                elif subscript>0:
                    Standby_Str1="§" + Insert_inputColor +Standby_Str1
            elif Insert_inputColor=="":
                if len(Standby_Str1)==0:
                    colorlist.append(Afterlist[indexnum])
                    break
                elif len(Standby_Str1)>0:
                    colorlist.append(Standby_Str1)
                    break
            else:
                print("函数错误InsertColor")
        indexnum+=1
    Afterlist.clear()
    Afterlist.extend(colorlist)