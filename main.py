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
    bishop = Chesspiece.Bishop("Black")

class White:
    knight = Chesspiece.Knight("White")
    queen = Chesspiece.Queen("White", "E1")
    rook = Chesspiece.Rook("White")
    bishop = Chesspiece.Bishop("White")

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

def knightTests():
    print(Black.knight.knights)
    Black.knight.moveTo("C4")
    print(Black.knight.knights)

#knightTests()

def rookTests():
    pass

def bishopTests():
    print(Black.bishop.bishops)
    Black.bishop.moveTo("D2")
    Black.bishop.moveTo("H6")
    Black.bishop.moveTo("H8")
    #Chessboard.Chessboard().board = (Black.bishop.name, "H6")
    #Chessboard.Chessboard().printBoard()
    
#bishopTests()

def queenTests():
    print(White.queen)
    White.queen.moveTo("E8")
    White.queen.moveTo("H8")
    White.queen.moveTo("A1")
    White.queen.moveTo("B3")

queenTests()