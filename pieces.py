a_white_piece = "wR" or "wP" or "wB" or "wK" or "wN" or "wQ"
a_black_piece = "bR" or "bP" or "bB" or "bK" or "bN" or "bQ"


class chessPiece():  # parent class
    def __init__(self, name, color, coord):
        self.name = name
        self.color = color
        self.coord = coord

        self.move = True
        self.canMove = False
        self.onBoard = True

    def moveTo(self, new_coord):
        self.coord = new_coord

    def __repr__(self):
        return self.name


# classes for the pieces themselves
class Pawn(chessPiece):
    def __init__(self, name, color, coord):
        super().__init__(name, color, coord)
        self.num_moves = 0

    def get_moves(self, board_coord, board, first_click_coord):
        """
        Function to return all possible moves of the piece at the location of the first click
        :param board_coord: current state of the board
        :param board: the
        :param first_click_coord:
        :return:
        """
        black_pawn_moves = []

        # black to move
        if self.color is True:
            possible_moves = []

            # TODO: pawn promotion -> if black piece at row 6, white piece at row 1

            # en passant: if current black piece is on row 4 & there is a white pawn to its left/right w/ num_moves = 1
            if board_coord[0] == 4:

                # there is a white pawn to its left w/ num_moves = 1
                if withinBoardBounds(sumTuple(board_coord, (0, -1))):
                    l1 = board[board_coord[0]][board_coord[1] - 1]
                    if isinstance(l1, Pawn):
                        if not l1.color:
                            if l1.num_moves == 1:
                                possible_moves.append(sumTuple(first_click_coord, (1, -1)))  # can move down 1 left 1

                # there is a white pawn to its right w/ num_moves = 1
                if withinBoardBounds(sumTuple(board_coord, (0, 1))):
                    r1 = board[board_coord[0]][board_coord[1] + 1]
                    if isinstance(r1, Pawn):
                        if not r1.color:
                            if r1.num_moves == 1:
                                possible_moves.append(sumTuple(first_click_coord, (1, 1)))  # can move down 1 right 1

            # regular diagonal capture: down 1 right 1
            if withinBoardBounds(sumTuple(board_coord, (1, 1))):
                d1r1 = board[board_coord[0] + 1][board_coord[1] + 1]
                if isinstance(d1r1, chessPiece):
                    print('a chess piece at the right diagonal')
                    if not d1r1.color:
                        possible_moves.append(sumTuple(first_click_coord, (1, 1)))
            # regular diagonal capture: down 1 left 1
            if withinBoardBounds(sumTuple(board_coord, (1, -1))):
                d1l1 = board[board_coord[0] + 1][board_coord[1] - 1]
                if isinstance(d1l1, chessPiece):
                    print('a chess piece at the left diagonal')
                    if not d1l1.color:
                        possible_moves.append(sumTuple(first_click_coord, (1, -1)))

            # at start position, able to move forward two spaces when BOTH spaces ahead are empty
            if board_coord[0] == 1:
                if board[board_coord[0] + 2][board_coord[1]] is None and board[board_coord[0] + 1][board_coord[1] +
                                                                                                   0] is None:
                    possible_moves.append(sumTuple(first_click_coord, (2, 0)))

            # in general, can move forward one space when space ahead is empty
            if board[board_coord[0] + 1][board_coord[1]] is None:
                possible_moves.append(sumTuple(first_click_coord, (1, 0)))

            return possible_moves

        # white to move
        if self.color is False:
            possible_moves = []

            # en passant: if current white piece is on row 3 & there is a black pawn to its left/right w/ num_moves = 1
            if board_coord[0] == 3:

                # there is a black pawn to its left w/ num_moves = 1
                if withinBoardBounds(sumTuple(board_coord, (0, -1))):
                    l1 = board[board_coord[0]][board_coord[1] - 1]
                    if isinstance(l1, Pawn):
                        if l1.color:
                            if l1.num_moves == 1:
                                possible_moves.append(sumTuple(first_click_coord, (-1, -1)))  # can move up 1 left 1

                # there is a white pawn to its right w/ num_moves = 1
                if withinBoardBounds(sumTuple(board_coord, (0, 1))):
                    r1 = board[board_coord[0]][board_coord[1] + 1]
                    if isinstance(r1, Pawn):
                        if r1.color:
                            if r1.num_moves == 1:
                                possible_moves.append(sumTuple(first_click_coord, (-1, 1)))  # can move up 1 right 1

            # capture diagonal: up 1 right 1
            if withinBoardBounds(sumTuple(board_coord, (-1, 1))):
                u1r1 = board[board_coord[0] - 1][board_coord[1] + 1]
                if isinstance(u1r1, chessPiece):
                    print('a chess piece at the right diagonal')
                    if u1r1.color:
                        possible_moves.append(sumTuple(first_click_coord, (-1, 1)))  # can move up 1 right 1
            # capture diagonal: up 1 left 1
            if withinBoardBounds(sumTuple(board_coord, (-1, -1))):
                u1l1 = board[board_coord[0] - 1][board_coord[1] - 1]
                if isinstance(u1l1, chessPiece):
                    print('a chess piece at the left diagonal')
                    if u1l1.color:
                        possible_moves.append(sumTuple(first_click_coord, (-1, -1)))  # can move up 1 left 1

            # at start position, able to move forward two spaces when BOTH spaces ahead are empty
            if board_coord[0] == 6:
                if board[board_coord[0] - 2][board_coord[1]] is None and board[board_coord[0] - 1][
                    board_coord[1]] is None:
                    possible_moves.append(sumTuple(first_click_coord, (-2, 0)))

            # in general, can move forward one space when space ahead is empty
            if board[board_coord[0] - 1][board_coord[1]] is None:
                possible_moves.append(sumTuple(first_click_coord, (-1, 0)))

            return possible_moves


