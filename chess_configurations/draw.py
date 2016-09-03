# -*- coding: utf-8 -*-


def draw_board(board):
    res = '┌'
    res += '─' * board.n * 2
    res += '┐\n'
    for i in range(0, board.n):
        res += '│'
        for j in range(0, board.m):
            if (i, j) in board.pieces:
                res += '{0} '.format(board.pieces[(i, j)])
            else:
                res += '_ '
        res += '│'
        res +='\n'

    res += '└'
    res += '─' * board.m * 2
    res += '┘'
    return res
