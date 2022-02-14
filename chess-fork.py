class Chessboard:
    def __init__(self, piece = None):
        self.board = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
        self.piece = piece
    def __str__(self):
        return str(self.board)

class Chesspiece:
    def __init__(self, name, position, board = None):
        self.name = name
        self.position = position
        self.board = board
    def __repr__(self):
        return self.name + " is on " + self.position
    # Updates the position of the piece
    def move_piece(self, new_pos):
        self.position = new_pos
        print(self) 

chessBoard = Chessboard()
chessPiece = Chesspiece('Rook', 'A2')

print(chessBoard)

print(chessPiece)

chessPiece.move_piece('C4')
