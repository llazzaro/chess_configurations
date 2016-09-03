#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from pytest import raises

from chess_configurations.models import Board, King, Rook, Knight


class TestBoard:

    def test_equal_with_the_same_pieces_at_same_positions(self):
        king = King()
        board = Board(3, 3)
        board.put(king, 0, 0)
        another_board = Board(3, 3)
        another_board.put(king, 0, 0)
        assert another_board == board
        assert another_board == board
        assert hash(another_board) == hash(board)

    def test_equal_with_the_same_pieces_at_same_positions_added_in_different_order(self):
        king = King()
        king_2 = King()
        board = Board(3, 3)
        board.put(king, 0, 0)
        board.put(king_2, 2, 2)
        another_board = Board(3, 3)
        another_board.put(king_2, 2, 2)
        another_board.put(king, 0, 0)
        assert another_board == board
        assert hash(another_board) == hash(board)

    def test_copy_method_copies_every_piece_and_dimension_are_correct(self):
        king = King()
        king_2 = King()
        board = Board(3, 3)
        board.put(king, 0, 0)
        board.put(king_2, 2, 2)

        another_board = board.copy()

        assert another_board == board
        assert set(another_board.pieces.keys()) == set(board.pieces.keys())
        assert set(another_board.pieces.values()) == set(board.pieces.values())
        assert another_board.n == another_board.n
        assert another_board.m == another_board.m

    def test_clean_when_there_is_a_piece_in_the_position(self):
        king = King()
        board = Board(3, 3)
        board.put(king, 0, 0)
        board.clean(0, 0)
        assert board.pieces == {}

    def test_clean_when_in_an_empty_position(self):
        board = Board(3, 3)
        with raises(AssertionError):
            board.clean(0, 0)

    def test_free_with_empty_board(self):
        board = Board(3, 3)
        for i in range(0, 3):
            for j in range(0, 3):
                assert board.free(i, j)

    def test_free_outside_the_board_raises_exception(self):
        board = Board(3, 3)
        with raises(AssertionError):
            board.free(100, 1)
        with raises(AssertionError):
            board.free(1, 100)

    def test_free_with_a_king_in_the_board_happy_path(self):
        king = King()
        board = Board(3, 3)
        board.put(king, 0, 0)
        assert board.free(0, 0) is False
        assert board.free(0, 1) is False
        assert board.free(2, 2) is True

    def test_complete_with_empty_board(self):
        board = Board(3, 3)
        assert board.complete([])

    def test_complete_returns_false_when_pieces_are_missing(self):
        board = Board(3, 3)
        assert board.complete([King()]) is False

    def test_complete_returns_true_when_all_pieces_are_in_the_board(self):

        king = King()
        board = Board(3, 3)
        board.put(king, 0, 0)

        assert board.complete([King()]) is True

    def test_pieces_positions_check(self):
        king = King()
        board = Board(3, 3)
        board.put(king, 1, 1)

        assert [position for position in board.pieces_positions()] == [(1, 1)]

    def test_to_json_with_a_board_with_two_pieces(self):
        king = King()
        rook = Rook()
        board = Board(3, 4)
        board.put(king, 1, 1)
        board.put(rook, 2, 2)
        res = json.loads(board.to_json())
        expected = json.loads('{"m": 4, "pieces": {"(2, 2)": "R", "(1, 1)": "K"}, "n": 3}')
        assert res == expected

    def test_from_json_with_a_board_with_two_pieces(self):
        king = King()
        rook = Rook()
        expected_board = Board(3, 4)
        expected_board.put(king, 1, 1)
        expected_board.put(rook, 2, 2)
        res = Board.from_json('{"m": 4, "pieces": {"(2, 2)": "R", "(1, 1)": "K"}, "n": 3}')
        assert res == expected_board


class TestKing:

    def test_of_a_bug_it_was_possible_to_put_a_king_that_takes_a_rook(self):
        king = King()
        board = Board(3, 3)
        board.put(king, 0, 0)
        positions_to_take = king.positions_to_take(board, 0, 0)
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


class TestKnight:

    def test_occupy_functions(self):
        knight = Knight()
        small_board = Board(5, 5)
        small_board.put(knight, 2, 2)
        valid_positions = [
            (0, 1),
            (1, 0),
            (0, 3),
            (2, 2),
            (1, 4),
            (3, 0),
            (4, 1),
            (3, 4),
            (4, 3),
        ]
        for i in range(0, 5):
            for j in range(0, 5):
                if (i, j) in valid_positions:
                    assert knight.occupy_function(small_board, 2, 2, i, j) is True
                else:
                    assert knight.occupy_function(small_board, 2, 2, i, j) is False

    def test_taken_position_generator(self):
        knight = Knight()
        small_board = Board(5, 5)
        small_board.put(knight, 2, 2)
        valid_positions = [
            (0, 1),
            (1, 0),
            (0, 3),
            (2, 2),
            (1, 4),
            (3, 0),
            (4, 1),
            (3, 4),
            (4, 3),
        ]
        assert set(list(knight.positions_to_take(small_board, 2, 2))) == set(valid_positions)


class TestBishop:

    def test_(self):
        pass


class TestQueen:

    def test_(self):
        pass
