# -*- coding: utf-8 -*-
import json

from chess_configurations.models import (
    Board,
    King,
    Queen,
    Rook,
    Bishop,
    Knight,
)

def load_test_case_input(parameter_filename):
    mapping = {'K': King, 'Q': Queen, 'R': Rook, 'B': Bishop, 'N': Knight}
    with open(parameter_filename, 'r') as parameter_file:
        input_parameters = json.loads(parameter_file.read())
        board = Board(int(input_parameters['n']), int(input_parameters['m']))
        pieces = []
        for piece_type in input_parameters['pieces']:
            pieces.append(mapping[piece_type]())

    return board, pieces


def load_test_case_solution(solution_filename):
        with open(solution_filename, 'r') as solution_file:
            for solution in solution_file:
                expected.append(Board.from_json(solution))
