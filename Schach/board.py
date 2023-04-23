import piece

class board:
    def __init__(self):
        self.Brett = []
        for i in range (8):
            self.Brett.append([None]*8)
        # Platzieren der Figuren auf ihre Startposition
            # Schwarz
        for i in range(8):
            self.Brett[1][i] = piece.pawn(False)

        self.Brett[0][0] = piece.rook(False)
        self.Brett[0][1] = piece.knight(False)
        self.Brett[0][2] = piece.bishop(False)
        self.Brett[0][3] = piece.queen(False)
        self.Brett[0][4] = piece.king(False)
        self.Brett[0][5] = piece.bishop(False)
        self.Brett[0][6] = piece.knight(False)
        self.Brett[0][7] = piece.rook(False)

        # Weiß
        for i in range(8):
            self.Brett[6][i] = piece.pawn(True)

        self.Brett[7][0] = piece.rook(True)
        self.Brett[7][1] = piece.knight(True)
        self.Brett[7][2] = piece.bishop(True)
        self.Brett[7][3] = piece.queen(True)
        self.Brett[7][4] = piece.king(True)
        self.Brett[7][5] = piece.bishop(True)
        self.Brett[7][6] = piece.knight(True)
        self.Brett[7][7] = piece.rook(True)

    def print_board(self):
        spalte = 8
        for i in range(len(self.Brett)):
            print("\t")
            print(f"\033[1;34;48m{str(spalte)}\033[1;37;0m |",end="")
            spalte -= 1
            for y in self.Brett[i]:
                if y == None:
                    print(" ",end= " |")
                elif y.color == True:
                    print(y.name,end= " |")
                else:
                    print("\033[1;31;48m" + y.name + "\033[1;37;0m", end= " |")
        print("\n \033[1;34;48m  A  B  C  D  E  F  G  H\033[1;37;0m")
        # Code für Underline -> Verschönerung des Bretts?: \033[4;37;48m für end: \033[1;37;0m

schachbrett = board()

schachbrett.print_board()


