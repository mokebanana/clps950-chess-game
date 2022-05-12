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

    def get_moves(self, board, board_coord, first_click_coord):
        """
        Function to return all possible moves of the piece at the location of the first click
        :param board: current state of the board
        :param board_coord: the
        :param first_click_coord:
        :return:
        """
        # black to move
        if self.color is True:
            possible_moves = []
            if board_coord[board[0] + 1][board[1] + 1] is not None:
                if board_coord[board[0] + 1][board[1] + 1] == ("wR" or "wP" or "wB" or "wN" or "wQ"):
                    possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, 1)))))
                else:
                    pass
            elif board_coord[board[0] - 1][board[1] + 1] is not None:
                if board_coord[board[0] + 1][board[1] - 1] == ("wR" or "wP" or "wB" or "wN" or "wQ"):
                    possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, 1)))))
                else:
                    pass
            elif board[1] == 1:
                if board_coord[board[0] + 0][board[1] + 2] is None:
                    possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, 2)))))
                if board_coord[board[0] + 0][board[1] + 1] is None:
                    possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, 1)))))
            elif board_coord[board[0] + 0][board[1] + 1] is None:
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, -1)))))
            else:
                pass
            return possible_moves
        # white to move
        if self.color is False:
            possible_moves = []
            if board_coord[board[0] + 1][board[1] - 1] is not None:
                if board_coord[board[0] + 1][board[1] - 1] == ("bR" or "bP" or "bB" or "bN" or "bQ"):
                    # add the possible move for capturing diagonal
                    possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, -1)))))
                else:
                    pass
            elif board_coord[board[0] - 1][board[1] - 1] is not None:
                if board_coord[board[0] - 1][board[1] - 1] == ("bR" or "bP" or "bB" or "bN" or "bQ"):
                    possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, -1)))))
                else:
                    pass
            elif board[1] == 6:
                if board_coord[board[0] + 0][board[1] - 2] is None:
                    tupP1 = tuple(map(sum, zip(first_click_coord, (0, -2))))
                    possible_moves.append(tupP1)
                if board_coord[board[0] + 0][board[1] - 1] is None:
                    tupP2 = tuple(map(sum, zip(first_click_coord, (0, -1))))
                    possible_moves.append(tupP2)
            elif board_coord[board[0] + 0][board[1] - 1] is None:
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, -1)))))
            else:
                pass
            return possible_moves


class Bishop(chessPiece):
    def __init__(self, name, color, coord):
        super().__init__(name, color, coord)
        self.canMove = False

    def get_moves(self, board, board_coord, first_click_coord):
        possible_moves = []
        still_looking = True
        considering_coord = (tuple(map(sum, zip(first_click_coord, (1, 1)))))
        # diagonally up and to the right
        while still_looking:
            if board_coord[board[0] + 1][board[1] + 1] is not None:
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
        while (still_looking):
            if board_coord[board[0] + 1][board[1] - 1] is not None:
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
            if considering_coord2 == None:
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, -1)))))
        considering_coord3 = (tuple(map(sum, zip(first_click_coord, (-1, -1)))))
        while (still_looking):
            if board_coord[board[0] - 1][board[1] - 1] is not None:
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
            if considering_coord3 == None:
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, -1)))))
        considering_coord4 = (tuple(map(sum, zip(first_click_coord, (-1, 1)))))
        while (still_looking):
            if board_coord[board[0] - 1][board[1] + 1] is not None:
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
            if considering_coord2 == None:
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, 1)))))
        return possible_moves

