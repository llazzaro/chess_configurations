#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_chess_configurations
----------------------------------

Tests for `chess_configurations` module.
"""
from chess_configurations.models import Board, King, Rook

class TestBoard:

    def test_equal_with_the_same_pieces_at_same_positions(self):
        king = King()
        board = Board(3,3)
        board.put(king, 0, 0)
        another_board = Board(3, 3)
        another_board.put(king, 0, 0)
        assert another_board == board

    def test_equal_with_the_same_pieces_at_same_positions(self):
        king = King()
        board = Board(3,3)
        board.put(king, 0, 0)
        board.put(king, 2, 2)
        another_board = Board(3, 3)
        another_board.put(king, 2, 2)
        another_board.put(king, 0, 0)
        assert another_board == board

    def test_piece_position_with_multiple_kings(self):
        king = King()
        king_2 = King()
        board = Board(3,3)
        board.put(king, 0, 0)
        board.put(king_2, 0, 2)
        assert board.position(king) != board.position(king_2)


class TestKing:

    def test_of_a_bug_it_was_possible_to_put_a_king_that_takes_a_rook(self):
        king = King()
        positions_to_take = king.positions_to_take(board, current_i, current_j)
        assert (0, 1) in positions_to_take

    def test_pieces_of_the_same_type_are_indistingueable(self):
        king = King()
        king_2 = King()
        assert king == king_2

    def test_pieces_of_different_type_are_distingueable(self):
        king = King()
        rook = Rook()
        assert king != rook

    def test_positions_used_from_for_king_in_the_upper_corner_are_valid(self):
        king_piece = King()
        small_board = Board(3, 3)
        assert (0, 0) in king_piece.positions_to_take(small_board, 0, 0)
        assert (1, 0) in king_piece.positions_to_take(small_board, 0, 0)
        assert (1, 1) in king_piece.positions_to_take(small_board, 0, 0)
        assert (0, 1) in king_piece.positions_to_take(small_board, 0, 0)
        assert (0, 2) not in king_piece.positions_to_take(small_board, 0, 0)

    def test_king_occupy_function_happy_cases(self):
        """
            The King can move anywhere but only by one step.
            This test asserts that the function returns True for all valid cases
        """

        king_piece = King()
        small_board = Board(3, 3)
        small_board.put(king_piece, 1, 1)
        assert king_piece.occupy_function(small_board, 1, 1, 0, 0)
        assert king_piece.occupy_function(small_board, 1, 1, 0, 1)
        assert king_piece.occupy_function(small_board, 1, 1, 0, 2)
        assert king_piece.occupy_function(small_board, 1, 1, 1, 0)
        assert king_piece.occupy_function(small_board, 1, 1, 1, 1)
        assert king_piece.occupy_function(small_board, 1, 1, 1, 2)
        assert king_piece.occupy_function(small_board, 1, 1, 2, 0)
        assert king_piece.occupy_function(small_board, 1, 1, 2, 0)
        assert king_piece.occupy_function(small_board, 1, 1, 2, 1)
        assert king_piece.occupy_function(small_board, 1, 1, 2, 2)

    def test_king_cant_move_more_than_one_step(self):
        king_piece = King()
        small_board = Board(3, 3)
        small_board.put(king_piece, 0, 0)
        assert king_piece.occupy_function(small_board, 0, 0, 2, 2) is False
        assert king_piece.occupy_function(small_board, 0, 0, 0, 2) is False


class TestRook:

    def test_rook_valid_moves(self):
        rook_piece = Rook()
        small_board = Board(3, 3)
        small_board.put(rook_piece, 0, 0)
        assert rook_piece.occupy_function(small_board, 0, 0, 0, 0)
        assert rook_piece.occupy_function(small_board, 0, 0, 0, 1)
        assert rook_piece.occupy_function(small_board, 0, 0, 0, 2)
        assert rook_piece.occupy_function(small_board, 0, 0, 1, 0)
        assert rook_piece.occupy_function(small_board, 0, 0, 2, 0)

    def test_rook_cant_move_can_move_in_diagonal_direction(self):
        rook_piece = Rook()
        small_board = Board(3, 3)
        small_board.put(rook_piece, 1, 2)
        assert rook_piece.occupy_function(small_board, 0, 0, 1, 1) is False
        assert rook_piece.occupy_function(small_board, 0, 0, 2, 2) is False
        # just in case
        assert rook_piece.occupy_function(small_board, 0, 0, 1, 2) is False
