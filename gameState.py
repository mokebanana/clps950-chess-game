"""
Class for storing current state of game state for the chess game.
    responsible for determining valid and invalid moves.
"""


class GameState:
    def __init__(self, board):
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
    def makeMove(self, move)


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
    #change matrix to chess notation
    ranksToRows = {"1":7, "2":6, "3":5, "4":4, "5":3, "6":2, "7":1, "8":0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToColumns = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    columnsToFiles = {v: k for k, v in filesToColumns.items()}
    #print chess notation for move
    def chessNotation(self):
        return self.getRankFile(self.startR, self.startC) + self.getRankFile(self.endR, self.endC)
    def RankAndFile(self, r, c):
        return self.columnsToFiles[c] + self.rowsToRanks[r]


