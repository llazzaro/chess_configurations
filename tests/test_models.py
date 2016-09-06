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
    """
        Verifies that given that a list of valid positions are the
        only ones.
    """
    for i in range(0, board.n):
        for j in range(0, board.m):
            if (i, j) in valid_positions:
                assert piece.takes(board, current_pos_i, current_pos_j, i, j) is True
            else:
                assert piece.takes(board, current_pos_i, current_pos_j, i, j) is False


def test_equal_on_different_board():
    """
        docstrings should comply to pep257 for every public class
        and method and module function (except from tests)
    """
    king = King()
    board = Board(3, 3)
    board.put(king, 0, 0)

    another_board = Board(3, 3)
    another_board.put(king, 2, 2)

    assert another_board != board
    assert hash(another_board) != hash(board)


def test_equals_different_board_2():
    """ test_equals_on_different_board_different_piece_in_same_position """
    king = King()
    bishop = Bishop()
    board = Board(3, 3)
    board.put(king, 0, 0)

    another_board = Board(3, 3)
    another_board.put(bishop, 0, 0)

    assert another_board != board
    assert hash(another_board) != hash(board)


def test_equal_same_positions():
    """ test_equal_with_the_same_pieces_at_same_positions """
    king = King()
    board = Board(3, 3)
    board.put(king, 0, 0)
    another_board = Board(3, 3)
    another_board.put(king, 0, 0)
    assert another_board == board
    assert another_board == board
    assert hash(another_board) == hash(board)


def test_equal_order():
    """ test_equal_with_the_same_pieces_at_same_positions_added_in_different_order"""
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


def test_copy_is_ok():
    """ test_copy_method_copies_every_piece_and_dimension_are_correct """
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


def test_clean_is_ok():
    """ test_clean_when_there_is_a_piece_in_the_position """
    king = King()
    board = Board(3, 3)
    board.put(king, 0, 0)
    board.clean(0, 0)
    assert board.pieces == {}


def test_clean_empty():
    """ test_clean_when_in_an_empty_position"""
    board = Board(3, 3)
    with raises(AssertionError):
        board.clean(0, 0)


def test_free_with_empty_board():
    """
        docstrings should comply to pep257 for every public class
        and method and module function (except from tests)
    """
    board = Board(3, 3)
    for i in range(0, 3):
        for j in range(0, 3):
            assert (i, j) in board.free_positions()


def test_free_with_king():
    """test_free_with_a_king_in_the_board_happy_path """
    king = King()
    board = Board(3, 3)
    board.put(king, 0, 0)
    assert (0, 0) not in board.free_positions()
    assert (0, 1) not in board.free_positions()
    assert (2, 2) in board.free_positions()

def test_free_with_pieces():
    """test_free_with_a_king_in_the_board_happy_path """
    king = King()
    queen = Queen()
    board = Board(7, 7)
    assert len(board.free_positions()) == 49
    board.put(king, 5, 5)
    assert len(board.free_positions()) == 40
    board.clean(5, 5)
    assert len(board.free_positions()) == 49
    board.put(queen, 4, 3)
    assert len(board.free_positions()) == 26
    board.clean(4, 3)
    assert len(board.free_positions()) == 49

def test_free_bug():
    queen = Queen()
    queen_2 = Queen()
    board = Board(7, 7)
    assert len(board.free_positions()) == 49
    board.put(queen, 4, 3)
    assert len(board.free_positions()) == 26
    board.put(queen, 0, 0)
    assert len(board.free_positions()) == 12
    board.clean(0, 0)
    assert len(board.free_positions()) == 26

def test_complete_with_empty_board():
    """
        docstrings should comply to pep257 for every public class
        and method and module function (except from tests)
    """
    board = Board(3, 3)
    assert board.complete([])


def test_complete_returns_false():
    """ test_complete_returns_false_when_pieces_are_missing"""
    board = Board(3, 3)
    assert board.complete([King()]) is False


