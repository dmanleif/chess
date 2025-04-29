from piece import Piece

class Knight(Piece):
    def __init__(self, white_in,):
        super().__init__(white_in)
        self.name = "knight"

    def canMove(self, moveContext):
        start = moveContext.start
        end = moveContext.end
        
        deltaRow = end.getRow() - start.getRow()
        deltaCol = end.getCol() - start.getCol()

        if ( (end.getPiece() == None or self.isWhite() != end.getPiece().isWhite()) and abs(deltaRow * deltaCol) == 2 ):
            return True
        
        return False