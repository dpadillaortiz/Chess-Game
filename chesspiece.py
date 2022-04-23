# chesspiece.py
import chessboard as Chessboard
import gamestate as Gamestate

class Chesspiece:
    kingInCheck = False
    canMove = True
    
    def __init__(self, name = None, position = None):
        self.__name = name
        self.__position = position
        self.__color = None
        self.__isTaken = False
        #Chessboard.Chessboard().updateBoard((self.name, self.position))

    @property
    def name(self):
        return self.__name

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, new_pos):
        self.__position = new_pos.upper()
    
    @property
    def isTaken(self):
        return self.__isTaken

    @isTaken.setter
    def isTaken(self, state):
        self.__isTaken = state

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color

    def calcDist(self, new_pos):
        toPos = new_pos.upper()
        fromPos = self.position
        run = Chessboard.Chessboard().board[toPos][0][0] - Chessboard.Chessboard().board[fromPos][0][0]
        rise = int(Chessboard.Chessboard().board[toPos][0][1]) - int(Chessboard.Chessboard().board[fromPos][0][1])
        return (run, rise)

    def updatePiece(self, boardSetter, newPos):
        currentPos = self.position
        Chessboard.Chessboard().updateBoard(boardSetter, currentPos)
        print("{} moved from {} to {}.".format(self.name, currentPos, newPos))
        self.position = newPos

    def takesPiece(self, position):
        self.updatePiece((self.name, position), position)
        pieceTaken = Chessboard.Chessboard().board[position][1]
        Chessboard.Chessboard().board[position].pop(1)
        print("{} takes {}".format(self.name, pieceTaken))

    def __repr__(self):
        return "{} is on {}".format(self.name, self.position)


class Pawn(Chesspiece):
    __name = "Pawn"

    def __init__(self, position):
        super().__init__(Pawn.__name, position)
        self.__firstMove = True
    
    @property
    def firstMove(self):
        return self.__firstMove

    @firstMove.setter
    def firstMove(self, state):
        self.__firstMove = state

    def moveTo(self, position):
        run, rise = self.calcDist(position)
        if rise > 0 and run == 0:
            if rise**2 == 1:
                self.updatePiece((self.name, position), position)
                self.firstMove = False
            elif self.firstMove == True and rise**2 == 4:
                self.updatePiece((self.name, position), position)
                self.firstMove = False
        elif rise > 0 and rise**2 + run**2 == 2 and len(Chessboard.Chessboard().board[position]) == 2:
            self.takesPiece(position)
            self.firstMove = False
        else:
            print("{} cannot move from {} to {}.".format(self.name, self.position, position))

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

    def __init__(self, position):
        super().__init__(Rook.__name, position)
        self.__firstMove = True 

    @property
    def firstMove(self):
        return self.__firstMove

    @firstMove.setter
    def firstMove(self, state):
        self.__firstMove = state

    def moveTo(self, position):
        run, rise = self.calcDist(position)
        if run**2 == 0:
            self.updatePiece((self.name, position), position)
            self.firstMove = False
        elif rise**2 == 0:
            self.updatePiece((self.name, position), position)
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
    __name = "Knight"
    knights7 = {
        "knight1": "B1",
        "knight2": "G1"
    }

    def __init__(self, position = None):
        super().__init__(Knight.__name, position)
        self.__knights = { 
            "knight1": "A1", 
            "knight2": "C1"
        }
    @property
    def knights(self):
        return self.__knights

    @knights.setter
    def knights(self, n_setter):
        knight, position = n_setter
        self.__knights[knight] = position
        

    def calcDist(self, newPos, lastPos):
        toPos = newPos.upper()
        run = Chessboard.Chessboard().board[toPos][0][0] - Chessboard.Chessboard().board[lastPos][0][0]
        rise = int(Chessboard.Chessboard().board[toPos][0][1]) - int(Chessboard.Chessboard().board[lastPos][0][1])
        return (run, rise)

    def validMove(self, newPos, currentPos):
        run, rise = self.calcDist(newPos, currentPos)
        if run**2 + rise**2 == 5:
            return True
        else:
            return False
    
    def moveTo(self, newPos):
        knight1Val = self.validMove(newPos, self.knights["knight1"])
        knight2Val = self.validMove(newPos, self.knights["knight2"])
        if knight1Val == True and knight2Val == False:
            currentPos = self.knights["knight1"]
            self.knights = ("knight1", newPos)
            print("{} moved from {} to {}.".format(self.name, currentPos, newPos))
        elif knight2Val == True and knight1Val == False:
            currentPos = self.knights["knight2"]
            self.knights = ("knight2", newPos)
            print("{} moved from {} to {}.".format(self.name, currentPos, newPos))
        elif knight1Val == True and knight2Val == True:
            print("Move too ambiguous")
        else:
            print("{} cannot move to {}.".format(self.name, newPos))

    

class Bishop(Chesspiece):
    pass

class Queen(Chesspiece):
    __name = "Queen"

    def __init__(self, position = None):
        super().__init__(Queen.__name, position)
    
    def moveTo(self, newPos):
        run, rise = self.calcDist(newPos)
        currentPos = self.position
        if run**2 == rise**2:
            self.position = newPos
            print("{} moved from {} to {}.".format(self.name, currentPos, newPos))
        elif (run**2 == 0) ^ (rise**2 == 0):
            self.position = newPos
            print("{} moved from {} to {}.".format(self.name, currentPos, newPos))
        else:
            print("{} cannot move from {} to {}.".format(self.name, currentPos, newPos))

    def validMove(self, newPos):
        run, rise = self.calcDist(newPos)
        currentPos = self.position
        if run**2 == rise**2:
            print("{} moved from {} to {}.".format(self.name, currentPos, newPos))
        elif (run**2 == 0) ^ (rise**2 == 0):
            print("{} moved from {} to {}.".format(self.name, currentPos, newPos))
        else:
            print("{} cannot move from {} to {}.".format(self.name, currentPos, newPos))
    
class King(Chesspiece):
    __name = "King"
    initPos = True

    def __init__(self, position):
        super().__init__(King.__name, position)
        self.__firstMove = True

