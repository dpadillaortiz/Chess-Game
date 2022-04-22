# main.py

import chessboard as Chessboard
import chesspiece as Chesspiece





def testme():
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

ChessBoard = Chessboard.Chessboard()

chessNotation = {
    "N": Chesspiece.Knight(),
    "Q": Chesspiece.Queen()
}

test = chessNotation["N"]
print(test.name)
"""
test = chessNotation["N"]
#test.position = "A3"
test.moveTest("C3")
print(test.knights)
test.moveTest("A2")
print(test.knights)
test.moveTest("C1")
print(test.knights)
"""
def testMeToo():
    print("Welcome to Chessgame")
    knight = chessNotation["N"]
    test.moveTest("C3")
    play = input("Move Knight").upper()
    piece = play[:1]
    newPos = play[1:]
    if piece in play and newPos in play:
        chessNotation[piece].moveTest(newPos)

testMeToo()
