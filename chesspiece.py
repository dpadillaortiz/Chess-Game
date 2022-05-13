# chesspiece.py
import chessboard as Chessboard
import gamestate as Gamestate

class Chesspiece:
    kingInCheck = False
    canMove = True
    
    def __init__(self, name = None, color = None):
        self.__name = name
        self.__color = color
        self.__isTaken = False

    @property
    def name(self):
        return self.__name

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

    def calcDist(self, newPos, lastPos):
        toPos = newPos.upper()
        run = Chessboard.Chessboard().board[toPos][0][0] - Chessboard.Chessboard().board[lastPos][0][0]
        rise = int(Chessboard.Chessboard().board[toPos][0][1]) - int(Chessboard.Chessboard().board[lastPos][0][1])
        return (run, rise)


class Pawn(Chesspiece):
    __name = "Pawn"

    def __init__(self, position):
        super().__init__(Pawn.__name, position)
        self.__pawns = {
            "pawn1":{
                "position":"A2",
                "firstMove":True
            },
            "pawn2":{
                "position":"B2",
                "firstMove":True
            },
            "pawn3":{
                "position":"C2",
                "firstMove":True
            },
            "pawn4":{
                "position":"D2",
                "firstMove":True
            },
            "pawn5":{
                "position":"E2",
                "firstMove":True
            },
            "pawn6":{
                "position":"F2",
                "firstMove":True
            },
            "pawn7":{
                "position":"G2",
                "firstMove":True
            },
            "pawn8":{
                "position":"H2",
                "firstMove":True
            },
        }

    @property
    def pawns(self):
        return self.__pawns

    @pawns.setter
    def pawns(self, pSetter):
        pawn, position = pSetter
        self.__pawns[pawn]["position"] = position
        self.__pawns[pawn]["firstMove"] = False
   
    def validMove(self, pawn, newPos, lastPos):
        if Chessboard.Chessboard().onBoard(newPos) == False:
            return False
        
        run, rise = self.calcDist(newPos, lastPos)
        if rise > 0 and run**2 == 0:
            if rise**2 == 1:
                return True
            elif rise**2 == 4 and self.pawns[pawn]["firstMove"] == True:
                return True
        else:
            return False

    def moveTo(self, newPos):
        pawnCounter = []
        pawnPiece = None
        for pawn in self.pawns:
            if self.validMove(pawn, newPos, self.pawns[pawn]["position"]) == True:
                    pawnCounter.append(pawn)
                    pawnPiece = pawn
        if len(pawnCounter) == 1:
            currentPos = self.pawns[pawnPiece]["position"]
            self.pawns = (pawnPiece, newPos)
            print("{} moved from {} to {}.".format(self.name, currentPos, newPos))
        elif len(pawnCounter) > 1:
            print("Move too ambiguous")
        else:
            print("{} cannot move to {}.".format(self.name, newPos))

class Rook(Chesspiece):
    __name = "Rook"

    def __init__(self, color):
        super().__init__(Rook.__name, color = color)
        self.__rooks = { 
            "rook1": {
                "position":"A1",
                "firstMove": True
            }, 
            "rook2": {
                "position":"H1",
                "firstMove": True
            }
        }

    @property
    def rooks(self):
        return self.__rooks

    @rooks.setter
    def rooks(self, rSetter):
        rook, position = rSetter
        self.__rooks[rook]["position"] = position
        self.__rooks[rook]["firstMove"] = False

    def validMove(self, newPos, lastPos):
        run, rise = self.calcDist(newPos, lastPos)
        if (run**2 == 0) ^ (rise**2 == 0):
            return True
        else:
            return False

    def moveTo(self, newPos):
        r1ValidMove = self.validMove(newPos, self.rooks["rook1"]["position"])
        r2ValidMove = self.validMove(newPos, self.rooks["rook2"]["position"])
        if r1ValidMove == True and r2ValidMove == False:
            currentPos = self.rooks["rook1"]["position"]
            self.rooks = ("rook1", newPos)
            print("{} moved from {} to {}.".format(self.name, currentPos, newPos))
        elif r1ValidMove == False and r2ValidMove == True:
            currentPos = self.rooks["rook2"]["position"]
            self.rooks = ("rook2", newPos)
            print("{} moved from {} to {}.".format(self.name, currentPos, newPos))
        elif r1ValidMove == True and r2ValidMove == True:
            print("Move too ambiguous")
        else:
            print("{} cannot move to {}.".format(self.name, newPos))

