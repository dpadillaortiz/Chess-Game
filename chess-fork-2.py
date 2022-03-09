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
    # defining getter for board
    @property
    def get_board(self):
        return self.__board
    # defining setter for board
    @get_board.setter
    def update_board(self, name_pos, old_position = None):
        name, position, old_position = name_pos
        # using __board_positions to check valid position is replacing the need for on_board
        if self.spot_available(position) == True:
            self.__board[self.x_axis][self.y_axis] = name
            if old_position != None:
                self.x_old = self._board_key[old_position[0]]
                self.y_old = self._board_key[old_position[1]]
                self.__board[self.x_old][self.y_old] = None
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

class Chesspiece:
    def __init__(self, name, position, chessboard = None, color = None):
        self.__name = name
        self.__position = position.upper()
        self.__chessboard = chessboard
        self.__chessboard.update_board = (self.__name, self.__position, None)
        self.__color = color
    # getter
    @property
    def color(self):
        return self.__color
    #setter
    @color.setter
    def color(self, colour):
        self.color = colour
    #getter
    @property
    def get_name(self):
        return self.__name
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
            self.__position, self.__chessboard.update_board = self.to_pos, (self.get_name, self.to_pos, self.from_pos)
            print("{} moved from {} to {}".format(self.get_name, self.from_pos, self.to_pos))
    # calculates distance bw new position and old position
    def calc_dist(self, position):
        self.to_pos = position.upper()
        self.from_pos = self.get_position
        self.a = self.__chessboard._board_key[self.to_pos[1]] - self.__chessboard._board_key[self.from_pos[1]]
        self.b = self.__chessboard._board_key[self.to_pos[0]] - self.__chessboard._board_key[self.from_pos[0]]
        return (self.a, self.b)
    # print position
    def print_position(self):
        print("{} is on {}.".format(self.get_name, self.get_position))
    # print color
    def get_color(self):
        print(self.color)

class Rook(Chesspiece):
    def __init__(self, position, chessboard = None, color = None):
        super().__init__("Rook", position, chessboard, color)
    def move_to(self, position):
        a_side, b_side = self.calc_dist(position)
        if a_side**2 == 0:
            self.set_position = position
        elif b_side**2 == 0:
            self.set_position = position
    def valid_moves(self, position):
        a_side, b_side = self.calc_dist(position)
        if a_side**2 == 0:
            print("{} can move to {}.".format(self.get_name, position))
        elif b_side**2 == 0:
            print("{} can move to {}.".format(self.get_name, position))

class Knight(Chesspiece):
    def __init__(self, position, chessboard = None, color = None):
        super().__init__("Knight", position, chessboard, color)
    def move_to(self, position):
        a_side, b_side = self.calc_dist(position)
        if a_side**2 + b_side**2 == 5:
            self.set_position = position
    def valid_moves(self, position):
        a_side, b_side = self.calc_dist(position)
        if a_side**2 + b_side**2 == 5:
            print("{} can move to {}.".format(self.get_name, position))

class Bishop(Chesspiece):
    def __init__(self, position, chessboard = None, color = None):
        super().__init__("Bishop", position, chessboard, color)
    def move_to(self, position):
        a_side, b_side = self.calc_dist(position)
        if a_side**2 == b_side**2:
            self.set_position = position
    def valid_moves(self, position):
        a_side, b_side = self.calc_dist(position)
        if a_side**2 == b_side**2:
            print("{} can move to {}.".format(self.get_name, position))

class Queen(Chesspiece):
    def __init__(self, position, chessboard = None, color = None):
        super().__init__("Queen", position, chessboard, color)
    def move_to(self, position):
        a_side, b_side = self.calc_dist(position)
        if a_side**2 == b_side**2:
            self.set_position = position
        elif a_side**2 == 0:
            self.set_position = position
        elif b_side**2 == 0:
            self.set_position = position
    def valid_moves(self, position):
        a_side, b_side = self.calc_dist(position)
        if a_side**2 == b_side**2:
            print("{} can move to {}.".format(self.get_name, position))
        elif a_side**2 == 0:
            print("{} can move to {}.".format(self.get_name, position))
        elif b_side**2 == 0:
            print("{} can move to {}.".format(self.get_name, position))

