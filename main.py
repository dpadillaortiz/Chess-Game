# main.py

import chessboard as Chessboard
import chesspiece as Chesspiece
import gamestate as Gamestate

chessBoard = Chessboard.Chessboard()

rook = Chesspiece.Rook("A3", "Black")
print(rook)
rook.moveTo("A4")
print(rook)
print("______________________________")

pawn = Chesspiece.Pawn("C3", "Black")
print(pawn)
pawn.moveTo("C5")
pawn.moveTo("C7")
pawn.moveTo("C6")

print("______________________________")
Chessboard.Chessboard().printBoard()