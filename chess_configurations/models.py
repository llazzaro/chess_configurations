# -*- coding: utf-8 -*-
import json
from collections import Counter


class Board:
    """
        Instances of this class represents the board were
        pieces can be put.
        The board can tell you which places are free and if a free
        position can be taken.
    """

    def __init__(self, dimension_n, dimension_m):
        self.n = dimension_n
        self.m = dimension_m
        self.pieces = {}
        self.free_places = Counter()
        self._reset_free_places()

    def _reset_free_places(self):
        """
            Set all possible positions (i, j) as free.
            A free place means that a piece can be put it
        """
        for i in range(0, self.n):
            for j in range(0, self.m):
                self.free_places[(i, j)] = 0

    def __eq__(self, other):
        """
            Equal function used to compare it against other objects
        """
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
        """
            Since __eq__ was implemented it was required to add the __hash__
        """
        dimension = '{0}{1}'.format(self.n, self.m)
        positions = ''.join(sorted(map(str, self.pieces.keys())))
        pieces = map(lambda piece: piece.piece_identification, self.pieces.values())

        return hash((dimension, positions, ''.join(sorted(pieces))))

    @classmethod
    def from_json(cls, data):
        """
            Use this class method to load board from json
        """
        mapping = {'K': King, 'Q': Queen, 'R': Rook, 'B': Bishop, 'N': Knight}
        raw_dict = json.loads(data)
        res = Board(raw_dict['n'], raw_dict['m'])
        for position, piece_type in raw_dict['pieces'].items():
            i, j = position.strip(')').strip('(').split(',')
            res.put(mapping[piece_type](), int(i), int(j))

        return res

    def to_json(self):
        """
            Dumps the board to a json
        """
        pieces_dict = {}
        for position, piece in self.pieces.items():
            pieces_dict[str(position)] = piece.piece_identification
        return json.dumps({
            'n': self.n,
            'm': self.m,
            'pieces': pieces_dict
        })

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

        for position_to_take in piece.positions_to_take(self, i, j):
            current_usages = self.free_places[position_to_take[0], position_to_take[1]]
            self.free_places[position_to_take[0], position_to_take[1]] = current_usages + 1
        self.pieces[(i, j)] = piece

    def copy(self):
        """
            Returns a copy of the board.
            this is used to avoid destroying board on the backtracking
        """
        res = Board(self.n, self.m)
        for position, piece in self.pieces.items():
            res.pieces[position] = piece
        res.free_places = self.free_places.copy()
        return res

    def clean(self, i, j):
        """ Remove a piece at the position i,j
            i -- integer that must be inside the limits of the board
            j -- integer that must be inside the limits of the board
            raises AssertionError when the place i,j is free.
            returns None, but changes the board.
        """
        assert (i, j) in self.pieces
        for new_free_position in self.pieces[(i, j)].positions_to_take(self, i, j):
            current_usages = self.free_places[new_free_position[0], new_free_position[1]]
            self.free_places[new_free_position[0], new_free_position[1]] = current_usages - 1
        del self.pieces[(i, j)]

    def complete(self, pieces):
        """
            Checks if the board has all the pieces.
            It never check if the pieces could take anyother!!
            pieces -- a collection of pieces to verify is the board has all of them.
            returns True if the board has all the pieces.
        """
        return set(pieces) == set(self.pieces.values()) and len(pieces) == len(self.pieces.values())

    def piece_positions(self):
        """
            returns a generation of the positions of all the pieces
        """
        return (position for position in self.pieces.keys())

    def free_positions(self):
        """
            Returns a list of the free positions on the board
        """
        return [key for key, value in self.free_places.items() if value == 0]

    def conflict(self, current_i, current_j):
        """
            Check if other piece could take the position current_i, current_j
        """
        other_takes_place = False
        for position, board_piece in self.pieces.items():
            if board_piece.takes(self, position[0], position[1], current_i, current_j):
                other_takes_place = True
                break

        return other_takes_place


class Piece:
    """
        Abstract class for Pieces that represents the common behaviour
    """

    def positions_to_take(self, board, i, j):
        """
            This method is used when a new piece is put in the board.
            Since the new piece could take the ones already in the board we
            need if the piece could take the ones in the board
            Positions returned are from i, j
        """
        raise NotImplementedError('Abstract method called')

    @property
    def takes(self):
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
    """ Piece that represents the King """

    def positions_to_take(self, board, i, j):
        """ See Piece class for more information """
        all_positions = [
            (i - 1, j), (i - 1, j - 1), (i, j - 1),
            (i, j), (i - 1, j + 1), (i + 1, j - 1),
            (i + 1, j), (i + 1, j + 1), (i, j + 1)]

        return [(i, j) for i, j in all_positions if 0 <= i < board.n and 0 <= j < board.m]

    @property
    def takes(self):
        """ See Piece class for more information """
        def move_anywhere_by_one_place(_, position_i, position_j, move_to_i, move_to_j):
            """
                King can move anywhere by only one step.
            """
            return abs(position_i - move_to_i) <= 1 and abs(position_j - move_to_j) <= 1

        return move_anywhere_by_one_place

    @property
    def piece_identification(self):
        """ See Piece class for more information """
        return 'K'


