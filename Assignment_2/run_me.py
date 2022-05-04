from antlr4 import * 
from G01Lexer import G01Lexer
from G01Parser import G01Parser
from G01Visitor import G01Visitor
import time

def main():
    lexer = G01Lexer (FileStream("G01_test"))
    token_stream = CommonTokenStream(lexer)
    parser = G01Parser(token_stream)
    visitor = G01Visitor()

   
    while True: 
        tree = parser.start()
        if tree.expr() == None:
            break
        print(tree.toStringTree(recog=parser))
        visitor.visit(tree)

    time.sleep(5)

if __name__ == '__main__':
    main()
