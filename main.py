# main.py

import chessboard as Chessboard
import chesspiece as Chesspiece
#import gamestate as Gamestate




def testme():
    ChessBoard = Chessboard.Chessboard()
    knight = Chesspiece.Knight("G8")
    print("Welcome to chess game!")
    print(knight)
    yo = input()
    yo_split = yo.split()
    gameOn = True
    if "Knight to" in yo:
        knight.moveTo(yo_split[-1])
    if "Turn off game" == yo:
        gameOn = False
        print("Game ended")

chessNotation = {
    "N": Chesspiece.Knight(),
    "Q": Chesspiece.Queen()
}

test = chessNotation["N"]
print(test.name)
test = chessNotation["Q"]
print(test.name)
test.position = "A3"
test.moveTo("A8")
test.moveTo("H8")
test.moveTo("A1")
test.moveTo("B3")
print("yo")
test = chessNotation["N"]
#test.position = "A3"
test.moveTest("C3")
print(test.knights)