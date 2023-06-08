from typing import List, Tuple
import src.Tokens as Tokens
import json

KEYWORDS:List[str] = []

class Lexer:
    def __init__(self, file_name:str) -> None:
        self.file_name = file_name
        self.content = open(file_name, "r").read()
        self.tokens:List[Tuple[Tokens.LexerTokens, List[str]]] = []
        
    def run(self) -> None:
        # on traite le contenu du fichier pour virer les \n et les espaces
        content = self.content.replace("\n", " ")
        while "  " in content:
            content = content.replace("  ", " ")
        list_elements:List[str] = content.split(" ")
        for element in list_elements:
            # si l'élément est un nombre
            if element.isnumeric():
                self.tokens.append((Tokens.LexerTokens.ELEMENT, ["int", element]))
            # si l'élément est un mot clé
            elif element in KEYWORDS:
                self.tokens.append((Tokens.LexerTokens.COMMAND, [element]))