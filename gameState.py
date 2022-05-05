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
        """
        import pieces
        # black pieces starting positions
        br1 = pieces.Rook("bR", True, (0, 0))
        bn1 = pieces.Knight("bN", True, (0, 1))
        bb1 = pieces.Bishop("bB", True, (0, 2))
        bq = pieces.Queen("bQ", True, (0, 3))
        bk = pieces.King("bK", True, (0, 4))
        bb2 = pieces.Bishop("bB", True, (0, 5))
        bn2 = pieces.Knight("bN", True, (0, 6))
        br2 = pieces.Rook("bR", True, (0, 7))
        bp1 = pieces.Pawn("bP", True, (1, 0))
        bp2 = pieces.Pawn("bP", True, (1, 1))
        bp3 = pieces.Pawn("bP", True, (1, 2))
        bp4 = pieces.Pawn("bP", True, (1, 3))
        bp5 = pieces.Pawn("bP", True, (1, 4))
        bp6 = pieces.Pawn("bP", True, (1, 5))
        bp7 = pieces.Pawn("bP", True, (1, 6))
        bp8 = pieces.Pawn("bP", True, (1, 7))

        # white pieces starting positions
        wr1 = pieces.Rook("wR", True, (7, 0))
        wn1 = pieces.Knight("wN", True, (7, 1))
        wb1 = pieces.Bishop("wB", True, (7, 2))
        wq = pieces.Queen("wQ", True, (7, 3))
        wk = pieces.King("wK", True, (7, 4))
        wb2 = pieces.Bishop("wB", True, (7, 5))
        wn2 = pieces.Knight("wN", True, (7, 6))
        wr2 = pieces.Rook("wR", True, (7, 7))
        wp1 = pieces.Pawn("wP", True, (6, 0))
        wp2 = pieces.Pawn("wP", True, (6, 1))
        wp3 = pieces.Pawn("wP", True, (6, 2))
        wp4 = pieces.Pawn("wP", True, (6, 3))
        wp5 = pieces.Pawn("wP", True, (6, 4))
        wp6 = pieces.Pawn("wP", True, (6, 5))
        wp7 = pieces.Pawn("wP", True, (6, 6))
        wp8 = pieces.Pawn("wP", True, (6, 7))

        self.board = [[br1, bn1, bb1, bq, bk, bb2, bn2, br2],
                      [bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8],
                      [wr1, wn1, wb1, wq, wk, wb2, wn2, wr2]]

        self.whiteMoveNext = True  # white moves first
        self.checkMate = False

        def movePiece(piece, new_coord):
            """
            Function to move piece from its current (old) coord to newCoord
                updates old square to None
                updates new square to have piece
            """
            # update square at oldCoord: None
            old_coord = getattr(piece, 'coord')
            old_r = old_coord[0]
            old_c = old_coord[1]
            self.board[old_r][old_c] = None

            # update square at newCoord: piece
            new_r = new_coord[0]
            new_c = new_coord[1]
            self.board[new_r][new_c] = piece
