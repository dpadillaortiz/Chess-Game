# main.py

import chessboard as Chessboard
import chesspiece as Chesspiece
#import gamestate as Gamestate




def testme():
    ChessBoard = Chessboard.Chessboard()
    knight = Chesspiece.Knight("B1")
    knight = Chesspiece.Knight("G1")
    knight = Chesspiece.Knight("B8")
    knight = Chesspiece.Knight("G8")
    print("Welcome to chess game!")
    print(knight)
    yo = input()
    yo_split = yo.split()
    if "Knight to" in yo:
        print(yo_split[-1])
        knight.moveTo(yo_split[-1])

testme()