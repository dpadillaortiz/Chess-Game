# chessboard.py

import string

class Chessboard:
    rank = list(string.ascii_uppercase)[:8] 
    numbers = [str(x) for x in range(1,9)]
    # Creates list ["A1", ..., "A8", ..., "H1", ..., "H8"]
    positions = [list(string.ascii_uppercase)[:8][y] + [str(x) for x in range(1,9)][x] for y in range(8) for x in range(8)]
    __board = {key:value for key, value in zip(positions, [[(x,y)] for x in range(1,9) for y in range(1,9)])}
   
    # Get Functions
    @property
    def board(self):
        return self.__board

    # Set Functions
    @board.setter
    def board(self, name_pos):
        # the name_pos parameter is a tuple
        name, new_pos = name_pos
        self.__board[new_pos].append(name)

    # Other
    def isFree(self, position):
    # Checks whether the position is available on the board
        if len(Chessboard.__board[position]) == 1:
            return True
    
    def onBoard(self, position):
    # Checks whether the position is valid
        if position in Chessboard.positions:
            return True

    def updateBoard(self, newPos, lastPos = None):
        if lastPos == None:
            self.board = newPos
        else:
            self.board[lastPos].pop(1)
            self.board = newPos


    def printBoard(self):
        print(self.board)
