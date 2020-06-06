from imageSource import ImageSource,CELL_STEP
import pygame
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 100)
# pylint: disable=no-member
pygame.init()
# pylint: disable=no-member

#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (200, 0, 0)
black = (0, 0, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

X = 1200
Y = 700

BOARD_POS_X = 300
BOARD_POS_Y = 50




gameDisplay = pygame.display.set_mode((X, Y))
pygame.display.set_caption("chaos chess")

gameDisplay.fill(white)

for i in range(1):
    for j in range(1):
        gameDisplay.blit(ImageSource.CELL.value, (BOARD_POS_X + i * CELL_STEP,
                                             BOARD_POS_Y + j * CELL_STEP))


font = pygame.font.Font('freesansbold.ttf', 32)

# create a text suface object,
# on which text is drawn on it.
text = font.render('button', True, green, blue)

# create a rectangular object for the
# text surface object
textRect = text.get_rect()

# set the center of the rectangular object.
textRect.center = (X // 2, Y // 2)


gameDisplay.blit(text, textRect)

RUN = True
FLAG_CLICK = False

while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = event.pos
            FLAG_CLICK = True
            if textRect.collidepoint(mouse):
                print("click zo tao rau")
            print(mouse)

        if event.type == pygame.MOUSEBUTTONUP:
            FLAG_CLICK = False

    pygame.display.update()


pygame.quit()
# quit()
