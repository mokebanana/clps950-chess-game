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

    def get_moves(self, board_coord, board, first_click_coord):
        """
        Function to return all possible moves of the piece at the location of the first click
        :param board_coord: current state of the board
        :param board: the
        :param first_click_coord:
        :return:
        """
        # black to move
        if self.color is True:
            possible_moves = []
            if board[board_coord[0] + 1][board_coord[1] + 1] is not None:
                if board[board_coord[0] + 1][board_coord[1] + 1] == ("wR" or "wP" or "wB" or "wN" or "wQ"):
                    possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, 1)))))
                else:
                    pass
            elif board[board_coord[0] - 1][board_coord[1] + 1] is not None:
                if board[board_coord[0] + 1][board_coord[1] - 1] == ("wR" or "wP" or "wB" or "wN" or "wQ"):
                    possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, 1)))))
                else:
                    pass
            elif board_coord[1] == 1:
                if board[board_coord[0] + 0][board_coord[1] + 2] is None:
                    possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, 2)))))
                if board[board_coord[0] + 0][board_coord[1] + 1] is None:
                    possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, 1)))))
            elif board[board_coord[0] + 0][board_coord[1] + 1] is None:
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, -1)))))
            else:
                pass
            return possible_moves
        # white to move
        if self.color is False:
            possible_moves = []
            if board[board_coord[0] + 1][board_coord[1] - 1] is not None:
                if board[board_coord[0] + 1][board_coord[1] - 1] == ("bR" or "bP" or "bB" or "bN" or "bQ"):
                    # add the possible move for capturing diagonal
                    possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, -1)))))
                else:
                    pass
            elif board[board_coord[0] - 1][board_coord[1] - 1] is not None:
                if board[board_coord[0] - 1][board_coord[1] - 1] == ("bR" or "bP" or "bB" or "bN" or "bQ"):
                    possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, -1)))))
                else:
                    pass
            elif board_coord[1] == 6:
                if board[board_coord[0] + 0][board_coord[1] - 2] is None:
                    tupP1 = tuple(map(sum, zip(first_click_coord, (0, -2))))
                    possible_moves.append(tupP1)
                if board[board_coord[0] + 0][board_coord[1] - 1] is None:
                    tupP2 = tuple(map(sum, zip(first_click_coord, (0, -1))))
                    possible_moves.append(tupP2)
            elif board[board_coord[0] + 0][board_coord[1] - 1] is None:
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, -1)))))
            else:
                pass
            return possible_moves


class Bishop(chessPiece):
    def __init__(self, name, color, coord):
        super().__init__(name, color, coord)
        self.canMove = False

    def get_moves(self, board_coord, board, first_click_coord):
        possible_moves = []
        still_looking = True
        considering_coord = (tuple(map(sum, zip(first_click_coord, (1, 1)))))
        # diagonally up and to the right
        while still_looking:
            if board[board_coord[0] + 1][board_coord[1] + 1] is not None:
                if self.color is False:
                    if considering_coord == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                        still_looking = False
                    elif considering_coord == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                        possible_moves.append(considering_coord)
                        break
                if self.color is True:
                    if considering_coord == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                        still_looking = False
                    elif considering_coord == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                        possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, 1)))))
                        still_looking = False
            else:
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, 1)))))
                considering_coord = (tuple(map(sum, zip(considering_coord, (1, 1)))))
        considering_coord2 = (tuple(map(sum, zip(first_click_coord, (1, -1)))))  # TODO: why is this code unreachable?
        while still_looking:
            if board[board_coord[0] + 1][board_coord[1] - 1] is not None:
                if self.color is False:
                    if considering_coord2 == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                        still_looking = False
                    elif considering_coord2 == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                        possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, -1)))))
                        break
                if self.color is True:
                    if considering_coord2 == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                        still_looking = False
                    elif considering_coord2 == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                        possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, -1)))))
                        still_looking = False
            else:
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, -1)))))
                considering_coord2 = (tuple(map(sum, zip(considering_coord, (1, -1)))))
        considering_coord3 = (tuple(map(sum, zip(first_click_coord, (-1, -1)))))
        while still_looking:
            if board[board_coord[0] - 1][board_coord[1] - 1] is not None:
                if self.color is False:
                    if considering_coord3 == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                        still_looking = False
                    elif considering_coord3 == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                        possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, -1)))))
                        break
                if self.color is True:
                    if considering_coord3 == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                        still_looking = False
                    elif considering_coord3 == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                        possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, -1)))))
                        still_looking = False
            else:
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, -1)))))
                considering_coord3 = (tuple(map(sum, zip(considering_coord, (-1, -1)))))
        considering_coord4 = (tuple(map(sum, zip(first_click_coord, (-1, 1)))))
        while still_looking:
            if board[board_coord[0] - 1][board_coord[1] + 1] is not None:
                if self.color is False:
                    if considering_coord4 == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                        still_looking = False
                    elif considering_coord4 == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                        possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, 1)))))
                        break
                if self.color is True:
                    if considering_coord4 == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                        still_looking = False
                    elif considering_coord4 == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                        possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, 1)))))
                        still_looking = False
            else:
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, 1)))))
                considering_coord = (tuple(map(sum, zip(considering_coord, (-1, 1)))))
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


