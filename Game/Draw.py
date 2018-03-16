from pygame.draw import rect

def drawPlayer(surface, r, col = [0, 0, 0]):
    rect(surface, col, r)

def drawPlayers(surface, rects, col = None):
    if col == None: col = [[0, 0, 0] for r in rs]
    for i in range(len(rects)):
        rect(surface, col[i], rects[i])
