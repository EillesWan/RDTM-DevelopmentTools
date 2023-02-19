

with open(input("月度汇总文件："),'r',encoding='utf-8') as f:
    final_data_list = [["".join(j.split('"')).strip("﻿") for j in i.split(',')] for i in f.read().strip().split('\n')[1:]]

data_dict = {}
for piece in final_data_list:
    try:
        data_dict[int(piece[0])][1][int(piece[1])] = int(piece[-1])
    except:
        data_dict[int(piece[0])] = [piece[2],{int(piece[1]):int(piece[-1])}]


print(data_dict)