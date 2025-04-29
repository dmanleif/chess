from piece import Piece

class Bishop(Piece):
    def __init__(self, white_in,):
        super().__init__(white_in)
        self.name = "bishop"

    def canMove(self, moveContext):
        start = moveContext.start
        end = moveContext.end
        board = moveContext.board

        startRow = start.getRow()
        startCol = start.getCol()
        endRow = end.getRow()
        endCol = end.getCol()

        deltaRow = endRow - startRow
        deltaCol = endCol - startCol
        
        # check that move is diagonal
        if (abs(deltaRow) != abs(deltaCol)):
            return False
        

        # check spot is available
        if (end.getPiece() is not None and 
            end.getPiece().isWhite() == self.isWhite()):
            return False
        
        # check that all spots on diagonal are empty
        rowDir = 1 if deltaRow > 0 else -1
        colDir = 1 if deltaCol > 0 else -1
        
        startRow += rowDir
        startCol += colDir
        while (startRow != endRow):
            if (board.getSquare(startRow, startCol).getPiece() is not None):
                return False
            
            startRow += rowDir
            startCol += colDir
        
        return True