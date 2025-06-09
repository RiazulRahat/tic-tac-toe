import pygame, sys

# CONSTANTS -------------------------------------------------------------

# NOTE: Keep HEIGHT and WIDTH as 3 times the CELL_SIZE for optimal display
WIDTH = 600
HEIGHT = 600
CELL_SIZE = 200

CELL_NUMBER = 3
FRAMERATE = 60

CIRCLE_IMG_PATH = "src/tictactoe/assets/circle.svg.png"
CROSS_IMG_PATH = "src/tictactoe/assets/cross.svg.png"

CIRCLE_TURN = True

# ----------------------------------------------------------------------

# May be used by Game Logic

moves = []
contains = [['-','-','-'],
            ['-','-','-'],
            ['-','-','-']]

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
# -----------------------------------------------------------------------

# Image Loading
circle, circleRect = loadImage(CIRCLE_IMG_PATH)
cross, crossRect = loadImage(CROSS_IMG_PATH)

# Main Game Loop --------------------------------------------------------
while True:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button clicks only 
                x, y = event.pos
                # print col and row
                col = (x // CELL_SIZE)
                row = (y // CELL_SIZE)

                coord = (row,col)

                if contains[row][col] == '-':
                    contains[row][col] = 'O' if CIRCLE_TURN else 'X'
                    image = circle if CIRCLE_TURN else cross
                    imageRect = image.get_rect(center=(
                        col * CELL_SIZE,
                        row * CELL_SIZE
                        ))
                    moves.append((image, imageRect, coord))
                    CIRCLE_TURN = not CIRCLE_TURN
                else:
                    continue

    # draw grid background
    drawGrid(CELL_SIZE)

    # Draw moves
    for image, imageRect, _unusedCoord in moves:
        SCREEN.blit(image, imageRect.center)



    pygame.display.update()
    clock.tick(FRAMERATE)
# ----------------------------------------------------------------------