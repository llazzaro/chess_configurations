# -*- coding: utf-8 -*-
import os
import sys
import time

from collections import defaultdict
from chess_configurations.models import Rook, Queen
from chess_configurations.draw import draw_board


def backtracking(board, original_pieces, pieces, result, animation=None):
    """
        I'm doing the recursion on the pieces parameter.
    """
    for current_i, current_j in board.free_positions():
        if not pieces:
            break
        for piece in set(pieces):
            positions_to_take = piece.positions_to_take(board, current_i, current_j)
            takes_other_piece = any([position in board.piece_positions() for position in positions_to_take])
            no_other_piece_takes_new_piece = not board.conflict(current_i, current_j)
            if not takes_other_piece and no_other_piece_takes_new_piece:
                board.put(piece, current_i, current_j)
                next_pieces = pieces.copy()
                next_pieces.remove(piece)
                yield from backtracking(board, original_pieces, next_pieces, result, animation)
                # now we have to remove the same type of piece to avoid duplicate results
                board.clean(current_i, current_j)

    if animation:
        print(draw_board(board))
        if board.complete(original_pieces) and board not in result:
            print('RESULT!')
        time.sleep(0.05)
        os.system('clear')
    if board.complete(original_pieces) and board not in result:
        result_board = board.copy()
        result.add(result_board)
        yield result_board
