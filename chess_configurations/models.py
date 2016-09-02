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
        """ Puts a piece on the board at position i,j
            i -- integer that must be inside the limits of the board
            j -- integer that must be inside the limits of the board
            returns None
            raises AssertException when i or j are invalid or a piece is in that position.
        """
        assert 0 <= i < self.n
        assert 0 <= j < self.m
        assert (i, j) not in self.pieces
        self.pieces[(i, j)] = piece

    def copy(self):
        """ Returns a copy of the board. this is used to avoid destroying board on the backtracking"""
        res = Board(self.n, self.m)
        for position, piece in self.pieces.items():
            res.pieces[position] = piece
        return res

    def clean(self, i, j):
        """ Remove a piece at the position i,j
            i -- integer that must be inside the limits of the board
            j -- integer that must be inside the limits of the board
            raises AssertionError when the place i,j is free.
            returns None, but changes the board.
        """
        assert (i, j) in self.pieces
        del self.pieces[(i, j)]

    def free(self, i, j):
        """
            Checks if another piece could take the position i,j
            i -- integer that must be inside the limits of the board
            j -- integer that must be inside the limits of the board
            complexity: O(p), where p is the number of pieces on the board.
                        we require that occupy_function is O(1) always.
            return True if there is not other piece which could take i
            raises AssertionError when the i,j is outside the board
        """
        assert 0 <= i < self.n
        assert 0 <= j < self.m
        res = True
        for position, piece in self.pieces.items():
            if piece.occupy_function(self, position[0], position[1], i, j):
                return False
        return res

    def complete(self, pieces):
        """
            Checks if the board has all the pieces.
            It never check if the pieces could take anyother!!
            pieces -- a collection of pieces to verify is the board has all of them.
            returns True if the board has all the pieces.
        """
        return set(pieces) == set(self.pieces.values()) and len(pieces) == len(self.pieces.values())

    def pieces_positions(self):
        """
            returns a generation of the positions of all the pieces
        """
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
        """ Returns the string representation. used in the draw function """
        return self.piece_identification

    def __eq__(self, other):
        """
            Pieces of the same type should be indistinguishable to avoid duplicate solutions
            where pieces of the same tpye are permuted.

            other -- Any object to compare with

            returns a boolean
        """
        if not getattr(other, 'piece_identification', None):
            return False
        return self.piece_identification == other.piece_identification

    def __hash__(self):
        """
            Since __eq__ was implemented it was required to implement __hash__
            we use piece_identification string to calculate the hash.
        """
        return hash(self.piece_identification)

    @property
    def piece_identification(self):
        """
            returns a string with the piece identification
                    only this values can be returned : ['K', 'B', 'N', 'Q', 'R']
        """
        raise NotImplementedError('Abstract method called')


class King(Piece):

    @property
    def piece_identification(self):
        """ See Piece class method doc string"""
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
            return abs(piece_position_i - move_to_i) <= 1 and abs(piece_position_j - move_to_j) <= 1

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


class Knight(Piece):

    @property
    def piece_identification(self):
        return 'N'

    def positions_to_take(self, board, i, j):

        position_1 = (i - 2, j - 1)
        position_2 = (i - 1, j - 2)
        position_3 = (i + 1, j - 2)
        position_4 = (i + 2, j - 1)
        position_5 = (i - 2, j + 1)
        position_6 = (i - 1, j + 2)
        position_7 = (i + 1, j + 2)
        position_8 = (i + 2, j + 1)
        return [
            position_1,
            position_2,
            position_3,
            position_4,
            position_5,
            position_6,
            position_7,
            position_8,
            (i, j),
        ]

    @property
    def occupy_function(self):
        def move_with_as_knight(board, piece_position_i, piece_position_j, move_to_i, move_to_j):
            """
            """
            valid_shape_move_1 = abs(piece_position_i - move_to_i) == 1 and abs(piece_position_j - move_to_j) == 2
            valid_shape_move_2 = abs(piece_position_i - move_to_i) == 2 and abs(piece_position_j - move_to_j) == 1
            no_move = piece_position_i == move_to_i and piece_position_j == move_to_j
            return any([valid_shape_move_1, valid_shape_move_2, no_move])

        return move_with_as_knight


class Bishop(Piece):
    """
        Since queens it beheaves like a Rook and a Bishop it inherits from both.
        the multiple inheritance was not done for code reusage.
    """

    @property
    def piece_identification(self):
        return 'B'

    def positions_to_take(self, board, i, j):
        for combination in range(0, max(board.n, board.m)):
            yield (i + combination + 1, j + combination + 1)
            yield (i + combination - 1, j + combination + 1)
            yield (i + combination - 1, j + combination - 1)
            yield (i + combination + 1, j + combination - 1)

    @property
    def occupy_function(self):
        def move_vertically_or_horizontally(board, piece_position_i, piece_position_j, move_to_i, move_to_j):
            """
                Rooks can move vertically or horizontally only
            """
            return abs(piece_position_i - move_to_i) == abs(piece_position_j - move_to_j)

        return move_vertically_or_horizontally


class Queen(Rook, Bishop):
    """
        Since queens it beheaves like a Rook and a Bishop it inherits from both.
        the multiple inheritance was not done for code reusage.
    """

    @property
    def piece_identification(self):
        return 'Q'

    def positions_to_take(self, board, i, j):
        pass

    @property
    def occupy_function(self):
        pass
