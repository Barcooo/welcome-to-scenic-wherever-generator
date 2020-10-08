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


def draw_line(surface, x, y, color, angle=0):
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


all_colors = list(pygame.colordict.THECOLORS.items())
# convert color dictionar to a list for random selection once

if __name__ == "__main__":
    pygame.init()
    screen_width,screen_height = 640, 480
    surface = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Random Circles')
    clock = pygame.time.Clock() #for limiting FPS
    FPS = 10
    exit_demo = False
    # start with a white background
    surface.fill(pygame.Color("white"))
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
        name, random_color = get_random_named_color()
        pos = get_random_position()
        circle_size = 10 #random.randint(1,10)
        pygame.draw.circle(surface, random_color, pos, circle_size)
        draw_arrow(surface, 100, 100, random_color)
        #print("{} at {}".format(name, pos))
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()