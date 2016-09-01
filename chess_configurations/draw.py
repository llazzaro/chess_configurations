# -*- coding: utf-8 -*-


def draw_board(board):
    res = '_' * board.m
    for i in range(0, board.n):
        for j in range(0, board.m):
            if (i, j) in board.pieces:
                res += '{0}|'.format(board.pieces[(i, j)])
        res +='\n'
