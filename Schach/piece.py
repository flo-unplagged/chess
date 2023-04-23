class piece:
    def __init__(self, color):
        self.name = ""
        self.color = color

class pawn(piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "P"


class rook(piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "R"

class knight(piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "N"

class bishop(piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "B"

class queen(piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "Q"

class king(piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "K"







