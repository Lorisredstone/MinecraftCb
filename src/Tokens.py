from enum import IntEnum, auto

class LexerTokens(IntEnum):
    ELEMENT = auto()
    COMMAND = auto()
    
class ParserTokens(IntEnum):
    PASS = auto()
    PUSH = auto()