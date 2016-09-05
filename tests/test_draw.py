#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chess_configurations.models import Board, King, Rook
from chess_configurations.draw import draw_board


def test_draw_an_empy_board():
    """ test draw method of an empty board """
    expected = "┌──────┐\n"
    expected += "│_ _ _ │\n"
    expected += "│_ _ _ │\n"
    expected += "│_ _ _ │\n"
    expected += "└──────┘\n\n"
    board = Board(3, 3)
    res = draw_board(board)
    assert res == expected


def test_draw_a_board_with_one_king():
    """
        test draw with one king.
        checks that the king is drawn in the correct pos
    """
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


def test_king_right_corner():
    """
        Checks that the king is drawn in the corner.
        Edge case test.
    """
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


def test_example_one():
    """
        Case used in one example.
    """
    expected = "┌──────┐\n"
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
