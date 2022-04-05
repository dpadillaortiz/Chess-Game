import string

class Gamestate:
    pass

class Chessboard:
    rank = list(string.ascii_uppercase)[:8] 
    numbers = [str(x) for x in range(1,9)]
    # Creates list ["A1", ..., "A8", ..., "H1", ..., "H8"]
    cords = [Chessboard.rank[y] + Chessboard.numbers[x] for y in range(8) for x in range(8)]
    def __init__(self):
        # Creates {'A':0, ..., 'H':7, '1':0, ..., '8':7}
        self.__boardKey = {key:value for key, value in zip(cords, [None for x in range(len(cords))])}
    
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
    name = "Pawn"

    def __init__(self, position, color, chessboard = None):
        super().__init__(Pawn.name, position, color, chessboard)

class Rook(Chesspiece):
    pass

class Knight(Chesspiece):
    pass

class Bishop(Chesspiece):
    pass

class Queen(Chesspiece):
    pass

class King(Chesspiece):
    inCheck = False




rook = Pawn("A3", "Black")
print(rook.name)
print(rook.color)

chessBoard = Chessboard()
print(chessBoard.board)


