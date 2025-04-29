from piece import Piece

class Pawn(Piece):
    
    def __init__(self, white_in,):
        super().__init__(white_in)
        self.name = "pawn"
        self.setDirection()


    def canMove(self, moveContext):
        start = moveContext.start
        end = moveContext.end
        board = moveContext.board

        deltaRow = end.getRow() - start.getRow()
        deltaCol = end.getCol() - start.getCol()
        

        if (deltaCol == 0):
            # pawn moves up one
            
            if (deltaRow == self.direction and end.getPiece() is None):
                
                return True
            
            # pawn moves up two
            elif (not self.hasMoved() and deltaRow == 2*self.direction and 
                  board.getSquare(start.getRow() + self.direction, start.getCol()).getPiece() is None and end.getPiece() is None):
                return True

        if (abs(deltaCol) == 1 and deltaRow == self.direction and end.getPiece() is not None and end.getPiece().isWhite() != self.isWhite()):
            return True
        
        return False
    
    

    def setDirection(self):
        self.direction = 1 if self.isWhite() else -1
        