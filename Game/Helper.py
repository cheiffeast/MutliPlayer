import pygame

def setup(size = [500, 500]):
    pygame.init()
    screen = pygame.display.set_mode([500, 500])
    clock = pygame.time.Clock()

    return screen, clock, True

def eventLoop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def refresh(rect = [0, 0, 500, 500]):
    pygame.display.update(rect)

def keys():
    return pygame.key.get_pressed()

def mouse():
    return pygame.mouse.get_pressed()

def dxdy(keys):
    dx, dy = 0, 0
    if keys[pygame.K_w]: dy -= 1
    if keys[pygame.K_d]: dx += 1
    if keys[pygame.K_s]: dy += 1
    if keys[pygame.K_a]: dx -= 1

    return dx, dy

def generateRects(players):
    return [pygame.Rect(player[1] + [player[3], player[3]]) for player in players]
