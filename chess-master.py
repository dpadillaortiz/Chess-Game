import string

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
        name, new_pos = pos_name
        if self.isFree(new_pos) == True:
            self.__board[new_pos].append(name)

    # Other
    def isFree(self, position):
    # Checks whether the position is available on the board
        if len(self.__board[position]) == 1:
            return True

    def onBoard(self, test):
    # Checks whether the position is valid
        if test in Chessboard.positions:
            return True

    def printBoard(self):
        print(self.board)

class Gamestate:
    turn = 0


class Chesspiece:
    kingInCheck = False
    canMove = True
    
    def __init__(self, name, position, color, chessboard = None):
        self.__name = name
        self.__position = position
        self.__color = color
        #self.chessboard = chessboard
        #self.chessboard.board = (self.__name, self.__position)

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

    # Other Functions:



class Pawn(Chesspiece):
    name = "Pawn"
    initPos = True

    def __init__(self, position, color, chessboard = None):
        super().__init__(Pawn.name, position, color, chessboard)

class Rook(Chesspiece):
    name = "Rook"
    initPos = True

    def __init__(self, position, color, chessboard = None):
        super().__init__(Rook.name, position, color, chessboard)


class Knight(Chesspiece):
    pass

class Bishop(Chesspiece):
    pass

class Queen(Chesspiece):
    pass

class King(Chesspiece):
    name = "King"
    initPos = True

    def __init__(self, position, color, chessboard = None):
        super().__init__(Rook.name, position, color, chessboard)


# Make separate file for this
chessBoard = Chessboard()
pawn = Pawn("A3", "Black")
rook = Rook("B1", "White")
king = King("B2", "White")

chessBoard.board = (pawn.name, pawn.position)
chessBoard.board = (rook.name, rook.position)
chessBoard.board = (king.name, king.position)
#chessBoard.printBoard()

print("     Chesspiece class    inCheck atrribute:", Chesspiece.kingInCheck)
print("pawn Chesspiece instance inCheck atrribute:", pawn.kingInCheck)
print("rook Chesspiece instance inCheck atrribute:", rook.kingInCheck)
print("king Chesspiece instance inCheck atrribute:", king.kingInCheck)

print("--Changing class inCheck attribute--")

Chesspiece.kingInCheck = True
print("     Chesspiece class    inCheck atrribute:", Chesspiece.kingInCheck)
print("pawn Chesspiece instance inCheck atrribute:", pawn.kingInCheck)
print("rook Chesspiece instance inCheck atrribute:", rook.kingInCheck)
print("king Chesspiece instance inCheck atrribute:", king.kingInCheck)

print("--Changing king inCheck attribute--")
Chesspiece.kingInCheck = False
king.kingInCheck = True
print("     Chesspiece class    inCheck atrribute:", Chesspiece.kingInCheck)
print("pawn Chesspiece instance inCheck atrribute:", pawn.kingInCheck)
print("rook Chesspiece instance inCheck atrribute:", rook.kingInCheck)
print("king Chesspiece instance inCheck atrribute:", king.kingInCheck)

print("--Adding function to change inCheck for the rest--")
if king.kingInCheck == True:
    Chesspiece.kingInCheck = True
    print("     Chesspiece class    inCheck atrribute:", Chesspiece.kingInCheck)
    print("pawn Chesspiece instance inCheck atrribute:", pawn.kingInCheck)
    print("rook Chesspiece instance inCheck atrribute:", rook.kingInCheck)
    print("king Chesspiece instance inCheck atrribute:", king.kingInCheck)