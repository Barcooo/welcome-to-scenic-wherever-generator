import math

import pygame
import random


def get_random_position():
    """return a random (x,y) position in the screen"""
    return (random.randint(0, screen_width - 1),  #randint includes both endpoints.
            random.randint(0, screen_height - 1))


def get_random_named_color():
    """return one of the builtin colors"""
    return random.choice(all_colors)


def draw_arrow(surface, x, y, color, angle=0):
    def rotate(pos, angle):
        cen = (5 + x, 0 + y)
        angle *= -(math.pi / 180)
        cos_theta = math.cos(angle)
        sin_theta = math.sin(angle)
        ret = ((cos_theta * (pos[0] - cen[0]) - sin_theta * (pos[1] - cen[1])) + cen[0],
               (sin_theta * (pos[0] - cen[0]) + cos_theta * (pos[1] - cen[1])) + cen[1])
        return ret

    p0 = rotate((0 + x, -4 + y), angle + 90)
    p1 = rotate((0 + x, 4 + y), angle + 90)
    p2 = rotate((10 + x, 0 + y), angle + 90)

    pygame.draw.polygon(surface, color, [p0, p1, p2])


def draw_line(surface, pos1, pos2, color):
    pygame.draw.line(surface, color, pos1, pos2)


all_colors = list(pygame.colordict.THECOLORS.items())
# convert color dictionar to a list for random selection once

if __name__ == "__main__":
    pygame.init()
    screen_width,screen_height = 640, 480
    surface = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Random Circles')
    clock = pygame.time.Clock() #for limiting FPS
    FPS = 5
    exit_demo = False
    # start with a white background
    surface.fill(pygame.Color("white"))
    fpos = get_random_position()
    while not exit_demo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_demo = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # fill the screen with white, erasing everything
                    surface.fill(pygame.Color("white"))
                # Up/Down arrows to change FPS limit
                elif event.key == pygame.K_UP:
                    FPS *= 2
                elif  event.key == pygame.K_DOWN:
                    FPS /= 2
        # calculate the properties of a circle
        circle_size = 10
        pygame.draw.circle(surface, get_random_named_color()[1], fpos, circle_size)
        lpos = get_random_position()
        pygame.draw.circle(surface, get_random_named_color()[1], lpos, circle_size)
        name, random_color = get_random_named_color()
        draw_line(surface, fpos, lpos, random_color)
        draw_arrow(surface, fpos[0], fpos[1], random_color)
        fpos = lpos
        #print("{} at {}".format(name, pos))
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()