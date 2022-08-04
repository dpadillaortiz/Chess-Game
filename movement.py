#! /bin/usr/python3

def distance_between(initial_position: tuple, final_position: tuple) -> tuple:
    '''Distance between two points 
    i.e. Pythagoras theorem
    d^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2
    where (x_2 - x_1) and (y_2 - y_1) are not the hypothenuse 
    Note: returns ((x_2 - x_1), (y_2 - y_1))
    '''
    initial_x, initial_y = initial_position
    final_x, final_y = final_position
    x = final_x - initial_x
    y = final_y - initial_y
    return (x, y)

def pawn_to(from_position: tuple, to_position: tuple) -> tuple:
    run, rise = distance_between(from_position, to_position)
    if (rise == 1 or rise == 2) and run == 0:
        return to_position
    
def rook_to(from_position: tuple, to_position: tuple) -> tuple:
    run, rise = distance_between(from_position, to_position)
    if run == 0 ^ rise == 0:
        return to_position 
        
def knight_to(from_position: tuple, to_position: tuple) -> tuple:
    run, rise = distance_between(from_position, to_position)
    if run**2 + rise**2 == 5:
        return to_position

def bishop_to(from_position: tuple, to_position: tuple) -> tuple:
    run, rise = distance_between(from_position, to_position)
    if run**2 == rise**2:
        return to_position

def king_to(from_position: tuple, to_position: tuple) -> tuple:
    run, rise = distance_between(from_position, to_position)
    if run**2 + rise**2 == 1:
        return to_position

def queen_to(from_position: tuple, to_position: tuple) -> tuple:
    run, rise = distance_between(from_position, to_position)
    if run**2 == rise**2:
        return to_position
    elif (rise**2 == 0) ^ (run**2 == 0):
        return to_position


if __name__ == '__main__':
    x = queen_to((2,1),(4,1))
    print(x)       
