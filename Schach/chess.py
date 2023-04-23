import board
import piece

class chess:
    def __init__(self):
        self.turn = True


    def turn_check(self):
        if self.turn == True:
            print("White to move: ", end="")
            spiel.white_move()
        else:
            print("Black to move: ", end="")
            spiel.black_move()

    def white_move(self):
        move = input()
        for row in board.schachbrett.Brett:
            for element in row:
                if issubclass(type(element), piece.piece):
                    if move[0] == element.name and element.color == True:
                        print("Wir haben den weißen König")
        self.turn = False
        spiel.turn_check()

    def black_move(self):
        move = input()
        for row in board.schachbrett.Brett:
            for element in row:
                if issubclass(type(element), piece.piece):
                    if move[0] == element.name and element.color == False:
                        print("Wir haben den schwarzen König")
        self.turn = True
        spiel.turn_check()


spiel = chess()
spiel.turn_check()