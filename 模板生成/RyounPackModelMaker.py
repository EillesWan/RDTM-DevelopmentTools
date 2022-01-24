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



import os, uuid, random



SameUuid = uuid.uuid4()
behaviorUuid = uuid.uuid4()
resourceUuid = uuid.uuid4()
dmValue = str(random.randint(233, 99999))


TempBehaviorDirs = [
    "animation_controllers",
    "animations",
    "config",
    "entities",
    "functions",
    "loot_tables/blocks",
    "loot_tables/chests",
    "loot_tables/entities",
    "loot_tables/equipment",
    "loot_tables/gameplay",
    "spawn_rules",
    "structures",
    "trading/economy_trades"
]
for BehaviorDirs in TempBehaviorDirs:
    try:
        os.makedirs("./RyounPack/behavior_packs/Ryoun/"+ str(BehaviorDirs) +"")
    except:
        pass


TempResourceDirs = [
    "animation_controllers",
    "animations",
    "attachables",
    "effects",
    "entity",
    "materials",
    "models/entity",
    "particles",
    "render_controllers",
    "shaders/glsl",
    "sounds",
    "texts",
    "textures/blocks",
    "textures/blocksmodel",
    "textures/entity",
    "textures/environment",
    "textures/gui",
    "textures/items",
    "textures/models",
    "textures/particles",
    "textures/sfxs",
    "textures/ui",
    "ui"
]
for ResourceDirs in TempResourceDirs:
    try:
        os.makedirs("./RyounPack/resource_packs/Ryoun/"+ str(ResourceDirs) +"")
    except:
        pass
open("./RyounPack/resource_packs/Ryoun/biomes_client.json","w",encoding='UTF-8').write("{  \"biomes\": {    \"\": {    }  }}")
open("./RyounPack/resource_packs/Ryoun/blocks.json","w",encoding='UTF-8').write("{\n  \n}")
open("./RyounPack/resource_packs/Ryoun/models/netease_models.json","w",encoding='UTF-8').write("{\n  \n}")
open("./RyounPack/resource_packs/Ryoun/sounds/sound_definitions.json","w",encoding='UTF-8').write("{\n  \n}")
open("./RyounPack/resource_packs/Ryoun/sounds.json","w",encoding='UTF-8').write("{\n  \n}")
open("./RyounPack/resource_packs/Ryoun/texts/zh_CN.lang","w",encoding='UTF-8')
open("./RyounPack/resource_packs/Ryoun/textures/flipbook_textures.json","w",encoding='UTF-8').write("[\n  {\n    \"atlas_tile\": \"\",\n    \"flipbook_texture\": \"textures/blocks/\",\n    \"ticks_per_frame\": \n  }\n]")
open("./RyounPack/resource_packs/Ryoun/textures/item_texture.json","w",encoding='UTF-8').write("{\n  \"resource_packs_name\": \"RyounPack\",\n  \"texture_name\": \"atlas.items\",\n  \"texture_data\": {\n    \"\": {\n      \"textures\": \"textures/items/\"\n    }\n  }\n}")
open("./RyounPack/resource_packs/Ryoun/textures/terrain_texture.json","w",encoding='UTF-8').write("{\n  \"resource_packs_name\": \"RyounPack\",\n  \"texture_name\": \"atlas.terrain\",\n  \"texture_data\": {\n    \"\": {\n      \"textures\": \"textures/blocks/\"\n    }\n  }\n}")
open("./RyounPack/resource_packs/Ryoun/ui/_ui_defs.json","w",encoding='UTF-8').write("{\n  \"ui_defs\": [\n    \"ui/.json\"\n  ]\n}")
open("./RyounPack/behavior_packs/Ryoun/manifest.json","w",encoding='UTF-8').write("{\n  \"format_version\": 1,\n  \"header\": {\n    \"description\": \"Ryoun Pack : behavior pack\",\n    \"version\": [ 0, 0, 1 ],\n    \"name\": \"RyounPack\",\n    \"uuid\": \""+ str(behaviorUuid) +"\"\n  },\n  \"modules\": [\n    {\n      \"description\": \"Ryoun Pack : behavior pack\",\n      \"type\": \"data\",\n      \"version\": [ 0, 0, 1 ],\n      \"uuid\": \""+ str(SameUuid) +"\"\n    }\n  ]\n}")
open("./RyounPack/resource_packs/Ryoun/manifest.json","w",encoding='UTF-8').write("{\n  \"format_version\": 1,\n  \"header\": {\n    \"description\": \"Ryoun Pack : resource pack\",\n    \"version\": [ 0, 0, 1 ],\n    \"name\": \"RyounPack\",\n    \"uuid\": \""+ str(resourceUuid) +"\"\n  },\n  \"modules\": [\n    {\n      \"description\": \"Ryoun Pack : resource pack\",\n      \"type\": \"resources\",\n      \"version\": [ 0, 0, 1 ],\n      \"uuid\": \""+ str(SameUuid) +"\"\n    }\n  ]\n}")
open("./RyounPack/world_behavior_packs.json","w",encoding='UTF-8').write("[\n  {\"pack_id\": \""+ str(behaviorUuid) +"\",\n  \"version\": [ 0, 0, 1 ]}\n]")
open("./RyounPack/world_resource_packs.json","w",encoding='UTF-8').write("[\n  {\"pack_id\": \""+ str(resourceUuid) +"\",\n  \"version\": [ 0, 0, 1 ]}\n]")
open("./RyounPack/behavior_packs/Ryoun/functions/Hello_World.mcfunction","w",encoding='UTF-8').write('''
say Hello World!
tell @a Hello World!
me Hello World!
title @a title Hello World!
title @a actionbar Hello World!
title @a subtitle Hello World!''')

open("./RyounPack/behavior_packs/Ryoun/functions/test.mcfunction","w",encoding='UTF-8').write('''tellraw @a {"rawtext":[{"text":"Hello World!\\n§b§lRyounForever!\\n§l§b凌云永存！\\n§b§l凌雲永存！"}]}''')

open("./RyounPack/behavior_packs/Ryoun/pack_icon.png","w",encoding='UTF-8').write('')
open("./RyounPack/resource_packs/Ryoun/pack_icon.png","w",encoding='UTF-8').write('')