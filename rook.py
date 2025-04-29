from piece import Piece

class Rook(Piece):
    def __init__(self, white_in,):
        super().__init__(white_in)
        self.name = "rook"


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

        # check that move is vertical or horizontal
        if (deltaRow != 0 and deltaCol != 0):
            return False
        
        # check spot is available
        if (end.getPiece() is not None and 
            end.getPiece().isWhite() == self.isWhite()):
            return False
        
        # check that all spots on line are empty
    
        rowDir = 1 if deltaRow > 0 else -1
        colDir = 1 if deltaCol > 0 else -1
        
        if (deltaRow != 0): startRow += rowDir
        if (deltaCol != 0): startCol += colDir

        while (startRow != endRow or startCol != endCol):
            if (board.getSquare(startRow, startCol).getPiece() is not None):
                return False
            
            if (deltaRow != 0): startRow += rowDir
            if (deltaCol != 0): startCol += colDir
        
        return True