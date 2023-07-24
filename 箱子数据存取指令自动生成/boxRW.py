# 适用基岩旧版本指令的容器读写指令生成工具

'''
   Copyright © 2023 金羿Eilles & Team-Ryoun

   Licensed under the Apache License, Version 2.0
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
'''


def formatipt(notice: str, fun, errnote: str = "", *extraArg):
    '''循环输入，以某种格式
    notice: 输入时的提示
    fun: 格式函数
    errnote: 输入不符格式时的提示
    *extraArg: 对于函数的其他参数'''

    '''
    此函数拷贝并修改自 TriM-Organization 的 [伶伦转换器](https://gitee.com/TriM-Organization/Linglun-Converter/blob/master/utils/io.py#L159)
    中的部分代码，已经依照其[开源声明](https://gitee.com/TriM-Organization/Linglun-Converter/blob/master/LICENSE.md)
    中适用特殊授权之款项特殊授权
    若需要拷贝或在别处使用此段代码
    须向原作者请求授权或依照其开源声明从原文件处获取授权
    '''
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
        raise ValueError("参数需为正整数")
    


maxbit = formatipt("请输入二进制位数：",isintPositive,"输入数据需为正整数。")[1]
scoreboard_name = input("请输入计分板名称：")
target_selector = input("请输入玩家选择器：")

# @a[tag=writeInto]

output_file_write = open('out_write.txt','w',encoding="utf-8")

output_file_write.write(f"#\n# 第0位 判断正负\nexecute {target_selector} ~ ~ ~ execute @s[scores="+"{"+scoreboard_name+"=..-1}] ~ ~ ~ replaceitem block ~ ~-3 ~ slot.container 0 destroy minecraft:light_block 0\n")
output_file_write.write(f"# CDT\n")
output_file_write.write(f"execute {target_selector} ~ ~ ~ scoreboard players operation @s {scoreboard_name} *= n-1 {scoreboard_name}\n")


for i in range(1,maxbit+1):
    output_file_write.write(f"#\n# 第{i}位 计算 [{int(2**(i-1))},{2**(i)})\n"+(f"execute {target_selector} ~ ~ ~ scoreboard players operation @s {scoreboard_name} /= n2 {scoreboard_name}\n" if i != 1 else "")+f"execute {target_selector} ~ ~ ~ scoreboard players operation @s {scoreboard_name}_c = @s {scoreboard_name}\nexecute {target_selector} ~ ~ ~ scoreboard players operation @s {scoreboard_name}_c %= n2 {scoreboard_name}\n")
    output_file_write.write(f"execute {target_selector} ~ ~ ~ execute @s[scores={'{'+scoreboard_name+'_c=0}'}] ~ ~ ~ replaceitem block ~ ~-{3+int(i/27)} ~ slot.container {i%27} destroy minecraft:light_block {i} {int((i-1)/4+1)}\n")



output_file_write.write(f"\nscoreboard players set n2 {scoreboard_name} 2")

output_file_write.close()



output_file_read = open('out_read.txt','w',encoding="utf-8")

for i in range(1,maxbit+1):
    output_file_read.write(f"#\n# 第{i}位 计算 [{int(2**(i-1))},{2**(i)})\nexecute {target_selector} ~ ~ ~ replaceitem block ~ ~-{3+int(i/27)} ~ slot.container {i%27} keep air 1\n")
    output_file_read.write(f"# CDT\n")
    output_file_read.write(f"execute {target_selector} ~ ~ ~ scoreboard players add @s {scoreboard_name} {2**(i-1)}\n")


output_file_read.write(f"# 第0位 负数判断\nexecute {target_selector} ~ ~ ~ replaceitem block ~ ~-3 ~ slot.container 0 keep air 1\n")
output_file_read.write(f"# CDT\n")
output_file_read.write(f"execute {target_selector} ~ ~ ~ scoreboard players operation @s {scoreboard_name} *= n-1 {scoreboard_name}\n\n")

output_file_read.write(f"scoreboard players set n-1 {scoreboard_name} -1")

output_file_read.close()