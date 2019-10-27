# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#decl.
    def visitDecl(self, ctx:MCParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#vardecl.
    def visitVardecl(self, ctx:MCParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primitivetype.
    def visitPrimitivetype(self, ctx:MCParser.PrimitivetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#listvar.
    def visitListvar(self, ctx:MCParser.ListvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var.
    def visitVar(self, ctx:MCParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcdecl.
    def visitFuncdecl(self, ctx:MCParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#functype.
    def visitFunctype(self, ctx:MCParser.FunctypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcname.
    def visitFuncname(self, ctx:MCParser.FuncnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#listparam.
    def visitListparam(self, ctx:MCParser.ListparamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#paradecl.
    def visitParadecl(self, ctx:MCParser.ParadeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#arraypointertype.
    def visitArraypointertype(self, ctx:MCParser.ArraypointertypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#stmt.
    def visitStmt(self, ctx:MCParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exprstmt.
    def visitExprstmt(self, ctx:MCParser.ExprstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#breakstmt.
    def visitBreakstmt(self, ctx:MCParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continuestmt.
    def visitContinuestmt(self, ctx:MCParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#blockstmt.
    def visitBlockstmt(self, ctx:MCParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#ifstmt.
    def visitIfstmt(self, ctx:MCParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#whilestmt.
    def visitWhilestmt(self, ctx:MCParser.WhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#forstmt.
    def visitForstmt(self, ctx:MCParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#returnstmt.
    def visitReturnstmt(self, ctx:MCParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr.
    def visitExpr(self, ctx:MCParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr1.
    def visitExpr1(self, ctx:MCParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr2.
    def visitExpr2(self, ctx:MCParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#operand.
    def visitOperand(self, ctx:MCParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcall.
    def visitFuncall(self, ctx:MCParser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#listarg.
    def visitListarg(self, ctx:MCParser.ListargContext):
        return self.visitChildren(ctx)



del MCParser