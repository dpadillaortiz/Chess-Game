# To do:
    # Clean up Chessboard:
        # Right now when I call move_piece/move_to, it likes behind the position
        # When I move to a new position, that index should be cleaned 

import string

class Chessboard:
    def __init__(self):
        # Creates an 8x8 board
        self.board = [[None for x in range(8)] for x in range(8)]
        # Makes this 'ABCDEFGH12345678'into a list - each element is of type str
        self.board_index = list(string.ascii_uppercase)[:8] + [str(x) for x in range(1,9)]
        # Creates {'A':0, ..., 'H':7, '1':0, ..., '8':7}
        self.board_key = {key:value for key, value in zip(self.board_index, [x for x in range(8)] + [x for x in range(8)])}
    def __str__(self):
        return str(self.board)
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
            print("Position is not available")

class Chesspiece:
    def __init__(self, name, position, board_obj = None):
        self.name = name
        self.board_obj = board_obj
        self.position = position
        self.board_obj.update_board(position)
    def __repr__(self):
        return self.name + " is on " + self.position
    # Updates the position of the piece
    def move_piece(self, new_pos):
        # Updates the position of Chesspiece and adds it to Chessboard.board
        def update_position(func):
            if func == True:
                if self.board_obj.spot_available(new_pos) == True:
                    self.position = new_pos
                    self.board_obj.update_board(self.position)
                    print(self.name, "is on", self.position)     
        update_position(self.board_obj.on_board(new_pos))

class Rook(Chesspiece):
    # Initialized Rook differently and I'm still able to use move_piece
    def __init__(self, position, board_obj = None):
        self.name = "Rook"
        self.board_obj = board_obj
        self.position = position
        self.board_obj.update_board(position)
    # movement specific to Rook
    def move_to(self, position):
        self.start_pos = self.position
        self.end_pos = position
        # move horizontally
        if self.start_pos[1] == self.end_pos[1]:
            print(self.name, "moved to", self.end_pos)
            self.move_piece(position)
            return self.end_pos
        # move vertically
        elif self.start_pos[0] == self.end_pos[0]:
            print(self.name, "moved to", self.end_pos)
            return self.end_pos
        else:
            print(self.name, "cannot move to", self.end_pos)

class Knight(Chesspiece):
    def __init__(self, position, board_obj = None):
        self.name = "Knight"
        self.position = position
        self.board_obj = board_obj
        self.board_obj.update_board(position)
    # movement specific to Rook
    def move_to(self, new_pos):
        self.a = self.board_obj.board_key[new_pos[1]] - self.board_obj.board_key[self.position[1]]
        self.b = self.board_obj.board_key[new_pos[0]] - self.board_obj.board_key[self.position[0]]
        if self.a**2 + self.b**2 == 5:
            self.move_piece(new_pos)
        else:
            print("Not a valid Knight move")

class Bishop(Chesspiece): 
    # Bishop movement will work similarly like Knight's movement
    # if you create a right triagnle with the starting and ending point
    # the triangle will alway be isoceles triangle i.e. both legs the same
    # x^2 + x^2 = c^2 => 2x^2 = c^2
    # unlike Knight the triangle won't be the same every time 
    def __init__(self, position, board_obj = None):
        self.name = "Bishop"
        self.position = position
        self.board_obj = board_obj
        self.board_obj.update_board(position)
    def move_to(self, new_pos):
        self.a = self.board_obj.board_key[new_pos[1]] - self.board_obj.board_key[self.position[1]]
        self.b = self.board_obj.board_key[new_pos[0]] - self.board_obj.board_key[self.position[0]]
        if self.a**2 == self.b**2:
            print(new_pos, "is valid Bishop move")
             #self.move_piece(new_pos)
        else:
            print("Not a valid Bishop move")

# class Pawn:
    # movement is dependent on whether or not the pawn has moved

# class Queen:
    # Inherit Rook
    # Inherit Bishop
# class King
    # Possibly inherit Pawn

chessBoard = Chessboard()
print(chessBoard)

# Bishop movement
bishop = Bishop("C1", chessBoard)
print(bishop)
print(chessBoard)

letters = list(string.ascii_uppercase)[:8] 
numbers = [str(x) for x in range(1,9)]
positions = [letters[y] + numbers[x] for y in range(len(letters)) for x in range(len(numbers))]

for spot in positions:
    bishop.move_to(spot)

"""
# Knight movement
knight = Knight("A1", chessBoard)
print(knight)
print(chessBoard)
knight.move_to("C3")
print(chessBoard)
knight.move_to("B3")
knight.move_to("C4")
knight.move_to("D7")
knight.move_to("D2")
"""