class Knight(Chesspiece):
    __name = "Knight"

    def __init__(self, color):
        super().__init__(Knight.__name, color = color)
        self.__knights = { 
            "knight1": {
                "position":"B2"
            }, 
            "knight2": {
                "position":"G2"
            }
        }
    
    @property
    def knights(self):
        return self.__knights

    @knights.setter
    def knights(self, nSetter):
        knight, position = nSetter
        self.__knights[knight]["position"] = position

    def validMove(self, newPos, currentPos):
        run, rise = self.calcDist(newPos, currentPos)
        if run**2 + rise**2 == 5:
            return True
        else:
            return False
    
    def moveTo(self, newPos):
        knight1Val = self.validMove(newPos, self.knights["knight1"]["position"])
        knight2Val = self.validMove(newPos, self.knights["knight2"]["position"])
        if knight1Val == True and knight2Val == False:
            currentPos = self.knights["knight1"]["position"]
            self.knights = ("knight1", newPos)
            print("{} moved from {} to {}.".format(self.name, currentPos, newPos))
        elif knight2Val == True and knight1Val == False:
            currentPos = self.knights["knight2"]["position"]
            self.knights = ("knight2", newPos)
            print("{} moved from {} to {}.".format(self.name, currentPos, newPos))
        elif knight1Val == True and knight2Val == True:
            print("Move too ambiguous")
        else:
            print("{} cannot move to {}.".format(self.name, newPos))

class Bishop(Chesspiece):
    __name = "Bishop"

    def __init__(self, color):
        super().__init__(Bishop.__name, color = color)
        self.__bishops = { 
            "bishop1": {
                "position":"C1"
            }, 
            "bishop2": {
                "position":"F1"
            }
        }

    @property
    def bishops(self):
        return self.__bishops

    @bishops.setter
    def bishops(self, bSetter):
        bishop, position = bSetter
        self.__bishops[bishop]["position"] = position

    def validMove(self, newPos, currentPos):
        run, rise = self.calcDist(newPos, currentPos)
        if run**2 == rise**2:
            return True
        else:
            return False
    
    def moveTo(self, newPos):
        bishop1ValMov = self.validMove(newPos, self.bishops["bishop1"]["position"])
        bishop2ValMov = self.validMove(newPos, self.bishops["bishop2"]["position"])
        if bishop1ValMov == True and bishop2ValMov == False:
            currentPos = self.bishops["bishop1"]["position"]
            self.bishops = ("bishop1", newPos)
            print("{} moved from {} to {}.".format(self.name, currentPos, newPos))
        elif bishop2ValMov == True and bishop1ValMov == False:
            currentPos = self.bishops["bishop2"]["position"]
            self.bishops = ("bishop2", newPos)
            print("{} moved from {} to {}.".format(self.name, currentPos, newPos))
        elif bishop1ValMov == True and bishop2ValMov == True:
            print("Move too ambiguous")
        else:
            print("{} cannot move to {}.".format(self.name, newPos))

class Queen(Chesspiece):
    __name = "Queen"

    def __init__(self, color, position):
        super().__init__(Queen.__name, color = color)
        self.__position = position

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, new_pos):
        self.__position = new_pos.upper()
    
    def validMove(self, newPos):
        currentPos = self.position
        run, rise = self.calcDist(newPos, currentPos)
        if (run**2 == rise**2) ^ ((run**2 == 0) ^ (rise**2 == 0)):
            return True
        else:
            return False
        
    def moveTo(self, newPos):
        currentPos = self.position
        if self.validMove(newPos) == True:
            self.position = newPos
            print("{} moved from {} to {}.".format(self.name, currentPos, newPos))
        else:
            print("{} cannot move from {} to {}.".format(self.name, currentPos, newPos))

class King(Chesspiece):
    __name = "King"

    def __init__(self, color, position):
        super().__init__(King.__name, color = color)
        self.__firstMove = True
        self.__position = position
    
    @property
    def firstMove(self):
        return self.__firstMove

    @firstMove.setter
    def firstMove(self, state):
        self.__firstMove == state

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, new_pos):
        self.__position = new_pos.upper()

    def validMove(self, position):
        currentPos = self.position
        run, rise = self.calcDist(position, currentPos)
        if (run**2 + rise**2 == 2) ^ ((run**2 == 1) ^ (rise**2 == 1)):
            return True
        else: 
            return False

    def moveTo(self, newPos):
        currentPos = self.position
        if self.validMove(newPos) == True:
            self.position = newPos
            self.firstMove = False
            print("{} moved from {} to {}.".format(self.name, currentPos, newPos))
        else:
            print("{} cannot move from {} to {}.".format(self.name, currentPos, newPos))
