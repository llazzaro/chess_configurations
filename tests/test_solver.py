#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_chess_configurations
----------------------------------

Tests for `chess_configurations` module.
"""
from chess_configurations.solver import backtracking
from chess_configurations.models import Board, King, Rook


class TestSolverWithBoardCases(object):
    """
        Board test cases for the solver
    """

    def test_very_simple_1x1_board_with_one_piece(self):
        """
            A board with one position
        """
        board = Board(1, 1)
        pieces = []
        res = []
        for board in backtracking(board, pieces, 0, 0):
            print(board.pieces)
            res.append(board)

    def test_a_board_were_only_one_piece_can_be_added(self):
        """
            In this case we will set a board of 2x2 with only queen.
            There is no way to add more than one piece.
        """
        pass

    def test_example_test_case_given(self):
        """
            This test case was given as an example
        """
        import pdb
        board = Board(3, 3)
        pieces = [King(), King(), Rook()]
        res = []
        pdb.set_trace()
        for board in backtracking(board, pieces, 0, 0):
            res.append(board)

#         assert len(res) == 4
