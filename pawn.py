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

        if abs(deltaCol) == 1:
            # pawn captures
            if deltaRow == self.direction and end.getPiece() is not None and end.getPiece().isWhite() != self.isWhite():
                return True
            
            # en passant
            piece = board.getSquare(start.getRow(), start.getCol() + deltaCol).getPiece()
            enPassantRows = [3, 4]
      
            if deltaRow == self.direction and end.getPiece() is None and piece is not None and piece.getPieceName() == "pawn" and piece.isWhite() != self.isWhite() and piece.moved == 1 and start.getRow() in enPassantRows:
                return True
    
        return False


        
    def setDirection(self):
        self.direction = 1 if self.isWhite() else -1

    def Move(self, moveContext):
        start = moveContext.start
        end = moveContext.end
        board = moveContext.board
        deltaCol = end.getCol() - start.getCol()

        if abs(deltaCol) == 1 and end.getPiece() is None:
            board.getSquare(start.getRow(), start.getCol() + deltaCol).setPiece(None)

        end.setPiece(start.getPiece())
        start.setPiece(None)
        self.setMoved()
        