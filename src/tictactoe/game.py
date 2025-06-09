import pygame, sys

WIDTH = 600
HEIGHT = 600
FRAMERATE = 60
CELL_SIZE = 200
CELL_NUMBER = 3


pygame.init()
SCREEN = pygame.display.set_mode((CELL_SIZE*CELL_NUMBER, CELL_SIZE*CELL_NUMBER))
clock = pygame.time.Clock()

# colors
lineColor = pygame.Color('grey')
backgroundColor = pygame.Color('black')

# functions
def drawGrid(boxSize):
    SCREEN.fill(backgroundColor)

    # vertical line
    for x in range(boxSize, WIDTH, boxSize):
        pygame.draw.line(SCREEN, lineColor, (x,0), (x,HEIGHT))

    # horizontal line
    for y in range(boxSize, HEIGHT, boxSize):
        pygame.draw.line(SCREEN, lineColor, (0,y), (WIDTH,y))

def drawClick():
    pass

# main game loop
while True:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # draw grid
    drawGrid(200)

    pygame.display.update()
    clock.tick(FRAMERATE)
