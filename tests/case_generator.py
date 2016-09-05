#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
from random import choice, randint

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
    """
        Generates test cases data used in tests.
    """
    for case_nro in range(0, 20):
        dimension_n = randint(3, 5)
        dimension_m = randint(3, 5)
        mapping = {'K': King, 'Q': Queen, 'R': Rook, 'B': Bishop, 'N': Knight}
        board = Board(dimension_n, dimension_m)
        pieces = []
        number_of_pieces = randint(0, 6)
        for _ in range(0, number_of_pieces):
            pieces.append(mapping[choice([key for key in mapping.keys()])]())

        inputs = {
            'n': dimension_n,
            'm': dimension_m,
            'pieces': [piece.piece_identification for piece in pieces]}
        print('Generate case with {0}'.format(inputs))
        input_filename = os.path.join(TEST_DATA_PATH, 'params_{0}'.format(case_nro))
        with open(input_filename, 'w') as input_params_file:
            input_params_file.write(json.dumps(inputs))
        solution_filename = os.path.join(TEST_DATA_PATH, 'solution_{0}'.format(case_nro))
        with open(solution_filename, 'a') as output_file:
            for board in backtracking(board, pieces.copy(), pieces, set()):
                output_file.write(board.to_json() + '\n')


if __name__ == '__main__':
    main()
