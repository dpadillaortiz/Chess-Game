# To do:
    # [x] Create classes for rook, bishop, etc...
    # [x] Put Chesspiece class within specific piece class
    # [x] Map the board_index to corresponding spot in self.board
    # Check if a piece is already on that spot 
        # Might have to include taking pieces
        # Should I create a different class to keep track of where pieces are?
    # Create Rook movement

import string

class Chessboard:
    def __init__(self, piece = None):
        # Creates an 8x8 board
        self.board = [[None for x in range(8)] for x in range(8)]
        self.piece = piece
        # Makes this 'ABCDEFGH12345678'into a list - each element is of type str
        self.board_index = list(string.ascii_uppercase)[:8] + [str(x) for x in range(1,9)]
        # Creates {'A':0, ..., 'H':7, '1':0, ..., '8':7}
        self.board_key = {key:value for key, value in zip(self.board_index, [x for x in range(8)] + [x for x in range(8)])}
    def __str__(self):
        return str(self.board)
    # Updates the board with the position of the piece
    def update_board(self, position):
            self.x_pos = self.board_key[position[0]]
            self.y_pos = self.board_key[position[1]]
            self.board[self.x_pos][self.y_pos] = position

class Chesspiece:
    def __init__(self, name, position, board_obj = None):
        self.name = name
        self.position = position
        self.board_obj = board_obj
    def __repr__(self):
        return self.name + " is on " + self.position
    # Updates the position of the piece
    def move_piece(self, new_pos):
        # Checks to see if new_pos is a within the bounds of the board
        def on_board():
            if new_pos[0] in self.board_obj.board_index and new_pos[1:] in self.board_obj.board_index:
                return True
            else:
                print(new_pos, "is out of bounds.")
        # Updates the position of Chesspiece and adds it to Chessboard.board
        def update_position(func):
            if func == True:
                self.position = new_pos
                self.board_obj.update_board(self.position)
        update_position(on_board())

# class Pawn:
    # movement is dependent on whether or not the pawn has moved
# class Rook:
# class Knight:

# class Bishop:
# class Queen:
    # Inherit Rook
    # Inherit Bishop
# class King
    # Possibly inherit Pawn

chessBoard = Chessboard()


chessPiece = Chesspiece('Rook', 'A2', chessBoard)
print(chessPiece)
chessPiece.move_piece('C4')
chessPiece.move_piece('z4')
chessPiece.move_piece('2J')
chessPiece.move_piece('20')

print(chessBoard)