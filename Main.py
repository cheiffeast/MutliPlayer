from Game import Player, Draw, Helper
from random import randint as r
from Multi import Client
from time import time
from math import sqrt

# Globals
screen, clock, running = Helper.setup([1000, 500])
io                     = Client.createSocket()
p, players, uid        = Player.player([250, 250], color = [r(0, 255), r(0, 255), r(0, 255)], size = r(5, 30)), [], None
sleep, lastUpdated     = None, time()
timeout, objects       = 5, []
lastProj = 0

def tick(*args):
    global players, lastUpdated, objects
    lastUpdated = time()
    players = args[0]["players"]
    objects = args[0]["objects"]
    io.emit("tickReply", {"position": p.pos + [p.size, p.size], "color": p.col})

def setup(*args):
    global sleep, uid
    sleep = args[0]["sleep"]
    uid = args[0]["uid"]


io.on("tick", tick)
io.on("setup", setup)
io.wait(1)

while running:
    screen.fill([0, 0, 0])
    running = Helper.eventLoop()

    # Organise objects
    statics  = [obj for obj in objects if obj[2][0] == 0 and obj[2][1] == 0]
    dynamics = [obj for obj in objects if obj[2][0] != 0 or obj[2][1] != 0]

    # Player rects
    pRects = Helper.generateRects([p[1] for p in players if p[0] != uid])
    staticRects = Helper.generateRects([obj[0] for obj in statics])
    dynamicRects = Helper.generateRects([obj[0] for obj in dynamics])

    # Check last time we got data from the Server
    if time() - lastUpdated > timeout:
        running = False

    # Drawing
    Draw.drawPlayer(screen, p.rect, p.offset, p.col)
    Draw.drawRects(screen, pRects, p.offset, [ps[2] for ps in players if ps[0] != uid])
    Draw.drawRects(screen, staticRects, p.offset, [obj[1] for obj in statics])
    Draw.drawRects(screen, dynamicRects, p.offset, [obj[1] for obj in dynamics])

    # Player movement
    keys = Helper.keys()
    dx, dy = Helper.dxdy(keys)
    c = p.move(pRects + staticRects, dx, dy)


    colourChange = [p.setColor(dynamics[col][1]) if col != -1 else None for col in [p.rect.collidelist(dynamicRects)]][0]

    if len(c):
        c = c[0]
        if c > len(players) - 2:
            p.setColor(statics[c - 2][1])


    # Check mouse clicks
    if Helper.mouse()[0] and time() - lastProj > 1:
        lastProj = time()
        pos = Helper.mousepos()
        vect = [(pos[0] - (p.pos[0] + p.offset[0])) / 100, (pos[1] - (p.pos[1] + p.offset[1])) / 100]
        io.emit("addProjectile", {"position": p.pos + [5, 5], "color": p.color, "velocity": vect});



    # Refresh and wait for response from server
    Helper.refresh([0, 0, 1000, 1000])
    io.wait(sleep)
