#! /bin/usr/python3

def generate_coordinates() -> list:
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

def vertical_movement(initial_position: tuple, final_position: tuple) -> bool:
    '''Vertical movement is checked by verifing there was no horizontal movement
    i.e. run in distance_between is 0'''
    run, rise = distance_between(from_position, to_position)
    return run**2 == 0

def horizontal_movement(initial_position: tuple, final_position: tuple) -> bool:
    '''Horizontal movement is checked by verifing there was no vertical movement
    i.e. rise in distance_between is 0'''
    run, rise = distance_between(from_position, to_position)
    return rise**2 == 0

def diagonal_movement(initial_position: tuple, final_position: tuple) -> bool:
    '''Diagonal movement is checked by verifing that horizontal and vertical movement are the same
    i.e. rise and run in distance_between are equal'''
    run, rise = distance_between(from_position, to_position)
    return rise**2 == rise**2

def moved_pawn(initial_position: tuple, final_position: tuple) -> bool:
    '''Pawn movement is checked by verifing there was no horizontal movement and it moved vertically once
    i.e. run and rise in distance_between are 0 and 1 respectively
    Note: Pawns can move vertically twice but only in the first turn. I included the logic but the function will not return True if a pawn moved twice.'''
    run, rise = distance_between(from_position, to_position)
    moved_vertically_once = run**2 == 0 and rise**2 == 1
    moved_vertically_twice = run**2 == 0 and rise**2 == 2
    return moved_vertically_once

def moved_knight(initial_position: tuple, final_position: tuple) -> bool:
    '''Knight movement is checked by verifing that it moved in an L 
    - mathematically speaking, run^2 + rise^2 is equal to 5
    i.e. moved vertically twice and moved horizontally once or
    moved horizontally twice and moved vertically once'''
    run, rise = distance_between(from_position, to_position)
    moved_knight = run**2 + rise**2 == 5
    return moved_knight

def moved_king(initial_position: tuple, final_position: tuple) -> bool:
    '''King movement is checked by verifing that it moved once horizontally, vertically, or diagonally
    i.e. run or rise (but not both) is equal to one, or run and rise are both equal to 1'''
    run, rise = distance_between(from_position, to_position)
    moved_diagonally_once = run**2 + rise**2 == 2
    moved_hor_ver_once = run**2 + rise**2 == 1
    return moved_diagonally_once ^ moved hor_ver_once

def moved_rook() -> bool:
    '''Checks whether a rook moved horizontally or vertically'''
    return horizontal_movement ^ vertical_movement

def moved_bishop() -> bool:
    '''Checks whether a bishop moved diagonally'''
    return diagonal_movement
    
def moved_queen() -> bool:
    '''Check whether a queen moved horizontally, vertically, or diagonally using the moved_rook and moved_bishop funcitons'''
    return moved_bishop() ^ moved_rook()
