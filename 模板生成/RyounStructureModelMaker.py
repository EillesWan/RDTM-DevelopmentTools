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


import os, uuid

behaviorUuid = uuid.uuid4()

packname = input("The pack's name:")

try:
    os.makedirs("./Ryoun"+packname+"Pack/behavior_packs/Ryoun"+packname+"/structures")
except:
    pass

open("./Ryoun"+packname+"Pack/world_behavior_packs.json","w",encoding='UTF-8').write("[\n  {\"pack_id\": \""+ str(behaviorUuid) +"\",\n  \"version\": [ 0, 0, 1 ]}\n]")

open("./Ryoun"+packname+"Pack/behavior_packs/Ryoun"+packname+"/manifest.json","w",encoding='UTF-8').write("{\n  \"format_version\": 1,\n  \"header\": {\n    \"description\": \"This Pack is only for loading structures\",\n    \"version\": [ 0, 0, 1 ],\n    \"name\": \"Ryoun"+packname+"Pack\",\n    \"uuid\": \""+ str(behaviorUuid) +"\"\n  },\n  \"modules\": [\n    {\n      \"description\": \"Ryoun "+packname+" Pack : behavior pack\",\n      \"type\": \"data\",\n      \"version\": [ 0, 0, 1 ],\n      \"uuid\": \""+ str(uuid.uuid4()) +"\"\n    }\n  ]\n}")


open("./Ryoun"+packname+"Pack/behavior_packs/Ryoun"+packname+"/structures/empty.mcstructure","w",encoding='UTF-8').write('''''')
