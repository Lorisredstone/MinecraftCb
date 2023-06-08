get = input("Enter the block you want to convert: ")
# get = """/setblock -8 57 4 minecraft:repeating_command_block[conditional=false,facing=south]{Command:"execute if score TEMP2 constants matches 0 run setblock ~ ~-1 ~ air",CustomName:'{"text":"@"}',LastExecution:263724L,LastOutput:'{"extra":[{"translate":"commands.setblock.success","with":["-8","56","4"]}],"text":"[13:41:20] "}',SuccessCount:1,TrackOutput:1b,UpdateLastExecution:1b,auto:0b,conditionMet:1b,powered:0b}"""
# /setblock -8 57 4 minecraft:repeating_command_block[conditional=false,facing=south]{Command:"execute if score TEMP2 constants matches 0 run setblock ~ ~-1 ~ air",CustomName:'{"text":"@"}',LastExecution:263724L,LastOutput:'{"extra":[{"translate":"commands.setblock.success","with":["-8","56","4"]}],"text":"[13:41:20] "}',SuccessCount:1,TrackOutput:1b,UpdateLastExecution:1b,auto:0b,conditionMet:1b,powered:0b}
x = int(get.split(" ")[1])
y = int(get.split(" ")[2])
z = int(get.split(" ")[3])
print(x-0, y-58, z-0)

import re
# the name of the block
name = re.findall(r"minecraft:(\w+)", get)[0]
command = re.findall(r"Command:\"([^\"]+)\"", get)[0]
settings = "["+re.findall(r"\[([^\]]+)\]", get)[0]+"]"
auto = re.findall(r"auto:(\d+)", get)[0]
new_command = f"\"setblock ~{x} ~{y-58} ~{z} {name}{settings}"+r"{"+f"auto:{auto}b,Command:\\\"{command}\\\""+"} destroy\","
print(new_command)
import pyperclip
pyperclip.copy(new_command)