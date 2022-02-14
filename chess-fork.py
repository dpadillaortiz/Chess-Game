class Chessboard:
    def __init__(self, piece = None):
        # To do:
            # add a way to print to board line by line
            # make a one line for loop to create chess board
            # 8x8 chessboard
        self.board = [[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]
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
        # To do:
            # [x] Check if position is valid
            # [x] Check to see if that conditional should be a defined function
        def on_board_w():
            board_index = 'ABCDEFGHabcdefgh123456789'
            if new_pos[0] in board_index and new_pos[1] in board_index:
                update_board()
        def update_board_w():
            """
            if func == True:
                self.position = new_pos
                self.board_obj.board[0][3] = self.position
            """
            if self.board_obj == None:
                pass
            else:
                self.position = new_pos
                self.board_obj.board[0][3] = self.position
        def on_board():
            board_index = 'ABCDEFGHabcdefgh123456789'
            if new_pos[0] in board_index and new_pos[1] in board_index:
                return True
        def update_board(func):
            if func == True:
                self.position = new_pos
                self.board_obj.board[0][3] = self.position
        # would not work with update_board(on_board)
        update_board(on_board())
        print("Moved to:", self.position) 



# To do:
    # Create classes for rook, bishop, etc...
    # Put Chesspiece class within specific piece class
chessBoard = Chessboard()
chessPiece = Chesspiece('Rook', 'A2', chessBoard)
print(chessPiece)
chessPiece.move_piece('C4')


