# -*- coding: utf-8 -*-


class Board:

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.pieces = {}

    def put(self, piece, i, j):
        assert 0 <= i < self.n
        assert 0 <= j < self.m
        assert (i, j) not in self.pieces
        self.pieces[(i, j)] = piece

    def position(self, piece):
        for position, current_piece in self.pieces.items():
            if piece == current_piece:
                return position
        raise LookupError('Piece Not Found!')

    def clean(self, i, j):
        if (i, j) in self.pieces:
            del self.pieces[(i, j)]

    def free(self, i, j):
        """
            Return  True if there is not other piece which could take it
        """
        res = True
        for position, piece in self.pieces.items():
            if piece.occupy_function(self, i, j):
                return False
        return res

    def complete(self, pieces):
        return set(pieces) == set(self.pieces.values()) and len(pieces) == len(self.pieces.values())


class Piece:

    @property
    def occupy_function(self):
        """
            returns a function to be called with current (i,j) position and the new (x,y).
            this function returns True or False to know is the piece can move to there.
            ideally this functions has to be O(1) to have a reasonable performance.
        """
        raise NotImplementedError('Abstract method called')


class King(Piece):

    def positions_used_from(self, board, i, j):
        """
            This method is used when a new piece is put in the board.
            Since the new piece could take the ones already in the board we
            need if the piece could take the ones in the board
            Positions returned are from i, j
        """
        return [
                (i - 1, j), (i -1, j - 1), (i, j - 1),
                (i, j),
                (i + 1, j), (i + 1, j + 1), (i, j + 1)]

    @property
    def occupy_function(self):
        def move_anywhere_by_one_place(board, move_to_i, move_to_j):
            """
                King can move anywhere by only one step.
            """
            current_i, current_j = board.position(self)
            valid_i_moves = current_i + 1 == move_to_i or current_i - 1 == move_to_i or current_i == move_to_i
            valid_j_moves = current_j + 1 == move_to_j or current_j - 1 == move_to_j or current_j == move_to_j
            return valid_i_moves and valid_j_moves

        return move_anywhere_by_one_place

    def __str__(self):
        return 'K'


class Rook(Piece):

    def positions_used_from(self, board, i, j):
        for take_i in range(0, board.n):
            yield (take_i, j)

        for take_j in range(0, board.m):
            yield (i, take_j)

    @property
    def occupy_function(self):
        def move_vertically_or_horizontally(board, move_to_i, move_to_j):
            """
                Rooks can move vertically or horizontally only
            """
            current_i, current_j = board.position(self)
            valid_i_moves = current_i == move_to_i and move_to_j % board.m == 0 or current_i == move_to_i
            valid_j_moves = current_j == move_to_j and move_to_i % board.n == 0 or current_j == move_to_j
            return valid_i_moves or valid_j_moves

        return move_vertically_or_horizontally

    def __str__(self):
        return 'R'
