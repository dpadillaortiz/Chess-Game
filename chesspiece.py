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
    __name = "Pawn"

    def __init__(self, position, color):
        super().__init__(Pawn.__name, position, color)
        self.__firstMove = True
        self.__isTaken = False
    
    @property
    def firstMove(self):
        return self.__firstMove

    @firstMove.setter
    def firstMove(self, state):
        self.__firstMove = state

    @property
    def isTaken(self):
        return self.__isTaken

    @isTaken.setter
    def isTaken(self, state):
        self.__isTaken = state

    def moveTo(self, position):
        run, rise = self.calcDist(position)
        if rise == 1 and run == 0:
            Chessboard.Chessboard().updateBoard(self.position, (self.name, position))
            print("{} moved from {} to {}.".format(self.name, self.position, position))
            self.position = position
            self.firstMove = False
        elif self.firstMove == True and rise == 2 and run == 0:
            Chessboard.Chessboard().updateBoard(self.position, (self.name, position))
            print("{} moved from {} to {}.".format(self.name, self.position, position))
            self.position = position
            self.firstMove = False
            print(self.position)
        else:
            print("Cannot move to {} from {}".format(position, self.position))

    def validMove(self, position):
        run, rise = self.calcDist(position)
        if rise == 1 and run == 0:
            print("{} can move from {} to {}.".format(self.name, self.position, position))
        elif self.firstMove == True and rise == 2 and run == 0:
            print("{} can move from {} to {}.".format(self.name, self.position, position))
        else:
            print("{} can move from {} to {}.".format(self.name, self.position, position))


class Rook(Chesspiece):
    __name = "Rook"

    def __init__(self, position, color):
        super().__init__(Rook.__name, position, color)
        self.__firstMove = True 
        self.__isTaken = False

    @property
    def firstMove(self):
        return self.__firstMove

    @firstMove.setter
    def firstMove(self, state):
        self.__firstMove = state

    @property
    def isTaken(self):
        return self.__isTaken

    @isTaken.setter
    def isTaken(self, state):
        self.__isTaken = state

    def moveTo(self, position):
        run, rise = self.calcDist(position)
        if run**2 == 0:
            Chessboard.Chessboard().updateBoard(self.position, (self.name, position))
            self.position = position
            self.firstMove = False
        elif rise**2 == 0:
            Chessboard.Chessboard().updateBoard(self.position, (self.name, position))
            self.position = position
            self.firstMove = False

    def validMove(self, position):
        run, rise = self.calcDist(position)
        if run**2 == 0:
            print("{} can move to {} from {}.".format(self.name, position, self.position))
        elif rise**2 == 0:
            print("{} can move to {} from {}.".format(self.name, position, self.position))
        else:
            print("{} cannot move to {} from {}".format(self.name, position, self.position))

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
