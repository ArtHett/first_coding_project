from time import sleep

import pygame


def draw_arrow(screen, x, y, size=60, color=(200, 200, 200), reverse=False):
    """Zeichnet einen Pfeil an Position (x, y)."""
    if not reverse:
        # Pfeil zeigt nach OBEN
        points = (
            (x, y - size),                    # Spitze oben
            (x + size * 0.5, y - size * 0.1), # rechts oben
            (x + size * 0.15, y - size * 0.1),# rechts innen
            (x + size * 0.15, y + size),      # rechts unten (Schaft)
            (x - size * 0.15, y + size),      # links unten (Schaft)
            (x - size * 0.15, y - size * 0.1),# links innen
            (x - size * 0.5, y - size * 0.1), # links oben
        )
    else:
        # Pfeil zeigt nach UNTEN
        points = (
            (x, y + size),                    # Spitze unten
            (x + size * 0.5, y + size * 0.1), # rechts unten
            (x + size * 0.15, y + size * 0.1),# rechts innen
            (x + size * 0.15, y - size),      # rechts oben (Schaft)
            (x - size * 0.15, y - size),      # links oben (Schaft)
            (x - size * 0.15, y + size * 0.1),# links innen
            (x - size * 0.5, y + size * 0.1), # links unten
        )
    
    pygame.draw.polygon(screen, color, points, 0)# Füllung
    pygame.draw.polygon(screen, (100, 100, 100), points, 2)# Kontur
    pygame.display.flip(), sleep(0.5)


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


def enemy_hit_vert(screen):#standard attack
    '''enemy hit animation'''
    for i in range(4):
        pygame.draw.rect(
            screen, (255, 255, 255),
            (645, 130, 4 - i, 40 + i*80))
        pygame.display.flip(), sleep(0.06)


def enemy_hit_hor(screen):
    '''alternative enemy hit animation'''
    for i in range(4):
        pygame.draw.rect(
            screen, (255, 255, 255), 
            (550, 250, i*60, 4 - i))
        pygame.display.flip(), sleep(0.06)


def enemy_magic_hit(screen):#standard magic atk
    '''enemy magic-hit animation'''
    for i in range(4):
        pygame.draw.circle(
            screen, (i*40, 0, 250 - i*40),
            (650, 240), 15 + i*7, 15 + i*3)
        pygame.display.flip(), sleep(0.1)


def vertical_beam(screen):
    '''special magic hit animation'''
    for i in range(4):
        pygame.draw.rect(
            screen, (250, 250, 250 - i*80), 
            (645 - i*2, 120, 5 + i*4, 80 + i*70))
        pygame.display.flip(), sleep(0.1)