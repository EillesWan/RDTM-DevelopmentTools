#-*-coding:utf-8-*-

import time
from Tpack.TXTSlice import TSTXTSlice
from Tpack.TitleColor import InsertColor
from Tpack.BatchGenerateTS import BatchTitle,BatchSubtitle

timeNow=time.localtime(time.time())
GlobaltimeNow=time.strftime('[%Y-%m-%d %H:%M:%S]',timeNow)

ChooseCleartext=input("输入1清除AutoT.mcfunction里的指令\n"
                      "回车取消清除：")
if ChooseCleartext=="1":
    ClearText=open('AutoT.mcfunction','w')
    ClearText.write('')
    ClearText.close()
    print(" 已清除AutoT.mcfunction文件里的字符串")
elif ChooseCleartext=="":
    print(" 已取消清除AutoT.mcfunction文件里的字符串")
else:
    print(" 没有选择")

InputTitle=[]
InputSubTitle=[]

ChooseOpenInputTitle=open('Input/InputTitle.TXT','r')
ChooseOpenInputSubTitle=open('Input/InputSubtitle.TXT','r')
TSTXTSlice(ChooseOpenInputTitle,InputTitle)
TSTXTSlice(ChooseOpenInputSubTitle,InputSubTitle)
print(" 已读取Input/InputTitle.TXT和Input/InputSubtitle.TXT")

input_score=str(input("输入计分板名称(必填)："))
input_exe=str(input("输入选择器(注意:加[])："))

CountLenTitle = -1
CountLenSubtitle = -1
score_num_t = 0
score_num_s = 0

i=0
while i<1:
    CountLenTitle+=1
    CountLenSubtitle+=1

    list_title = []
    list_subtitle = []

    if CountLenTitle>=InputTitle.__len__() and CountLenSubtitle>=InputSubTitle.__len__():
        i=1

    for frence_t in InputTitle[CountLenTitle]:
        list_title.append(frence_t)
    for frence_s in InputSubTitle[CountLenSubtitle]:
        list_subtitle.append(frence_s)

    InsertColor(list_title)
    InsertColor(list_subtitle)

    TReplacementlist = []
    SReplacementlist = []
    TReplacementStr = ''
    SReplacementStr = ''
    for TTraversalReplacement in range(len(list_title)):
        TReplacementStr = TReplacementStr + list_title[TTraversalReplacement]
        TReplacementlist.append(TReplacementStr)
    for STraversalReplacement in range(len(list_subtitle)):
        SReplacementStr = SReplacementStr + list_subtitle[STraversalReplacement]
        SReplacementlist.append(SReplacementStr)
    list_title = TReplacementlist
    list_subtitle = SReplacementlist

    if InputTitle[CountLenTitle] != '':
        for ergodic_t in list_title:
            if input_score != "":
                if len(list_title) == 0:
                    break
                else:
                    if len(InputTitle[CountLenTitle]) > len(InputSubTitle[CountLenSubtitle]):
                        score_num_t += 1
                        BatchTitle(input_exe, input_score, score_num_t, ergodic_t)
                    elif len(InputSubTitle[CountLenSubtitle]) > len(InputTitle[CountLenTitle]):
                        score_num_t = int(score_num_t + (len(InputSubTitle[CountLenSubtitle])) / (len(InputTitle[CountLenTitle])))
                        BatchTitle(input_exe, input_score, score_num_t, ergodic_t)
                    elif len(InputSubTitle[CountLenSubtitle]) == 0:
                        score_num_t += 1
                        BatchTitle(input_exe, input_score, score_num_t, ergodic_t)
                    elif len(InputTitle[CountLenTitle]) == len(InputSubTitle[CountLenSubtitle]):
                        score_num_t += 1
                        BatchTitle(input_exe, input_score, score_num_t, ergodic_t)
                    else:
                        print("报错7")
            else:
                print("报错2")
    elif InputTitle[CountLenTitle] == "":
        ""
    else:
        print("报错5")

    if InputSubTitle[CountLenSubtitle] != '':
        for ergodic_s in list_subtitle:
            if input_score != "":
                if len(list_subtitle) == 0:
                    break
                else:
                    if len(InputSubTitle[CountLenSubtitle]) > len(InputTitle[CountLenTitle]):
                        score_num_s += 1
                        BatchSubtitle(input_exe, input_score, score_num_s, ergodic_s)
                    elif len(InputTitle[CountLenTitle]) > len(InputSubTitle[CountLenSubtitle]):
                        score_num_s = int(score_num_s + (len(InputTitle[CountLenTitle])) / (len(InputSubTitle[CountLenSubtitle])))
                        BatchSubtitle(input_exe, input_score, score_num_s, ergodic_s)
                    elif len(InputTitle[CountLenTitle]) == 0:
                        score_num_s += 1
                        BatchSubtitle(input_exe, input_score, score_num_s, ergodic_s)
                    elif len(InputSubTitle[CountLenSubtitle]) == len(InputTitle[CountLenTitle]):
                        score_num_s += 1
                        BatchSubtitle(input_exe, input_score, score_num_s, ergodic_s)
                    else:
                        print("报错6")
            else:
                print("报错3")
    elif InputSubTitle[CountLenSubtitle] == "":
        ""
    else:
        print("报错4")

exit()