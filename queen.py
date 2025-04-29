from piece import Piece
from bishop import Bishop
from rook import Rook

class Queen(Piece):
    def __init__(self, white_in,):
        super().__init__(white_in)
        self.name = "queen"

    def canMove(self, moveContext):
        start = moveContext.start
        end = moveContext.end
        board = moveContext.board

        bishop = Bishop(self.isWhite())
        rook = Rook(self.isWhite())

        if (bishop.canMove(moveContext) or rook.canMove(moveContext)):
            return True
        
        return False

