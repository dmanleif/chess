import pygame
from spot import Spot
from board import Board
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from rook import Rook
from player import Player
from move_context import MoveContext

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
GRID_SIZE = WIDTH // 8
WHITE = (255, 255, 255)
BLACK = (225, 193, 110)

# Load piece images (replace with your actual image paths)
piece_images = {
    "white_pawn": pygame.image.load("/Users/danielleifer/Documents/Chess_Python/classic/white_pawn.png"),
    "white_rook": pygame.image.load("/Users/danielleifer/Documents/Chess_Python/classic/white_rook.png"),
    "white_knight": pygame.image.load("/Users/danielleifer/Documents/Chess_Python/classic/white_knight.png"),
    "white_bishop": pygame.image.load("/Users/danielleifer/Documents/Chess_Python/classic/white_bishop.png"),
    "white_queen": pygame.image.load("/Users/danielleifer/Documents/Chess_Python/classic/white_queen.png"),
    "white_king": pygame.image.load("/Users/danielleifer/Documents/Chess_Python/classic/white_king.png"),
    "black_pawn": pygame.image.load("/Users/danielleifer/Documents/Chess_Python/classic/black_pawn.png"),
    "black_rook": pygame.image.load("/Users/danielleifer/Documents/Chess_Python/classic/black_rook.png"),
    "black_knight": pygame.image.load("/Users/danielleifer/Documents/Chess_Python/classic/black_knight.png"),
    "black_bishop": pygame.image.load("/Users/danielleifer/Documents/Chess_Python/classic/black_bishop.png"),
    "black_queen": pygame.image.load("/Users/danielleifer/Documents/Chess_Python/classic/black_queen.png"),
    "black_king": pygame.image.load("/Users/danielleifer/Documents/Chess_Python/classic/black_king.png"),
}

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Assuming you have a Board class instance named 'board'
# from board import Board  # Uncomment this line if the Board class is in a separate file
# board = Board() # creates the board

def draw_board():
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_pieces(board, start):
    for row in range(8):
        for col in range(8):
            spot = board.getSquare(row, col)
            if start is not None and start.getRow() == row and start.getCol() == col:
                pass
            elif spot.getPiece() is not None:
                piece = spot.getPiece()
                piece_name = "white_" + piece.getPieceName() if piece.isWhite() else "black_" + piece.getPieceName()
                image = piece_images.get(piece_name)
                if image:
                    # Scale the image to fit the grid
                    image = pygame.transform.scale(image, (GRID_SIZE, GRID_SIZE))
                    screen.blit(image, (col * GRID_SIZE, (7 - row) * GRID_SIZE))



def clickDownEvent(dragging):
    col, row = pygame.mouse.get_pos()
    row = 7 - row // GRID_SIZE
    col //= GRID_SIZE
    spot = None
    if board.getSquare(row, col).getPiece() is not None and board.getSquare(row, col).getPiece().isWhite() == players[turn].getColor():
        spot = board.getSquare(row, col)
        dragging = True
    return spot, dragging


def dragEvent(dragging, start):
    if dragging:
        x, y = pygame.mouse.get_pos()  # Get current cursor position

        piece_name = "white_" + start.getPiece().getPieceName() if start.getPiece().isWhite() else "black_" + start.getPiece().getPieceName()
        image = piece_images.get(piece_name)
        #if image:
        image = pygame.transform.scale(image, (GRID_SIZE, GRID_SIZE))  # Ensure it's the right size
 
        # Draw the image centered at the cursor
        screen.blit(image, (x - GRID_SIZE // 2, y - GRID_SIZE // 2))




def clickUpEvent(dragging):
    col, row = pygame.mouse.get_pos()
    row = 7 - row // GRID_SIZE
    col //= GRID_SIZE
    spot = board.getSquare(row, col)
    dragging = False
    
    return spot, dragging


# Game loop
board = Board()
board.initializeBoard()
players = [Player(True, board.getSquare(0, 4)), Player(False, board.getSquare(7, 4))]
turn = 0
running = True
dragging = False
start, end = None, None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start, dragging = clickDownEvent(dragging)
        elif event.type == pygame.MOUSEBUTTONUP:
            end, dragging = clickUpEvent(dragging)
            moveContext = MoveContext(board, players[turn], start, end)
            success = players[turn].make_move(moveContext)
            if success:
                turn = (turn + 1) % 2

            start, end = None, None


        
    # Draw the board and pieces
    
    draw_board()
    draw_pieces(board, start)  # Pass the board instance to the draw_pieces function
    dragEvent(dragging, start)
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
