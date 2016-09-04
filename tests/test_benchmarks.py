#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
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

from . import load_test_case_input, load_test_case_solution

TEST_DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')


class TestCasesToBenchmark:

    @pytest.mark.benchmark(warmup=True, warmup_iterations=10 ** 8, max_time=10)
    def test_with_past_execution_information(self, benchmark):
        parameter_filename = os.path.join(TEST_DATA_PATH, '4_queens.in')
        res = []
        board, pieces = load_test_case_input(parameter_filename)
        for board in benchmark(backtracking, board, pieces.copy(), pieces, 0, 0, set()):
            res.append(board)
        solution_filename = '4_queens_solution.out'
        solution_filename = os.path.join(TEST_DATA_PATH, solution_filename)
        expected = load_test_case_solution(solution_filename)

        assert set(expected) == set(res)
