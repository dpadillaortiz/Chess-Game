#! /bin/usr/python3

def generate_coordinates():
    '''Returns a list of coordinates for an 8x8 grid:
    (1,1),...,(1,8),...,(8,1),...,(8,8)
    '''
    range_of_eight = range(1,9)
    coordinates = [(x,y) for x in range_of_eight for y in range_of_eight]
    return coordinates


def distance_between(initial_position: tuple, final_position: tuple) -> tuple:
    '''Distance between two points derived from pythagoras theorem
    d^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2
    where (x_2 - x_1) and (y_2 - y_1) are not the hypothenuse and
    where run = x_2 - x_1 and rise = y_2 - y_1
    returns (run, rise)
    '''
    initial_x, initial_y = initial_position
    final_x, final_y = final_position
    run = final_x - initial_x
    rise = final_y - initial_y
    return run, rise

def vertical_movement():
    run, rise = distance_between(from_position, to_position)
    return run**2 == 0

def horizontal_movement():
    run, rise = distance_between(from_position, to_position)
    return rise**2 == 0

def diagonal_movement():
    run, rise = distance_between(from_position, to_position)
    return rise**2 == rise**2

def moved_rook():
    return horizontal_movement ^ vertical_movement

def moved_bishop():
    return diagonal_movement
    
def moved_queen():
    return moved_bishop() ^ moved_rook()

def moved_pawn():
    run, rise = distance_between(from_position, to_position)
    moved_vertically_once = run**2 == 0 and rise**2 == 1
    moved_vertically_twice = run**2 == 0 and rise**2 == 2
    return moved_vertically_once

def moved_knight():
    run, rise = distance_between(from_position, to_position)
    moved_knight = run**2 + rise**2 == 5
    return moved_knight

def moved_king():
    run, rise = distance_between(from_position, to_position)
    moved_horizontally_once = run**2 == 1 and rise**2 == 0
    moved_vertically_once = run**2 == 0 and rise**2 == 1
    moved_diagonally_once = run**2 == 1 and rise**2 == 1
    moved_hor_ver_once = moved_horizontally_once ^ move_vertically_once
    return moved_diagonally_once ^ moved hor_ver_once
