#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
from glob import iglob

import pytest

from chess_configurations.solver import backtracking
from chess_configurations.models import (
    Board,
    Bishop,
    King,
    Rook,
    Knight,
    Queen
)

TEST_DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')


class TestSavedExecutions(object):

    def test_with_past_execution_information(self):
        mapping = {'K': King, 'Q': Queen, 'R': Rook, 'B': Bishop, 'N': Knight}
        for parameter_filename in iglob(os.path.join(TEST_DATA_PATH, 'params_*')):
            case_nro = parameter_filename.split('/')[-1].split('_')[1]
            with open(parameter_filename, 'r') as parameter_file:
                input_parameters = json.loads(parameter_file.read())
                board = Board(int(input_parameters['n']), int(input_parameters['m']))
                pieces = []
                for piece_type in input_parameters['pieces']:
                    pieces.append(mapping[piece_type]())
                res = []
                for board in backtracking(board, pieces.copy(), pieces, 0, 0, set()):
                    res.append(board)

            solution_filename = 'solution_{0}'.format(case_nro)
            expected = []
            with open(os.path.join(TEST_DATA_PATH, solution_filename), 'r') as solution_file:
                for solution in solution_file:
                    expected.append(Board.from_json(solution))

            assert set(expected) == set(res)
