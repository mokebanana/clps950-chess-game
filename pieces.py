
class chessPiece(): # parent class
    def __init__(self, name, color, coord):
        self.name = name
        self.color = color
        self.coord = coord

        self.move = True
        self.canMove = False
        self.onBoard = True

        def get_color(self):
            return self.color

        def get_coord(self):
            return self.coord

        def can_move(self):
            return self.canMove

        def is_on_board(self):
            return self.onBoard

        def moveTo(new_coord):
            self.coord = new_coord

class Pawn(chessPiece):
    def __init__(self, name, color, coord):
        super().__init__(name, color, coord)




class Bishop:
    def __init__(self, color, coord):
        self.color = color
        self.coord = coord
        self.move = False
        self.onBoard = True


class King:
    def __init__(self, color, coord):
        self.color = color
        self.coord = coord
        self.move = False
        self.onBoard = True


class Queen:
    def __init__(self, color, coord):
         self.color = color
         self.coord = coord
         self.move = False
         self.onBoard = True


class Rook:
    def __init__(self, color, coord):
          self.color = color
          self.coord = coord
          self.move = False
          self.onBoard = True


class Knight:
    def __init__(self, color, coord):
          self.color = color
          self.coord = coord

          self.move = True
          self.onBoard = True

    def move_to(self, new_coord):
          self.move = False
          self.onBoard = True
