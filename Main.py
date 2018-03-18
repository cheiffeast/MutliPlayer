from Game import Player, Draw, Helper
from random import randint as r
from Multi import Client
from time import time

# Globals
screen, clock, running = Helper.setup()
io                     = Client.createSocket()
p, players, uid        = Player.player([250, 250], color = [r(0, 255), r(0, 255), r(0, 255)], size = r(5, 30)), [], None
sleep, lastUpdated     = None, time()
timeout                = 5

def tick(*args):
    global players, lastUpdated
    lastUpdated = time()
    players = args[0]
    io.emit("tickReply", {"position": p.pos, "color": p.col, "size": p.size})

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

    # Player rects
    rects = Helper.generateRects([p for p in players if p[0] != uid])

    # Check last time we got data from the Server
    if time() - lastUpdated > timeout:
        running = False

    # Drawing
    Draw.drawPlayer(screen, p.rect, p.col)
    Draw.drawPlayers(screen, rects, [ps[2] for ps in players if ps[0] != uid])

    # Player movement
    keys = Helper.keys()
    dx, dy = Helper.dxdy(keys)
    p.move(rects, dx, dy)


    # Refresh and wait for response from server
    Helper.refresh()
    io.wait(sleep)
