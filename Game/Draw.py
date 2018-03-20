from pygame.draw import rect

def drawPlayer(surface, r, offset, col = [0, 0, 0]):
    r = [r[0] + offset[0], r[1] + offset[1], r[2], r[3]]
    rect(surface, col, r)

def drawRects(surface, rects, offset, col = None):
    if col == None: col = [[255, 255, 255] for r in rects]
    for i in range(len(rects)):
        r = [rects[i][0] + offset[0], rects[i][1] + offset[1], rects[i][2], rects[i][3]]
        rect(surface, col[i], r)
