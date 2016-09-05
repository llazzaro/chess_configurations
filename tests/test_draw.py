#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chess_configurations.models import Board, King, Rook
from chess_configurations.draw import draw_board


class TestDraw:

    def test_draw_an_empy_board(self):
        expected = "┌──────┐\n"
        expected += "│_ _ _ │\n"
        expected += "│_ _ _ │\n"
        expected += "│_ _ _ │\n"
        expected += "└──────┘\n\n"
        board = Board(3, 3)
        res = draw_board(board)
        assert res == expected

    def test_draw_a_board_with_one_king(self):
        expected = "┌──────┐\n"
        expected += "│K _ _ │\n"
        expected += "│_ _ _ │\n"
        expected += "│_ _ _ │\n"
        expected += "└──────┘\n\n"
        board = Board(3, 3)
        king = King()
        board.put(king, 0, 0)
        res = draw_board(board)
        assert res == expected

    def test_draw_a_board_with_one_king_right_corner(self):
        expected = "┌──────┐\n"
        expected += "│_ _ _ │\n"
        expected += "│_ _ _ │\n"
        expected += "│_ _ K │\n"
        expected += "└──────┘\n\n"
        board = Board(3, 3)
        king = King()
        board.put(king, 2, 2)
        res = draw_board(board)
        assert res == expected

    def test_draw_a_board_with_example_one(self):
        expected =  "┌──────┐\n"
        expected += "│K _ K │\n"
        expected += "│_ _ _ │\n"
        expected += "│_ R _ │\n"
        expected += "└──────┘\n\n"
        board = Board(3, 3)
        king = King()
        rook = Rook()
        board.put(king, 0, 0)
        board.put(king, 0, 2)
        board.put(rook, 2, 1)
        res = draw_board(board)
        assert res == expected
