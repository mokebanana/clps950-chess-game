

class chessPiece(): # parent class
    def __init__(self, name, color, coord):
        self.name = name
        self.color = color
        self.coord = coord

        self.move = True
        self.canMove = False
        self.onBoard = True

        def moveTo(new_coord):
            self.coord = new_coord

class Pawn(chessPiece):
    def __init__(self, name, color, coord):
        super().__init__(name, color, coord)

class Bishop(chessPiece):
    def __init__(self, name, color, coord):
        super().__init__(name, color, coord)

class King(chessPiece):
    def __init__(self, name, color, coord):
        super().__init__(name, color, coord)

class Queen(chessPiece):
    def __init__(self, name, color, coord):
        super().__init__(name, color, coord)

class Rook(chessPiece):
    def __init__(self, name, color, coord):
        super().__init__(name, color, coord)

class Knight(chessPiece):
    def __init__(self, name, color, coord):
        super().__init__(name, color, coord)


