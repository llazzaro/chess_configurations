#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import pytest

from chess_configurations.solver import backtracking

from . import load_test_case_input, load_test_case_solution

TEST_DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')


@pytest.mark.benchmark(warmup=True, warmup_iterations=10 ** 8, max_time=10)
def test_with_2_queens(benchmark):
    """ Instance of N-queens with n= 2 """
    parameter_filename = os.path.join(TEST_DATA_PATH, '2_queens.in')
    res = []
    board, pieces = load_test_case_input(parameter_filename)
    for board in benchmark(backtracking, board, pieces.copy(), pieces, set()):
        res.append(board)
    solution_filename = '2_queens_solution.out'
    solution_filename = os.path.join(TEST_DATA_PATH, solution_filename)
    expected = load_test_case_solution(solution_filename)

    assert set(expected) == set(res)


@pytest.mark.benchmark(warmup=True, warmup_iterations=10 ** 8, max_time=10)
def test_with_3_queens(benchmark):
    """ Instance of N-queens with n= 3 """
    parameter_filename = os.path.join(TEST_DATA_PATH, '3_queens.in')
    res = []
    board, pieces = load_test_case_input(parameter_filename)
    for board in benchmark(backtracking, board, pieces.copy(), pieces, set()):
        res.append(board)
    solution_filename = '3_queens_solution.out'
    solution_filename = os.path.join(TEST_DATA_PATH, solution_filename)
    expected = load_test_case_solution(solution_filename)

    assert set(expected) == set(res)


@pytest.mark.benchmark(warmup=True, warmup_iterations=10 ** 8, max_time=10)
def test_with_4_queens(benchmark):
    """ Instance of N-queens with n= 4 """
    parameter_filename = os.path.join(TEST_DATA_PATH, '4_queens.in')
    res = []
    board, pieces = load_test_case_input(parameter_filename)
    for board in benchmark(backtracking, board, pieces.copy(), pieces, set()):
        res.append(board)
    solution_filename = '4_queens_solution.out'
    solution_filename = os.path.join(TEST_DATA_PATH, solution_filename)
    expected = load_test_case_solution(solution_filename)

    assert set(expected) == set(res)
