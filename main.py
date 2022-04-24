# main.py

import chessboard as Chessboard
import chesspiece as Chesspiece


chessNotation = {
    "N": Chesspiece.Knight("yo"),
    "Q": Chesspiece.Queen("memes")
}

class Black:
    knight = Chesspiece.Knight("Black")
    queen = Chesspiece.Queen("Black")
    rook = Chesspiece.Rook("Black")

class White:
    knight = Chesspiece.Knight("White")
    queen = Chesspiece.Queen("White")
    rook = Chesspiece.Rook("White")

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