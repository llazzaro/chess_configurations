#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_chess_configurations
----------------------------------

Tests for `chess_configurations` module.
"""

from chess_configurations.solver import backtracking
from chess_configurations.models import Board, Piece


class TestSolverWithBoardCases(object):
    """
        Board test cases for the solver
    """

    def test_very_simple_1x1_board_with_one_piece(self):
        """
            A board with one position
        """
        board = Board(1, 1)
        pieces = [Piece('Q')]
        for solutions in backtracking(board, pieces, 0, 0):
            pass

    def test_a_board_were_only_one_piece_can_be_added(self):
        """
            In this case we will set a board of 2x2 with only queen.
            There is no way to add more than one piece.
        """
        pass
