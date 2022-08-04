#!/bin/usr/python3

import movement as move
import unittest

class TestDistance(unittest.TestCase):
    def test_distance(self):
        self.assertEqual(move.distance_between((2,1),(4,1)), (2,0), 'Expected (2,0)')

class TestMovement(unittest.TestCase):
    def test_queen_to(self):
        self.assertEqual(move.queen_to((2,1),(4,1)), (4,1), 'Expected (4,1)')

unittest.main()
