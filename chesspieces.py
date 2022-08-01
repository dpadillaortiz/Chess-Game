#! /bin/usr/python3


class Movement:

    def distance(self, from_position, to_position):
        from_x, from_y = from_position
        to_x, to_y = to_position
        x = to_x - from_x
        y = to_y - from_y 
        return (x, y)

    def move_pawn_to(self, from_position, to_position, first_move=False):
        if first_move == True and self.distance(from_position, to_position) == (0,2):
            return to_position
        elif distance(from_position, to_position) == (0,1):
            return to_position
    
    def move_rook_to(self, from_position, to_position):
        run, rise = self.distance(from_position, to_position)
        if run == 0 ^ rise == 0:
            return to_position 
        
    def move_knight_to(self, from_position, to_position):
        run, rise = self.distance(from_position, to_position)
        if run**2 + rise**2 == 5:
            return to_position

    def move_bishop_to(self, from_position, to_position):
        run, rise = self.distance(from_position, to_position)
        if run**2 == rise**2:
            return to_position

    def move_king_to(self, from_position, to_position):
        run, rise = self.distance(from_position, to_position)
        if run**2 + rise**2 == 1:
            return to_position

    def move_queen_to(self, from_position, to_position):
        run, rise = self.distance(from_position, to_position)
        if run**2 == rise**2:
            return to_position
        elif rise**2 == 0 ^ run**2 == 0:
            return to_position


        
