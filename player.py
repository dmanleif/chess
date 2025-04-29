from spot import Spot
from piece import Piece
from move_context import MoveContext

class Player:
    def __init__(self, color_in, kingSpot_in):
        self.color = color_in
        self.kingSpot = kingSpot_in

    def getColor(self):
        return self.color


    def isChecked(self, board, row, col):
        
        

        # --- Directional threats: Rook/Queen (straight) ---
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # up, down, right, left

        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                piece = board.getSquare(r,c).getPiece()
                if piece is None:
                    r += dr
                    c += dc
                    continue
                if piece.isWhite() == self.color:
                    break  # Blocked by friendly
                if piece.getPieceName() in ["rook", "queen"]:
                    return True
                else:
                    break  # Enemy but not threatening
        
        # --- Directional threats: Bishop/Queen (diagonal) ---
        diag_dirs = [(1,1), (1,-1), (-1,1), (-1,-1)]
        for dr, dc in diag_dirs:
            print("new")
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                print(f"r: {r}, c: {c}")
                piece = board.getSquare(r,c).getPiece()
                if piece is None:
                    r += dr
                    c += dc
                    continue
                if piece.isWhite() == self.color:
                    break
                if piece.getPieceName() in ["bishop", "queen"]:
                    print("found")
                    return True
                else:
                    break


        # --- Knight threats ---
        knight_moves = [(2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)]
        for dr, dc in knight_moves:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                piece = board.getSquare(r,c).getPiece()
                if piece and piece.getPieceName() == "knight" and piece.isWhite() != self.color:
                    return True


        # --- Pawn threats ---
        pawn_dirs = [(1, -1), (1, 1)] if self.color else [(-1, -1), (-1, 1)]
        for dr, dc in pawn_dirs:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                piece = board.getSquare(r,c).getPiece()
                if piece and piece.getPieceName() == "pawn" and piece.isWhite() != self.color:
                    return True
                
        return False
    




    def make_move(self, moveContext):
        start = moveContext.start
        end = moveContext.end
        board = moveContext.board

        if start is None or end is None or start.getPiece() is None or start.getPiece().isWhite() != self.color:
            return False
        

        piece = start.getPiece()
        
        
        if piece.canMove(moveContext):
            piece.Move(moveContext)
            
            if self.isChecked(board, self.kingSpot.getRow(), self.kingSpot.getCol()):
                piece.Move(end, start)
                
                return False    
            
            return True
        else:
            return False