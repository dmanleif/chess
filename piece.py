class Piece:
    def __init__(self, white_in):
        self.white = white_in
        self.killed = False
        self.moved = False

    def setMoved(self):
        self.moved = True


    def isWhite(self):
        return self.white
    
    def isKilled(self):
        return self.killed
    
    def getPieceName(self):
        return self.name
    
    def Move(self, moveContext):
        start = moveContext.start
        end = moveContext.end
        end.setPiece(start.getPiece())
        start.setPiece(None)
        self.setMoved()

    def hasMoved(self):
        return self.moved