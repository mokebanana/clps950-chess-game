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
        self.canMove = True
       # if self.color = True:
        #    self.canMoveTo = coord+(-1, 0)
      #  else:
       #     self.canMoveTo = coord+(1,0)


class Bishop(chessPiece):
    def __init__(self, name, color, coord):
        super().__init__(name, color, coord)
        self.canMove = False

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


class Knight(chessPiece):
    def __init__(self, name, color, coord):
        super().__init__(name, color, coord)
        self.canMove = True
        #self.canMoveTo = coord+(1,2) or coord+(1,-2) or coord+(-1,-2);
        #   or coord+(2,1) or coord+(2,-1) or coord+(-2,1) or coord+(-2,-1) or coord+(-1,2)