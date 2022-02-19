# To do:
    # [x] Create classes for rook, bishop, etc...
    # [x] Put Chesspiece class within specific piece class
    # [x] Map the board_index to corresponding spot in self.board
    # [x]Check if a piece is already on that spot 
        # [x] Might have to include taking pieces
        # [x] Should I create a different class to keep track of where pieces are?
            # Added to Chessboard
    # [x] Create Rook movement
    # [x] Move on_board to Chessboard
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
    # move to
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


# class Pawn:
    # movement is dependent on whether or not the pawn has moved
# class Knight:
# class Bishop:
# class Queen:
    # Inherit Rook
    # Inherit Bishop
# class King
    # Possibly inherit Pawn

chessBoard = Chessboard()
print(chessBoard)
"""
chessPiece = Chesspiece('Rook', 'A2', chessBoard)
print(chessPiece)
chessPiece.move_piece('C4')
chessPiece.move_piece('z4')
chessPiece.move_piece('2J')
chessPiece.move_piece('20')

print(chessBoard)


queenchessPiece = Chesspiece('Queen', 'A3', chessBoard)
print(queenchessPiece)
# Should print "Position is not available"
queenchessPiece.move_piece('C4')
# Should have A3 on the board
print(chessBoard)

kingchessPiece = Chesspiece('King', 'C4', chessBoard)
print(kingchessPiece)

"""
rook = Rook("A3", chessBoard)
print(rook)
rook.move_piece('C4')
print(chessBoard)
rook.move_to("F4")
rook.move_to("C8")
rook.move_to("F8")
rook.move_to("F4")

rook.move_to("F2")
rook.move_to("F2")

print(chessBoard)
