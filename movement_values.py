#!/bin/usr/python3

import movement as move

eight = range(1,9)
cordinates = [(x,y) for x in eight for y in eight]

with open('valid_moves.txt', 'w') as f:
    f.write('Valid moves for queen\n')
    initial_position = (4,4)
    valid_moves_counter = 0
    for cordinate in cordinates:
        valid_move = move.queen_to(initial_position, cordinate)
        if valid_move != None:
            initial_pos = str(initial_position) 
            final_pos = str(cordinate)
            to_write = f'({initial_pos}, {final_pos}), {final_pos}, "Expected final_pos: {final_pos}"\n'
            valid_moves_counter += 1
            f.write(to_write)
    f.write(f'Number of valid moves: {valid_moves_counter}\n')

