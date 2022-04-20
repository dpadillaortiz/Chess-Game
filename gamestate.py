# gamestate.py
import chessboard as Chessboard 
import chesspiece as Chesspiece

class Gamestate:
    chessboard = Chessboard.Chessboard()
    turn = 0

class PlayerOne:
    pawn1 = Chesspiece.Chesspiece().Pawn("A2", "White")
    pawn2 = Chesspiece.Chesspiece().Pawn("B2", "White")
    pawn3 = Chesspiece.Chesspiece().Pawn("C2", "White")
    pawn4 = Chesspiece.Chesspiece().Pawn("D2", "White")
    pawn5 = Chesspiece.Chesspiece().Pawn("E2", "White")
    pawn6 = Chesspiece.Chesspiece().Pawn("F2", "White")
    pawn7 = Chesspiece.Chesspiece().Pawn("G2", "White")
    pawn8 = Chesspiece.Chesspiece().Pawn("H2", "White")
    rook1 = Chesspiece.Chesspiece().Rook("A1", "White")
    rook2 = Chesspiece.Chesspiece().Rook("H1", "White")
