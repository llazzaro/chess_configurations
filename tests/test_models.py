#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_chess_configurations
----------------------------------

Tests for `chess_configurations` module.
"""
from chess_configurations.models import Board, King, Rook


class TestPieces(object):

    def test_king_occupy_function_happy_cases(self):
        """
            The King can move anywhere but only by one step.
            This test asserts that the function returns True for all valid cases
        """

        king_piece = King()
        small_board = Board(3, 3)
        small_board.put(king_piece, 1, 1)
        assert king_piece.occupy_function(small_board, 0, 0)
        assert king_piece.occupy_function(small_board, 0, 1)
        assert king_piece.occupy_function(small_board, 0, 2)
        assert king_piece.occupy_function(small_board, 1, 0)
        assert king_piece.occupy_function(small_board, 1, 1)
        assert king_piece.occupy_function(small_board, 1, 2)
        assert king_piece.occupy_function(small_board, 2, 0)
        assert king_piece.occupy_function(small_board, 2, 0)
        assert king_piece.occupy_function(small_board, 2, 1)
        assert king_piece.occupy_function(small_board, 2, 2)

    def test_king_cant_move_more_than_one_step(self):
        king_piece = King()
        small_board = Board(3, 3)
        small_board.put(king_piece, 0, 0)
        assert king_piece.occupy_function(small_board, 2, 2) is False
        assert king_piece.occupy_function(small_board, 0, 2) is False

    def test_rook_valid_moves(self):
        rook_piece = Rook()
        small_board = Board(3, 3)
        small_board.put(rook_piece, 0, 0)
        assert rook_piece.occupy_function(small_board, 0, 0)
        assert rook_piece.occupy_function(small_board, 0, 1)
        assert rook_piece.occupy_function(small_board, 0, 2)
        assert rook_piece.occupy_function(small_board, 1, 0)
        assert rook_piece.occupy_function(small_board, 2, 0)

    def test_rook_cant_move_can_move_in_diagonal_direction(self):
        rook_piece = Rook()
        small_board = Board(3, 3)
        small_board.put(rook_piece, 0, 0)
        assert rook_piece.occupy_function(small_board, 1, 1) is False
        assert rook_piece.occupy_function(small_board, 2, 2) is False
        # just in case
        assert rook_piece.occupy_function(small_board, 1, 2) is False
