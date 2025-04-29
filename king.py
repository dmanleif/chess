from piece import Piece
from player import Player
from move_context import MoveContext


class King(Piece):
    def __init__(self, white_in,):
        super().__init__(white_in)
        self.name = "king"
    

    def canMove(self, moveContext):
        start = moveContext.start
        end = moveContext.end
        player = moveContext.player
        board = moveContext.board

        deltaRow = end.getRow() - start.getRow()
        deltaCol = end.getCol() - start.getCol()

        if self.moved == False and deltaRow == 0 and abs(deltaCol) == 2 and self.canCastle(board, player, start, end):
            return True

        if (end.getPiece() == None or self.isWhite() != end.getPiece().isWhite()) and abs(deltaRow) <= 1 and abs(deltaCol) <= 1:
            return True
        
        return False
    
    def Move(self, moveContext):
        start = moveContext.start
        end = moveContext.end
        player = moveContext.player
        board = moveContext.board
        
        end.setPiece(start.getPiece())
        start.setPiece(None)
        self.setMoved()
        player.kingSpot = end

        deltaCol = end.getCol() - start.getCol()
        direction = 1 if deltaCol > 0 else -1
        if abs(deltaCol) == 2:
            if deltaCol == 2:
                rookSpot = board.getSquare(start.getRow(), 7)
            elif deltaCol == -2:
                rookSpot = board.getSquare(start.getRow(), 0)

            rookPiece = rookSpot.getPiece()
            moveContextRook = MoveContext(board, player, rookSpot, board.getSquare(start.getRow(), start.getCol() + direction))
            rookPiece.Move(moveContextRook)
        
    def canCastle(self, board, player, start, end):
        deltaCol = end.getCol() - start.getCol()
        direction = 1 if deltaCol > 0 else -1

        col = start.getCol() + direction
        row = start.getRow()
        
        if direction == 1:
            if board.getSquare(row, 7) is None or board.getSquare(row, 7).getPiece().getPieceName() != "rook" or board.getSquare(row, 7).getPiece().hasMoved():
                return False
        else:
            if board.getSquare(row, 0) is None or board.getSquare(row, 0).getPiece().getPieceName() != "rook" or board.getSquare(row, 0).getPiece().hasMoved():
                return False

        while col <= end.getCol():
            if board.getSquare(start.getRow(), col).getPiece() is not None or player.isChecked(board, start.getRow(), col):
                return False
            col += direction

        return True
    