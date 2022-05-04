# -*- coding: utf-8 -*-

'''

   Copyright 2022 Team-Ryoun

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

'''


input('''使用计分板生成一组简单的字幕''')

# 注意，下面只是样例，请自己看着写

s = 'Once upon a time, there was a beautiful princess lived in a castle.'

cmdlst = []

for i in range(len(s)):
    cmdlst.append('execute @a[scores={}] ~ ~ ~ title @s actionbar '+s[0:i+1])

print(cmdlst)

