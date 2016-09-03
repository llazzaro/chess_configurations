#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
import argparse
from random import choice, randint

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

TEST_DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')


def main():
    for case_nro in range(0, 20):
        n = randint(3, 7)
        m = randint(3, 7)
        mapping = {'K': King, 'Q': Queen, 'R': Rook, 'B': Bishop, 'N': Knight}
        board = Board(n, m)
        pieces = []
        number_of_pieces = randint(0, 6)
        for _ in range(0, number_of_pieces):
            pieces.append(mapping[choice([key for key in mapping.keys()])]())

        inputs = {'n': n, 'm': m, 'pieces': [piece.piece_identification for piece in pieces]}
        with open(os.path.join(TEST_DATA_PATH, 'params_{0}'.format(case_nro)), 'w') as input_params_file:
            input_params_file.write(json.dumps(inputs))

        with open(os.path.join(TEST_DATA_PATH, 'solution_{0}'.format(case_nro)), 'a') as output_file:
            for board in backtracking(board, pieces.copy(), pieces, 0, 0, set()):
                output_file.write(board.to_json() + '\n')


if __name__ == '__main__':
    main()