class Rook(Piece):
    """ Piece that represents the Rook """

    def positions_to_take(self, board, i, j):
        """ See Piece class for more information """
        for take_i in range(0, board.n):
            yield (take_i, j)

        for take_j in range(0, board.m):
            yield (i, take_j)

    @property
    def takes(self):
        """ See Piece class for more information """
        def move_vertically_or_horizontally(board, position_i, position_j, move_to_i, move_to_j):
            """
                Rooks can move vertically or horizontally only
            """
            valid_i_moves = position_i == move_to_i and move_to_j % board.m == 0 or position_i == move_to_i
            valid_j_moves = position_j == move_to_j and move_to_i % board.n == 0 or position_j == move_to_j
            return valid_i_moves or valid_j_moves

        return move_vertically_or_horizontally

    @property
    def piece_identification(self):
        """ See Piece class for more information """
        return 'R'


class Knight(Piece):
    """ Piece that represetns a Knight """

    def positions_to_take(self, board, i, j):
        """ See Piece class for more information """
        position_1 = (i - 2, j - 1)
        position_2 = (i - 1, j - 2)
        position_3 = (i + 1, j - 2)
        position_4 = (i + 2, j - 1)
        position_5 = (i - 2, j + 1)
        position_6 = (i - 1, j + 2)
        position_7 = (i + 1, j + 2)
        position_8 = (i + 2, j + 1)
        return filter(lambda pos: 0 <= pos[0] < board.n and 0 <= pos[1] < board.m, [
            position_1,
            position_2,
            position_3,
            position_4,
            position_5,
            position_6,
            position_7,
            position_8,
            (i, j),
        ])

    @property
    def takes(self):
        """ See Piece class for more information """
        def move_with_as_knight(_, position_i, position_j, move_to_i, move_to_j):
            """
                Knight move in a L shape. this function check if the position to move
                is valid in O(1)
            """
            valid_shape_move_1 = abs(position_i - move_to_i) == 1 and abs(position_j - move_to_j) == 2
            valid_shape_move_2 = abs(position_i - move_to_i) == 2 and abs(position_j - move_to_j) == 1
            no_move = position_i == move_to_i and position_j == move_to_j
            return any([valid_shape_move_1, valid_shape_move_2, no_move])

        return move_with_as_knight

    @property
    def piece_identification(self):
        """ See Piece class for more information """
        return 'N'


class Bishop(Piece):
    """
        Piece that represents a Bishop
    """

    def positions_to_take(self, board, i, j):
        """ See Piece class for more information """
        for current_i in range(0, board.n):
            for current_j in range(0, board.m):
                if self.takes(board, current_i, current_j, i, j):
                    yield (current_i, current_j)

    @property
    def takes(self):
        """ See Piece class for more information """
        def move_vertically_or_horizontally(_, position_i, position_j, move_to_i, move_to_j):
            """
                Bishop can move only in diagonal
            """
            return abs(position_i - move_to_i) == abs(position_j - move_to_j)

        return move_vertically_or_horizontally

    @property
    def piece_identification(self):
        """ See Piece class for more information """
        return 'B'


class Queen(Rook, Bishop):
    """
        Since queens it beheaves like a Rook and a Bishop it inherits from both.
        the multiple inheritance was not done for code reusage.
    """

    def positions_to_take(self, board, i, j):
        """ See Piece class for more information """
        yield from Bishop.positions_to_take(self, board, i, j)
        yield from Rook.positions_to_take(self, board, i, j)

    @property
    def takes(self):
        """ See Piece class for more information """
        def move_like_a_queen(board, position_i, position_j, move_to_i, move_to_j):
            """
                Queen can move in diagonal, vertical and horital directions
            """
            valid_movement_like_bishop = Bishop().takes(board, position_i, position_j, move_to_i, move_to_j)
            valid_movement_like_rook = Rook().takes(board, position_i, position_j, move_to_i, move_to_j)
            return valid_movement_like_bishop or valid_movement_like_rook

        return move_like_a_queen

    @property
    def piece_identification(self):
        """ See Piece class for more information """
        return 'Q'
