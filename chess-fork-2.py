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

    # Checks if position is available
    def spot_available(self, position):
        self.x_axis = self.__board_key[position[0]]
        self.y_axis = self.__board_key[position[1]]
        position = position.upper()
        if position in self.__board_positions:
            if self.__board[self.x_axis][self.y_axis] == None:
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
    
    # defining setter for board
    @get_board.setter
    def update_board(self, name_pos):
        name, position = name_pos
        # using __board_positions to check valid position 
        # is replacing the need for on_board
        if self.spot_available(position) == True:
            self.__board[self.x_axis][self.y_axis] = name

class Chesspiece:
    def __init__(self, name, position, chessboard = None):
        self.__name = name
        self.__position = position
        self.__chessboard = chessboard
        self.__chessboard.update_board = (self.__name, self.__position)
    # defining getter for chesspiece
    @property
    def get_position(self):
        return self.__position
    # defining setter
    @get_position.setter
    def set_position(self, position):
        self.to_pos = position
        self.from_pos = self.__position
        if self.__chessboard.spot_available(self.to_pos) == True:
            self.__position, self.__chessboard.update_board = self.to_pos, (self.__name, self.to_pos)
            print("{} moved from {} to {}".format(self.__name, self.from_pos, self.to_pos))







test = Chessboard()
rook = Chesspiece("Rook", "B3", test)
test.print_board()
print()
rook.set_position = "C3"
test.print_board()


