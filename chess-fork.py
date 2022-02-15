class Chessboard:
    def __init__(self, piece = None):
        # Creates an 8x8 board
        self.board = [[None for x in range(8)] for x in range(8)]
        self.piece = piece
    def __str__(self):
        return str(self.board)

class Chesspiece:
    def __init__(self, name, position, board_obj = None):
        self.name = name
        self.position = position
        self.board_obj = board_obj
    def __repr__(self):
        return self.name + " is on " + self.position
    # Updates the position of the piece
    def move_piece(self, new_pos):
        def on_board():
            board_index = 'ABCDEFGHabcdefgh123456789'
            if new_pos[0] in board_index and new_pos[1] in board_index:
                return True
            else:
                print(new_pos, "is out of bounds.")
        def update_board(func):
            if func == True:
                self.position = new_pos
                self.board_obj.board[0][3] = self.position
                print(self.name, "moved to", self.position) 
        update_board(on_board())
# To do:
    # [x] Create classes for rook, bishop, etc...
    # [x] Put Chesspiece class within specific piece class
# class Pawn
# class Rook:
# class Bishop:
# class Knight:
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