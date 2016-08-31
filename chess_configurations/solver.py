# -*- coding: utf-8 -*-


def backtracking(board, pieces, i, j):
    if not board.valid:
        return
    if current_i == board.n + 1 and current_j == board.m + 1:
        # we arrived to the end of the board. print current solution
        yield board

    for current_i in range(i, board.n):
        for current_j in range(j, board.m):
            for piece in pieces:
                board.put(piece, current_i, current_j)
                backtrack(board, pieces, current_i + 1, current_j)
                board.clean(current_i, current_j)