class King(Chesspiece):
    def __init__(self, position, chessboard = None, color = None):
        super().__init__("King", position, chessboard, color)
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
    def valid_moves(self, position):
        a_side, b_side = self.calc_dist(position)
        # move once diagonally 
        if a_side**2 == 1 and b_side**2 == 1:
            print("{} can move to {}.".format(self.get_name, position))
        # move once vertically  
        elif a_side**2 == 1 and b_side**2 == 0:
            print("{} can move to {}.".format(self.get_name, position))
        # move once horizontally 
        elif a_side**2 == 0 and b_side**2 == 1:
            print("{} can move to {}.".format(self.get_name, position))
            
class Pawn(Chesspiece):
    def __init__(self, position, chessboard = None, color = None):
        super().__init__("Pawn", position, chessboard, color)
    def move_to(self, position):
        a_side, b_side = self.calc_dist(position)
        if a_side > 0 and a_side**2 == 1 and b_side**2 == 0:
            self.set_position = position
    def valid_moves(self, position):
        a_side, b_side = self.calc_dist(position)
        if a_side > 0 and a_side**2 == 1 and b_side**2 == 0:
            print("{} can move to {}.".format(self.get_name, position))

def test(chess_piece):
    chessBoard = Chessboard()
    rook = Rook("C3", chessBoard, "black")
    knight = Knight("C3", chessBoard, "black")
    bishop = Bishop("C3", chessBoard, "black")
    queen = Queen("C3", chessBoard, "black")
    king = King("C3", chessBoard, "black")
    pawn = Pawn("C3", chessBoard, "black")
    pieces = {"pawn":pawn, "rook":rook, "knight":knight, "bishop":bishop, "queen":queen, "king":king}

    letters = list(string.ascii_uppercase)[:8] 
    numbers = [str(x) for x in range(1,9)]
    positions = [letters[y] + numbers[x] for y in range(len(letters)) for x in range(len(numbers))]

    if chess_piece in pieces:
        for spot in positions:
            pieces[chess_piece].valid_moves(spot)

# -- Ideas --

class GameState:
    def __init__(self):
        self.__round = 1
        self.__turn = None
    @property
    def round(self):
        return self.__round
    @round.setter
    def round(self, round):
        self.__round += round
    @property
    def turn(self): 
        return self.__turn
    @turn.setter
    def turn(self, color):
        self.__turn = color



class Color:
    def __init__(self, board = None, color = None):
        self.pawn_1 = Pawn("A2", board, color)
        self.pawn_2 = Pawn("B2", board, color)
        self.pawn_3 = Pawn("C2", board, color)
        self.pawn_4 = Pawn("D2", board, color)
        self.pawn_5 = Pawn("E2", board, color)
        self.pawn_6 = Pawn("F2", board, color)
        self.pawn_7 = Pawn("G2", board, color)
        self.pawn_8 = Pawn("H2", board, color)

        self.rook_1 = Rook("A1", board, color)
        self.rook_2 = Rook("H1", board, color)

        self.knight_1 = Knight("B1", board, color)
        self.knight_2 = Knight("G1", board, color)

        self.bishop_1 = Bishop("C1", board, color)
        self.bishop_2 = Bishop("F1", board, color)

        self.king = King("D1", board, color)
        self.queen = Queen("E1", board, color)
        

class Black(Color):
    def __init__(self, board = None):
        # super().__init__(board, "Black")
        self.pawn_1 = Pawn("A2", board, "Black")
        self.pawn_2 = Pawn("B2", board, "Black")

class White(Color):
    def __init__(self, board = None):
        # super().__init__(board, "White")
        self.pawn_1 = Pawn("A6", board, "Black")
        self.pawn_2 = Pawn("B6", board, "Black")



chessboard = Chessboard()
daniel = Black(chessboard)
player = White(chessboard)
chessboard.print_board()
daniel.pawn_1.get_color()




