# main.py

import chessboard as Chessboard
import chesspiece as Chesspiece


chessNotation = {
    "N": Chesspiece.Knight(),
    "Q": Chesspiece.Queen()
}

class Black:
    knight = Chesspiece.Knight()
    queen = Chesspiece.Queen()
    knight.color = "black"

class White:
    knight = Chesspiece.Knight()
    #knight.color = "black"

def testKnight():
    knight = chessNotation["N"]
    print(knight.name)
    print(knight.knights)

    knight.moveTo("C2")
    print(knight.knights)
    knight.moveTo("D3")
    print(knight.knights)
    knight.moveTo("D8")

def testClasses():
    Black.knight.moveTo("B3")
    Black.knight.moveTo("C2")
    print("####")
    White.knight.moveTo("B3")
    White.knight.moveTo("C2")


    White.knight.moveTo("E3")
    Black.knight.moveTo("A1")

    print(White.knight.knights)
    print(Black.knight.knights)

print(Black.queen.color)
print(White.knight.color)
print(Black.queen.color)