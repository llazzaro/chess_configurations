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
        for board in backtracking(board, pieces, pieces, 0, 0, set()):
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
        pieces = [King(), King(), Rook()]
        board = Board(3, 3)
        res = []
        for board in backtracking(board, pieces.copy(), pieces, 0, 0, set()):
            res.append(board)
        assert len(res) == 4

        board_0 = res[0]
        assert board_0.pieces[(0, 0)].piece_identification == 'K'
        assert board_0.pieces[(0, 2)].piece_identification == 'K'
        assert board_0.pieces[(2, 1)].piece_identification == 'R'

        board_1 = res[1]
        assert board_1.pieces[(0, 0)].piece_identification == 'K'
        assert board_1.pieces[(2, 0)].piece_identification == 'K'
        assert board_1.pieces[(2, 1)].piece_identification == 'R'

        board_2 = res[2]
        assert board_2.pieces[(0, 0)].piece_identification == 'K'
        assert board_2.pieces[(0, 2)].piece_identification == 'K'
        assert board_2.pieces[(2, 1)].piece_identification == 'R'

        board_3 = res[3]
        assert board_3.pieces[(0, 0)].piece_identification == 'K'
        assert board_3.pieces[(0, 2)].piece_identification == 'K'
        assert board_3.pieces[(2, 1)].piece_identification == 'R'
