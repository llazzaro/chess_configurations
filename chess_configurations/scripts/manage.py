#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import argparse

from chess_configurations.draw import draw_board
from chess_configurations.models import (
    King,
    Knight,
    Rook,
    Queen,
    Bishop,
    Board
)
from chess_configurations.solver import backtracking


def parse_args():
    # Create the arguments
    parser = argparse.ArgumentParser()

    parser.add_argument('-n', help='The value N of the board nxm', required=True)
    parser.add_argument('-m', help='The value M of the board nxm', required=True)
    parser.add_argument('-p', '--pieces', help='List of pieces to be used. Valid optiosn are: K,Q,B,N,R', required=True)
    parser.add_argument('-o', '--output', help='Output filename')
    parser.add_argument('-f', '--output_format', help='Output format. valid options are: text, json')
    parser.add_argument('-a', '--animation', help='It will print all solution, even the invalid ones. Usefull for debugging', action='store_true')

    return parser.parse_args()


def main():
    mapping = {'K': King, 'Q': Queen, 'R': Rook, 'B': Bishop, 'N': Knight}
    args = parse_args()
    board = Board(int(args.n), int(args.m))
    pieces = []
    for piece_type in args.pieces.split(','):
        pieces.append(mapping[piece_type]())

    res = set()
    start = time.time()
    for board in backtracking(board, pieces.copy(), pieces, res, args.animation):
        if args.output:
            with open(args.output, 'a') as output_file:
                if args.output_format == 'json':
                    output_file.write(board.to_json() + '\n')
                if args.output_format == 'text':
                    output_file.write(draw_board(board) + '\n')
        elif not args.animation:
            print(draw_board(board))
    end = time.time()
    print('Total unique configurations found {0}'.format(len(res)))
    print('Total time {0} seconds'.format(end - start))

if __name__ == '__main__':
    main()
