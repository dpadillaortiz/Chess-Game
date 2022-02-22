# To do:
    # Clean up Chessboard:
        # Right now when I call move_piece/move_to, it likes behind the position
        # When I move to a new position, that index should be cleaned 

import string

class Chessboard:
    def __init__(self):
        # Creates an 8x8 board
        self.board = [[None for x in range(8)] for x in range(8)]
        self.letters = list(string.ascii_uppercase)[:8] 
        self.numbers = [str(x) for x in range(1,9)]
        # Creates list ['A', ..., 'H','1', ..., '8']
        self.board_index = self.letters + self.numbers
        # Creates {'A':0, ..., 'H':7, '1':0, ..., '8':7}
        self.board_key = {key:value for key, value in zip(self.board_index, [x for x in range(8)] + [x for x in range(8)])}
        # Creates list ["A1", ..., "A8", ..., "H1", ..., "H8"]
        self.board_positions = [self.letters[y] + self.numbers[x] for y in range(len(self.letters)) for x in range(len(self.numbers))]
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
    def move_to(self, new_pos):
        # move horizontally
        if new_pos[1] == self.position[1]:
            self.move_piece(new_pos)
        # move vertically
        elif new_pos[0] == self.position[0]:
            self.move_piece(new_pos)
        else:
            print(new_pos,"is not a valid Rook move.")

class Knight(Chesspiece):
    def __init__(self, position, board_obj = None):
        self.name = "Knight"
        self.position = position
        self.board_obj = board_obj
        self.board_obj.update_board(position)
    # movement specific to Knight
    def move_to(self, new_pos):
        self.a = self.board_obj.board_key[new_pos[1]] - self.board_obj.board_key[self.position[1]]
        self.b = self.board_obj.board_key[new_pos[0]] - self.board_obj.board_key[self.position[0]]
        if self.a**2 + self.b**2 == 5:
            self.move_piece(new_pos)
        else:
            print(new_pos,"is not a valid Knight move.")

class Bishop(Chesspiece): 
    def __init__(self, position, board_obj = None):
        self.name = "Bishop"
        self.position = position
        self.board_obj = board_obj
        self.board_obj.update_board(position)
    # Movement specific to Bishop
    def move_to(self, new_pos):
        self.a = self.board_obj.board_key[new_pos[1]] - self.board_obj.board_key[self.position[1]]
        self.b = self.board_obj.board_key[new_pos[0]] - self.board_obj.board_key[self.position[0]]
        if self.a**2 == self.b**2:
            self.move_piece(new_pos)
        else:
            print(new_pos,"is not a valid Bishop move.")
        

# class Pawn:
    # movement is dependent on whether or not the pawn has moved

# class Queen:
    # Inherit Rook
    # Inherit Bishop
# class King
    # Possibly inherit Pawn

chessBoard = Chessboard()
print(chessBoard)

"""
# Rook movement
rook = Rook("D4", chessBoard)
print(rook)
print(chessBoard)

letters = list(string.ascii_uppercase)[:8] 
numbers = [str(x) for x in range(1,9)]
positions = [letters[y] + numbers[x] for y in range(len(letters)) for x in range(len(numbers))]

for spot in positions:
    rook.move_to(spot)
"""

"""
# Bishop movement
bishop = Bishop("E4", chessBoard)
print(bishop)
print(chessBoard)

letters = list(string.ascii_uppercase)[:8] 
numbers = [str(x) for x in range(1,9)]
positions = [letters[y] + numbers[x] for y in range(len(letters)) for x in range(len(numbers))]

for spot in positions:
    bishop.move_to(spot)
"""

"""
# Knight movement
knight = Knight("C3", chessBoard)
print(knight)
print(chessBoard)

letters = list(string.ascii_uppercase)[:8] 
numbers = [str(x) for x in range(1,9)]
positions = [letters[y] + numbers[x] for y in range(len(letters)) for x in range(len(numbers))]

for spot in positions:
    knight.move_to(spot)
"""

