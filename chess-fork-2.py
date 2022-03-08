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
        self._board_key = {key:value for key, value in zip(self.__board_axis, [x for x in range(8)] + [x for x in range(8)])}
        # Creates list ["A1", ..., "A8", ..., "H1", ..., "H8"]
        self.__board_positions = [self.__letters[y] + self.__numbers[x] for y in range(8) for x in range(8)]

    # Checks if position is available
    def spot_available(self, position):
        spot = position.upper()
        self.x_axis = self._board_key[spot[0]]
        self.y_axis = self._board_key[spot[1]]
        if spot in self.__board_positions:
            if self.__board[self.x_axis][self.y_axis] == None:
                return True

    # Prints board in a legible way 
    def print_board(self):
        chessboard = self.get_board
        for row in chessboard:
            print(row)
    
    # defining getter for board
    @property
    def get_board(self):
        return self.__board
    
    # defining setter for board
    @get_board.setter
    def update_board(self, name_pos, old_position = None):
        name, position, old_position = name_pos
        # using __board_positions to check valid position 
        # is replacing the need for on_board
        if self.spot_available(position) == True:
            self.__board[self.x_axis][self.y_axis] = name
            if old_position != None:
                self.x_old = self._board_key[old_position[0]]
                self.y_old = self._board_key[old_position[1]]
                self.__board[self.x_old][self.y_old] = None

class Chesspiece:
    def __init__(self, name, position, chessboard = None):
        self.__name = name
        self.__position = position.upper()
        self.__chessboard = chessboard
        self.__chessboard.update_board = (self.__name, self.__position, None)
    
    # defining getter for chesspiece
    @property
    def get_position(self):
        return self.__position

    # defining setter
    @get_position.setter
    def set_position(self, position):
        self.to_pos = position.upper()
        self.from_pos = self.get_position
        if self.__chessboard.spot_available(self.to_pos) == True:
            # update position and update the board
            self.__position, self.__chessboard.update_board = self.to_pos, (self.__name, self.to_pos, self.from_pos)
            print("{} moved from {} to {}".format(self.__name, self.from_pos, self.to_pos))

    def calc_dist(self, position):
        self.to_pos = position.upper()
        self.from_pos = self.get_position
        self.a = self.__chessboard._board_key[self.to_pos[1]] - self.__chessboard._board_key[self.from_pos[1]]
        self.b = self.__chessboard._board_key[self.to_pos[0]] - self.__chessboard._board_key[self.from_pos[0]]
        return (self.a, self.b)


class Rook(Chesspiece):
    def __init__(self, position, chessboard = None):
        super().__init__("Rook", position, chessboard)
    def move_to(self, position):
        a_side, b_side = self.calc_dist(position)
        if a_side**2 == 0:
            self.set_position = position
        elif b_side**2 == 0:
            self.set_position = position


class Knight(Chesspiece):
    def __init__(self, position, chessboard = None):
        super().__init__("Knight", position, chessboard)
    def move_to(self, position):
        a_side, b_side = self.calc_dist(position)
        if a_side**2 + b_side**2 == 5:
            self.set_position = position


class Bishop(Chesspiece):
    def __init__(self, position, chessboard = None):
        super().__init__("Bishop", position, chessboard)
    def move_to(self, position):
        a_side, b_side = self.calc_dist(position)
        if a_side**2 == b_side**2:
            self.set_position = position


class Queen(Chesspiece):
    def __init__(self, position, chessboard = None):
        super().__init__("Queen", position, chessboard)
    def move_to(self, position):
        a_side, b_side = self.calc_dist(position)
        if a_side**2 == b_side**2:
            self.set_position = position
        elif a_side**2 == 0:
            self.set_position = position
        elif b_side**2 == 0:
            self.set_position = position


class King(Chesspiece):
    def __init__(self, position, chessboard = None):
        super().__init__("King", position, chessboard)
    def move_to(self, position):
        a_side, b_side = self.calc_dist(position)
        # move once diagonally 
        if a_side**2 == 1 and b_side**2 == 1:
            self.set_position = position
        # move once vertically  
        elif a_side**2 == 1 and b_side**2 == 0:
            self.set_position = position
        # move once horizontally 
        elif a_side**2 == 0 and b_side**2 == 1:
            self.set_position = position


class Pawn(Chesspiece):
    def __init__(self, position, chessboard = None):
        super().__init__("Pawn", position, chessboard)
    def move_to(self, position):
        a_side, b_side = self.calc_dist(position)
        if a_side > 0 and a_side**2 == 1 and b_side**2 == 0:
            self.set_position = position


def test(chess_piece):
    chessBoard = Chessboard()
    # rook = Rook("C3", chessBoard)
    # knight = Knight("C3", chessBoard)
    # bishop = Bishop("C3", chessBoard)
    # queen = Queen("C3", chessBoard)
    # king = King("C3", chessBoard)
    pawn = Pawn("C3", chessBoard)
    pieces = {"pawn":pawn}

    letters = list(string.ascii_uppercase)[:8] 
    numbers = [str(x) for x in range(1,9)]
    positions = [letters[y] + numbers[x] for y in range(len(letters)) for x in range(len(numbers))]

    if chess_piece in pieces:
        for spot in positions:
            pieces[chess_piece].move_to(spot)

    chessBoard.print_board()


test("pawn")

"""
'|        |'
'[ Pawn   ]'
'|--------|'
'[-Pawn---]'
'|-Rook---|'
'|-Knight-|'
'|-Bishop-|'
'|-Queen--|'
'|-King---|'

'|A1:Knight|'
'|A2:Rook  |'


# board_0 = [["{}{}:".format(l,x+1) for l in letters] for x in range(8)]
"""

