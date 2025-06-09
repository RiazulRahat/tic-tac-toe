import pygame, sys

WIDTH = 600
HEIGHT = 600
FRAMERATE = 60
CELL_SIZE = 200
CELL_NUMBER = 3
CIRCLE_IMG_PATH = "src/tictactoe/assets/circle.svg.png"
CROSS_IMG_PATH = "src/tictactoe/assets/cross.svg.png"

CIRCLE_TURN = True #


pygame.init()
SCREEN = pygame.display.set_mode((CELL_SIZE*CELL_NUMBER, CELL_SIZE*CELL_NUMBER))
clock = pygame.time.Clock()

# colors
lineColor = pygame.Color('grey')
backgroundColor = pygame.Color('black')

# functions
def loadImage(imagePath):
    image = pygame.image.load(imagePath)
    image = pygame.transform.scale(image, (200,200))
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


# Image Loading
circle, circleRect = loadImage(CIRCLE_IMG_PATH)
cross, crossRect = loadImage(CROSS_IMG_PATH)

showImage = False

# main game loop
while True:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mousePos button 
                x, y = event.pos
                # print col and row
                col = (x // CELL_SIZE)
                row = (y // CELL_SIZE)

                crossRect.center = (
                    col * CELL_SIZE,
                    row * CELL_SIZE)

                showImage = True

    # draw grid
    drawGrid(CELL_SIZE)

    if showImage:
        SCREEN.blit(cross, crossRect.center)



    pygame.display.update()
    clock.tick(FRAMERATE)
