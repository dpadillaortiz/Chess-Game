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
    def board(self, pos_name):
        # the pos_name parameter is a tuple
        name, new_pos = pos_name
        self.__board[new_pos].append(name)
        """if self.isFree(new_pos) == True and self.onBoard(new_pos):
            self.__board[new_pos].append(name)"""

    # Other
    def isFree(self, position):
    # Checks whether the position is available on the board
        if len(Chessboard.__board[position]) == 1:
            return True

    def onBoard(self, test):
    # Checks whether the position is valid
        if test in Chessboard.positions:
            return True

    def printBoard(self):
        print(self.board)
