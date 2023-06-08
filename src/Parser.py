import mod.colorprint as colorprint
from typing import List, Tuple
import src.Tokens as Tokens

class Parser:
    def __init__(self, tokens:List[Tuple[Tokens.LexerTokens, List[str]]]) -> None:
        self.lexerTokens = tokens
        self.parserTokens:List[Tuple[Tokens.ParserTokens, List[str]]] = []
        
    def run(self) -> None:
        for token, args in self.lexerTokens:
            match token:
                case Tokens.LexerTokens.ELEMENT:
                    self.parserTokens.append((Tokens.ParserTokens.PUSH, args))
                case _:
                    colorprint.colorprint("Erreur de parsing", colorprint.colors["red"])