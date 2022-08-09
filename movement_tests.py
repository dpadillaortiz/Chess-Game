#!/bin/usr/python3

import movement as move
import unittest
import valid_moves as valid_move

class TestDistance(unittest.TestCase):
    def test_distance(self):
        self.assertEqual(move.distance_between((2,1),(4,1)), (2,0), 'Expected (2,0)')

class TestMovement(unittest.TestCase):
    def test_queen_to(self):
        initial_position = (4,4)
        coordinate_list = valid_move.generate_coordinates()
        valid_queen_moves_list = valid_move.valid_queen_moves(initial_position, coordinate_list)
        valid_queen_move = valid_queen_moves_list[4]
        move_queen_to = move.queen_to(initial_position, valid_queen_move)
        self.assertEqual(move_queen_to, valid_queen_move, f'Expected {valid_queen_move}')

    def test_king_to(self):
        initial_position = (4,4)
        coordinate_list = valid_move.generate_coordinates()
        valid_king_move_list = valid_move.valid_king_moves(initial_position, coordinate_list)
        for index, coordinate in enumerate(coordinate_list):
            print(index)
            with self.subTest(coordinate):
                valid_king_move = valid_king_move_list[index]
                move_king_to = move.king_to(initial_position, valid_king_move)
                self.assertEqual(move_king_to, valid_king_move, f'Expected {valid_king_move}')

unittest.main()
