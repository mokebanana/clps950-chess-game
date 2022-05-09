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

    def get_moves(self, board_coord, current_piece):
        #black to move
        if self.color is True:
            possible_moves = []
            if current_piece(board_coord + (1, 1)) is not None:
                if board_coord(self.coord + (1, 1)) == ("wR" or "wP" or "wB" or "wN" or "wQ"):
                    possible_moves.append(self.coord + (1, 1))
                else:
                    pass
            elif board_coord(self.coord + (1, -1)) is not None:
                if board_coord(self.coord + (1, -1)) == ("wR" or "wP" or "wB" or "wN" or "wQ"):
                    possible_moves.append(self.coord + (1, -1))
                else:
                    pass
            elif self.coord[1] == 1:
                possible_moves.append(self.coord + (2, 0))
                possible_moves.append(self.coord + (1, 0))
            else:
                possible_moves.append(self.coord + (1, 0))
        #white to move
        if self.color is False:
            possible_moves = []
            if current_piece(board_coord + (1, -1)) is not None:
                if board_coord(self.coord + (1, -1)) == ("bR" or "bP" or "bB" or "bN" or "bQ"):
                    possible_moves.append(self.coord + (1, -1))
                else:
                    pass
            elif board_coord(self.coord + (-1, -1)) is not None:
                if board_coord(self.coord + (-1, -1)) == ("bR" or "bP" or "bB" or "bN" or "bQ"):
                    possible_moves.append(self.coord + (-1, -1))
                else:
                    pass
            elif self.coord[1] == 6:
                possible_moves.append(self.coord + (0, -2))
                possible_moves.append(self.coord + (0, -1))
            else:
                possible_moves.append(self.coord + (0, -1))
        return possible_moves

class Bishop(chessPiece):
    def __init__(self, name, color, coord):
        super().__init__(name, color, coord)
        self.canMove = False

    def get_moves(self, board, current_piece):
        possible_moves = []
        still_looking = True
        considering_coord = (self.coord + (1, 1))
        # diagonally up and to the right
        while (still_looking):
            if considering_coord is not None:
                if self.color is False:
                    if considering_coord == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                        still_looking = False
                    elif considering_coord == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                        possible_moves.append(self.coord+(1, 1))
                        break
                if self.color is True:
                    if considering_coord == ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                        still_looking = False
                    elif considering_coord == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                        possible_moves.append(self.coord+(1, 1))
                        break
            if considering_coord == None:
                possible_moves.append(self.coord+(1, 1))
        return possible_moves

class King(chessPiece):
    def __init__(self, name, color, coord):
        super().__init__(name, color, coord)
        # self.canMoveTo = coord+(1,1) or coord+(1,-1) or coord+(-1,-1);
        #   or coord+(-1,1) or coord+(1,0) or coord+(-1,0) or coord+(0,-1) or coord+(0,1)

class Queen(chessPiece):
    def __init__(self, name, color, coord):
        super().__init__(name, color, coord)


class Rook(chessPiece):
    def __init__(self, name, color, coord):
        super().__init__(name, color, coord)

    def get_moves(self, board, current_piece):
        possible_moves = []
        if self.color == False:
            still_looking = True
            considering_coord = (self.coord + (1, 1))
            # diagonally up and to the right
            while (still_looking):
                if considering_coord is not None:
                    if considering_coord == ("wR" or "wP" or "wB" or "wK" or "wN" or "wQ"):
                        still_looking = False
                    if ("bR" or "bP" or "bB" or "bK" or "bN" or "bQ"):
                        possible_moves.append(self.coord+(1, 1))
                        break
                if considering_coord == None:
                    possible_moves.append(self.coord+(1, 1))
        return possible_moves

class Knight(chessPiece):
    def __init__(self, name, color, coord):
        super().__init__(name, color, coord)
        self.canMove = True
        #self.canMoveTo = coord+(1,2) or coord+(1,-2) or coord+(-1,-2);
        #   or coord+(2,1) or coord+(2,-1) or coord+(-2,1) or coord+(-2,-1) or coord+(-1,2)