summon falling_block ~ ~1 ~ {Time:1,BlockState:{Name:redstone_block},Passengers:[{id:falling_block,Passengers:[{id:falling_block,Time:1,BlockState:{Name:activator_rail},Passengers:[{id:command_block_minecart,Command:'tellraw @a {"text":"D�but de l\'initialisation","color":"red"}'},{id:command_block_minecart,Command:'scoreboard objectives remove stack'},{id:command_block_minecart,Command:'scoreboard objectives remove constants'},{id:command_block_minecart,Command:'scoreboard objectives add stack dummy'},{id:command_block_minecart,Command:'scoreboard players set ELEMENT0 stack 0'},{id:command_block_minecart,Command:'scoreboard players set ELEMENT1 stack 0'},{id:command_block_minecart,Command:'scoreboard players set ELEMENT2 stack 0'},{id:command_block_minecart,Command:'scoreboard players set ELEMENT3 stack 0'},{id:command_block_minecart,Command:'scoreboard players set ELEMENT4 stack 0'},{id:command_block_minecart,Command:'scoreboard players set ELEMENT5 stack 0'},{id:command_block_minecart,Command:'scoreboard players set ELEMENT6 stack 0'},{id:command_block_minecart,Command:'scoreboard players set ELEMENT7 stack 0'},{id:command_block_minecart,Command:'scoreboard players set ELEMENT8 stack 0'},{id:command_block_minecart,Command:'scoreboard players set ELEMENT9 stack 0'},{id:command_block_minecart,Command:'scoreboard players set SIZE stack 0'},{id:command_block_minecart,Command:'scoreboard objectives add constants dummy'},{id:command_block_minecart,Command:'scoreboard objectives setdisplay sidebar constants'},{id:command_block_minecart,Command:'scoreboard players set PUSH_VALUE constants 0'},{id:command_block_minecart,Command:'scoreboard players set INST_COUNT constants 0'},{id:command_block_minecart,Command:'setblock ~ ~-2 ~5 command_block[facing=south]{auto:0,Command:"say PUSH"} destroy'},{id:command_block_minecart,Command:'setblock ~ ~-1 ~4 command_block[facing=up]{auto:0,Command:"setblock ~ ~-1 ~ air"} destroy'},{id:command_block_minecart,Command:'setblock ~-4 ~-2 ~5 command_block[facing=south]{auto:0,Command:"tellraw @a {\\"text\\":\\"Load de la prochaine instruction\\",\\"color\\":\\"green\\"}"} destroy'},{id:command_block_minecart,Command:'setblock ~-4 ~-1 ~4 command_block[facing=up]{auto:0,Command:"setblock ~ ~-1 ~ air"} destroy'},{id:command_block_minecart,Command:'setblock ~-4 ~-2 ~6 chain_command_block[facing=south]{auto:1,Command:"summon armor_stand ~6 ~ ~-6"} destroy'},{id:command_block_minecart,Command:'tellraw @a {"text":"Fin de l\'initialisation","color":"red"}'},{id:command_block_minecart,Command:'setblock ~3 ~-2 ~0 command_block[facing=east]{auto:0,Command:"tellraw @a {\\"text\\":\\"Push int 1\\",\\"color\\":\\"green\\"}"} destroy'},{id:command_block_minecart,Command:'setblock ~4 ~-2 ~0 chain_command_block[facing=east,conditional=true]{auto:1,Command:"scoreboard players set PUSH_VALUE constants 1"} destroy'},{id:command_block_minecart,Command:'setblock ~5 ~-2 ~0 chain_command_block[facing=east,conditional=true]{auto:1,Command:"setblock ~-5 ~ ~4 redstone_block"} destroy'},{id:command_block_minecart,Command:'setblock ~6 ~-2 ~0 chain_command_block[facing=east,conditional=true]{auto:1,Command:"setblock ~-4 ~ ~ air"} destroy'},{id:command_block_minecart,Command:'setblock ~3 ~-2 ~1 command_block[facing=east]{auto:0,Command:"tellraw @a {\\"text\\":\\"Push int 2\\",\\"color\\":\\"green\\"}"} destroy'},{id:command_block_minecart,Command:'setblock ~4 ~-2 ~1 chain_command_block[facing=east,conditional=true]{auto:1,Command:"scoreboard players set PUSH_VALUE constants 2"} destroy'},{id:command_block_minecart,Command:'setblock ~5 ~-2 ~1 chain_command_block[facing=east,conditional=true]{auto:1,Command:"setblock ~-5 ~ ~3 redstone_block"} destroy'},{id:command_block_minecart,Command:'setblock ~6 ~-2 ~1 chain_command_block[facing=east,conditional=true]{auto:1,Command:"setblock ~-4 ~ ~ air"} destroy'},{id:command_block_minecart,Command:'setblock ~3 ~-2 ~2 command_block[facing=east]{auto:0,Command:"tellraw @a {\\"text\\":\\"Push int 3\\",\\"color\\":\\"green\\"}"} destroy'},{id:command_block_minecart,Command:'setblock ~4 ~-2 ~2 chain_command_block[facing=east,conditional=true]{auto:1,Command:"scoreboard players set PUSH_VALUE constants 3"} destroy'},{id:command_block_minecart,Command:'setblock ~5 ~-2 ~2 chain_command_block[facing=east,conditional=true]{auto:1,Command:"setblock ~-5 ~ ~2 redstone_block"} destroy'},{id:command_block_minecart,Command:'setblock ~6 ~-2 ~2 chain_command_block[facing=east,conditional=true]{auto:1,Command:"setblock ~-4 ~ ~ air"} destroy'},{id:command_block_minecart,Command:'data merge block ~ ~-2 ~ {auto:0}'},{id:command_block_minecart,Command:'setblock ~ ~1 ~ command_block{auto:1,Command:"fill ~ ~ ~ ~ ~-3 ~ air"}'},{id:command_block_minecart,Command:'kill @e[type=command_block_minecart,distance=..1]'},{id:command_block_minecart,Command:'kill @e[type=falling_block,distance=..1]'},]}]}]}