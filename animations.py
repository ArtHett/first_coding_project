from time import sleep

import pygame


def enemy_hit(screen):
    '''enemy hit animation'''
    pygame.draw.rect(
            screen, (0, 0, 0), (645, 130, 3, 280))
    pygame.display.flip(), sleep(0.2)


def enemy_hit_alt(screen):
    '''alternative enemy hit animation'''
    pygame.draw.rect(
            screen, (0, 0, 0), (550, 250, 180, 3))
    pygame.display.flip(), sleep(0.2)


def enemy_magic_hit(screen):
    '''enemy magic-hit animation'''
    for i in range(4):
        pygame.draw.circle(
                screen, (i*40, 0, 250 - i*40),
                (650, 240), 15 + i*7, 15 + i*3)
        pygame.display.flip(), sleep(0.1)