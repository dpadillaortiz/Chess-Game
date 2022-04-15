# chesspiece.py
import chessboard as Chessboard

class Chesspiece:
    kingInCheck = False
    canMove = True
    
    def __init__(self, name, position, color):
        self.__name = name
        self.__position = position
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
        #print("test")
        self.__position = new_pos

        
         

    # Other Functions:
    def __repr__(self):
        return "{} is on {}".format(self.name, self.position)


class Pawn(Chesspiece):
    name = "Pawn"
    initPos = True

    def __init__(self, position, color):
        super().__init__(Pawn.name, position, color)

class Rook(Chesspiece):
    name = "Rook"
    initPos = True

    def __init__(self, position, color):
        super().__init__(Rook.name, position, color)


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
