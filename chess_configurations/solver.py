# -*- coding: utf-8 -*-
from copy import copy


def backtracking(board, original_pieces, pieces, i, j):
    """
        TODO: complete this doc string
    """
    for current_i in range(0, board.n):
        for current_j in range(0, board.m):
            if not pieces:
                # cut to avoid iterate over all range
                break
            print('Current position {0} {1}'.format(current_i, current_j))
            if board.free(current_i, current_j):
                new_board = copy(board)
                for piece in pieces:
                    pieces_positions = set(new_board.pieces_positions())
                    positions_to_take = piece.positions_to_take(board, current_i, current_j)
                    current_pieces_intersect_to_take = pieces_positions.intersection(positions_to_take)
                    if not current_pieces_intersect_to_take:
                        new_board.put(piece, current_i, current_j)
                        yield from backtracking(new_board, original_pieces, pieces[1:], current_i, current_j)
                        new_board.clean(current_i, current_j)

    if board.complete(original_pieces):
        # to be a valid solution the board must have all the pieces
        yield board
