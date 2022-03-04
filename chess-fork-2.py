# Chess Project

import string

class Chessboard:
    def __init__(self):
        # Creates an 8x8 board
        self.__board = [[None for x in range(8)] for x in range(8)]
        self.__letters = list(string.ascii_uppercase)[:8] 
        self.__numbers = [str(x) for x in range(1,9)]
        # Creates list ['A', ..., 'H','1', ..., '8']
        self.__board_axis = self.__letters + self.__numbers
        # Creates {'A':0, ..., 'H':7, '1':0, ..., '8':7}
        self.__board_key = {key:value for key, value in zip(self.__board_axis, [x for x in range(8)] + [x for x in range(8)])}
        # Creates list ["A1", ..., "A8", ..., "H1", ..., "H8"]
        self.__board_positions = [self.__letters[y] + self.__numbers[x] for y in range(len(self.__letters)) for x in range(len(self.__numbers))]
    def __repr__(self):
        return str(self.__board)

    # Checks if position is available
    def spot_available(self, position):
        self.x_pos = self.__board_key[position[0]]
        self.y_pos = self.__board_key[position[1]]
        if self.__board[self.x_pos][self.y_pos] == None:
            return True

    # Prints board in a legible way 
    def print_board(self):
        meme_p = self.get_board
        for row in meme_p:
            print(row)
    
    # defining getter for board
    @property
    def get_board(self):
        return self.__board
    
    @get_board.setter
    def update_board(self, position):
        # using __board_positions to check valid position 
        # is replacing the need for on_board
        position = position.upper()
        if position in self.__board_positions:
            if self.spot_available(position):
                self.__board[self.x_pos][self.y_pos] = position
        else:
            print("Position is unavailable")
    



test = Chessboard()
test.update_board = "A3"
test.print_board()
test.update_board = "r4"
test.update_board = "h3"
test.print_board()