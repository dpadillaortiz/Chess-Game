# main.py

import chessboard as Chessboard
import chesspiece as Chesspiece

chessBoard = Chessboard.Chessboard()
pawn = Chesspiece.Pawn("A3", "Black")
rook = Chesspiece.Rook("B1", "White")
king = Chesspiece.King("B2", "White")

chessBoard.board = (pawn.name, pawn.position)
chessBoard.board = (rook.name, rook.position)
chessBoard.board = (king.name, king.position)
#chessBoard.printBoard()

print("     Chesspiece class    inCheck atrribute:", Chesspiece.kingInCheck)
print("pawn Chesspiece instance inCheck atrribute:", pawn.kingInCheck)
print("rook Chesspiece instance inCheck atrribute:", rook.kingInCheck)
print("king Chesspiece instance inCheck atrribute:", king.kingInCheck)

print("--Changing class inCheck attribute--")

Chesspiece.kingInCheck = True
print("     Chesspiece class    inCheck atrribute:", Chesspiece.kingInCheck)
print("pawn Chesspiece instance inCheck atrribute:", pawn.kingInCheck)
print("rook Chesspiece instance inCheck atrribute:", rook.kingInCheck)
print("king Chesspiece instance inCheck atrribute:", king.kingInCheck)

print("--Changing king inCheck attribute--")
Chesspiece.kingInCheck = False
king.kingInCheck = True
print("     Chesspiece class    inCheck atrribute:", Chesspiece.kingInCheck)
print("pawn Chesspiece instance inCheck atrribute:", pawn.kingInCheck)
print("rook Chesspiece instance inCheck atrribute:", rook.kingInCheck)
print("king Chesspiece instance inCheck atrribute:", king.kingInCheck)

print("--Adding function to change inCheck for the rest--")
if king.kingInCheck == True:
    Chesspiece.kingInCheck = True
    print("     Chesspiece class    inCheck atrribute:", Chesspiece.kingInCheck)
    print("pawn Chesspiece instance inCheck atrribute:", pawn.kingInCheck)
    print("rook Chesspiece instance inCheck atrribute:", rook.kingInCheck)
    print("king Chesspiece instance inCheck atrribute:", king.kingInCheck)

chessBoard.printBoard()