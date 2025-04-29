


class Spot:
    def __init__(self, piece_in, row_in, col_in):
        self.piece = piece_in
        self.row = row_in
        self.col = col_in

    def setPiece(self, piece_in):
        self.piece = piece_in

    def removePieve(self):
        self.piece = None

    def getPiece(self):
        return self.piece
    
    def getRow(self):
        return self.row
    
    def getCol(self):
        return self.col