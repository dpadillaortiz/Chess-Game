class Chessboard:
    def __init__(self, piece):
        self.board = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
        self.piece = piece

        if "A" in self.piece.position:
            self.board[0][2] = self.piece
    def __str__(self):
        return self.board

class Chesspiece:
    def __init__(self, name, position, board):
        self.name = name
        self.position = position
        self.board = board
    def __repr__(self):
        return self.name + " is on " + self.position
    # Updates the position of the piece
    def move_piece(self, new_pos):
        self.position = new_pos
        if "F" in self.position:
            if self.board[0][2] == None:
                self.board[0][2] = self.name
                print(self.name,"moved to",self.board[0][2])


board = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]

rook = Chesspiece("rook","A2",board)
print(rook)

#chessb = Chessboard(rook)
#print(chessb)

#test = [None,None,None]
#print(test)

rook.move_piece("F4")
#print(rook)

print(board)
