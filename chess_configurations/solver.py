# -*- coding: utf-8 -*-
from copy import copy


def backtracking(board, pieces, i, j):
    """
        TODO: complete this doc string
    """
    import pdb
    pdb.set_trace()
    for current_i in range(0, board.n):
        for current_j in range(0, board.m):
            print('Current position {0} {1}'.format(current_i, current_j))
            if board.free(current_i, current_j):
                new_board = copy(board)
                for piece in pieces:
                    will_take_another_piece = False
                    for position_to_take in piece.positions_used_from(board, current_i, current_j):
                        if not new_board.free(position_to_take[0], position_to_take[1]):
                            # adding the new piece will take another piece already in the board!.
                            will_take_another_piece = True
                            break
                    if not will_take_another_piece:
                        new_board.put(piece, current_i, current_j)
                        yield from backtracking(new_board, pieces[1:], current_i, current_j)
                        new_board.clean(current_i, current_j)

    if board.complete(pieces):
        # to be a valid solution the board must have all the pieces
        yield board
