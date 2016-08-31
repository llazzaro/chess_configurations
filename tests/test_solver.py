#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_chess_configurations
----------------------------------

Tests for `chess_configurations` module.
"""

import pytest

from contextlib import contextmanager
from click.testing import CliRunner

from chess_configurations.solver import backtracking


class TestSolverWithBoardCases(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_very_simple_1x1_board_with_one_piece(self):
        board = Board(1, 1)
        pieces = [Piece('Q')]
        for solutions in backtracking(board, pieces, 0, 0):
            pass
