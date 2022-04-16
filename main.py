# main.py

import chessboard as Chessboard
import chesspiece as Chesspiece
import gamestate as Gamestate

chessBoard = Chessboard.Chessboard()

rook = Chesspiece.Rook("A3", "Black")
chessBoard.board = (rook, "A3")
chessBoard.printBoard()
print(rook)


rook.position = "B4"
chessBoard.board = (rook, "B4")
chessBoard.printBoard()
print(rook)


pawn = Chesspiece.Pawn("C3", "Black")
chessBoard.board = (pawn, "C3")
pawn.moveTo("C5")
chessBoard.board = (pawn, "C5")
chessBoard.printBoard()
print(pawn)
pawn.moveTo("C7")
pawn.moveTo("C6")
print(pawn)
