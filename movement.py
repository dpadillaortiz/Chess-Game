#! /bin/usr/python3

import chess_tools

def pawn_to(from_position: tuple, to_position: tuple) -> tuple:
    if chess_tools.moved_pawn(from_position, to_position): 
        return to_position
    
def rook_to(from_position: tuple, to_position: tuple) -> tuple:
    if chess_tools.moved_rook(from_position, to_position):
        return to_position 
        
def knight_to(from_position: tuple, to_position: tuple) -> tuple:
    if chess_tools.moved_knight(from_position, to_position):
        return to_position

def bishop_to(from_position: tuple, to_position: tuple) -> tuple:
    if chess_tools.moved_bishop(from_position, to_position):
        return to_position

def king_to(from_position: tuple, to_position: tuple) -> tuple:
    if chess_tools.moved_king(from_position, to_position):
        return to_position

def queen_to(from_position: tuple, to_position: tuple) -> tuple:
    if chess_tools.moved_queen(from_position, to_position):
        return to_position

if __name__ == '__main__':
    x = chess_tools.moved_rook((2,1),(4,1))
    y = chess_tools.moved_bishop((2,1),(4,1))
    print(x)      
    print(y) 
    print(queen_to((2,1),(4,1)))
