# main.py

import chessboard as Chessboard
import chesspiece as Chesspiece


chessNotation = {
    "N": Chesspiece.Knight(),
    "Q": Chesspiece.Queen()
}

class Black:
    knight = chessNotation["N"]
    knight.color = "black"

class White:
    knight = chessNotation["N"]
    knight.color = "black"

def testKnight():
    knight = chessNotation["N"]
    print(knight.name)
    print(knight.knights)

    knight.moveTo("C2")
    print(knight.knights)
    knight.moveTo("D3")
    print(knight.knights)
    knight.moveTo("D8")

Black.knight.moveTo("B3")
Black.knight.moveTo("C2")
print("####")
White.knight.moveTo("B3")
White.knight.moveTo("C2")
