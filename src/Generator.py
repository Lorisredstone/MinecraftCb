from typing import List, Tuple, Callable
import mod.colorprint as colorprint
import src.Tokens as Tokens

BRA_O, BRA_F, BACKSLASH = "{", "}", "\\"
print_color = lambda text, color, level : f"tellraw @a {BRA_O}{BACKSLASH*2**(level) if level else ''}\"text{BACKSLASH*2**(level) if level else ''}\":{BACKSLASH*2**(level) if level else ''}\"%s{BACKSLASH*2**(level) if level else ''}\",{BACKSLASH*2**(level) if level else ''}\"color{BACKSLASH*2**(level) if level else ''}\":{BACKSLASH*2**(level) if level else ''}\"%s{BACKSLASH*2**(level) if level else ''}\"{BRA_F}" % (text, color)

STACK_PUSH:List[str] = [
    "setblock ~ ~-2 ~5 command_block[facing=south]{auto:0,Command:\"say\"} destroy",
    "setblock ~ ~-1 ~4 command_block[facing=up]{auto:0,Command:\"setblock ~ ~-1 ~ air\"} destroy",
    "setblock ~0 ~-2 ~6 chain_command_block[conditional=false,facing=south]{auto:1b,Command:\"scoreboard players add INST_COUNT constants 1\"} destroy",
    "setblock ~0 ~-2 ~7 chain_command_block[conditional=false,facing=south]{auto:1b,Command:\"setblock ~-4 ~ ~-3 minecraft:redstone_block\"} destroy",
]

NEXT_INST:List[str] = [
    "setblock ~-4 ~-2 ~5 command_block[facing=south]{auto:0,Command:\"%s\"} destroy"
    # % print_color("Load de la prochaine instruction", "green", 1),
    % "say",
    "setblock ~-4 ~-1 ~4 command_block[facing=up]{auto:0,Command:\"setblock ~ ~-1 ~ air\"} destroy",
    "setblock ~-4 ~-2 ~6 chain_command_block[facing=south]{auto:1,Command:\"summon armor_stand ~6 ~ ~-7\"} destroy",
    "setblock ~-4 ~-2 ~7 chain_command_block[facing=south]{auto:1,Command:\"setblock ~-1 ~ ~-3 redstone_block\"} destroy",
    "setblock ~-5 ~-2 ~5 repeating_command_block[facing=south]{auto:0,Command:\"execute if score INST_COUNT constants > 0 constants run scoreboard players remove INST_COUNT constants 1\"} destroy",
    "setblock ~-5 ~-2 ~6 chain_command_block[facing=south,conditional=true]{auto:1,Command:\"scoreboard players add TEMP1 constants 1\"} destroy",
    "setblock ~-5 ~-2 ~7 chain_command_block[facing=south,conditional=true]{auto:1,Command:\"scoreboard players add TEMP2 constants 1\"} destroy",
    "setblock ~-6 ~-2 ~4 repeating_command_block[conditional=false,facing=south]{auto:0b,Command:\"execute if score INST_COUNT constants matches 0 run setblock ~1 ~ ~ air\"} destroy",
    "setblock ~-6 ~-2 ~5 chain_command_block[facing=south,conditional=true]{auto:1,Command:\"setblock ~-1 ~ ~ minecraft:redstone_block\"} destroy",
    "setblock ~-6 ~-2 ~6 chain_command_block[facing=south]{auto:0,Command:\"execute if score INST_COUNT constants matches 0 run setblock ~1 ~ ~ air\"} destroy",
    "setblock ~-7 ~-2 ~6 repeating_command_block[conditional=false,facing=south]{auto:0b,Command:\"execute if score TEMP1 constants > 0 constants run scoreboard players remove TEMP1 constants 1\"} destroy",
    "setblock ~-7 ~-2 ~7 chain_command_block[conditional=true,facing=south]{auto:1b,Command:\"scoreboard players add INST_COUNT constants 1\"} destroy",
    "setblock ~-7 ~-1 ~6 chain_command_block[conditional=true,facing=south]{auto:1b,Command:\"setblock ~-1 ~-1 ~-2 minecraft:redstone_block\"} destroy",
    "setblock ~-7 ~-1 ~5 repeating_command_block[conditional=false,facing=south]{auto:0b,Command:\"execute if score TEMP1 constants matches 0 run setblock ~ ~-1 ~ air\"} destroy",
    "setblock ~-8 ~-1 ~4 repeating_command_block[conditional=false,facing=south]{auto:0b,Command:\"execute if score TEMP2 constants matches 0 run setblock ~ ~-1 ~ air\"} destroy",
    "setblock ~-8 ~-1 ~5 chain_command_block[conditional=true,facing=south]{auto:1b,Command:\"execute at @e[type=minecraft:armor_stand] run setblock ~ ~ ~ minecraft:redstone_block\"} destroy",
    "setblock ~-8 ~-2 ~5 repeating_command_block[conditional=false,facing=south]{auto:0b,Command:\"execute if score TEMP2 constants > 0 constants run execute as @e[type=minecraft:armor_stand] run execute at @s run tp @s ~ ~ ~1\"} destroy",
    "setblock ~-8 ~-1 ~6 chain_command_block[conditional=true,facing=south]{auto:1b,Command:\"kill @e[type=minecraft:armor_stand]\"} destroy",
    "setblock ~-8 ~-2 ~6 chain_command_block[conditional=true,facing=south]{auto:1b,Command:\"scoreboard players remove TEMP2 constants 1\"} destroy",
]

