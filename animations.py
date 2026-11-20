from time import sleep

import pygame


def defend_symbol(screen):
    '''Animation for defend-move'''
    shield_points = (
    (700, 550),   # oben Mitte (Spitze)
    (750, 565),   # oben rechts
    (750, 600),   # Mitte rechts
    (700, 660),   # unten Mitte (Spitze)
    (650, 600),   # Mitte links
    (650, 565),   # oben links
    )

    pygame.draw.polygon(screen, (100, 100, 100), shield_points, 0)
    pygame.draw.polygon(screen, (10, 10, 10), shield_points, 3)
    pygame.display.flip(), sleep(0.4)


def lightning_symbol(screen, x, y, size=100, color=(255, 255, 0)):
    """Zeichnet ein gefülltes Blitz-Symbol an Position (x, y)."""
    points = (
        (x + size * 0.4,  y - size),        # oben (Spitze)
        (x - size * 0.2,  y - size * 0.1),  # links Knick
        (x + size * 0.1,  y - size * 0.1),  # Mitte
        (x - size * 0.3,  y + size),        # unten (Spitze)
        (x + size * 0.2,  y + size * 0.1),  # rechts Knick
        (x - size * 0.1,  y + size * 0.1),  # Mitte
        )
    
    pygame.draw.polygon(screen, color, points, 0)# Füllung
    pygame.draw.polygon(screen, (150, 100, 0), points, 3)# Kontur
    pygame.display.flip()


def enemy_hit(screen):#standard attack
    '''enemy hit animation'''
    pygame.draw.rect(
            screen, (0, 0, 0), (645, 130, 3, 280))
    pygame.display.flip(), sleep(0.2)


def enemy_hit_alt(screen):
    '''alternative enemy hit animation'''
    pygame.draw.rect(
            screen, (0, 0, 0), (550, 250, 180, 3))
    pygame.display.flip(), sleep(0.2)


def enemy_magic_hit(screen):#standard magic atk
    '''enemy magic-hit animation'''
    for i in range(4):
        pygame.draw.circle(
                screen, (i*40, 0, 250 - i*40),
                (650, 240), 15 + i*7, 15 + i*3)
        pygame.display.flip(), sleep(0.1)