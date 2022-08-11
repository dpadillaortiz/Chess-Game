#!/bin/usr/python3

import movement as move
import unittest
import valid_moves as valid_move


class TestDistance(unittest.TestCase):
    def test_distance(self):
        self.assertEqual(move.distance_between((2,1),(4,1)), (2,0), 'Expected (2,0)')

class TestMovement(unittest.TestCase):
    initial_position = (4,4)
    coordinate_list = valid_move.generate_coordinates()

    def test_queen_to(self):
        valid_queen_move_list = valid_move.valid_queen_moves(self.initial_position, self.coordinate_list)
        for valid_queen_move in valid_queen_move_list:
            with self.subTest(valid_queen_move):
                move_queen_to = move.queen_to(self.initial_position, valid_queen_move)
                self.assertEqual(move_queen_to, valid_queen_move, f'Expected {valid_queen_move}')

    def test_king_to(self):
        valid_king_move_list = valid_move.valid_king_moves(self.initial_position, self.coordinate_list)
        for valid_king_move in valid_king_move_list:
            with self.subTest(valid_king_move):
                move_king_to = move.king_to(self.initial_position, valid_king_move)
                self.assertEqual(move_king_to, valid_king_move, f'Expected {valid_king_move}')

    def test_bishop_to(self):
        valid_bishop_move_list = valid_move.valid_bishop_moves(self.initial_position, self.coordinate_list)
        for valid_bishop_move in valid_bishop_move_list:
            with self.subTest(valid_bishop_move):
                move_bishop_to = move.bishop_to(self.initial_position, valid_bishop_move)
                self.assertEqual(move_bishop_to, valid_bishop_move, f'Expected {valid_bishop_move}')

    def test_knight_to(self):
        valid_knight_move_list = valid_move.valid_knight_moves(self.initial_position, self.coordinate_list)
        for valid_knight_move in valid_knight_move_list:
            with self.subTest(valid_knight_move):
                move_knight_to = move.knight_to(self.initial_position, valid_knight_move)
                self.assertEqual(move_knight_to, valid_knight_move, f'Expected {valid_knight_move}')

    def test_rook_to(self):
        valid_rook_move_list = valid_move.valid_rook_moves(self.initial_position, self.coordinate_list)
        for valid_rook_move in valid_rook_move_list:
            with self.subTest(valid_rook_move):
                move_rook_to = move.rook_to(self.initial_position, valid_rook_move)
                self.assertEqual(move_rook_to, valid_rook_move, f'Expected {valid_rook_move}')

    def test_pawn_to(self):
        valid_pawn_move_list = valid_move.valid_pawn_moves(self.initial_position, self.coordinate_list)
        for valid_pawn_move in valid_pawn_move_list:
            with self.subTest(valid_pawn_move):
                move_pawn_to = move.pawn_to(self.initial_position, valid_pawn_move)
                self.assertEqual(move_pawn_to, valid_pawn_move, f'Expected {valid_pawn_move}')

if __name__ == '__main__':
    unittest.main()
