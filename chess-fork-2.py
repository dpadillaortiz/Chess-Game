# Chess Project

import string

class Chessboard:
    def __init__(self):
        # Creates an 8x8 board
        self.__board = [[None for x in range(8)] for x in range(8)]
        self.__letters = list(string.ascii_uppercase)[:8] 
        self.__numbers = [str(x) for x in range(1,9)]
        # Creates list ['A', ..., 'H','1', ..., '8']
        # self.__board_index = self.letters + self.numbers
        # Creates {'A':0, ..., 'H':7, '1':0, ..., '8':7}
        #self.__board_key = {key:value for key, value in zip(self.board_index, [x for x in range(8)] + [x for x in range(8)])}
        # Creates list ["A1", ..., "A8", ..., "H1", ..., "H8"]
        self.__board_positions = [self.__letters[y] + self.__numbers[x] for y in range(len(self.__letters)) for x in range(len(self.__numbers))]
    def __repr__(self):
        return str(self.__board)
    # Checks to see if new_pos is a within the bounds of the board
    def on_board(self, position):
        if position[0] in self.board_index and position[1:] in self.board_index:
            return True
        else:
            print(position, "is out of bounds.")
    # Updates the board with the position of the piece
    def update_board(self, position):
        self.x_pos = self.board_key[position[0]]
        self.y_pos = self.board_key[position[1]]
        self.board[self.x_pos][self.y_pos] = position
    # Checks if position is available
    def spot_available(self, position):
        self.x_pos = self.board_key[position[0]]
        self.y_pos = self.board_key[position[1]]
        if self.board[self.x_pos][self.y_pos] == None:
            return True
        else:
            print(position + " is taken.")
    # defining getter for board
    @property
    def get_board(self):
        return self.__board

    # Prints board in a legible way 
    def print_board(self):
        """
        Problem:
        Got TypeError: 'list' object is not callable when using `meme_p = self.get_board()` 
        "The Python “typeerror: ‘list’ object is not callable” error is raised 
        when you try to access a list as if it were a function."

        Solution: 
        Do not use "()" at the end
        """
        meme_p = self.get_board
        for row in meme_p:
            print(row)
    
    """
    the def function does not have to be the same name as the 
    property decorated function
    """
    @get_board.setter
    def update_board(self, position):
        if position.upper() in self.__board_positions:
            print("yo")
            self.__board[0][2] = position
        else:
            print("baego")
    



test = Chessboard()
test.update_board = "A3"
test.print_board()