def test_complete_returns_true():
    """ test_complete_returns_true_when_all_pieces_are_in_the_board """

    king = King()
    board = Board(3, 3)
    board.put(king, 0, 0)

    assert board.complete([King()]) is True


def test_pieces_positions_check():
    """
        docstrings should comply to pep257 for every public class
        and method and module function (except from tests)
    """
    king = King()
    board = Board(3, 3)
    board.put(king, 1, 1)

    assert [position for position in board.piece_positions()] == [(1, 1)]


def test_to_json_two_pieces():
    """test_to_json_with_a_board_with_two_pieces"""
    king = King()
    rook = Rook()
    board = Board(3, 4)
    board.put(king, 1, 1)
    board.put(rook, 2, 2)
    res = json.loads(board.to_json())
    expected = json.loads('{"m": 4, "pieces": {"(2, 2)": "R", "(1, 1)": "K"}, "n": 3}')
    assert res == expected


def test_from_json_two_pieces():
    """test_from_json_with_a_board_with_two_pieces"""
    king = King()
    rook = Rook()
    expected_board = Board(3, 4)
    expected_board.put(king, 1, 1)
    expected_board.put(rook, 2, 2)
    res = Board.from_json('{"m": 4, "pieces": {"(2, 2)": "R", "(1, 1)": "K"}, "n": 3}')
    assert res == expected_board


def test_equals_case_1():
    """ test_equals_case_detected_in_a_bug"""
    board_set = set()

    board = Board(6, 4)
    rook = Rook()
    queen = Queen()
    bishop = Bishop()
    board.put(rook, 2, 1)
    board.put(queen, 4, 0)
    board.put(bishop, 5, 2)
    board_set.add(board)

    another_board = Board(6, 4)
    rook = Rook()
    queen = Queen()
    bishop = Bishop()
    another_board.put(rook, 2, 1)
    another_board.put(queen, 4, 0)
    another_board.put(bishop, 5, 2)

    assert another_board in board_set

    board_set.add(another_board)
    assert len(board_set) == 1


def test_conflict_case():
    """test_conflict_special_case_found"""
    board = Board(6, 4)
    rook = Rook()
    queen = Queen()
    board.put(rook, 2, 1)
    assert board.conflict(4, 0) is False
    assert board.conflict(5, 2) is False
    assert (5, 2) in board.free_positions()
    board.put(queen, 4, 0)
    assert (5, 2) in board.free_positions()
    assert board.conflict(5, 2) is False


def test_clean_frees_place():
    """test_clean_frees_places_in_the_board"""
    board = Board(4, 4)
    rook = Rook()
    board.put(rook, 2, 2)
    expected = [(0, 1), (0, 0), (1, 3), (3, 3), (3, 0), (3, 1), (1, 0), (1, 1), (0, 3)]
    assert set(expected) == set(board.free_positions())
    expected_after_clean = [
        (0, 1), (0, 0),
        (1, 3), (3, 3),
        (3, 0), (3, 1),
        (1, 0), (1, 1),
        (0, 3), (0, 2),
        (1, 2), (2, 2),
        (3, 2), (2, 0),
        (2, 1), (2, 2),
        (2, 3)]
    board.clean(2, 2)
    assert set(expected_after_clean) == set(board.free_positions())


# TestPiece:

def test_equals_other_object():
    """test_equals_against_other_object"""
    piece = Piece()
    assert piece != 1


# TestKing:

def test_king_takes_rook():
    """test_of_a_bug_it_was_possible_to_put_a_king_that_takes_a_rook"""
    king = King()
    board = Board(3, 3)
    board.put(king, 0, 0)
    positions_to_take = king.positions_to_take(board, 0, 0)
    assert (0, 1) in positions_to_take


def test_used_king_ok():
    """test_positions_used_from_for_king_in_the_upper_corner_are_valid"""
    king_piece = King()
    small_board = Board(3, 3)
    assert (0, 0) in king_piece.positions_to_take(small_board, 0, 0)
    assert (1, 0) in king_piece.positions_to_take(small_board, 0, 0)
    assert (1, 1) in king_piece.positions_to_take(small_board, 0, 0)
    assert (0, 1) in king_piece.positions_to_take(small_board, 0, 0)
    assert (0, 2) not in king_piece.positions_to_take(small_board, 0, 0)


