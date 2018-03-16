from pygame.draw import rect

def drawPlayer(surface, r, col = [0, 0, 0]):
    rect(surface, col, r)

def drawPlayers(surface, rs, col = None, sizes = None):
    if col == None: col = [[0, 0, 0] for r in rs]
    if sizes == None: size = [20 for r in rs]
    for i in range(len(rs)):
        rect(surface, col[i], rs[i] + [sizes[i], sizes[i]])

