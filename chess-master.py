import string
import unittest

class Gamestate:
    pass

class Chessboard:
    def __init__(self):
        self.__letters = list(string.ascii_uppercase)[:8] 
        self.__numbers = [str(x) for x in range(1,9)]
         # Creates list ["A1", ..., "A8", ..., "H1", ..., "H8"]
        self.__cords = [self.__letters[y] + self.__numbers[x] for y in range(8) for x in range(8)]
        # Creates {'A':0, ..., 'H':7, '1':0, ..., '8':7}
        self.__boardKey = {key:value for key, value in zip(self.__cords, [None for x in range(len(self.__cords))])}
    
    # Get Functions
    @property
    def board(self):
        return self.__boardKey

    # Set Functions


class Chesspiece:
    def __init__(self, name, position, color, chessboard = None):
        self.__name = name
        self.__position = position
        self.__color = color

    # Get Functions
    @property
    def name(self):
        return self.__name

    @property
    def position(self):
        return self.__position

    @property
    def color(self):
        return self.__color
    
    # Set Functions



        



class Pawn(Chesspiece):
    pass

class Rook(Chesspiece):
    pass

class Knight(Chesspiece):
    pass

class Bishop(Chesspiece):
    pass

class Queen(Chesspiece):
    pass

class King(Chesspiece):
    def __init__(self):
        self.__inCheck = True
    # Get Functions
    @property
    def inCheck(self):
        print("I'm in the King class")
        return self.__inCheck



rook = Chesspiece("Rook", "A3", "Black")
print(rook.name)
print(rook.color)

chess = Chessboard()
print(chess.board)


