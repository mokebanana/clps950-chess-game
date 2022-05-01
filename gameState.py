"""
Class for storing current state of game state for the chess game.
    responsible for determining valid and invalid moves.
"""


class GameState:
    def __init__(self):
        """
        The chess board is represented by 8x8 2d list
        Each character is represented by a 2-letter str.
            1st char: color ('b', 'w')
            2nd char: piece type ('R', 'N', 'B', 'Q', 'K' or 'p')
            empty space: '--'

            (character notations inspired by GitHub user mikolaj-skrzypczak)
        """
        self.board = [["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                      ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
                      ["--", "--", "--", "--", "--", "--", "--", "--"],
                      ["--", "--", "--", "--", "--", "--", "--", "--"],
                      ["--", "--", "--", "--", "--", "--", "--", "--"],
                      ["--", "--", "--", "--", "--", "--", "--", "--"],
                      ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
                      ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]

        self.whiteMoveNext = True  # white moves first
        self.checkMate = False

        # TODO: initialize pawn promotion, enpassant, castling, etc. conditions here

        def movePiece(self, move):
            """
            Function to make a move
            :param self:
            :param move:
            :return:
            """
            self.board[move.startRow][move.startCol] = "--"


"""
Class for moving pieces from start to end square
    responsible for 
"""


class Move:
    def __init__(self, board, start, end):
        # store coordinates of start and end points of piece
        self.startR = start[0]
        self.startC = start[1]
        self.endR = end[0]
        self.endC = end[1]

        # origin square of piece [first click]
        self.startSquare = board[self.startR][self.startC]

        # target square of piece [second click]
        self.endSquare = board[self.endR][self.endC]
