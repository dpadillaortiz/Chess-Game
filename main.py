# main.py

import chessboard as Chessboard
import chesspiece as Chesspiece
import gamestate as Gamestate

chessBoard = Chessboard.Chessboard()

rook = Chesspiece.Rook("A3", "Black")
chessBoard.board = (rook.name, "A3")
chessBoard.printBoard()
print(rook)


rook.position = "B4"
chessBoard.printBoard()
print(rook)

print("______________________________")
pawn = Chesspiece.Pawn("C3", "Black")
chessBoard.board = (pawn.name, "C3")
print(pawn)
pawn.moveTo("C5")
chessBoard.printBoard()
print(pawn)
pawn.moveTo("C7")
pawn.moveTo("C6")
print(pawn)

print("______________________________")
rook = Chesspiece.Rook("H3", "Black")
chessBoard.board = (rook.name, "H3")
rook.moveTo("D3")
print(rook)
rook.moveTo("D7")
print(rook)

print("______________________________")
Chessboard.Chessboard().printBoard()