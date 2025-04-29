from spot import Spot
from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King


class Board:
    def __init__(self):
        self.squares = []
        self.initializeBoard()

    def initializeBoard(self):
        # Initialize the squares of the board
        for i in range(8):
            self.squares.append([])
            for j in range(8):
                self.squares[i].append(Spot(None, i, j))  # Initially, all spots are empty

        # Place the white pieces
        self.squares[0][0] = Spot(Rook(True), 0, 0)
        self.squares[0][1] = Spot(Knight(True), 0, 1)
        self.squares[0][2] = Spot(Bishop(True), 0, 2)
        self.squares[0][3] = Spot(Queen(True), 0, 3)
        self.squares[0][4] = Spot(King(True), 0, 4)
        self.squares[0][5] = Spot(Bishop(True), 0, 5)
        self.squares[0][6] = Spot(Knight(True), 0, 6)
        self.squares[0][7] = Spot(Rook(True), 0, 7)
        for i in range(8):
            self.squares[1][i] = Spot(Pawn(True), 1, i)

        # Place the black pieces
        self.squares[7][0] = Spot(Rook(False), 7, 0)
        self.squares[7][1] = Spot(Knight(False), 7, 1)
        self.squares[7][2] = Spot(Bishop(False), 7, 2)
        self.squares[7][3] = Spot(Queen(False), 7, 3)
        self.squares[7][4] = Spot(King(False), 7, 4)
        self.squares[7][5] = Spot(Bishop(False), 7, 5)
        self.squares[7][6] = Spot(Knight(False), 7, 6)
        self.squares[7][7] = Spot(Rook(False), 7, 7)
        for i in range(8):
            self.squares[6][i] = Spot(Pawn(False), 6, i)
    
    def getSquare(self, row, col):
        return self.squares[row][col]
    
