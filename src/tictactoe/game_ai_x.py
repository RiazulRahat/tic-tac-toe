import pygame, sys
from ttt_engine import GS_tictactoe as ttt
from utilities import actions, result, winner, remove_move, terminal, minimax

# CONSTANTS -------------------------------------------------------------
CELL_SIZE = 200
CELL_NUMBER = 3
WIDTH = CELL_SIZE * CELL_NUMBER
HEIGHT = CELL_SIZE * CELL_NUMBER

FRAMERATE = 60

CIRCLE_IMG_PATH = "src/tictactoe/assets/circle.svg.png"
CROSS_IMG_PATH = "src/tictactoe/assets/cross.svg.png"

GAME_END_DELAY = 1000

# --------------------------
# Initialize a new board
board = ttt()
# --------------------------

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# colors
lineColor = pygame.Color('grey12')
backgroundColor = pygame.Color('oldlace')

# Functions ------------------------------------------------------------
def loadImage(imagePath):
    image = pygame.image.load(imagePath).convert_alpha()
    image = pygame.transform.scale(image, (CELL_SIZE,CELL_SIZE))
    imageRect = image.get_rect(center=(CELL_SIZE // 2, CELL_SIZE // 2))
    return image, imageRect


def drawGrid(boxSize):
    SCREEN.fill(backgroundColor)

    # vertical line
    for x in range(boxSize, WIDTH, boxSize):
        pygame.draw.line(SCREEN, lineColor, (x,0), (x,HEIGHT))

    # horizontal line
    for y in range(boxSize, HEIGHT, boxSize):
        pygame.draw.line(SCREEN, lineColor, (0,y), (WIDTH,y))

def game_over_text():
    font = pygame.font.SysFont('Arial', 120)
    textSurface = font.render(winner(board), True, pygame.Color('darkseagreen'))
    textRect = textSurface.get_rect(center=(WIDTH//2, HEIGHT//2))
    SCREEN.blit(textSurface, textRect)

# -----------------------------------------------------------------------

# Image Loading
circle, circleRect = loadImage(CIRCLE_IMG_PATH)
cross, crossRect = loadImage(CROSS_IMG_PATH)

# Populate image for pygame screen
image_list = []
def add_image(row, col, turn):
    image = circle if turn=='O' else cross
    imageRect = image.get_rect(center=(col * CELL_SIZE, row * CELL_SIZE))
    image_list.append((image, imageRect))


def botMove():
    if not terminal(board):
        botMove = minimax(board) 
        b_row,b_col = botMove 
        result(board, botMove)

        turn = board.contains[b_row][b_col]
        add_image(b_row, b_col, turn)

# Main Game Loop --------------------------------------------------------
running = True
while running:

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button clicks only 
                x, y = event.pos
                # print row and col
                row = (y // CELL_SIZE)
                col = (x // CELL_SIZE)
                coord = (row,col)

                if coord in actions(board):
                    result(board, coord)
                    turn = board.contains[row][col]
                    add_image(row, col, turn)
                
                    botMove()
        
        # remove move by pressing 'b'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            if len(image_list) > 0:
                # pop twice for bot moves
                image_list.pop()
                board = remove_move(board)
                image_list.pop()
                board = remove_move(board)
    
    # draw grid background
    drawGrid(CELL_SIZE)

    # Draw moves
    for image, imageRect in image_list:
        SCREEN.blit(image, imageRect.center)

    pygame.display.update()
    clock.tick(FRAMERATE)

    if board.is_game_over():
        game_over_text()
        pygame.display.update()
        pygame.time.delay(GAME_END_DELAY)
        running = False

# ----------------------------------------------------------------------

# Exit
pygame.quit()
sys.exit()