def formatipt(notice: str, fun, errnote: str = "", *extraArg):
    '''循环输入，以某种格式
    notice: 输入时的提示
    fun: 格式函数abc
    errnote: 输入不符格式时的提示
    *extraArg: 对于函数的其他参数'''
    while True:
        result = input(notice)
        try:
            funresult = fun(result, *extraArg)
            break
        except:
            print(errnote)
            continue
    return result, funresult

def isintPositive(sth: str):
    if int(sth) > 0:
        return int(sth)
    else:
        raise
    


maxbit = formatipt("请输入二进制位数：",isintPositive,"输入数据需为正整数。")[1]
scoreboard_name = input("请输入计分板名称：")
target_selector = input("请输入玩家选择器：")

output_file_read = open('out.txt','w',encoding="utf-8")

for i in range(1,maxbit+1):
    output_file_read.write(f"#\n# 第{i}位 计算 [{int(2**(i-1))},{2**(i)})\nexecute {target_selector} ~ ~ ~ replaceitem block ~ ~-{3+int(i/27)} ~ slot.container {i%27} keep air 1\n")
    output_file_read.write(f"# CDT\n")
    output_file_read.write(f"execute {target_selector} ~ ~ ~ scoreboard players add @s {scoreboard_name} {2**(i-1)}\n")


output_file_read.write(f"# 第0位 负数判断\nexecute {target_selector} ~ ~ ~ replaceitem block ~ ~-3 ~ slot.container 0 keep air 1\n")
output_file_read.write(f"# CDT\n")
output_file_read.write(f"execute {target_selector} ~ ~ ~ scoreboard players operation @s {scoreboard_name} *= n-1 {scoreboard_name}\n\n")

output_file_read.write(f"scoreboard players set n-1 {scoreboard_name} -1")

output_file_read.close()