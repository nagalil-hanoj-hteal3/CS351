# Generated from G01.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .G01Parser import G01Parser
else:
    from G01Parser import G01Parser

# This class defines a complete generic visitor for a parse tree produced by G01Parser.

import turtle
turtle2 = turtle.Turtle()

class G01Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by G01Parser#start.
    def visitStart(self, ctx:G01Parser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G01Parser#oneDrawExprUsingG01.
    def visitOneDrawExprUsingG01(self, ctx:G01Parser.OneDrawExprUsingG01Context):
        target_x = int(ctx.x_cord.text)
        target_y = int(ctx.y_cord.text)
        cur_pos = turtle2.pos()

        if target_x > cur_pos[0]:
            turtle2.right(target_x)
        else:
            turtle2.left(-target_x)

        if target_y > cur_pos[1]:
            turtle2.forward(target_y)
        else:
            turtle2.backward(-target_y)

        return self.visitChildren(ctx)
	
    # Visit a parse tree produced by G01Parser#anotherDrawExprUsingG28.
    def visitAnotherDrawExprUsingG28(self, ctx:G01Parser.AnotherDrawExprUsingG28Context):
        target_a = int(ctx.a_cord.text)
        target_b = int(ctx.b_cord.text)
        cur_pos = turtle2.pos()

        if target_a > cur_pos[0]:
            turtle2.right(target_a)
        else:
            turtle2.left(-target_a)

        if target_b > cur_pos[1]:
            turtle2.forward(target_b)
        else:
            turtle2.backward(-target_b)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by G01Parser#lastDrawExprUsingF.
    def visitLastDrawExprUsingF(self, ctx:G01Parser.LastDrawExprUsingFContext):
        target_c = int(ctx.c_cord.text)
        target_d = int(ctx.d_cord.text)
        cur_pos = turtle2.pos()

        if target_c > cur_pos[0]:
            turtle2.right(target_c)
        else:
            turtle2.left(-target_c)

        if target_d > cur_pos[1]:
            turtle2.forward(target_d)
        else:
            turtle2.backward(-target_d)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by G01Parser#printForAllGrammarCodes.
    def visitPrintForAllGrammarCodes(self, ctx:G01Parser.PrintForAllGrammarCodesContext):
        print(f"Draw Line to {ctx.x_cord.text} {ctx.y_cord.text}")
        return self.visitChildren(ctx)



del G01Parser
