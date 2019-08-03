import pygame
import constants
import sys
from os import path

sys.path.append('..')
from Environment.Board import Board
from Environment import Agents


background_color = constants.ANTIQUE_WHITE
line_color = constants.PURPLE

pygame.init()
screen = pygame.display.set_mode(constants.SIZE)
pygame.display.set_caption(constants.CAPTION)
background = pygame.Surface(constants.SIZE)
background = background.convert()
background.fill(background_color)


def load_and_transform_image(path, width, height):
    image = pygame.image.load(path)
    image = pygame.transform.scale(image, (width, height))
    image = image.convert_alpha()
    return image


X = load_and_transform_image(constants.X_PATH, 160, 160)
O = load_and_transform_image(constants.O_PATH, 160, 160)


def draw_vertical_lines():
    for i in range(2):
        x_coord = constants.MARGIN + constants.LINE_MARGIN * i
        pygame.draw.line(background, line_color, (x_coord, 0),
                         (x_coord, constants.SIZE[1]), constants.LINE_WIDTH)


def draw_horizontal_lines():
    for i in range(2):
        y_coord = constants.MARGIN + constants.LINE_MARGIN * i
        pygame.draw.line(background, line_color, (0, y_coord),
                         (constants.SIZE[0], y_coord), constants.LINE_WIDTH)


def determine_quad(mouse_pos):
    quads = constants.BOUNDARIES
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    for index, quad in enumerate(quads, 0):
        if (mouse_x >= quad[0][0] and mouse_x <= quad[0][1]):
            if (mouse_y >= quad[1][0] and mouse_y <= quad[1][1]):
                return index, quad


def draw_marker(quad, side):
    if (side == 'X'):
        marker = X
    elif (side == 'O'):
        marker = O

    marker_pos = (quad[0][0] + constants.MARKER_MARGIN,
                  quad[1][0] + constants.MARKER_MARGIN)
    background.blit(marker, marker_pos)


draw_horizontal_lines()
draw_vertical_lines()


while True:
    screen.blit(background, (0, 0))
    pygame.display.flip()

    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evt.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = evt.pos
            index, quad = determine_quad(mouse_pos)
            draw_marker(quad, 'O')


def run_game():
    pass