class Rook(chessPiece):
    def __init__(self, name, color, coord):
        super().__init__(name, color, coord)

    def get_moves(self, board_coord, board, first_click_coord):
        possible_moves = []
        still_looking = True
        considering_coord = (tuple(map(sum, zip(first_click_coord, (0, 1)))))
        while still_looking:
            if board[board_coord[0] + 0][board_coord[1] + 1] is not None:
                if self.color is False:
                    if considering_coord == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                        still_looking = False
                    elif considering_coord == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                        possible_moves.append(considering_coord)
                        break
                if self.color is True:
                    if considering_coord == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                        still_looking = False
                    elif considering_coord == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                        possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, 1)))))
                        still_looking = False
            else:
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, 1)))))
                considering_coord = (tuple(map(sum, zip(considering_coord, (0, 1)))))
        considering_coord2 = (tuple(map(sum, zip(first_click_coord, (0, -1)))))
        while still_looking:
            if board[board_coord[0] + 0][board_coord[1] - 1] is not None:
                if self.color is False:
                    if considering_coord2 == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                        still_looking = False
                    elif considering_coord2 == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                        possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, -1)))))
                        break
                if self.color is True:
                    if considering_coord2 == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                        still_looking = False
                    elif considering_coord2 == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                        possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, -1)))))
                        still_looking = False
            else:
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, -1)))))
                considering_coord2 = (tuple(map(sum, zip(considering_coord, (0, -1)))))
        considering_coord3 = (tuple(map(sum, zip(first_click_coord, (1, 0)))))
        while still_looking:
            if board[board_coord[0] + 1][board_coord[1] + 0] is not None:
                if self.color is False:
                    if considering_coord3 == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                        still_looking = False
                    elif considering_coord3 == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                        possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, 0)))))
                        break
                if considering_coord is None:
                    possible_moves.append(self.coord + (1, 1))
                if self.color is True:
                    if considering_coord3 == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                        still_looking = False
                    elif considering_coord3 == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                        possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, 0)))))
                        still_looking = False
            else:
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, 0)))))
                considering_coord3 = (tuple(map(sum, zip(considering_coord, (1, 0)))))
        considering_coord4 = (tuple(map(sum, zip(first_click_coord, (-1, 0)))))
        while still_looking:
            if board[board_coord[0] - 1][board_coord[1] + 0] is not None:
                if self.color is False:
                    if considering_coord4 == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                        still_looking = False
                    elif considering_coord4 == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                        possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, 0)))))
                        break
                if self.color is True:
                    if considering_coord4 == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                        still_looking = False
                    elif considering_coord4 == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                        possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, 0)))))
                        still_looking = False
            else:
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, 0)))))
                considering_coord = (tuple(map(sum, zip(considering_coord, (-1, 0)))))
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
        u2l1 = (-2, -2)

        knight_moves = [d1r2, d1l2, u1r2, u1l2, d2r1, d2l1, u2r1, u2l1]

        def getSquare(knight_move):
            return board[board_coord[0] + knight_move[0]][board_coord[1] + knight_move[1]]

        def helpAppend(knight_move):
            return possible_moves.append(sumTuple(first_click_coord, knight_move))

        for move in knight_moves:

            # need to check if within chessboard bounds
            want_to_go_to = sumTuple(board_coord, move)
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
    a_white_piece = "wR" or "wP" or "wB" or "wK" or "wN" or "wQ"
    return target_square is None or target_square == a_white_piece


def canGoWhite(target_square):
    a_black_piece = "bR" or "bP" or "bB" or "bK" or "bN" or "bQ"
    return target_square is None or target_square == a_black_piece


def sumTuple(t1, t2):
    return tuple(map(sum, zip(t1, t2)))


def withinBoardBounds(want_to_go_to):
    return want_to_go_to[0] <= 7 and want_to_go_to[1] <= 7
