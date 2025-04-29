from spot import Spot
from board import Board
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from rook import Rook

board = Board()

knight = Knight(False)
bishop = Bishop(False)
rook = Rook(True)
queen = Queen(True)
board.getSquare(1, 2).setPiece(queen)

start = board.getSquare(1, 2)
end = board.getSquare(3, 5)

print(queen.canMove(board, start, end))
print("HI")