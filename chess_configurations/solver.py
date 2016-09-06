# -*- coding: utf-8 -*-
import os
import time

from chess_configurations.draw import draw_board


def backtracking(board, original_pieces, pieces, result, animation=None):
    """
        I'm doing the recursion on the pieces parameter.
    """
    free_positions = board.free_positions()
    while free_positions:
        current_pos = free_positions.pop()
        current_i, current_j = current_pos[0], current_pos[1]
        if not pieces:
            break
        # to avoid duplicates checks on solution a removed the with the set
        for piece in set(pieces):
            positions_to_take = piece.positions_to_take(board, current_i, current_j)
            positions_taken = [position in board.piece_positions() for position in positions_to_take]
            takes_other_piece = any(positions_taken)
            no_other_piece_takes_new_piece = not board.conflict(current_i, current_j)
            position_free = (current_i, current_j) in board.free_positions()
            if not position_free:
                break
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
