#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from pytest import raises

from chess_configurations.models import (
    Board,
    Piece,
    King,
    Rook,
    Knight,
    Bishop,
    Queen
)


def verify_piece_movement(piece, board, valid_positions, current_pos_i, current_pos_j):
    for i in range(0, board.n):
        for j in range(0, board.m):
            if (i, j) in valid_positions:
                assert piece.takes(board, current_pos_i, current_pos_j, i, j) is True
            else:
                assert piece.takes(board, current_pos_i, current_pos_j, i, j) is False


class TestBoard:

    def test_equal_on_different_board(self):
        king = King()
        board = Board(3, 3)
        board.put(king, 0, 0)

        another_board = Board(3, 3)
        another_board.put(king, 2, 2)

        assert another_board != board
        assert hash(another_board) != hash(board)

    def test_equals_on_different_board_different_piece_in_same_position(self):
        king = King()
        bishop = Bishop()
        board = Board(3, 3)
        board.put(king, 0, 0)

        another_board = Board(3, 3)
        another_board.put(bishop, 0, 0)

        assert another_board != board
        assert hash(another_board) != hash(board)

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
                assert (i, j) in board.free_positions()

    def test_free_with_a_king_in_the_board_happy_path(self):
        king = King()
        board = Board(3, 3)
        board.put(king, 0, 0)
        assert (0, 0) not in board.free_positions()
        assert (0, 1) not in board.free_positions()
        assert (2, 2) in board.free_positions()

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

        assert [position for position in board.piece_positions()] == [(1, 1)]

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

class TestPiece:

    def test_equals_against_other_object(self):
        piece = Piece()
        assert piece != 1

class TestKing:

    def test_of_a_bug_it_was_possible_to_put_a_king_that_takes_a_rook(self):
        king = King()
        board = Board(3, 3)
        board.put(king, 0, 0)
        positions_to_take = king.positions_to_take(board, 0, 0)
        assert (0, 1) in positions_to_take

    def test_positions_used_from_for_king_in_the_upper_corner_are_valid(self):
        king_piece = King()
        small_board = Board(3, 3)
        assert (0, 0) in king_piece.positions_to_take(small_board, 0, 0)
        assert (1, 0) in king_piece.positions_to_take(small_board, 0, 0)
        assert (1, 1) in king_piece.positions_to_take(small_board, 0, 0)
        assert (0, 1) in king_piece.positions_to_take(small_board, 0, 0)
        assert (0, 2) not in king_piece.positions_to_take(small_board, 0, 0)

    def test_pieces_of_the_same_type_are_indistingueable(self):
        king = King()
        king_2 = King()
        assert king == king_2

    def test_pieces_of_different_type_are_distingueable(self):
        king = King()
        rook = Rook()
        assert king != rook

    def test_king_takes_happy_cases(self):
        """
            The King can move anywhere but only by one step.
            This test asserts that the function returns True for all valid cases
        """

        king_piece = King()
        small_board = Board(3, 3)
        small_board.put(king_piece, 1, 1)
        assert king_piece.takes(small_board, 1, 1, 0, 0)
        assert king_piece.takes(small_board, 1, 1, 0, 1)
        assert king_piece.takes(small_board, 1, 1, 0, 2)
        assert king_piece.takes(small_board, 1, 1, 1, 0)
        assert king_piece.takes(small_board, 1, 1, 1, 1)
        assert king_piece.takes(small_board, 1, 1, 1, 2)
        assert king_piece.takes(small_board, 1, 1, 2, 0)
        assert king_piece.takes(small_board, 1, 1, 2, 0)
        assert king_piece.takes(small_board, 1, 1, 2, 1)
        assert king_piece.takes(small_board, 1, 1, 2, 2)

    def test_king_cant_move_more_than_one_step(self):
        king_piece = King()
        small_board = Board(3, 3)
        small_board.put(king_piece, 0, 0)
        assert king_piece.takes(small_board, 0, 0, 2, 2) is False
        assert king_piece.takes(small_board, 0, 0, 0, 2) is False

    def test_king_identification_is_K(self):
        piece = King()
        assert piece.piece_identification == 'K'


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

    def test_rook_valid_moves(self):
        rook_piece = Rook()
        small_board = Board(3, 3)
        small_board.put(rook_piece, 0, 0)
        assert rook_piece.takes(small_board, 0, 0, 0, 0)
        assert rook_piece.takes(small_board, 0, 0, 0, 1)
        assert rook_piece.takes(small_board, 0, 0, 0, 2)
        assert rook_piece.takes(small_board, 0, 0, 1, 0)
        assert rook_piece.takes(small_board, 0, 0, 2, 0)

    def test_rook_cant_move_can_move_in_diagonal_direction(self):
        rook_piece = Rook()
        small_board = Board(3, 3)
        small_board.put(rook_piece, 1, 2)
        assert rook_piece.takes(small_board, 0, 0, 1, 1) is False
        assert rook_piece.takes(small_board, 0, 0, 2, 2) is False
        # just in case
        assert rook_piece.takes(small_board, 0, 0, 1, 2) is False

    def test_rook_identification_is_R(self):
        piece = Rook()
        assert piece.piece_identification == 'R'

class TestKnight:

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

    def test_takess(self):
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
        verify_piece_movement(knight, small_board, valid_positions, 2, 2)

    def test_knight_identification_is_N(self):
        piece = Knight()
        assert piece.piece_identification == 'N'

class TestBishop:

    def test_model_positions_to_take(self):
        board = Board(7, 7)
        bishop = Bishop()
        board.put(bishop, 2, 4)
        expected = [
            (6, 0),
            (5, 1),
            (4, 2),
            (3, 3),
            (2, 4),
            (1, 5),
            (0, 6),
            (0, 2),
            (1, 3),
            (3, 5),
            (4, 6),
        ]
        res = bishop.positions_to_take(board, 2, 4)
        assert set([pos for pos in res]) == set(expected)

    def test_takess_diagonal(self):
        bishop = Bishop()
        small_board = Board(3, 3)
        small_board.put(bishop, 0, 0)
        valid_positions = [
            (0, 0),
            (1, 1),
            (2, 2),
        ]
        verify_piece_movement(bishop, small_board, valid_positions, 0, 0)

    def test_bishop_identification_is_B(self):
        piece = Bishop()
        assert piece.piece_identification == 'B'

class TestQueen:

    def test_queen_identification_is_Q(self):
        queen = Queen()
        assert queen.piece_identification == 'Q'

    def test_takes_in_diagonal_vertical_and_horizontal(self):
        queen = Queen()
        small_board = Board(3, 3)
        small_board.put(queen, 0, 0)
        valid_positions = [
            (0, 0),
            (1, 1),
            (2, 2),
            (0, 1),
            (0, 2),
            (1, 0),
            (2, 0),
        ]
        verify_piece_movement(queen, small_board, valid_positions, 0, 0)


    def test_model_positions_to_take(self):
        board = Board(3, 3)
        queen = Queen()
        board.put(queen, 1, 1)
        expected = [
            (0, 0), (0, 1), (0, 2),
            (1, 0), (1, 1), (1, 2),
            (2, 0), (2, 1), (2, 2),
        ]
        res = queen.positions_to_take(board, 1, 1)
        assert set([pos for pos in res]) == set(expected)
