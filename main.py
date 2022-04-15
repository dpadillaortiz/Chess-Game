# main.py

import chessboard as Chessboard
import chesspiece as Chesspiece
import gamestate as Gamestate

chessBoard = Chessboard.Chessboard()
chessBoard.printBoard()

rook = Chesspiece.Rook("A3", "Black")
print(rook)
print(chessBoard.isFree("B2"))

chessBoard.board = (rook, "B2")
chessBoard.printBoard()

rook.position = "B4"
print(rook)