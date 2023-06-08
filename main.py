import src.Generator as Generator
import src.Parser as Parser
import src.Lexer as Lexer
import sys

lexer = Lexer.Lexer(sys.argv[1])
lexer.run()

parser = Parser.Parser(lexer.tokens)
parser.run()

generator = Generator.Generator(parser.parserTokens)
output:str = generator.run()

open(sys.argv[2], "w").write(output)

# copy to clipboard (easy to paste in minecraft)
# exec to avoid import error
exec("import pyperclip\npyperclip.copy(output)", globals())