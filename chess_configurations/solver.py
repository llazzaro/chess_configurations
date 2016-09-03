# -*- coding: utf-8 -*-
from collections import defaultdict


def backtracking(board, original_pieces, pieces, i, j, result):
    for current_i in range(0, board.n):
        for current_j in range(0, board.m):
            if not pieces:
                break
            if board.free(current_i, current_j):
                for piece in pieces:
                    new_piece_will_take_other = False
                    for piece_position_in_board in set(board.pieces_positions()):
                        if piece.occupy_function(board, current_i, current_j, piece_position_in_board[0], piece_position_in_board[1]):
                            new_piece_will_take_other = True
                    # TODO: add cut with the number of free places
                    if not new_piece_will_take_other:
                        board.put(piece, current_i, current_j)
                        next_pieces = pieces.copy()
                        next_pieces.remove(piece)
                        yield from backtracking(board, original_pieces, next_pieces, current_i, current_j, result)
                        # now we have to remove the same type of piece to avoid duplicate results
                        board.clean(current_i, current_j)

    if board.complete(original_pieces) and board not in result:
        result.add(board)
        yield board.copy()