class Bishop(chessPiece):
    def __init__(self, name, color, coord):
        super().__init__(name, color, coord)
        self.canMove = False

    def get_moves(self, board_coord, board, first_click_coord):
        possible_moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for direction in directions:
            helpCheckPiece(first_click_coord, board, board_coord, possible_moves, direction)
        return possible_moves


class King(chessPiece):
    def __init__(self, name, color, coord):
        super().__init__(name, color, coord)

    def get_moves(self, board_coord, board, first_click_coord):
        possible_moves = []
        if self.color is True:
            if board[board_coord[0] + 1][board_coord[1] + 0] is None or board[board_coord[0] + 1][
                board_coord[1] + 0] == (
                    "wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, 0)))))
            else:
                pass
            if board[board_coord[0] - 1][board_coord[1] + 0] is None or board[board_coord[0] - 1][
                board_coord[1] + 0] == (
                    "wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, 0)))))
            else:
                pass
            if board[board_coord[0] + 1][board_coord[1] + 0] is None or board[board_coord[0] + 1][
                board_coord[1] + 0] == (
                    "wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, 0)))))
            else:
                pass
            if board[board_coord[0] - 1][board_coord[1] - 0] is None or board[board_coord[0] - 1][
                board_coord[1] - 0] == (
                    "wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, 0)))))
            else:
                pass
            if board[board_coord[0] + 0][board_coord[1] + 1] is None or board[board_coord[0] + 0][
                board_coord[1] + 1] == (
                    "wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, 1)))))
            else:
                pass
            if board[board_coord[0] + 0][board_coord[1] + 1] is None or board[board_coord[0] + 0][
                board_coord[1] + 1] == (
                    "wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, 1)))))
            else:
                pass
            if board[board_coord[0] + 0][board_coord[1] - 1] is None or board[board_coord[0] + 0][
                board_coord[1] - 1] == (
                    "wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, -1)))))
            else:
                pass
            if board[board_coord[0] + 0][board_coord[1] - 1] is None or board[board_coord[0] + 0][
                board_coord[1] - 1] == (
                    "wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, -1)))))
            else:
                pass
        if self.color is False:
            if board[board_coord[0] + 1][board_coord[1] + 0] is None or board[board_coord[0] + 1][
                board_coord[1] + 0] == (
                    "bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, 0)))))
            else:
                pass
            if board[board_coord[0] - 1][board_coord[1] + 0] is None or board[board_coord[0] - 1][
                board_coord[1] + 0] == (
                    "bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, 0)))))
            else:
                pass
            if board[board_coord[0] + 1][board_coord[1] + 0] is None or board[board_coord[0] + 1][
                board_coord[1] + 0] == (
                    "bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, 0)))))
            else:
                pass
            if board[board_coord[0] - 1][board_coord[1] + 0] is None or board[board_coord[0] - 1][
                board_coord[1] + 0] == (
                    "bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, 0)))))
            else:
                pass
            if board[board_coord[0] + 0][board_coord[1] + 1] is None or board[board_coord[0] + 0][
                board_coord[1] + 1] == (
                    "bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, 1)))))
            else:
                pass
            if board[board_coord[0] + 0][board_coord[1] + 1] is None or board[board_coord[0] + 0][
                board_coord[1] + 1] == (
                    "bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, 1)))))
            else:
                pass
            if board[board_coord[0] + 0][board_coord[1] - 1] is None or board[board_coord[0] + 0][
                board_coord[1] - 1] == (
                    "bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, -1)))))
            else:
                pass
            if board[board_coord[0] + 0][board_coord[1] - 1] is None or board[board_coord[0] + 0][
                board_coord[1] - 1] == (
                    "bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, -1)))))
            else:
                pass
        return possible_moves


class Queen(chessPiece):
    def __init__(self, name, color, coord):
        super().__init__(name, color, coord)

    def get_moves(self, board_coord, board, first_click_coord):
        possible_moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for direction in directions:
            helpCheckPiece(first_click_coord, board, board_coord, possible_moves, direction)

        return possible_moves


class Rook(chessPiece):
    def __init__(self, name, color, coord):
        super().__init__(name, color, coord)

    def get_moves(self, board_coord, board, first_click_coord):
        possible_moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for direction in directions:
            helpCheckPiece(first_click_coord, board, board_coord, possible_moves, direction)

        return possible_moves


class Knight(chessPiece):
    def __init__(self, name, color, coord):
        super().__init__(name, color, coord)
        self.canMove = True

    def get_moves(self, board_coord, board, first_click_coord):

        possible_moves = []

        # all 8 possible moves for knights
        d1r2 = (1, 2)
        d1l2 = (1, -2)
        u1r2 = (-1, 2)
        u1l2 = (-1, -2)
        d2r1 = (2, 1)
        d2l1 = (2, -1)
        u2r1 = (-2, 1)
        u2l1 = (-2, -1)

        knight_moves = [d1r2, d1l2, u1r2, u1l2, d2r1, d2l1, u2r1, u2l1]

        def getSquare(knight_move):
            ind = sumTuple(knight_move, board_coord)
            return board[ind[0]][ind[1]]

        def helpAppend(knight_move):
            return possible_moves.append(sumTuple(first_click_coord, knight_move))

        for move in knight_moves:
            print(' -> the move being checked is ' + str(move))

            # need to check if within chessboard bounds
            want_to_go_to = sumTuple(board_coord, move)
            print('     square: ' + str(want_to_go_to))

            if withinBoardBounds(want_to_go_to):

                # black
                if self.color is True:
                    if canGoBlack(getSquare(move)):
                        helpAppend(move)

                # white
                if self.color is False:
                    if canGoWhite(getSquare(move)):
                        helpAppend(move)

        return possible_moves


def canGoBlack(target_square):
    return target_square is None or (isinstance(target_square, chessPiece) and not target_square.color)


def canGoWhite(target_square):
    return target_square is None or (isinstance(target_square, chessPiece) and target_square.color)


def sumTuple(t1, t2):
    return tuple(map(sum, zip(t1, t2)))


def withinBoardBounds(want_to_go_to):
    return 7 >= want_to_go_to[0] >= 0 and 7 >= want_to_go_to[1] >= 0


def helpCheckPiece(first_click_coord, board, board_coord, possible_moves, tup):
    current_piece = board[board_coord[0]][board_coord[1]]
    considering_coord = sumTuple(first_click_coord, tup)
    while True:
        # if out of bounds of the board
        if not withinBoardBounds(considering_coord):
            break

        # now that we know the target square is not out of bounds...
        target_square = board[considering_coord[0]][considering_coord[1]]

        # considering a square with a piece
        if isinstance(target_square, chessPiece):
            if not current_piece.color:  # current piece is white
                if not target_square.color:  # target square has a white piece too
                    break
                if target_square.color:  # target square has a black piece
                    possible_moves.append(considering_coord)
                    break

            if current_piece.color:  # current piece is black
                if target_square.color:  # target square has a black piece too
                    break
                if not target_square.color:  # target square has a white piece
                    possible_moves.append(considering_coord)
                    break
        # considering an empty square
        else:
            possible_moves.append(considering_coord)
            considering_coord = sumTuple(considering_coord, tup)
