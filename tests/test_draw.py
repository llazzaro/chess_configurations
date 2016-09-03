#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_chess_configurations
----------------------------------

Tests for `chess_configurations` module.
"""
from pytest import raises

from chess_configurations.models import Board, King, Rook, Knight
from chess_configurations.draw import draw_board

class TestDraw:

    def test_draw_an_empy_board(self):
        expected =  "┌──────┐\n"
        expected += "│      │\n"
        expected += "│      │\n"
        expected += "│      │\n"
        expected += "└──────┘"
        board = Board(3, 3)
        res = draw_board(board)
        assert res == expected
