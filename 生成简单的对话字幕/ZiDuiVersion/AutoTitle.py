from Tpack.BatchGenerateTitle import BatchTitle
from Tpack.BatchGenerateSubtitle import BatchSubtitle
from Tpack.TitleColor import InsertColor

input_title=str(input("输入主标题："))
input_subtitle=str(input("输入副标题："))
input_score=str(input("输入计分板名称(必填)："))
input_exe=str(input("输入选择器(注意:加[])："))

if len(input_title)>len(input_subtitle):
    interval=len(input_subtitle)/len(input_title)
elif len(input_subtitle)>len(input_title):
    interval=len(input_title)/len(input_subtitle)
elif len(input_title)==len(input_subtitle):
    interval=1
else:
    print("报错1")

list_title=[]
list_subtitle=[]
score_num_t=0
score_num_s=0
interval=0

for frence_t in input_title:
    list_title.append(frence_t)
for frence_s in input_subtitle:
    list_subtitle.append(frence_s)

InsertColor(list_title)
InsertColor(list_subtitle)

TReplacementlist=[]
SReplacementlist=[]
TReplacementStr=''
SReplacementStr=''
for TTraversalReplacement in range(len(list_title)):
    TReplacementStr=TReplacementStr+list_title[TTraversalReplacement]
    TReplacementlist.append(TReplacementStr)
for STraversalReplacement in range(len(list_subtitle)):
    SReplacementStr=SReplacementStr+list_subtitle[STraversalReplacement]
    SReplacementlist.append(SReplacementStr)
list_title=TReplacementlist
list_subtitle=SReplacementlist


if  input_title!='':
    for ergodic_t in list_title:
        if input_score!="":
            if len(list_title)==0:
                break
            else:
                if len(input_title)>len(input_subtitle):
                    score_num_t+=1
                    BatchTitle(input_exe,input_score,score_num_t,ergodic_t)
                elif len(input_subtitle)>len(input_title):
                    score_num_t=int(score_num_t+(len(input_subtitle))/(len(input_title)))
                    BatchTitle(input_exe, input_score, score_num_t, ergodic_t)
                elif len(input_subtitle)==0:
                    score_num_t+=1
                    BatchTitle(input_exe, input_score, score_num_t, ergodic_t)
                elif len(input_title)==len(input_subtitle):
                    score_num_t += 1
                    BatchTitle(input_exe, input_score, score_num_t, ergodic_t)
                else:
                    print("报错7")
        else:
            print("报错2")
elif input_title=="":
    ""
else:
    print("报错5")

if input_subtitle!='':
    for ergodic_s in list_subtitle:
        if input_score!="":
            if len(list_subtitle)==0:
                break
            else:
                if len(input_subtitle)>len(input_title):
                    score_num_s += 1
                    BatchSubtitle(input_exe,input_score,score_num_s,ergodic_s)
                elif len(input_title)>len(input_subtitle):
                    score_num_s=int(score_num_s+(len(input_title))/(len(input_subtitle)))
                    BatchSubtitle(input_exe, input_score, score_num_s, ergodic_s)
                elif len(input_title)==0:
                    score_num_s += 1
                    BatchSubtitle(input_exe, input_score, score_num_s, ergodic_s)
                elif len(input_subtitle)==len(input_title):
                    score_num_s += 1
                    BatchSubtitle(input_exe, input_score, score_num_s, ergodic_s)
                else:
                    print("报错6")
        else:
            print("报错3")
elif input_subtitle=="":
    ""
else:
    print("报错4")

input("")