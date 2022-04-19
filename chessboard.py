# chessboard.py

import string

class Chessboard:
    rank = list(string.ascii_uppercase)[:8] 
    numbers = [str(x) for x in range(1,9)]
    # Creates list ["A1", ..., "A8", ..., "H1", ..., "H8"]
    positions = [list(string.ascii_uppercase)[:8][y] + [str(x) for x in range(1,9)][x] for y in range(8) for x in range(8)]
    __board = {key:value for key, value in zip(positions, [[(x,y)] for x in range(1,9) for y in range(1,9)])}

    @property
    def board(self):
        return self.__board

    @board.setter
    def board(self, name_pos):
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

    def updateBoard(self, boardSetter, currentPos = None):
        if currentPos == None:
            self.board = boardSetter
        else:
            self.board[currentPos].pop(1)
            self.board = boardSetter
            print(self.board[currentPos])

    def printBoard(self):
        print(self.board)
