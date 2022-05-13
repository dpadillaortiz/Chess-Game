# main.py

#import chessboard as Chessboard
import chesspiece as Chesspiece


"""chessNotation = {
    "N": Chesspiece.Knight("yo"),
    "Q": Chesspiece.Queen("memes")
}"""

class Black:
    knight = Chesspiece.Knight("Black")
    queen = Chesspiece.Queen("Black", "E1")
    rook = Chesspiece.Rook("Black")
    bishop = Chesspiece.Bishop("Black")
    king = Chesspiece.King("Black", "D1")
    pawn = Chesspiece.Pawn("Black")

class White:
    knight = Chesspiece.Knight("White")
    queen = Chesspiece.Queen("White", "E1")
    rook = Chesspiece.Rook("White")
    bishop = Chesspiece.Bishop("White")
    king = Chesspiece.King("White", "D1")
    pawn = Chesspiece.Pawn("White")

"""def testKnight():
    knight = chessNotation["N"]
    print(knight.name)
    print(knight.knights)

    knight.moveTo("C2")
    print(knight.knights)
    knight.moveTo("D3")
    print(knight.knights)
    knight.moveTo("D8")"""

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

def pawnTests():
    Black.pawn.moveTo("G4")
    Black.pawn.moveTo("G3")
    Black.pawn.moveTo("A4")
    Black.pawn.moveTo("B3")
    Black.pawn.moveTo("Z8")
pawnTests()

def rookTests():
    White.rook.moveTo("H8")
    White.rook.moveTo("A8")
rookTests()

def knightTests():
    Black.knight.moveTo("C4")
    
knightTests()

def bishopTests():
    print(Black.bishop.bishops)
    Black.bishop.moveTo("D2")
    Black.bishop.moveTo("H6")
    Black.bishop.moveTo("H8")
bishopTests()

def queenTests():
    White.queen.moveTo("E8")
    White.queen.moveTo("H8")
    White.queen.moveTo("A1")
    White.queen.moveTo("B3")
queenTests()

def kingTests():
    White.king.moveTo("C1")
    White.king.moveTo("C2")
    White.king.moveTo("D3")
    White.king.moveTo("H3")
    White.king.moveTo("D8")
kingTests()