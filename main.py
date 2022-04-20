# main.py

import chessboard as Chessboard
import chesspiece as Chesspiece
import gamestate as Gamestate

chessBoard = Chessboard.Chessboard()

rook = Chesspiece.Rook("b4", "Black")

pawn = Chesspiece.Pawn("C3", "Black")
pawn.moveTo("D4")
pawn.moveTo("B4")
pawn.moveTo("B3")

chessBoard.printBoard()
