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

# @a[tag=writeInto]

output_file_write = open('out.txt','w',encoding="utf-8")

output_file_write.write(f"#\n# 第0位 判断正负\nexecute {target_selector} ~ ~ ~ execute @s[scores="+"{"+scoreboard_name+"=..-1}] ~ ~ ~ replaceitem block ~ ~-3 ~ slot.container 0 destroy minecraft:light_block 0\n")
output_file_write.write(f"# CDT\n")
output_file_write.write(f"execute {target_selector} ~ ~ ~ scoreboard players operation @s {scoreboard_name} *= n-1 {scoreboard_name}\n")


for i in range(1,maxbit+1):
    output_file_write.write(f"#\n# 第{i}位 计算 [{int(2**(i-1))},{2**(i)})\n"+(f"execute {target_selector} ~ ~ ~ scoreboard players operation @s {scoreboard_name} /= n2 {scoreboard_name}\n" if i != 1 else "")+f"execute {target_selector} ~ ~ ~ scoreboard players operation @s {scoreboard_name}_c = @s {scoreboard_name}\nexecute {target_selector} ~ ~ ~ scoreboard players operation @s {scoreboard_name}_c %= n2 {scoreboard_name}\n")
    output_file_write.write(f"execute {target_selector} ~ ~ ~ execute @s[scores={'{'+scoreboard_name+'_c=0}'}] ~ ~ ~ replaceitem block ~ ~-{3+int(i/27)} ~ slot.container {i%27} destroy minecraft:light_block {i} {int((i-1)/4+1)}\n")



output_file_write.write(f"\nscoreboard players set n2 {scoreboard_name} 2")

output_file_write.close()


