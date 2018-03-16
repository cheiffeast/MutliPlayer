from Game import Player, Draw, Helper
from random import randint as r
from Multi import Client

# Globals
screen, clock, running = Helper.setup()
io                     = Client.createSocket()
p, players, uid        = Player.player([250, 250], color = [r(0, 255), r(0, 255), r(0, 255)], size = r(5, 30)), [], None
sleep                  = None

def tick(*args):
    global players
    players = args[0]
    io.emit("tickReply", {"position": p.pos, "color": p.col, "size": p.size})

def uid(*args):
    global uid
    uid = args[0]

def setup(*args):
    global sleep
    sleep = args[0]["sleep"]

io.on("uid", uid)
io.on("tick", tick)
io.on("setup", setup)
io.wait(1)

while running:
    screen.fill([0, 0, 0])
    running = Helper.eventLoop()

    # Drawing
    Draw.drawPlayer(screen, p.rect, p.col)
    Draw.drawPlayers(screen, [ps[1] for ps in players if ps[0] != uid], [ps[2] for ps in players if ps[0] != uid],
                             [ps[3] for ps in players if ps[0] != uid])

    # Player movement
    keys = Helper.keys()
    dx, dy = Helper.dxdy(keys)
    p.move(dx, dy)

    # Refresh and wait for response from server
    Helper.refresh()
    io.wait(sleep)
