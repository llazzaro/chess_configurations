# -*- coding: utf-8 -*-
from collections import defaultdict



def backtracking(board, original_pieces, pieces, i, j, result):
    for current_i in range(0, board.n):
        for current_j in range(0, board.m):
            if not pieces:
                break
            if board.free(current_i, current_j):
                for piece in pieces:
                    pieces_positions = set(board.pieces_positions())
                    positions_to_take = piece.positions_to_take(board, current_i, current_j)
                    current_pieces_intersect_to_take = pieces_positions.intersection(positions_to_take)
                    # TODO: add cut with the number of free places
                    if not current_pieces_intersect_to_take:
                        board.put(piece, current_i, current_j)
                        next_pieces = pieces.copy()
                        next_pieces.remove(piece)
                        yield from backtracking(board, original_pieces, next_pieces, current_i, current_j, result)
                        # now we have to remove the same type of piece to avoid duplicate results
                        board.clean(current_i, current_j)

    if board.complete(original_pieces) and board not in result:
        result.add(board)
        yield board.copy()
