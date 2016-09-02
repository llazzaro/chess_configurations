# -*- coding: utf-8 -*-


class Board:

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.pieces = {}

    def __eq__(self, other):
        equal_dimension = self.n == other.n and self.m == other.m
        equal_pieces = True
        for position, piece in self.pieces.items():
            if position not in other.pieces:
                equal_pieces = False
                break
            else:
                if other.pieces[position] != piece:
                    equal_pieces = False
                    break
        return equal_dimension and equal_pieces

    def __hash__(self):
        dimension = '{0}{1}'.format(self.n, self.m)
        positions = ''.join(sorted(map(lambda position: str(position), self.pieces.keys())))
        pieces = ''.join(sorted(map(lambda piece: piece.piece_identification, self.pieces.values())))

        return hash((dimension, positions, pieces))

    def put(self, piece, i, j):
        assert 0 <= i < self.n
        assert 0 <= j < self.m
        assert (i, j) not in self.pieces
        self.pieces[(i, j)] = piece

    def copy(self):
        res = Board(self.n, self.m)
        for position, piece in self.pieces.items():
            res.pieces[position] = piece
        return res

    def clean(self, i, j):
        if (i, j) in self.pieces:
            del self.pieces[(i, j)]

    def free(self, i, j):
        """
            Return  True if there is not other piece which could take it
        """
        res = True
        for position, piece in self.pieces.items():
            if piece.occupy_function(self, position[0], position[1], i, j):
                return False
        return res

    def complete(self, pieces):
        return set(pieces) == set(self.pieces.values()) and len(pieces) == len(self.pieces.values())

    def pieces_positions(self):
        return (position for position in self.pieces.keys())


class Piece:

    @property
    def occupy_function(self):
        """
            returns a function to be called with current (i,j) position and the new (x,y).
            this function returns True or False to know is the piece can move to there.
            ideally this functions has to be O(1) to have a reasonable performance.
        """
        raise NotImplementedError('Abstract method called')

    def __str__(self):
        return self.piece_identification

    def __eq__(self, other):
        return self.piece_identification == other.piece_identification

    def __hash__(self):
        return hash(self.piece_identification)

    @property
    def piece_identification(self):
        raise NotImplementedError('Abstract method called')


class King(Piece):

    @property
    def piece_identification(self):
        return 'K'

    def positions_to_take(self, board, i, j):
        """
            This method is used when a new piece is put in the board.
            Since the new piece could take the ones already in the board we
            need if the piece could take the ones in the board
            Positions returned are from i, j
        """
        return [
                (i - 1, j), (i - 1, j - 1), (i, j - 1),
                (i, j), (i - 1, j + 1), (i + 1, j - 1),
                (i + 1, j), (i + 1, j + 1), (i, j + 1)]

    @property
    def occupy_function(self):
        def move_anywhere_by_one_place(board, piece_position_i, piece_position_j, move_to_i, move_to_j):
            """
                King can move anywhere by only one step.
            """
            valid_i_moves = piece_position_i + 1 == move_to_i or piece_position_i - 1 == move_to_i or piece_position_i == move_to_i
            valid_j_moves = piece_position_j + 1 == move_to_j or piece_position_j - 1 == move_to_j or piece_position_j == move_to_j
            return valid_i_moves and valid_j_moves

        return move_anywhere_by_one_place


class Rook(Piece):

    @property
    def piece_identification(self):
        return 'R'

    def positions_to_take(self, board, i, j):
        for take_i in range(0, board.n):
            yield (take_i, j)

        for take_j in range(0, board.m):
            yield (i, take_j)

    @property
    def occupy_function(self):
        def move_vertically_or_horizontally(board, piece_position_i, piece_position_j, move_to_i, move_to_j):
            """
                Rooks can move vertically or horizontally only
            """
            valid_i_moves = piece_position_i == move_to_i and move_to_j % board.m == 0 or piece_position_i == move_to_i
            valid_j_moves = piece_position_j == move_to_j and move_to_i % board.n == 0 or piece_position_j == move_to_j
            return valid_i_moves or valid_j_moves

        return move_vertically_or_horizontally
