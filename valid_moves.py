#!/bin/usr/python3

import movement as move

def generate_coordinates() -> tuple:
    range_of_eight = range(1,9)
    coordinates = [(x,y) for x in range_of_eight for y in range_of_eight]
    return coordinates

def valid_queen_moves(initial_position: tuple, coordinate_list: list) -> list:
    valid_moves = []
    for coordinate in coordinate_list:
        valid_move = move.queen_to(initial_position, coordinate)
        if valid_move == initial_position:
            continue
        if valid_move != None:
            valid_moves.append(valid_move)
    return valid_moves

def valid_king_moves(initial_position: tuple, coordinate_list: list) -> list:
    valid_moves = []
    for coordinate in coordinate_list:
        valid_move = move.king_to(initial_position, coordinate)
        if valid_move == initial_position:
            continue
        if valid_move != None:
            valid_moves.append(valid_move)
    return valid_moves



if __name__ == '__main__':
    coordinates = generate_coordinates()
    initial_position = (4,4)
    valid_moves_for = {'queen': valid_queen_moves(initial_position, coordinates),
            'king': valid_king_moves(initial_position, coordinates)
    }
    for piece in valid_moves_for:
        print(f'Valid moves for {piece}:\n'+str(valid_moves_for[piece])+'\n')
