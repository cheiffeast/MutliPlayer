import pygame

def setup(size = [500, 500]):
    pygame.init()
    screen = pygame.display.set_mode(size)
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

def mousepos():
    return pygame.mouse.get_pos()

def dxdy(keys):
    dx, dy = 0, 0
    if keys[pygame.K_w]: dy -= 1
    if keys[pygame.K_d]: dx += 1
    if keys[pygame.K_s]: dy += 1
    if keys[pygame.K_a]: dx -= 1

    return dx, dy

def generateRects(objects):
    return [pygame.Rect(obj) for obj in objects]
