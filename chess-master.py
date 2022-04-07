import string

class Gamestate:
    turn = 0

class Chessboard:
    rank = list(string.ascii_uppercase)[:8] 
    numbers = [str(x) for x in range(1,9)]
    # Creates list ["A1", ..., "A8", ..., "H1", ..., "H8"]
    positions = [list(string.ascii_uppercase)[:8][y] + [str(x) for x in range(1,9)][x] for y in range(8) for x in range(8)]
  
    def __init__(self):
        # Creates {'A1':[(1,1)], ..., 'A8':[(1,8)], ..., 'H1':[(1,8)], ..., 'H8':[(8,8)]}
        self.__board = {key:value for key, value in zip(Chessboard.positions, [[(x,y)] for x in range(1,9) for y in range(1,9)])}
    
    # Get Functions
    @property
    def board(self):
        return self.__board

    # Set Functions
    @board.setter
    def board(self, pos_name):
        # the pos_name parameter is a tuple
        new_pos, name = pos_name
        if self.isFree(new_pos) == True:
            self.__board[new_pos].append(name)

    # Other
    def isFree(self, position):
        if len(self.__board[position]) == 1:
            return True
        else: 
            return False




class Chesspiece:
    kingInCheck = False
    
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
    initPos = True

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
    pass




rook = Pawn("A3", "Black")
print(rook.name)
print(rook.color)
pawn = Pawn("A3", "Black")
pawn.name = "test"
print(pawn.name)
print(rook.name)

chessBoard = Chessboard()
chessBoard.board = ("A3", "Rook")
print(chessBoard.board)


print(chessBoard.isFree("B2"))
print(chessBoard.isFree("A3"))
