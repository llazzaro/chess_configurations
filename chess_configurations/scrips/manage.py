#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

    parser.add_argument('-n', help='The value N of the board nxm')
    parser.add_argument('-m', help='The value M of the board nxm')
    parser.add_argument('-p', '--pieces', help='List of pieces to be used. Valid optiosn are: K,Q,B,N,R')
    parser.add_argument('-o', '--output', help='Output filename')
    parser.add_argument('-f', '--output_format', help='Output format. valid options are: text, json')

    return parser.parse_args()

def main():
    mapping = {'K': King, 'Q': Queen, 'R': Rook, 'B': Bishop, 'N': Knight}
    args = parse_args()
    board = Board(int(args.n), int(args.m))
    pieces = []
    for piece_type in args.pieces.split(','):
        pieces.append(mapping[piece_type]())

    for board in backtracking(board, pieces.copy(), pieces, 0, 0, set()):
        if args.output:
            with open(args.output, 'w') as output_file:
                if args.output_format == 'json':
                    output_file.write(board.to_json())
                if args.output_format == 'text':
                    output_file.write(draw_board(board))
        else:
            print(draw_board(board))




if __name__ == '__main__':
    main()
