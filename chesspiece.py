# chesspiece.py
import chessboard as Chessboard

class Chesspiece:
    kingInCheck = False
    canMove = True
    
    def __init__(self, name, position, color):
        self.__name = name
        self.__position = position.upper()
        self.__color = color

    # Get Functions
    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    # Set Functions
    @position.setter
    def position(self, new_pos):
        self.__position = new_pos.upper()

    # Other Functions:
    def calcDist(self, new_pos):
        toPos = new_pos.upper()
        fromPos = self.position

        run = Chessboard.Chessboard().board[toPos][0][0] - Chessboard.Chessboard().board[fromPos][0][0]
        rise = int(Chessboard.Chessboard().board[toPos][0][1]) - int(Chessboard.Chessboard().board[fromPos][0][1])

        return (run, rise)

    def __repr__(self):
        return "{} is on {}".format(self.name, self.position)


class Pawn(Chesspiece):
    name = "Pawn"

    def __init__(self, position, color):
        super().__init__(Pawn.name, position, color)
        self.__hasMoved = False
    
    @property
    def hasMoved(self):
        return self.__hasMoved

    @hasMoved.setter
    def hasMoved2(self, state):
        self.__hasMoved = state

    def moveTo(self, position):
        run, rise = self.calcDist(position)
        if rise == 1 and run == 0:
            self.position = position
        elif self.hasMoved == False and rise == 2 and run == 0:
            self.position = position
            self.hasMoved2 = True
        else:
            print("Cannot move to {} from {}".format(position, self.position))


class Rook(Chesspiece):
    name = "Rook"
    initPos = True

    def __init__(self, position, color):
        super().__init__(Rook.name, position, color)
        self.__firstMove = True 


class Knight(Chesspiece):
    pass

class Bishop(Chesspiece):
    pass

class Queen(Chesspiece):
    pass

class King(Chesspiece):
    name = "King"
    initPos = True

    def __init__(self, position, color):
        super().__init__(Rook.name, position, color)
        self.__firstMove = True
