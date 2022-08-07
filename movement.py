#! /bin/usr/python3

def distance_between(initial_position: tuple, final_position: tuple) -> tuple:
    '''Distance between two points 
    i.e. Pythagoras theorem
    d^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2
    where (x_2 - x_1) and (y_2 - y_1) are not the hypothenuse 
    Note: returns (x_2 - x_1, y_2 - y_1)
    '''
    initial_x, initial_y = initial_position
    final_x, final_y = final_position
    x = final_x - initial_x
    y = final_y - initial_y
    return (x, y)

def pawn_to(from_position: tuple, to_position: tuple) -> tuple:
    run, rise = distance_between(from_position, to_position)
    moved_vertically_once = run**2 == 0 and rise**2 == 1
    if moved_vertically_once: 
        return to_position
    
def rook_to(from_position: tuple, to_position: tuple) -> tuple:
    run, rise = distance_between(from_position, to_position)
    moved_horizontally = rise**2 == 0
    moved_vertically = run**2 == 0
    if moved_horizontally ^ moved_vertically:
        return to_position 
        
def knight_to(from_position: tuple, to_position: tuple) -> tuple:
    run, rise = distance_between(from_position, to_position)
    if run**2 + rise**2 == 5:
        return to_position

def bishop_to(from_position: tuple, to_position: tuple) -> tuple:
    run, rise = distance_between(from_position, to_position)
    moved_diagonally = run**2 == rise**2
    if moved_diagonally:
        return to_position

def king_to(from_position: tuple, to_position: tuple) -> tuple:
    run, rise = distance_between(from_position, to_position)
    moved_horizontally_once = run**2 == 1 and rise**2 == 0
    moved_vertically_once = run**2 == 0 and rise**2 == 1
    moved_diagonally_once = run**2 == 1 and rise**2 == 1
    if moved_horizontally_once ^ moved_vertically_once:
        return to_position
    elif moved_diagonally_once:
        return to_position

def queen_to(from_position: tuple, to_position: tuple) -> tuple:
    run, rise = distance_between(from_position, to_position)
    moved_horizontally = rise**2 == 0
    moved_vertically = run**2 == 0
    moved_diagonally = run**2 == rise**2
    if moved_diagonally:
        return to_position
    elif moved_horizontally ^ moved_vertically:
        return to_position


if __name__ == '__main__':
    x = queen_to((2,1),(4,1))
    print(x)       
