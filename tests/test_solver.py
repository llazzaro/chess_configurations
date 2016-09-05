#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from chess_configurations.solver import backtracking
from chess_configurations.models import Board, King, Rook, Knight


class TestSolverWithBoardCases(object):
    """
        Board test cases for the solver
    """

    def test_very_simple_1x1_board_with_one_piece(self):
        """
            A board with one position available.
        """
        expected = [{'pieces': {'(0, 0)': 'K'}, 'n': 1, 'm': 1}]
        board = Board(1, 1)
        pieces = [King()]
        board.put(pieces[0], 0, 0)
        res = []
        for board in backtracking(board, pieces, pieces, set()):
            res.append(json.loads(board.to_json()))

        assert res == expected

    def test_example_test_case_given(self):
        """
            This test case was given as an example.
            The assert were done manually before the to_json method was done.
            To make checks easily see: test_with_data which uses a "fuzzer"
            case generator to verify results.
        """
        expected = [
                {'pieces': {'(2, 0)': 'K', '(1, 2)': 'R', '(0, 0)': 'K'}, 'm': 3, 'n': 3},
                {'pieces': {'(0, 2)': 'K', '(2, 1)': 'R', '(0, 0)': 'K'}, 'm': 3, 'n': 3},
                {'pieces': {'(0, 1)': 'R', '(2, 0)': 'K', '(2, 2)': 'K'}, 'm': 3, 'n': 3},
                {'pieces': {'(0, 2)': 'K', '(1, 0)': 'R', '(2, 2)': 'K'}, 'm': 3, 'n': 3}]
        pieces = [King(), King(), Rook()]
        board = Board(3, 3)
        res = []
        for board in backtracking(board, pieces.copy(), pieces, set()):
            res.append(json.loads(board.to_json()))
        assert len(expected) == len(res)
        for expected_res in expected:
            assert expected_res in res

    def test_example_2_test_case_given(self):
        expected = [
                {'pieces': {'(3, 3)': 'N', '(1, 1)': 'N', '(2, 2)': 'R', '(3, 1)': 'N', '(1, 3)': 'N', '(0, 0)': 'R'}, 'm': 4, 'n': 4},
                {'pieces': {'(2, 0)': 'N', '(0, 2)': 'N', '(3, 1)': 'R', '(1, 3)': 'R', '(0, 0)': 'N', '(2, 2)': 'N'}, 'm': 4, 'n': 4},
                {'pieces': {'(3, 3)': 'R', '(1, 1)': 'R', '(2, 0)': 'N', '(2, 2)': 'N', '(0, 0)': 'N', '(0, 2)': 'N'}, 'm': 4, 'n': 4},
                {'pieces': {'(0, 1)': 'R', '(2, 3)': 'R', '(1, 2)': 'N', '(1, 0)': 'N', '(3, 2)': 'N', '(3, 0)': 'N'}, 'm': 4, 'n': 4},
                {'pieces': {'(0, 1)': 'N', '(2, 1)': 'N', '(1, 2)': 'R', '(2, 3)': 'N', '(0, 3)': 'N', '(3, 0)': 'R'}, 'm': 4, 'n': 4},
                {'pieces': {'(0, 1)': 'N', '(2, 3)': 'N', '(2, 1)': 'N', '(1, 0)': 'R', '(3, 2)': 'R', '(0, 3)': 'N'}, 'm': 4, 'n': 4},
                {'pieces': {'(3, 3)': 'N', '(1, 1)': 'N', '(2, 0)': 'R', '(0, 2)': 'R', '(3, 1)': 'N', '(1, 3)': 'N'}, 'm': 4, 'n': 4},
                {'pieces': {'(2, 1)': 'R', '(1, 2)': 'N', '(1, 0)': 'N', '(3, 2)': 'N', '(0, 3)': 'R', '(3, 0)': 'N'}, 'm': 4, 'n': 4}]
        pieces = [Rook(), Rook(), Knight(), Knight(), Knight(), Knight()]
        board = Board(4, 4)
        res = []
        for board in backtracking(board, pieces.copy(), pieces, set()):
            res.append(json.loads(board.to_json()))

        assert len(expected) == len(res)
        for expected_res in expected:
            assert expected_res in res
