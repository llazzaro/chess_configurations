# -*- coding: utf-8 -*-


def draw_board(board):
    """
        Given a board it returns a string with the text representation.
        This is used to print results in console.
    """
    res = '┌'
    res = res + '─' * board.n * 2
    res = res + '┐\n'
    for i in range(0, board.n):
        res = res + '│'
        for j in range(0, board.m):
            if (i, j) in board.pieces:
                res = res + '{0} '.format(board.pieces[(i, j)])
            else:
                res = res +'_ '
        res = res + '│'
        res = res + '\n'

    res = res + '└'
    res = res + '─' * board.m * 2
    res = res + '┘\n\n'
    return res