class King(chessPiece):
    def __init__(self, name, color, coord):
        super().__init__(name, color, coord)

    def get_moves(self, board, board_coord, first_click_coord):
        possible_moves = []
        if self.color is True:
            if board_coord[board[0] + 1][board[1] + 0] is None or board_coord[board[0] + 1][board[1] + 0] == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, 0)))))
            else:
                pass
            if board_coord[board[0] - 1][board[1] + 0] is None or board_coord[board[0] - 1][board[1] + 0] == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, 0)))))
            else:
                pass
            if board_coord[board[0] + 1][board[1] + 0] is None or board_coord[board[0] + 1][board[1] + 0] == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, 0)))))
            else:
                pass
            if board_coord[board[0] - 1][board[1] - 0] is None or board_coord[board[0] - 1][board[1] - 0] == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, 0)))))
            else:
                pass
            if board_coord[board[0] + 0][board[1] + 1] is None or board_coord[board[0] + 0][board[1] + 1] == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, 1)))))
            else:
                pass
            if board_coord[board[0] + 0][board[1] + 1] is None or board_coord[board[0] + 0][board[1] + 1] == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, 1)))))
            else:
                pass
            if board_coord[board[0] + 0][board[1] - 1] is None or board_coord[board[0] + 0][board[1] - 1] == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, -1)))))
            else:
                pass
            if board_coord[board[0] + 0][board[1] - 1] is None or board_coord[board[0] + 0][board[1] - 1] == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, -1)))))
            else:
                pass
        if self.color is False:
            if board_coord[board[0] + 1][board[1] + 0] is None or board_coord[board[0] + 1][board[1] + 0] == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, 0)))))
            else:
                pass
            if board_coord[board[0] - 1][board[1] + 0] is None or board_coord[board[0] - 1][board[1] + 0] == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, 0)))))
            else:
                pass
            if board_coord[board[0] + 1][board[1] + 0] is None or board_coord[board[0] + 1][board[1] + 0] == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, 0)))))
            else:
                pass
            if board_coord[board[0] - 1][board[1] + 0] is None or board_coord[board[0] - 1][board[1] + 0] == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, 0)))))
            else:
                pass
            if board_coord[board[0] + 0][board[1] + 1] is None or board_coord[board[0] + 0][board[1] + 1] == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, 1)))))
            else:
                pass
            if board_coord[board[0] + 0][board[1] + 1] is None or board_coord[board[0] + 0][board[1] + 1] == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, 1)))))
            else:
                pass
            if board_coord[board[0] + 0][board[1] - 1] is None or board_coord[board[0] + 0][board[1] - 1] == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, -1)))))
            else:
                pass
            if board_coord[board[0] + 0][board[1] - 1] is None or board_coord[board[0] + 0][board[1] - 1] == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
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

    def get_moves(self, board, board_coord, first_click_coord):
        possible_moves = []
        still_looking = True
        considering_coord = (tuple(map(sum, zip(first_click_coord, (0, 1)))))
        while still_looking:
            if board_coord[board[0] + 0][board[1] + 1] is not None:
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
        considering_coord2 = (tuple(map(sum, zip(first_click_coord, (0, -1)))))  # TODO: why is this code unreachable?
        while (still_looking):
            if board_coord[board[0] + 0][board[1] - 1] is not None:
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
            if considering_coord2 == None:
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (0, -1)))))
        considering_coord3 = (tuple(map(sum, zip(first_click_coord, (1, 0)))))
        while (still_looking):
            if board_coord[board[0] + 1][board[1] + 0] is not None:
                if self.color is False:
                    if considering_coord3 == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                        still_looking = False
                    elif considering_coord3 == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                        possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, 0)))))
                        break
                if self.color is True:
                    if considering_coord3 == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                        still_looking = False
                    elif considering_coord3 == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                        possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, 0)))))
                        still_looking = False
            if considering_coord3 == None:
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, 0)))))
        considering_coord4 = (tuple(map(sum, zip(first_click_coord, (-1, 0)))))
        while (still_looking):
            if board_coord[board[0] - 1][board[1] + 0] is not None:
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
            if considering_coord2 == None:
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, 0)))))
        return possible_moves


class Knight(chessPiece):
    def __init__(self, name, color, coord):
        super().__init__(name, color, coord)
        self.canMove = True

    def get_moves(self, board, board_coord, first_click_coord):
        possible_moves = []
        if self.color is True:
            if board_coord[board[0] + 1][board[1] + 2] is None or board_coord[board[0] + 1][board[1] + 2] == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, 2)))))
            else:
                pass
            if board_coord[board[0] - 1][board[1] + 2] is None or board_coord[board[0] - 1][board[1] + 2] == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, 2)))))
            else:
                pass
            if board_coord[board[0] + 1][board[1] - 2] is None or board_coord[board[0] + 1][board[1] - 2] == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, -2)))))
            else:
                pass
            if board_coord[board[0] - 1][board[1] - 2] is None or board_coord[board[0] - 1][board[1] - 2] == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, -2)))))
            else:
                pass
            if board_coord[board[0] + 2][board[1] + 1] is None or board_coord[board[0] + 2][board[1] + 1] == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (2, 1)))))
            else:
                pass
            if board_coord[board[0] - 2][board[1] + 1] is None or board_coord[board[0] -2][board[1] + 1] == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (-2, 1)))))
            else:
                pass
            if board_coord[board[0] + 2][board[1] - 1] is None or board_coord[board[0] + 2][board[1] - 1] == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (2, -1)))))
            else:
                pass
            if board_coord[board[0] - 2][board[1] - 1] is None or board_coord[board[0] - 2][board[1] - 1] == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (-2, -1)))))
            else:
                pass
        if self.color is False:
            if board_coord[board[0] + 1][board[1] + 2] is None or board_coord[board[0] + 1][board[1] + 2] == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, 2)))))
            else:
                pass
            if board_coord[board[0] - 1][board[1] + 2] is None or board_coord[board[0] - 1][board[1] + 2] == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, 2)))))
            else:
                pass
            if board_coord[board[0] + 1][board[1] - 2] is None or board_coord[board[0] + 1][board[1] - 2] == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (1, -2)))))
            else:
                pass
            if board_coord[board[0] - 1][board[1] - 2] is None or board_coord[board[0] - 1][board[1] - 2] == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (-1, -2)))))
            else:
                pass
            if board_coord[board[0] + 2][board[1] + 1] is None or board_coord[board[0] + 2][board[1] + 1] == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (2, 1)))))
            else:
                pass
            if board_coord[board[0] - 2][board[1] + 1] is None or board_coord[board[0] - 2][board[1] + 1] == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (-2, 1)))))
            else:
                pass
            if board_coord[board[0] + 2][board[1] - 1] is None or board_coord[board[0] + 2][board[1] - 1] == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (2, -1)))))
            else:
                pass
            if board_coord[board[0] - 2][board[1] - 1] is None or board_coord[board[0] - 2][board[1] - 1] == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                possible_moves.append(tuple(map(sum, zip(first_click_coord, (-2, -1)))))
            else:
                pass
        return possible_moves