INIT:List[str] = [
    print_color("Début de l\\'initialisation", "red", 0),
    # création des scoreboard
    "scoreboard objectives remove stack",
    "scoreboard objectives remove constants",
    # setup de la stack
    "scoreboard objectives add stack dummy",
    *[f"scoreboard players set ELEMENT{i} stack 0" for i in range(10)],
    "scoreboard players set SIZE stack 0",
    "scoreboard objectives add constants dummy",
    "scoreboard objectives setdisplay sidebar constants",
    # on met les constantes
    "scoreboard players set 0 constants 0",
    "scoreboard players set TEMP1 constants 0",
    "scoreboard players set TEMP2 constants 0",
    "scoreboard players set PUSH_VALUE constants 0",
    "scoreboard players set INST_COUNT constants 1",
    # on crée les fonctions
    *STACK_PUSH,
    *NEXT_INST,
    print_color("Fin de l\\'initialisation", "red", 0)
]

PUSH:Callable[[int, List[str]], List[str]] = lambda nb, args: [
    "setblock ~3 ~-2 ~%s command_block[facing=east]{auto:0,Command:\"%s\"} destroy"
    % (nb, print_color(f"Push {args[0]} {args[1]}", "green", 1)),
    "setblock ~4 ~-2 ~%s chain_command_block[facing=east,conditional=true]{auto:1,Command:\"%s\"} destroy"
    % (nb, f"scoreboard players set PUSH_VALUE constants {int(args[1])}"),
    "setblock ~5 ~-2 ~%s chain_command_block[facing=east,conditional=true]{auto:1,Command:\"%s\"} destroy"
    % (nb, f"setblock ~-5 ~ ~{4-nb} redstone_block"),
    "setblock ~6 ~-2 ~%s chain_command_block[facing=east,conditional=true]{auto:1,Command:\"%s\"} destroy"
    % (nb, "setblock ~-4 ~ ~ air"),
]

END:Callable[[int], List[str]] = lambda nb: [
    "setblock ~3 ~-2 ~%s command_block[facing=east]{auto:0,Command:\"%s\"} destroy"
    % (nb, print_color("Fin de l\\'exécution", "green", 1)),
    "setblock ~4 ~-2 ~%s chain_command_block[facing=east,conditional=false]{auto:1,Command:\"%s\"} destroy"
    % (nb, "setblock ~-2 ~ ~ air"),
]

class Generator:
    def __init__(self, tokens:List[Tuple[Tokens.ParserTokens, List[str]]]) -> None:
        self.parserTokens = tokens
        self.list_commands:List[str] = []
    
    def run(self) -> str:
        self.list_commands.extend(INIT)
        for i, (token, args) in enumerate(self.parserTokens):
            match token:
                case Tokens.ParserTokens.PUSH:
                    self.add_command(PUSH(i, args))
                case Tokens.ParserTokens.PASS:
                    pass
        self.add_command(END(len(self.parserTokens)))
        return self.generate()
        
    def add_command(self, command:str|List[str]) -> None:
        if isinstance(command, list):
            self.list_commands.extend(command)
        else:
            self.list_commands.append(command)
        
    def generate(self) -> str:
        one_command = """summon falling_block ~ ~1 ~ {Time:1,BlockState:{Name:redstone_block},Passengers:[{id:falling_block,Passengers:[{id:falling_block,Time:1,BlockState:{Name:activator_rail},Passengers:[%s]}]}]}"""
        liste_commandes_init = [
            "data merge block ~ ~-2 ~ {auto:0}",
            "setblock ~ ~1 ~ command_block{auto:1,Command:\"fill ~ ~ ~ ~ ~-3 ~ air\"}",
            "kill @e[type=command_block_minecart,distance=..1]",
            "kill @e[type=falling_block,distance=..1]"
        ]
        self.list_commands.extend(liste_commandes_init)
        to_insert = "".join("{id:command_block_minecart,Command:'%s'}," % command for command in self.list_commands)
        one_command %= to_insert
        return one_command
