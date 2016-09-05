# -*- coding: utf-8 -*-
import os
import sys
import time

from collections import defaultdict

from chess_configurations.draw import draw_board


def backtracking(board, original_pieces, pieces, i, j, result, animation=None):
    """
        I'm doing the recursion on the pieces parameter.
    """
    for current_i, current_j in board.free_positions():
        for piece in set(pieces):
            positions_to_take = piece.positions_to_take(board, current_i, current_j)
            takes_other_piece = any([position in board.piece_positions() for position in positions_to_take])
            none_takes_new_piece = True
            for position, board_piece in board.pieces.items():
                if board_piece.takes(board, position[0], position[1], current_i, current_j):
                    none_takes_new_piece = False
                    break
            if not takes_other_piece and none_takes_new_piece:
                board.put(piece, current_i, current_j)
                next_pieces = pieces.copy()
                next_pieces.remove(piece)
                yield from backtracking(board, original_pieces, next_pieces, current_i, current_j, result, animation)
                # now we have to remove the same type of piece to avoid duplicate results
                board.clean(current_i, current_j)

    if animation:
        print(draw_board(board))
        if board.complete(original_pieces) and board not in result:
            print('RESULT!')
        time.sleep(0.05)
        os.system('clear')
    if board.complete(original_pieces) and board not in result:
        result.add(board)
        yield board.copy()