def test_pieces__indistingueable():
    """test_pieces_of_the_same_type_are_indistingueable"""
    king = King()
    king_2 = King()
    assert king == king_2


def test_pieces_distingueable():
    """test_pieces_of_different_type_are_distingueable"""
    king = King()
    rook = Rook()
    assert king != rook


def test_king_takes_happy_cases():
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


def test_king_invalid_move():
    """test_king_cant_move_more_than_one_step"""
    king_piece = King()
    small_board = Board(3, 3)
    small_board.put(king_piece, 0, 0)
    assert king_piece.takes(small_board, 0, 0, 2, 2) is False
    assert king_piece.takes(small_board, 0, 0, 0, 2) is False


def test_identification_k():
    """test_king_identification_is_K"""
    piece = King()
    assert piece.piece_identification == 'K'


# TestRook:

def test_rook_valid_moves():
    """
        docstrings should comply to pep257 for every public class
        and method and module function (except from tests)
    """
    rook_piece = Rook()
    small_board = Board(3, 3)
    small_board.put(rook_piece, 0, 0)
    assert rook_piece.takes(small_board, 0, 0, 0, 0)
    assert rook_piece.takes(small_board, 0, 0, 0, 1)
    assert rook_piece.takes(small_board, 0, 0, 0, 2)
    assert rook_piece.takes(small_board, 0, 0, 1, 0)
    assert rook_piece.takes(small_board, 0, 0, 2, 0)


def test_rook_invalid_check():
    """test_rook_cant_move_can_move_in_diagonal_direction"""
    rook_piece = Rook()
    small_board = Board(3, 3)
    small_board.put(rook_piece, 1, 2)
    assert rook_piece.takes(small_board, 0, 0, 1, 1) is False
    assert rook_piece.takes(small_board, 0, 0, 2, 2) is False
    # just in case
    assert rook_piece.takes(small_board, 0, 0, 1, 2) is False


def test_rook_identification_r():
    """
        docstrings should comply to pep257 for every public class
        and method and module function (except from tests)
    """
    piece = Rook()
    assert piece.piece_identification == 'R'


# TestKnight:

def test_taken_position_generator():
    """
        docstrings should comply to pep257 for every public class
        and method and module function (except from tests)
    """
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


def test_takess():
    """
        docstrings should comply to pep257 for every public class
        and method and module function (except from tests)
    """
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


def test_knight_identification_n():
    """
        docstrings should comply to pep257 for every public class
        and method and module function (except from tests)
    """
    piece = Knight()
    assert piece.piece_identification == 'N'


# TestBishop:

def test_model_positions_to_take():
    """
        docstrings should comply to pep257 for every public class
        and method and module function (except from tests)
    """
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


def test_takess_diagonal():
    """
        docstrings should comply to pep257 for every public class
        and method and module function (except from tests)
    """
    bishop = Bishop()
    small_board = Board(3, 3)
    small_board.put(bishop, 0, 0)
    valid_positions = [
        (0, 0),
        (1, 1),
        (2, 2),
    ]
    verify_piece_movement(bishop, small_board, valid_positions, 0, 0)


def test_bishop_identification_b():
    """
        docstrings should comply to pep257 for every public class
        and method and module function (except from tests)
    """
    piece = Bishop()
    assert piece.piece_identification == 'B'


# TestQueen:

def test_queen_identification_q():
    """
        docstrings should comply to pep257 for every public class
        and method and module function (except from tests)
    """
    queen = Queen()
    assert queen.piece_identification == 'Q'


def test_takes_valid_ones():
    """test_takes_in_diagonal_vertical_and_horizontal"""
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


def test_queen_positions_to_take():
    """
        docstrings should comply to pep257 for every public class
        and method and module function (except from tests)
    """
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
