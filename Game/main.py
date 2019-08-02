import pygame
import constants
import sys

background_color = constants.ANTIQUE_WHITE
line_color = constants.PURPLE


def load_and_transform_image(path, width, height):
    image = pygame.image.load(path)
    image = pygame.transform.scale(image, (width, height))
    image = image.convert_alpha()
    return image


def draw_vertical_lines():
    for i in range(2):
        x_coord = constants.MARGIN + constants.LINE_MARGIN * i
        pygame.draw.line(background, line_color, (x_coord, 0), (x_coord, constants.SIZE[1]), constants.LINE_WIDTH)


def draw_horizontal_lines():
    for i in range(2):
        y_coord = constants.MARGIN + constants.LINE_MARGIN * i
        pygame.draw.line(background, line_color, (0, y_coord), (constants.SIZE[0], y_coord), constants.LINE_WIDTH)


pygame.init()

screen = pygame.display.set_mode(constants.SIZE)
pygame.display.set_caption(constants.CAPTION)
# pygame.mouse.set_visible(0)

X = load_and_transform_image(constants.X_PATH, 100, 100)
O = load_and_transform_image(constants.O_PATH, 100, 100)
background = pygame.Surface(constants.SIZE)
background = background.convert()
background.fill(background_color)
# background.blit(X, (500, 300))
# background.blit(O, (600, 300))
draw_horizontal_lines()
draw_vertical_lines()

while True:
    screen.blit(background, (0, 0))
    pygame.display.flip()

    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def init_game():
    pass


def run_game():
    pass
