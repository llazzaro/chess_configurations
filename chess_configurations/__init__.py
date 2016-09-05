# -*- coding: utf-8 -*-
import json
from multiprocessing import Process


class MultiProcessSolverConsumer(Process):

    def __init__(self, parameter_queue, results_queue):
        self.parameter_queue = parameter_queue
        self.results_queue = results_queue
        self.mapping = {'K': King, 'Q': Queen, 'R': Rook, 'B': Bishop, 'N': Knight}

    def run(self):
        while True:
            self._iteration()

    def _iteration(self):
        parameters = json.loads(self.parameter_queue.get())
        board = Board.from_json(parameters['board'])
        i = int(parameters['i'])
        j = int(parameters['j'])
        for piece_type in parameters['pieces']:
            pieces.append(self.mapping[piece_type]())
        for board in backtracking(board, pieces, pieces, i, j):
            self.results_queue.put(board.to_json())


class MultiProcessSolverProducer(Process)

    def __init__(self, n, m, pieces, parameter_queue):
        self.n = n
        self.m = m
        self.pieces = pieces
        self.parameter_queue = parameter_queue

    def run(self):
        self._iteration()

    def _iteration(self):
        pieces = self.pieces
        board = Board(self.n, self.m)
        for current_i in range(0, self.n):
            for current_j in range(0, self.m):
                for piece in set(pieces):
                    board.put(piece, current_i, current_j)
                    next_pieces = pieces.copy()
                    next_pieces.remove(piece)
                    parameters = json.dumps({
                        'board': board.to_json(),
                        'i': current_i,
                        'j': current_j,
                        'pieces': [piece.piece_identification for piece in next_pieces]
                    })
                    self.parameter_queue.put(parameters)
